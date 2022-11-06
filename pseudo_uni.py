# /bin python3
import json


def st(read, to_state, write, action):
    return dict(read=read, to_state=to_state, write=write, action=action)


def fl(l, *c):
    return list(filter(lambda v: v not in c, l))


def gen():
    L = "LEFT"
    R = "RIGHT"
    PTR = "^"
    STR = "*"
    BGN = "&"
    lp = (
        BGN +  # Start
        STR +  # Null - mem space start
        PTR +  # Pointer
        # "[]" # Programm block
        "{}"   # State block
        "[]"   # Rule block
        "<>"   # Direction
    )
    blank = " " 
    ls = ("ABCDEFCSPH")
    vblank = "."
    li = ("012345+" + vblank + blank)
    l = lp + ls + li

    transitions = [
        (
            "init", [
                st(s, f"goto-null-{s}", s, R) for s in ls
            ],
        ),

    ] + [
    ] + [
        (
            f"goto-null-{state}", [
                st(c, f"goto-null-{state}", c, R) for c in fl(lp + ls + li, STR)
            ] + [st(STR, f"goto-state-{state}", STR, R)],
        ) for state in ls
    ] + [
        (
            f"goto-state-{state}", [
                st(c, f"init-find-{state}:{(c if c != blank else vblank)}", PTR, L) for c in li
            ] if state != 'H' else [
                st(c, "HALT", c, R) for c in li
            ]
        ) for state in ls
    ] + [
        (
            f"init-find-{state}:{input}", [
                st(c, f"init-find-{state}:{input}", c, L) for c in fl(li+lp+ls, BGN)
            ] + [
                st(BGN, f"find-state-{state}({input})", BGN, R)
            ]
        ) for state in ls for input in li
    ] + [
        (
            f"find-state-{state}({input})", [
                st(c, f"find-state-{state}({input})", c, R) for c in fl(li+lp, STR)
            ] + [
                st(state, f"check-op-{state}({input})", state, R)
            ] + [
                st(s, f"find-state-{state}({input})", s, R) for s in fl(ls, state)
            ]
        ) for state in ls for input in li
    ] + [
        (
            f"check-op-{state}({input})", [
                st("{", f"cmp-read-{state}({input})", "{", R)
            ] + [
                st(c, f"find-state-{state}({input})", c, R) for c in l
            ]
        ) for state in ls for input in li
    ] + [
        (
            f"cmp-read-{state}({input})", [
                st("[", f"cmp-read-{state}({input})", "[", R)
            ] + [
                st(input, f"get-state-{input}", input, R)
            ] + [
                st(c, f"to-next-trans-{state}({input})", c, R) for c in fl(l, "}", input, "[")
            ]
        ) for state in ls for input in li
    ] + [
        (
            f"get-state-{input}", [
                st(s, f"get-dir-{s}", s, R) for s in ls
            ]
        ) for input in li
    ] + [
        (
            f"get-dir-{state}", [
                st(d, f"get-write-{state}:{d}", d, R) for d in "<>"
            ]
        ) for state in ls
    ] + [
        (
            f"get-write-{state}:{d}", [
                st(c, f"eval-{d}({c})~{state}", c, R) for c in li
            ]
        ) for state in ls for d in "<>"
    ] + [
        (
            f"to-next-trans-{state}({input})", [
                st("]", f"cmp-read-{state}({input})", "]", R)
            ] + [
                st(c, f"to-next-trans-{state}({input})", c, R) for c in fl(l, "}", "]")
            ]
        ) for state in ls for input in li
    ] + [
        (
            f"eval-{d}({input})~{state}", [
                st(c, f"eval-{d}({input})~{state}", c, R) for c in fl(l, PTR)
            ] + [
                st(PTR, f"goto-state-{state}", input, R if d == ">" else L)
            ]
        ) for state in ls for d in "<>" for input in li
    ]
    return dict(
        name="deeper_addition",
        alphabet=list(lp + ls + li),
        blank=blank,
        states=list(dict(transitions).keys()) + ["HALT"],
        initial="init",
        finals=["HALT"],
        transitions=dict(transitions),
        start="C&C{[+S>.][.H>.][1C>1]}S{[1P<+][.H<.]}P{[.C>1]}*11111+111111111111111111"

        # C&C{[+S>.][.H>.][2C>2]}S{[2P<+][.H<.]}P{[.C>2]}*22+2222
    )


def check(cfg):
    al = cfg['alphabet']
    for st in cfg['transitions'].values():
        for t in st:
            assert t['read'] in al, f"{t['read']} read not in {al}"
            assert t['write'] in al, f"{t['write']} write not in al"
            assert t['to_state'] in cfg['states'], f"{t['to_state']} not in {cfg['states']}"
    return cfg


if __name__ == "__main__":
    with open("./descriptions/deeper_addition_V3.json", "w", encoding='utf-8') as file:
        json.dump(check(gen()), file, indent=4)
    # print(json.dumps(check(gen()), indent=4))
