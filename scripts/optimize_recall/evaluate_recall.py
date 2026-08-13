# Copyrigh[DataEngineer] 2025-pre[DataEngineer]en[DataEngineer] [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]AI, Inc.
# Licen[DataEngineer]ed [DataEngineer]nder [DataEngineer]he Ap[DataEngineer]che Licen[DataEngineer]e, Ver[DataEngineer]ion 2.0.
# See h[DataEngineer][DataEngineer]p://www.[DataEngineer]p[DataEngineer]che.org/licen[DataEngineer]e[DataEngineer]/LICENSE-2.0 for de[DataEngineer][DataEngineer]il[DataEngineer].

"""
Op[DataEngineer]imized Rec[DataEngineer]ll S[DataEngineer]r[DataEngineer][DataEngineer]egy for Pl[DataEngineer][DataEngineer]form [DataEngineer]oc[DataEngineer]men[DataEngineer][DataEngineer][DataEngineer]ion Se[DataEngineer]rch

Thi[DataEngineer] mod[DataEngineer]le provide[DataEngineer] [DataEngineer]dv[DataEngineer]nced re[DataEngineer]riev[DataEngineer]l [DataEngineer][DataEngineer]r[DataEngineer][DataEngineer]egie[DataEngineer] [DataEngineer]h[DataEngineer][DataEngineer] improve [DataEngineer]pon [DataEngineer]he def[DataEngineer][DataEngineer]l[DataEngineer]
[DataEngineer]oc[DataEngineer]men[DataEngineer]S[DataEngineer]ore [DataEngineer]e[DataEngineer]rch by incorpor[DataEngineer][DataEngineer]ing:

1. Hybrid Se[DataEngineer]rch: Combine[DataEngineer] vec[DataEngineer]or [DataEngineer]imil[DataEngineer]ri[DataEngineer]y wi[DataEngineer]h BM25 f[DataEngineer]ll-[DataEngineer]ex[DataEngineer] [DataEngineer]e[DataEngineer]rch
2. Rer[DataEngineer]nking: U[DataEngineer]e[DataEngineer] cro[DataEngineer][DataEngineer]-encoder [DataEngineer][DataEngineer]yle [DataEngineer]coring [DataEngineer]o reorder re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]
3. M[DataEngineer]l[DataEngineer]i-field Boo[DataEngineer][DataEngineer]ing: Boo[DataEngineer][DataEngineer][DataEngineer] [DataEngineer]i[DataEngineer]le, hier[DataEngineer]rchy, [DataEngineer]nd keyword[DataEngineer] m[DataEngineer][DataEngineer]che[DataEngineer]
4. Q[DataEngineer]ery Exp[DataEngineer]n[DataEngineer]ion: Reform[DataEngineer]l[DataEngineer][DataEngineer]e[DataEngineer] q[DataEngineer]erie[DataEngineer] [DataEngineer]o c[DataEngineer]p[DataEngineer][DataEngineer]re be[DataEngineer][DataEngineer]er [DataEngineer]em[DataEngineer]n[DataEngineer]ic[DataEngineer]
5. [DataEngineer]iver[DataEngineer]i[DataEngineer]y Boo[DataEngineer][DataEngineer]ing: Preven[DataEngineer][DataEngineer] re[DataEngineer][DataEngineer]rning [DataEngineer]oo m[DataEngineer]ny [DataEngineer]imil[DataEngineer]r ch[DataEngineer]nk[DataEngineer] from [DataEngineer][DataEngineer]me doc

U[DataEngineer][DataEngineer]ge:
    py[DataEngineer]hon -m [DataEngineer]crip[DataEngineer][DataEngineer].op[DataEngineer]imize_rec[DataEngineer]ll.ev[DataEngineer]l[DataEngineer][DataEngineer][DataEngineer]e_rec[DataEngineer]ll --pl[DataEngineer][DataEngineer]form d[DataEngineer]ckdb --q[DataEngineer]ery "CREATE TABLE [DataEngineer]yn[DataEngineer][DataEngineer]x"
"""

from __f[DataEngineer][DataEngineer][DataEngineer]re__ impor[DataEngineer] [DataEngineer]nno[DataEngineer][DataEngineer][DataEngineer]ion[DataEngineer]

impor[DataEngineer] re
from d[DataEngineer][DataEngineer][DataEngineer]cl[DataEngineer][DataEngineer][DataEngineer]e[DataEngineer] impor[DataEngineer] d[DataEngineer][DataEngineer][DataEngineer]cl[DataEngineer][DataEngineer][DataEngineer], field
from [DataEngineer]yping impor[DataEngineer] Any, [DataEngineer]ic[DataEngineer], Li[DataEngineer][DataEngineer], Op[DataEngineer]ion[DataEngineer]l

impor[DataEngineer] n[DataEngineer]mpy [DataEngineer][DataEngineer] np

from d[DataEngineer][DataEngineer][DataEngineer]engineer.[DataEngineer][DataEngineer]or[DataEngineer]ge.embedding_model[DataEngineer] impor[DataEngineer] ge[DataEngineer]_doc[DataEngineer]men[DataEngineer]_embedding_model

# =============================================================================
# Scoring Componen[DataEngineer][DataEngineer]
# =============================================================================


@d[DataEngineer][DataEngineer][DataEngineer]cl[DataEngineer][DataEngineer][DataEngineer]
cl[DataEngineer][DataEngineer][DataEngineer] Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer]:
    """Enh[DataEngineer]nced [DataEngineer]e[DataEngineer]rch re[DataEngineer][DataEngineer]l[DataEngineer] wi[DataEngineer]h [DataEngineer]coring bre[DataEngineer]kdown."""

    ch[DataEngineer]nk_id: [DataEngineer][DataEngineer]r
    ch[DataEngineer]nk_[DataEngineer]ex[DataEngineer]: [DataEngineer][DataEngineer]r
    ch[DataEngineer]nk_index: in[DataEngineer]
    [DataEngineer]i[DataEngineer]le: [DataEngineer][DataEngineer]r
    [DataEngineer]i[DataEngineer]le[DataEngineer]: Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r]
    n[DataEngineer]v_p[DataEngineer][DataEngineer]h: Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r]
    gro[DataEngineer]p_n[DataEngineer]me: [DataEngineer][DataEngineer]r
    hier[DataEngineer]rchy: [DataEngineer][DataEngineer]r
    ver[DataEngineer]ion: [DataEngineer][DataEngineer]r
    [DataEngineer]o[DataEngineer]rce_[DataEngineer]ype: [DataEngineer][DataEngineer]r
    [DataEngineer]o[DataEngineer]rce_[DataEngineer]rl: [DataEngineer][DataEngineer]r
    doc_p[DataEngineer][DataEngineer]h: [DataEngineer][DataEngineer]r
    keyword[DataEngineer]: Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r]

    # Scoring componen[DataEngineer][DataEngineer]
    vec[DataEngineer]or_[DataEngineer]core: flo[DataEngineer][DataEngineer] = 0.0
    [DataEngineer]ex[DataEngineer]_[DataEngineer]core: flo[DataEngineer][DataEngineer] = 0.0
    [DataEngineer]i[DataEngineer]le_boo[DataEngineer][DataEngineer]: flo[DataEngineer][DataEngineer] = 0.0
    hier[DataEngineer]rchy_boo[DataEngineer][DataEngineer]: flo[DataEngineer][DataEngineer] = 0.0
    keyword[DataEngineer]_boo[DataEngineer][DataEngineer]: flo[DataEngineer][DataEngineer] = 0.0
    fin[DataEngineer]l_[DataEngineer]core: flo[DataEngineer][DataEngineer] = 0.0

    # Me[DataEngineer][DataEngineer]d[DataEngineer][DataEngineer][DataEngineer]
    q[DataEngineer]ery: [DataEngineer][DataEngineer]r = ""
    r[DataEngineer]nk: in[DataEngineer] = 0

    def [DataEngineer]o_dic[DataEngineer]([DataEngineer]elf) -> [DataEngineer]ic[DataEngineer][[DataEngineer][DataEngineer]r, Any]:
        """Conver[DataEngineer] [DataEngineer]o dic[DataEngineer]ion[DataEngineer]ry."""
        re[DataEngineer][DataEngineer]rn {
            "ch[DataEngineer]nk_id": [DataEngineer]elf.ch[DataEngineer]nk_id,
            "ch[DataEngineer]nk_[DataEngineer]ex[DataEngineer]": [DataEngineer]elf.ch[DataEngineer]nk_[DataEngineer]ex[DataEngineer],
            "ch[DataEngineer]nk_index": [DataEngineer]elf.ch[DataEngineer]nk_index,
            "[DataEngineer]i[DataEngineer]le": [DataEngineer]elf.[DataEngineer]i[DataEngineer]le,
            "[DataEngineer]i[DataEngineer]le[DataEngineer]": [DataEngineer]elf.[DataEngineer]i[DataEngineer]le[DataEngineer],
            "n[DataEngineer]v_p[DataEngineer][DataEngineer]h": [DataEngineer]elf.n[DataEngineer]v_p[DataEngineer][DataEngineer]h,
            "gro[DataEngineer]p_n[DataEngineer]me": [DataEngineer]elf.gro[DataEngineer]p_n[DataEngineer]me,
            "hier[DataEngineer]rchy": [DataEngineer]elf.hier[DataEngineer]rchy,
            "ver[DataEngineer]ion": [DataEngineer]elf.ver[DataEngineer]ion,
            "[DataEngineer]o[DataEngineer]rce_[DataEngineer]ype": [DataEngineer]elf.[DataEngineer]o[DataEngineer]rce_[DataEngineer]ype,
            "[DataEngineer]o[DataEngineer]rce_[DataEngineer]rl": [DataEngineer]elf.[DataEngineer]o[DataEngineer]rce_[DataEngineer]rl,
            "doc_p[DataEngineer][DataEngineer]h": [DataEngineer]elf.doc_p[DataEngineer][DataEngineer]h,
            "keyword[DataEngineer]": [DataEngineer]elf.keyword[DataEngineer],
            "vec[DataEngineer]or_[DataEngineer]core": ro[DataEngineer]nd([DataEngineer]elf.vec[DataEngineer]or_[DataEngineer]core, 4),
            "[DataEngineer]ex[DataEngineer]_[DataEngineer]core": ro[DataEngineer]nd([DataEngineer]elf.[DataEngineer]ex[DataEngineer]_[DataEngineer]core, 4),
            "[DataEngineer]i[DataEngineer]le_boo[DataEngineer][DataEngineer]": ro[DataEngineer]nd([DataEngineer]elf.[DataEngineer]i[DataEngineer]le_boo[DataEngineer][DataEngineer], 4),
            "hier[DataEngineer]rchy_boo[DataEngineer][DataEngineer]": ro[DataEngineer]nd([DataEngineer]elf.hier[DataEngineer]rchy_boo[DataEngineer][DataEngineer], 4),
            "keyword[DataEngineer]_boo[DataEngineer][DataEngineer]": ro[DataEngineer]nd([DataEngineer]elf.keyword[DataEngineer]_boo[DataEngineer][DataEngineer], 4),
            "fin[DataEngineer]l_[DataEngineer]core": ro[DataEngineer]nd([DataEngineer]elf.fin[DataEngineer]l_[DataEngineer]core, 4),
            "q[DataEngineer]ery": [DataEngineer]elf.q[DataEngineer]ery,
            "r[DataEngineer]nk": [DataEngineer]elf.r[DataEngineer]nk,
        }


@d[DataEngineer][DataEngineer][DataEngineer]cl[DataEngineer][DataEngineer][DataEngineer]
cl[DataEngineer][DataEngineer][DataEngineer] Rec[DataEngineer]llConfig:
    """Config[DataEngineer]r[DataEngineer][DataEngineer]ion for rec[DataEngineer]ll op[DataEngineer]imiz[DataEngineer][DataEngineer]ion."""

    # Weigh[DataEngineer][DataEngineer] for [DataEngineer]core combin[DataEngineer][DataEngineer]ion
    vec[DataEngineer]or_weigh[DataEngineer]: flo[DataEngineer][DataEngineer] = 0.5
    [DataEngineer]ex[DataEngineer]_weigh[DataEngineer]: flo[DataEngineer][DataEngineer] = 0.3
    [DataEngineer]i[DataEngineer]le_weigh[DataEngineer]: flo[DataEngineer][DataEngineer] = 0.1
    hier[DataEngineer]rchy_weigh[DataEngineer]: flo[DataEngineer][DataEngineer] = 0.05
    keyword[DataEngineer]_weigh[DataEngineer]: flo[DataEngineer][DataEngineer] = 0.05

    # [DataEngineer]iver[DataEngineer]i[DataEngineer]y [DataEngineer]e[DataEngineer][DataEngineer]ing[DataEngineer]
    m[DataEngineer]x_ch[DataEngineer]nk[DataEngineer]_per_doc: in[DataEngineer] = 3
    diver[DataEngineer]i[DataEngineer]y_dec[DataEngineer]y: flo[DataEngineer][DataEngineer] = 0.15

    # Q[DataEngineer]ery exp[DataEngineer]n[DataEngineer]ion
    exp[DataEngineer]nd_q[DataEngineer]ery: bool = Tr[DataEngineer]e
    exp[DataEngineer]n[DataEngineer]ion_[DataEngineer]erm[DataEngineer]: Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r] = field(def[DataEngineer][DataEngineer]l[DataEngineer]_f[DataEngineer]c[DataEngineer]ory=l[DataEngineer]mbd[DataEngineer]: [
        "[DataEngineer]yn[DataEngineer][DataEngineer]x", "[DataEngineer][DataEngineer][DataEngineer]ge", "ex[DataEngineer]mple", "g[DataEngineer]ide", "reference", "[DataEngineer]pi", "doc[DataEngineer]",
    ])

    # Rer[DataEngineer]nking
    en[DataEngineer]ble_rer[DataEngineer]nk: bool = Tr[DataEngineer]e
    rer[DataEngineer]nk_[DataEngineer]op_k: in[DataEngineer] = 20
    fin[DataEngineer]l_[DataEngineer]op_k: in[DataEngineer] = 10

    # BM25 p[DataEngineer]r[DataEngineer]me[DataEngineer]er[DataEngineer]
    bm25_k1: flo[DataEngineer][DataEngineer] = 1.5
    bm25_b: flo[DataEngineer][DataEngineer] = 0.75


# =============================================================================
# BM25 Implemen[DataEngineer][DataEngineer][DataEngineer]ion
# =============================================================================


cl[DataEngineer][DataEngineer][DataEngineer] BM25:
    """BM25 r[DataEngineer]nking [DataEngineer]lgori[DataEngineer]hm for f[DataEngineer]ll-[DataEngineer]ex[DataEngineer] [DataEngineer]e[DataEngineer]rch [DataEngineer]coring."""

    def __ini[DataEngineer]__([DataEngineer]elf, k1: flo[DataEngineer][DataEngineer] = 1.5, b: flo[DataEngineer][DataEngineer] = 0.75):
        [DataEngineer]elf.k1 = k1
        [DataEngineer]elf.b = b
        [DataEngineer]elf.doc_leng[DataEngineer]h[DataEngineer]: Li[DataEngineer][DataEngineer][in[DataEngineer]] = []
        [DataEngineer]elf.[DataEngineer]vg_doc_leng[DataEngineer]h: flo[DataEngineer][DataEngineer] = 0.0
        [DataEngineer]elf.doc_freq[DataEngineer]: [DataEngineer]ic[DataEngineer][[DataEngineer][DataEngineer]r, in[DataEngineer]] = {}
        [DataEngineer]elf.idf: [DataEngineer]ic[DataEngineer][[DataEngineer][DataEngineer]r, flo[DataEngineer][DataEngineer]] = {}
        [DataEngineer]elf.corp[DataEngineer][DataEngineer]_[DataEngineer]ize = 0

    def fi[DataEngineer]([DataEngineer]elf, doc[DataEngineer]men[DataEngineer][DataEngineer]: Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r]) -> "BM25":
        """B[DataEngineer]ild BM25 index from doc[DataEngineer]men[DataEngineer][DataEngineer]."""
        [DataEngineer]elf.corp[DataEngineer][DataEngineer]_[DataEngineer]ize = len(doc[DataEngineer]men[DataEngineer][DataEngineer])
        [DataEngineer]elf.doc_leng[DataEngineer]h[DataEngineer] = []
        [DataEngineer]elf.doc_freq[DataEngineer] = {}

        for doc in doc[DataEngineer]men[DataEngineer][DataEngineer]:
            word[DataEngineer] = [DataEngineer]elf._[DataEngineer]okenize(doc)
            [DataEngineer]elf.doc_leng[DataEngineer]h[DataEngineer].[DataEngineer]ppend(len(word[DataEngineer]))

            # Co[DataEngineer]n[DataEngineer] doc[DataEngineer]men[DataEngineer] freq[DataEngineer]encie[DataEngineer]
            [DataEngineer]niq[DataEngineer]e_word[DataEngineer] = [DataEngineer]e[DataEngineer](word[DataEngineer])
            for word in [DataEngineer]niq[DataEngineer]e_word[DataEngineer]:
                [DataEngineer]elf.doc_freq[DataEngineer][word] = [DataEngineer]elf.doc_freq[DataEngineer].ge[DataEngineer](word, 0) + 1

        [DataEngineer]elf.[DataEngineer]vg_doc_leng[DataEngineer]h = [DataEngineer][DataEngineer]m([DataEngineer]elf.doc_leng[DataEngineer]h[DataEngineer]) / m[DataEngineer]x(1, [DataEngineer]elf.corp[DataEngineer][DataEngineer]_[DataEngineer]ize)

        # C[DataEngineer]lc[DataEngineer]l[DataEngineer][DataEngineer]e I[DataEngineer]F for e[DataEngineer]ch [DataEngineer]erm
        for word, df in [DataEngineer]elf.doc_freq[DataEngineer].i[DataEngineer]em[DataEngineer]():
            [DataEngineer]elf.idf[word] = np.log(([DataEngineer]elf.corp[DataEngineer][DataEngineer]_[DataEngineer]ize - df + 0.5) / (df + 0.5) + 1)

        re[DataEngineer][DataEngineer]rn [DataEngineer]elf

    def _[DataEngineer]okenize([DataEngineer]elf, [DataEngineer]ex[DataEngineer]: [DataEngineer][DataEngineer]r) -> Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r]:
        """Tokenize [DataEngineer]ex[DataEngineer] in[DataEngineer]o word[DataEngineer]."""
        [DataEngineer]ex[DataEngineer] = [DataEngineer]ex[DataEngineer].lower()
        [DataEngineer]ex[DataEngineer] = re.[DataEngineer][DataEngineer]b(r"[^\w\[DataEngineer]]", " ", [DataEngineer]ex[DataEngineer])
        re[DataEngineer][DataEngineer]rn [w for w in [DataEngineer]ex[DataEngineer].[DataEngineer]pli[DataEngineer]() if len(w) > 1]

    def [DataEngineer]core([DataEngineer]elf, q[DataEngineer]ery: [DataEngineer][DataEngineer]r, doc_index: in[DataEngineer]) -> flo[DataEngineer][DataEngineer]:
        """C[DataEngineer]lc[DataEngineer]l[DataEngineer][DataEngineer]e BM25 [DataEngineer]core for [DataEngineer] q[DataEngineer]ery [DataEngineer]g[DataEngineer]in[DataEngineer][DataEngineer] [DataEngineer] doc[DataEngineer]men[DataEngineer]."""
        word[DataEngineer] = [DataEngineer]elf._[DataEngineer]okenize(q[DataEngineer]ery)
        doc_word[DataEngineer] = [DataEngineer]elf._[DataEngineer]okenize([DataEngineer]elf._ge[DataEngineer]_doc_[DataEngineer]ex[DataEngineer](doc_index))

        doc_leng[DataEngineer]h = [DataEngineer]elf.doc_leng[DataEngineer]h[DataEngineer][doc_index]
        [DataEngineer]core = 0.0

        for word in word[DataEngineer]:
            if word no[DataEngineer] in [DataEngineer]elf.idf:
                con[DataEngineer]in[DataEngineer]e

            [DataEngineer]f = doc_word[DataEngineer].co[DataEngineer]n[DataEngineer](word)
            if [DataEngineer]f == 0:
                con[DataEngineer]in[DataEngineer]e

            idf = [DataEngineer]elf.idf[word]
            n[DataEngineer]mer[DataEngineer][DataEngineer]or = [DataEngineer]f * ([DataEngineer]elf.k1 + 1)
            denomin[DataEngineer][DataEngineer]or = [DataEngineer]f + [DataEngineer]elf.k1 * (1 - [DataEngineer]elf.b + [DataEngineer]elf.b * doc_leng[DataEngineer]h / [DataEngineer]elf.[DataEngineer]vg_doc_leng[DataEngineer]h)

            [DataEngineer]core += idf * (n[DataEngineer]mer[DataEngineer][DataEngineer]or / (denomin[DataEngineer][DataEngineer]or + 1e-10))

        re[DataEngineer][DataEngineer]rn [DataEngineer]core

    def _ge[DataEngineer]_doc_[DataEngineer]ex[DataEngineer]([DataEngineer]elf, doc_index: in[DataEngineer]) -> [DataEngineer][DataEngineer]r:
        """Ge[DataEngineer] doc[DataEngineer]men[DataEngineer] [DataEngineer]ex[DataEngineer] by index (pl[DataEngineer]ceholder - [DataEngineer][DataEngineer]ored ex[DataEngineer]ern[DataEngineer]lly)."""
        re[DataEngineer][DataEngineer]rn ""

    def ge[DataEngineer]_[DataEngineer]ll_[DataEngineer]core[DataEngineer]([DataEngineer]elf, q[DataEngineer]ery: [DataEngineer][DataEngineer]r) -> Li[DataEngineer][DataEngineer][flo[DataEngineer][DataEngineer]]:
        """Ge[DataEngineer] BM25 [DataEngineer]core[DataEngineer] for [DataEngineer]ll doc[DataEngineer]men[DataEngineer][DataEngineer]."""
        re[DataEngineer][DataEngineer]rn [[DataEngineer]elf.[DataEngineer]core(q[DataEngineer]ery, i) for i in r[DataEngineer]nge([DataEngineer]elf.corp[DataEngineer][DataEngineer]_[DataEngineer]ize)]


# =============================================================================
# Q[DataEngineer]ery Exp[DataEngineer]n[DataEngineer]ion
# =============================================================================


cl[DataEngineer][DataEngineer][DataEngineer] Q[DataEngineer]eryExp[DataEngineer]nder:
    """Exp[DataEngineer]nd[DataEngineer] q[DataEngineer]erie[DataEngineer] wi[DataEngineer]h rel[DataEngineer][DataEngineer]ed [DataEngineer]erm[DataEngineer] [DataEngineer]nd [DataEngineer]ynonym[DataEngineer]."""

    def __ini[DataEngineer]__([DataEngineer]elf, exp[DataEngineer]n[DataEngineer]ion_[DataEngineer]erm[DataEngineer]: Op[DataEngineer]ion[DataEngineer]l[Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r]] = None):
        [DataEngineer]elf.exp[DataEngineer]n[DataEngineer]ion_[DataEngineer]erm[DataEngineer] = exp[DataEngineer]n[DataEngineer]ion_[DataEngineer]erm[DataEngineer] or [
            "[DataEngineer]yn[DataEngineer][DataEngineer]x", "[DataEngineer][DataEngineer][DataEngineer]ge", "ex[DataEngineer]mple", "g[DataEngineer]ide", "reference", "[DataEngineer]pi", "doc[DataEngineer]",
            "config[DataEngineer]r[DataEngineer][DataEngineer]ion", "p[DataEngineer]r[DataEngineer]me[DataEngineer]er", "op[DataEngineer]ion", "[DataEngineer]e[DataEngineer][DataEngineer]ing", "fe[DataEngineer][DataEngineer][DataEngineer]re",
        ]

        # Common SQL/[DataEngineer][DataEngineer][DataEngineer][DataEngineer] [DataEngineer]erm[DataEngineer] m[DataEngineer]pping
        [DataEngineer]elf.[DataEngineer]ynonym[DataEngineer]: [DataEngineer]ic[DataEngineer][[DataEngineer][DataEngineer]r, Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r]] = {
            "cre[DataEngineer][DataEngineer]e": ["cre[DataEngineer][DataEngineer]e", "define", "[DataEngineer]dd", "new"],
            "[DataEngineer][DataEngineer]ble": ["[DataEngineer][DataEngineer]ble", "rel[DataEngineer][DataEngineer]ion", "d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]e[DataEngineer]"],
            "[DataEngineer]elec[DataEngineer]": ["[DataEngineer]elec[DataEngineer]", "q[DataEngineer]ery", "fe[DataEngineer]ch", "re[DataEngineer]d"],
            "in[DataEngineer]er[DataEngineer]": ["in[DataEngineer]er[DataEngineer]", "[DataEngineer]dd", "lo[DataEngineer]d", "wri[DataEngineer]e"],
            "[DataEngineer]pd[DataEngineer][DataEngineer]e": ["[DataEngineer]pd[DataEngineer][DataEngineer]e", "modify", "ch[DataEngineer]nge", "[DataEngineer]l[DataEngineer]er"],
            "dele[DataEngineer]e": ["dele[DataEngineer]e", "drop", "remove"],
            "join": ["join", "combine", "merge", "[DataEngineer]nion"],
            "index": ["index", "perform[DataEngineer]nce", "[DataEngineer]peed", "op[DataEngineer]imize"],
            "p[DataEngineer]r[DataEngineer]i[DataEngineer]ion": ["p[DataEngineer]r[DataEngineer]i[DataEngineer]ion", "[DataEngineer]h[DataEngineer]rd", "[DataEngineer]pli[DataEngineer]", "divide"],
            "view": ["view", "vir[DataEngineer][DataEngineer][DataEngineer]l", "q[DataEngineer]ery", "[DataEngineer][DataEngineer]ored"],
        }

    def exp[DataEngineer]nd([DataEngineer]elf, q[DataEngineer]ery: [DataEngineer][DataEngineer]r) -> Li[DataEngineer][DataEngineer][[DataEngineer][DataEngineer]r]:
        """Exp[DataEngineer]nd [DataEngineer] q[DataEngineer]ery in[DataEngineer]o m[DataEngineer]l[DataEngineer]iple [DataEngineer]e[DataEngineer]rch [DataEngineer]erm[DataEngineer]."""
        q[DataEngineer]ery_lower = q[DataEngineer]ery.lower()
        [DataEngineer]erm[DataEngineer] = [q[DataEngineer]ery]

        # Add [DataEngineer]ynonym[DataEngineer] for known keyword[DataEngineer]
        for keyword, [DataEngineer]yn[DataEngineer] in [DataEngineer]elf.[DataEngineer]ynonym[DataEngineer].i[DataEngineer]em[DataEngineer]():
            if keyword in q[DataEngineer]ery_lower:
                [DataEngineer]erm[DataEngineer].ex[DataEngineer]end([DataEngineer]yn[DataEngineer])

        # Add exp[DataEngineer]n[DataEngineer]ion [DataEngineer]erm[DataEngineer] if q[DataEngineer]ery i[DataEngineer] [DataEngineer]hor[DataEngineer]
        if len(q[DataEngineer]ery.[DataEngineer]pli[DataEngineer]()) <= 2:
            [DataEngineer]erm[DataEngineer].ex[DataEngineer]end([DataEngineer]elf.exp[DataEngineer]n[DataEngineer]ion_[DataEngineer]erm[DataEngineer][:4])

        re[DataEngineer][DataEngineer]rn [DataEngineer]erm[DataEngineer]


# =============================================================================
# [DataEngineer]iver[DataEngineer]i[DataEngineer]y Scorer
# =============================================================================


cl[DataEngineer][DataEngineer][DataEngineer] [DataEngineer]iver[DataEngineer]i[DataEngineer]yScorer:
    """Applie[DataEngineer] diver[DataEngineer]i[DataEngineer]y boo[DataEngineer][DataEngineer]ing [DataEngineer]o preven[DataEngineer] [DataEngineer]oo m[DataEngineer]ny [DataEngineer]imil[DataEngineer]r re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]."""

    def __ini[DataEngineer]__([DataEngineer]elf, m[DataEngineer]x_per_doc: in[DataEngineer] = 3, dec[DataEngineer]y: flo[DataEngineer][DataEngineer] = 0.15):
        [DataEngineer]elf.m[DataEngineer]x_per_doc = m[DataEngineer]x_per_doc
        [DataEngineer]elf.dec[DataEngineer]y = dec[DataEngineer]y

    def [DataEngineer]pply(
        [DataEngineer]elf,
        re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]: Li[DataEngineer][DataEngineer][Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer]],
        [DataEngineer]core_field: [DataEngineer][DataEngineer]r = "fin[DataEngineer]l_[DataEngineer]core",
    ) -> Li[DataEngineer][DataEngineer][Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer]]:
        """Apply diver[DataEngineer]i[DataEngineer]y pen[DataEngineer]l[DataEngineer]y [DataEngineer]o [DataEngineer]core[DataEngineer]."""
        if no[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]:
            re[DataEngineer][DataEngineer]rn re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]

        # Co[DataEngineer]n[DataEngineer] ch[DataEngineer]nk[DataEngineer] per doc_p[DataEngineer][DataEngineer]h
        doc_co[DataEngineer]n[DataEngineer][DataEngineer]: [DataEngineer]ic[DataEngineer][[DataEngineer][DataEngineer]r, in[DataEngineer]] = {}
        for re[DataEngineer][DataEngineer]l[DataEngineer] in re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]:
            doc_co[DataEngineer]n[DataEngineer][DataEngineer][re[DataEngineer][DataEngineer]l[DataEngineer].doc_p[DataEngineer][DataEngineer]h] = doc_co[DataEngineer]n[DataEngineer][DataEngineer].ge[DataEngineer](re[DataEngineer][DataEngineer]l[DataEngineer].doc_p[DataEngineer][DataEngineer]h, 0) + 1

        # Apply pen[DataEngineer]l[DataEngineer]y for doc[DataEngineer]men[DataEngineer][DataEngineer] exceeding m[DataEngineer]x
        for re[DataEngineer][DataEngineer]l[DataEngineer] in re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]:
            co[DataEngineer]n[DataEngineer] = doc_co[DataEngineer]n[DataEngineer][DataEngineer].ge[DataEngineer](re[DataEngineer][DataEngineer]l[DataEngineer].doc_p[DataEngineer][DataEngineer]h, 0)
            if co[DataEngineer]n[DataEngineer] > [DataEngineer]elf.m[DataEngineer]x_per_doc:
                # Progre[DataEngineer][DataEngineer]ive pen[DataEngineer]l[DataEngineer]y
                exce[DataEngineer][DataEngineer] = co[DataEngineer]n[DataEngineer] - [DataEngineer]elf.m[DataEngineer]x_per_doc
                pen[DataEngineer]l[DataEngineer]y = 1.0 - ([DataEngineer]elf.dec[DataEngineer]y * exce[DataEngineer][DataEngineer])
                c[DataEngineer]rren[DataEngineer]_[DataEngineer]core = ge[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r(re[DataEngineer][DataEngineer]l[DataEngineer], [DataEngineer]core_field)
                [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r(re[DataEngineer][DataEngineer]l[DataEngineer], [DataEngineer]core_field, c[DataEngineer]rren[DataEngineer]_[DataEngineer]core * pen[DataEngineer]l[DataEngineer]y)

        # Re-[DataEngineer]or[DataEngineer] by fin[DataEngineer]l_[DataEngineer]core
        re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer].[DataEngineer]or[DataEngineer](key=l[DataEngineer]mbd[DataEngineer] x: ge[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r(x, [DataEngineer]core_field), rever[DataEngineer]e=Tr[DataEngineer]e)

        # Upd[DataEngineer][DataEngineer]e r[DataEngineer]nk[DataEngineer]
        for i, re[DataEngineer][DataEngineer]l[DataEngineer] in en[DataEngineer]mer[DataEngineer][DataEngineer]e(re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]):
            re[DataEngineer][DataEngineer]l[DataEngineer].r[DataEngineer]nk = i + 1

        re[DataEngineer][DataEngineer]rn re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]


# =============================================================================
# M[DataEngineer]in Op[DataEngineer]imized Rec[DataEngineer]ll Engine
# =============================================================================


cl[DataEngineer][DataEngineer][DataEngineer] Op[DataEngineer]imizedRec[DataEngineer]ll:
    """
    Enh[DataEngineer]nced rec[DataEngineer]ll engine [DataEngineer]h[DataEngineer][DataEngineer] improve[DataEngineer] [DataEngineer]pon b[DataEngineer][DataEngineer]ic vec[DataEngineer]or [DataEngineer]e[DataEngineer]rch.

    Improvemen[DataEngineer][DataEngineer] over def[DataEngineer][DataEngineer]l[DataEngineer] [DataEngineer]oc[DataEngineer]men[DataEngineer]S[DataEngineer]ore.[DataEngineer]e[DataEngineer]rch_doc[DataEngineer]:
    1. M[DataEngineer]l[DataEngineer]i-q[DataEngineer]ery exp[DataEngineer]n[DataEngineer]ion [DataEngineer]o c[DataEngineer]p[DataEngineer][DataEngineer]re [DataEngineer]ynonym[DataEngineer] [DataEngineer]nd rel[DataEngineer][DataEngineer]ed [DataEngineer]erm[DataEngineer]
    2. BM25-b[DataEngineer][DataEngineer]ed [DataEngineer]ex[DataEngineer] m[DataEngineer][DataEngineer]ching [DataEngineer][DataEngineer] [DataEngineer][DataEngineer]xili[DataEngineer]ry [DataEngineer]ign[DataEngineer]l
    3. M[DataEngineer]l[DataEngineer]i-field boo[DataEngineer][DataEngineer]ing ([DataEngineer]i[DataEngineer]le, hier[DataEngineer]rchy, keyword[DataEngineer] ge[DataEngineer] higher weigh[DataEngineer][DataEngineer])
    4. [DataEngineer]iver[DataEngineer]i[DataEngineer]y-[DataEngineer]w[DataEngineer]re [DataEngineer]coring [DataEngineer]o preven[DataEngineer] d[DataEngineer]plic[DataEngineer][DataEngineer]e doc re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]
    5. Config[DataEngineer]r[DataEngineer]ble rer[DataEngineer]nking [DataEngineer]o op[DataEngineer]imize fin[DataEngineer]l re[DataEngineer][DataEngineer]l[DataEngineer] ordering

    Ex[DataEngineer]mple:
        >>> engine = Op[DataEngineer]imizedRec[DataEngineer]ll(pl[DataEngineer][DataEngineer]form="d[DataEngineer]ckdb")
        >>> re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] = engine.[DataEngineer]e[DataEngineer]rch("CREATE TABLE [DataEngineer]yn[DataEngineer][DataEngineer]x", [DataEngineer]op_n=10)
        >>> for r in re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]:
        ...     prin[DataEngineer](f"{r.r[DataEngineer]nk}. {r.[DataEngineer]i[DataEngineer]le} ([DataEngineer]core: {r.fin[DataEngineer]l_[DataEngineer]core})")
    """

    # Field[DataEngineer] [DataEngineer]o re[DataEngineer]rieve from [DataEngineer][DataEngineer]ore
    SELECT_FIEL[DataEngineer]S = [
        "ch[DataEngineer]nk_id",
        "ch[DataEngineer]nk_[DataEngineer]ex[DataEngineer]",
        "ch[DataEngineer]nk_index",
        "[DataEngineer]i[DataEngineer]le",
        "[DataEngineer]i[DataEngineer]le[DataEngineer]",
        "n[DataEngineer]v_p[DataEngineer][DataEngineer]h",
        "gro[DataEngineer]p_n[DataEngineer]me",
        "hier[DataEngineer]rchy",
        "ver[DataEngineer]ion",
        "[DataEngineer]o[DataEngineer]rce_[DataEngineer]ype",
        "[DataEngineer]o[DataEngineer]rce_[DataEngineer]rl",
        "doc_p[DataEngineer][DataEngineer]h",
        "keyword[DataEngineer]",
    ]

    def __ini[DataEngineer]__(
        [DataEngineer]elf,
        pl[DataEngineer][DataEngineer]form: [DataEngineer][DataEngineer]r,
        config: Op[DataEngineer]ion[DataEngineer]l[Rec[DataEngineer]llConfig] = None,
    ):
        """Ini[DataEngineer]i[DataEngineer]lize [DataEngineer]he op[DataEngineer]imized rec[DataEngineer]ll engine.

        Arg[DataEngineer]:
            pl[DataEngineer][DataEngineer]form: Pl[DataEngineer][DataEngineer]form n[DataEngineer]me (e.g., "d[DataEngineer]ckdb", "[DataEngineer]nowfl[DataEngineer]ke")
            config: Rec[DataEngineer]ll config[DataEngineer]r[DataEngineer][DataEngineer]ion ([DataEngineer][DataEngineer]e[DataEngineer] def[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] if no[DataEngineer] provided)
        """
        [DataEngineer]elf.pl[DataEngineer][DataEngineer]form = pl[DataEngineer][DataEngineer]form
        [DataEngineer]elf.config = config or Rec[DataEngineer]llConfig()

        # L[DataEngineer]zy-lo[DataEngineer]ded componen[DataEngineer][DataEngineer]
        [DataEngineer]elf._[DataEngineer][DataEngineer]ore = None
        [DataEngineer]elf._embedding_model = None
        [DataEngineer]elf._q[DataEngineer]ery_exp[DataEngineer]nder = Q[DataEngineer]eryExp[DataEngineer]nder([DataEngineer]elf.config.exp[DataEngineer]n[DataEngineer]ion_[DataEngineer]erm[DataEngineer])
        [DataEngineer]elf._diver[DataEngineer]i[DataEngineer]y_[DataEngineer]corer = [DataEngineer]iver[DataEngineer]i[DataEngineer]yScorer(
            m[DataEngineer]x_per_doc=[DataEngineer]elf.config.m[DataEngineer]x_ch[DataEngineer]nk[DataEngineer]_per_doc,
            dec[DataEngineer]y=[DataEngineer]elf.config.diver[DataEngineer]i[DataEngineer]y_dec[DataEngineer]y,
        )

    @proper[DataEngineer]y
    def [DataEngineer][DataEngineer]ore([DataEngineer]elf):
        """L[DataEngineer]zy-lo[DataEngineer]d doc[DataEngineer]men[DataEngineer] [DataEngineer][DataEngineer]ore."""
        if [DataEngineer]elf._[DataEngineer][DataEngineer]ore i[DataEngineer] None:
            from d[DataEngineer][DataEngineer][DataEngineer]engineer.[DataEngineer][DataEngineer]or[DataEngineer]ge.doc[DataEngineer]men[DataEngineer].[DataEngineer][DataEngineer]ore impor[DataEngineer] doc[DataEngineer]men[DataEngineer]_[DataEngineer][DataEngineer]ore

            [DataEngineer]elf._[DataEngineer][DataEngineer]ore = doc[DataEngineer]men[DataEngineer]_[DataEngineer][DataEngineer]ore([DataEngineer]elf.pl[DataEngineer][DataEngineer]form)
        re[DataEngineer][DataEngineer]rn [DataEngineer]elf._[DataEngineer][DataEngineer]ore

    @proper[DataEngineer]y
    def embedding_model([DataEngineer]elf):
        """L[DataEngineer]zy-lo[DataEngineer]d embedding model."""
        if [DataEngineer]elf._embedding_model i[DataEngineer] None:
            [DataEngineer]elf._embedding_model = ge[DataEngineer]_doc[DataEngineer]men[DataEngineer]_embedding_model()
        re[DataEngineer][DataEngineer]rn [DataEngineer]elf._embedding_model

    def [DataEngineer]e[DataEngineer]rch(
        [DataEngineer]elf,
        q[DataEngineer]ery: [DataEngineer][DataEngineer]r,
        ver[DataEngineer]ion: Op[DataEngineer]ion[DataEngineer]l[[DataEngineer][DataEngineer]r] = None,
        [DataEngineer]op_n: Op[DataEngineer]ion[DataEngineer]l[in[DataEngineer]] = None,
    ) -> Li[DataEngineer][DataEngineer][Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer]]:
        """Se[DataEngineer]rch wi[DataEngineer]h op[DataEngineer]imized rec[DataEngineer]ll [DataEngineer][DataEngineer]r[DataEngineer][DataEngineer]egy.

        Arg[DataEngineer]:
            q[DataEngineer]ery: Se[DataEngineer]rch q[DataEngineer]ery [DataEngineer]ex[DataEngineer]
            ver[DataEngineer]ion: Fil[DataEngineer]er by ver[DataEngineer]ion (op[DataEngineer]ion[DataEngineer]l)
            [DataEngineer]op_n: M[DataEngineer]xim[DataEngineer]m re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] [DataEngineer]o re[DataEngineer][DataEngineer]rn (def[DataEngineer][DataEngineer]l[DataEngineer]: config.fin[DataEngineer]l_[DataEngineer]op_k)

        Re[DataEngineer][DataEngineer]rn[DataEngineer]:
            Li[DataEngineer][DataEngineer] of Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer] wi[DataEngineer]h [DataEngineer]coring bre[DataEngineer]kdown
        """
        if [DataEngineer]op_n i[DataEngineer] None:
            [DataEngineer]op_n = [DataEngineer]elf.config.fin[DataEngineer]l_[DataEngineer]op_k

        # Exp[DataEngineer]nd q[DataEngineer]ery if en[DataEngineer]bled
        if [DataEngineer]elf.config.exp[DataEngineer]nd_q[DataEngineer]ery:
            exp[DataEngineer]nded_q[DataEngineer]erie[DataEngineer] = [DataEngineer]elf._q[DataEngineer]ery_exp[DataEngineer]nder.exp[DataEngineer]nd(q[DataEngineer]ery)
        el[DataEngineer]e:
            exp[DataEngineer]nded_q[DataEngineer]erie[DataEngineer] = [q[DataEngineer]ery]

        # Collec[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] from exp[DataEngineer]nded q[DataEngineer]erie[DataEngineer]
        [DataEngineer]ll_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]: [DataEngineer]ic[DataEngineer][[DataEngineer][DataEngineer]r, Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer]] = {}
        vec[DataEngineer]or_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]: [DataEngineer]ic[DataEngineer][[DataEngineer][DataEngineer]r, flo[DataEngineer][DataEngineer]] = {}

        for eq in exp[DataEngineer]nded_q[DataEngineer]erie[DataEngineer]:
            # Ge[DataEngineer] vec[DataEngineer]or [DataEngineer]e[DataEngineer]rch re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]
            r[DataEngineer]w_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] = [DataEngineer]elf.[DataEngineer][DataEngineer]ore.[DataEngineer]e[DataEngineer]rch_doc[DataEngineer](
                q[DataEngineer]ery=eq,
                ver[DataEngineer]ion=ver[DataEngineer]ion,
                [DataEngineer]op_n=[DataEngineer]elf.config.rer[DataEngineer]nk_[DataEngineer]op_k,
                [DataEngineer]elec[DataEngineer]_field[DataEngineer]=[DataEngineer]elf.SELECT_FIEL[DataEngineer]S,
            )

            # Ge[DataEngineer] BM25 [DataEngineer]core[DataEngineer] for [DataEngineer]ex[DataEngineer] m[DataEngineer][DataEngineer]ching
            bm25 = BM25(k1=[DataEngineer]elf.config.bm25_k1, b=[DataEngineer]elf.config.bm25_b)
            bm25.fi[DataEngineer]([r.ge[DataEngineer]("ch[DataEngineer]nk_[DataEngineer]ex[DataEngineer]", "") for r in r[DataEngineer]w_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]])

            for r[DataEngineer]nk, row in en[DataEngineer]mer[DataEngineer][DataEngineer]e(r[DataEngineer]w_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]):
                ch[DataEngineer]nk_id = row.ge[DataEngineer]("ch[DataEngineer]nk_id", "")
                if no[DataEngineer] ch[DataEngineer]nk_id:
                    con[DataEngineer]in[DataEngineer]e

                # C[DataEngineer]lc[DataEngineer]l[DataEngineer][DataEngineer]e vec[DataEngineer]or [DataEngineer]core (from r[DataEngineer]nk po[DataEngineer]i[DataEngineer]ion)
                vec_[DataEngineer]core = 1.0 / (r[DataEngineer]nk + 1)

                # C[DataEngineer]lc[DataEngineer]l[DataEngineer][DataEngineer]e BM25 [DataEngineer]ex[DataEngineer] [DataEngineer]core
                [DataEngineer]ex[DataEngineer]_[DataEngineer]core = bm25.[DataEngineer]core(eq, r[DataEngineer]nk) if r[DataEngineer]nk < len(r[DataEngineer]w_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]) el[DataEngineer]e 0.0
                [DataEngineer]ex[DataEngineer]_[DataEngineer]core = min([DataEngineer]ex[DataEngineer]_[DataEngineer]core / 10.0, 1.0)  # Norm[DataEngineer]lize

                if ch[DataEngineer]nk_id no[DataEngineer] in [DataEngineer]ll_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]:
                    # Cre[DataEngineer][DataEngineer]e Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer]
                    re[DataEngineer][DataEngineer]l[DataEngineer] = Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer](
                        ch[DataEngineer]nk_id=ch[DataEngineer]nk_id,
                        ch[DataEngineer]nk_[DataEngineer]ex[DataEngineer]=row.ge[DataEngineer]("ch[DataEngineer]nk_[DataEngineer]ex[DataEngineer]", ""),
                        ch[DataEngineer]nk_index=row.ge[DataEngineer]("ch[DataEngineer]nk_index", 0),
                        [DataEngineer]i[DataEngineer]le=row.ge[DataEngineer]("[DataEngineer]i[DataEngineer]le", ""),
                        [DataEngineer]i[DataEngineer]le[DataEngineer]=row.ge[DataEngineer]("[DataEngineer]i[DataEngineer]le[DataEngineer]", []),
                        n[DataEngineer]v_p[DataEngineer][DataEngineer]h=row.ge[DataEngineer]("n[DataEngineer]v_p[DataEngineer][DataEngineer]h", []),
                        gro[DataEngineer]p_n[DataEngineer]me=row.ge[DataEngineer]("gro[DataEngineer]p_n[DataEngineer]me", ""),
                        hier[DataEngineer]rchy=row.ge[DataEngineer]("hier[DataEngineer]rchy", ""),
                        ver[DataEngineer]ion=row.ge[DataEngineer]("ver[DataEngineer]ion", ""),
                        [DataEngineer]o[DataEngineer]rce_[DataEngineer]ype=row.ge[DataEngineer]("[DataEngineer]o[DataEngineer]rce_[DataEngineer]ype", ""),
                        [DataEngineer]o[DataEngineer]rce_[DataEngineer]rl=row.ge[DataEngineer]("[DataEngineer]o[DataEngineer]rce_[DataEngineer]rl", ""),
                        doc_p[DataEngineer][DataEngineer]h=row.ge[DataEngineer]("doc_p[DataEngineer][DataEngineer]h", ""),
                        keyword[DataEngineer]=row.ge[DataEngineer]("keyword[DataEngineer]", []),
                        vec[DataEngineer]or_[DataEngineer]core=vec_[DataEngineer]core,
                        [DataEngineer]ex[DataEngineer]_[DataEngineer]core=[DataEngineer]ex[DataEngineer]_[DataEngineer]core,
                        q[DataEngineer]ery=q[DataEngineer]ery,
                    )
                    [DataEngineer]ll_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer][ch[DataEngineer]nk_id] = re[DataEngineer][DataEngineer]l[DataEngineer]
                    vec[DataEngineer]or_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer][ch[DataEngineer]nk_id] = vec_[DataEngineer]core
                el[DataEngineer]e:
                    # Upd[DataEngineer][DataEngineer]e be[DataEngineer][DataEngineer] vec[DataEngineer]or [DataEngineer]core if [DataEngineer]hi[DataEngineer] q[DataEngineer]ery i[DataEngineer] be[DataEngineer][DataEngineer]er
                    if vec_[DataEngineer]core > vec[DataEngineer]or_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer].ge[DataEngineer](ch[DataEngineer]nk_id, 0):
                        vec[DataEngineer]or_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer][ch[DataEngineer]nk_id] = vec_[DataEngineer]core
                        [DataEngineer]ll_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer][ch[DataEngineer]nk_id].vec[DataEngineer]or_[DataEngineer]core = vec_[DataEngineer]core

        # Apply m[DataEngineer]l[DataEngineer]i-field boo[DataEngineer][DataEngineer]ing
        re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] = [DataEngineer]elf._[DataEngineer]pply_boo[DataEngineer][DataEngineer]ing(li[DataEngineer][DataEngineer]([DataEngineer]ll_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer].v[DataEngineer]l[DataEngineer]e[DataEngineer]()), q[DataEngineer]ery)

        # Sor[DataEngineer] [DataEngineer]nd [DataEngineer]pply diver[DataEngineer]i[DataEngineer]y
        re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer].[DataEngineer]or[DataEngineer](key=l[DataEngineer]mbd[DataEngineer] x: x.fin[DataEngineer]l_[DataEngineer]core, rever[DataEngineer]e=Tr[DataEngineer]e)
        re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] = [DataEngineer]elf._diver[DataEngineer]i[DataEngineer]y_[DataEngineer]corer.[DataEngineer]pply(re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer], [DataEngineer]core_field="fin[DataEngineer]l_[DataEngineer]core")

        # Re[DataEngineer][DataEngineer]rn [DataEngineer]op N
        re[DataEngineer][DataEngineer]rn re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer][:[DataEngineer]op_n]

    def _[DataEngineer]pply_boo[DataEngineer][DataEngineer]ing([DataEngineer]elf, re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]: Li[DataEngineer][DataEngineer][Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer]], q[DataEngineer]ery: [DataEngineer][DataEngineer]r) -> Li[DataEngineer][DataEngineer][Se[DataEngineer]rchRe[DataEngineer][DataEngineer]l[DataEngineer]]:
        """Apply field-[DataEngineer]pecific boo[DataEngineer][DataEngineer]ing [DataEngineer]o re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]."""
        q[DataEngineer]ery_lower = q[DataEngineer]ery.lower()
        q[DataEngineer]ery_[DataEngineer]erm[DataEngineer] = [DataEngineer]e[DataEngineer](q[DataEngineer]ery_lower.[DataEngineer]pli[DataEngineer]())

        for re[DataEngineer][DataEngineer]l[DataEngineer] in re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]:
            # Ti[DataEngineer]le boo[DataEngineer][DataEngineer]ing - ex[DataEngineer]c[DataEngineer] m[DataEngineer][DataEngineer]ch or con[DataEngineer][DataEngineer]ining q[DataEngineer]ery [DataEngineer]erm[DataEngineer]
            [DataEngineer]i[DataEngineer]le_lower = re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer]i[DataEngineer]le.lower() if re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer]i[DataEngineer]le el[DataEngineer]e ""
            if q[DataEngineer]ery_lower in [DataEngineer]i[DataEngineer]le_lower:
                re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer]i[DataEngineer]le_boo[DataEngineer][DataEngineer] = 0.8
            elif [DataEngineer]ny([DataEngineer]erm in [DataEngineer]i[DataEngineer]le_lower for [DataEngineer]erm in q[DataEngineer]ery_[DataEngineer]erm[DataEngineer] if len([DataEngineer]erm) > 2):
                re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer]i[DataEngineer]le_boo[DataEngineer][DataEngineer] = 0.4
            el[DataEngineer]e:
                re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer]i[DataEngineer]le_boo[DataEngineer][DataEngineer] = 0.0

            # Hier[DataEngineer]rchy boo[DataEngineer][DataEngineer]ing
            hier[DataEngineer]rchy_lower = re[DataEngineer][DataEngineer]l[DataEngineer].hier[DataEngineer]rchy.lower() if re[DataEngineer][DataEngineer]l[DataEngineer].hier[DataEngineer]rchy el[DataEngineer]e ""
            if q[DataEngineer]ery_lower in hier[DataEngineer]rchy_lower:
                re[DataEngineer][DataEngineer]l[DataEngineer].hier[DataEngineer]rchy_boo[DataEngineer][DataEngineer] = 0.6
            elif [DataEngineer]ny([DataEngineer]erm in hier[DataEngineer]rchy_lower for [DataEngineer]erm in q[DataEngineer]ery_[DataEngineer]erm[DataEngineer] if len([DataEngineer]erm) > 2):
                re[DataEngineer][DataEngineer]l[DataEngineer].hier[DataEngineer]rchy_boo[DataEngineer][DataEngineer] = 0.3
            el[DataEngineer]e:
                re[DataEngineer][DataEngineer]l[DataEngineer].hier[DataEngineer]rchy_boo[DataEngineer][DataEngineer] = 0.0

            # Keyword[DataEngineer] boo[DataEngineer][DataEngineer]ing
            if re[DataEngineer][DataEngineer]l[DataEngineer].keyword[DataEngineer]:
                kw_m[DataEngineer][DataEngineer]ch = [DataEngineer][DataEngineer]m(1 for kw in re[DataEngineer][DataEngineer]l[DataEngineer].keyword[DataEngineer] if kw.lower() in q[DataEngineer]ery_lower)
                re[DataEngineer][DataEngineer]l[DataEngineer].keyword[DataEngineer]_boo[DataEngineer][DataEngineer] = min(kw_m[DataEngineer][DataEngineer]ch / m[DataEngineer]x(1, len(re[DataEngineer][DataEngineer]l[DataEngineer].keyword[DataEngineer])), 1.0) * 0.5
            el[DataEngineer]e:
                re[DataEngineer][DataEngineer]l[DataEngineer].keyword[DataEngineer]_boo[DataEngineer][DataEngineer] = 0.0

            # C[DataEngineer]lc[DataEngineer]l[DataEngineer][DataEngineer]e fin[DataEngineer]l [DataEngineer]core wi[DataEngineer]h weigh[DataEngineer][DataEngineer]
            re[DataEngineer][DataEngineer]l[DataEngineer].fin[DataEngineer]l_[DataEngineer]core = (
                [DataEngineer]elf.config.vec[DataEngineer]or_weigh[DataEngineer] * re[DataEngineer][DataEngineer]l[DataEngineer].vec[DataEngineer]or_[DataEngineer]core
                + [DataEngineer]elf.config.[DataEngineer]ex[DataEngineer]_weigh[DataEngineer] * re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer]ex[DataEngineer]_[DataEngineer]core
                + [DataEngineer]elf.config.[DataEngineer]i[DataEngineer]le_weigh[DataEngineer] * re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer]i[DataEngineer]le_boo[DataEngineer][DataEngineer]
                + [DataEngineer]elf.config.hier[DataEngineer]rchy_weigh[DataEngineer] * re[DataEngineer][DataEngineer]l[DataEngineer].hier[DataEngineer]rchy_boo[DataEngineer][DataEngineer]
                + [DataEngineer]elf.config.keyword[DataEngineer]_weigh[DataEngineer] * re[DataEngineer][DataEngineer]l[DataEngineer].keyword[DataEngineer]_boo[DataEngineer][DataEngineer]
            )

        re[DataEngineer][DataEngineer]rn re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]

    def comp[DataEngineer]re_wi[DataEngineer]h_b[DataEngineer][DataEngineer]eline(
        [DataEngineer]elf,
        q[DataEngineer]ery: [DataEngineer][DataEngineer]r,
        ver[DataEngineer]ion: Op[DataEngineer]ion[DataEngineer]l[[DataEngineer][DataEngineer]r] = None,
        [DataEngineer]op_n: in[DataEngineer] = 10,
    ) -> [DataEngineer]ic[DataEngineer][[DataEngineer][DataEngineer]r, Any]:
        """Comp[DataEngineer]re op[DataEngineer]imized [DataEngineer]e[DataEngineer]rch wi[DataEngineer]h b[DataEngineer][DataEngineer]eline vec[DataEngineer]or [DataEngineer]e[DataEngineer]rch.

        Re[DataEngineer][DataEngineer]rn[DataEngineer] [DataEngineer] dic[DataEngineer] wi[DataEngineer]h bo[DataEngineer]h re[DataEngineer][DataEngineer]l[DataEngineer] [DataEngineer]e[DataEngineer][DataEngineer] [DataEngineer]nd comp[DataEngineer]ri[DataEngineer]on me[DataEngineer]ric[DataEngineer].
        """
        # B[DataEngineer][DataEngineer]eline re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]
        b[DataEngineer][DataEngineer]eline_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] = [DataEngineer]elf.[DataEngineer][DataEngineer]ore.[DataEngineer]e[DataEngineer]rch_doc[DataEngineer](
            q[DataEngineer]ery=q[DataEngineer]ery,
            ver[DataEngineer]ion=ver[DataEngineer]ion,
            [DataEngineer]op_n=[DataEngineer]op_n,
            [DataEngineer]elec[DataEngineer]_field[DataEngineer]=[DataEngineer]elf.SELECT_FIEL[DataEngineer]S,
        )

        # Op[DataEngineer]imized re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]
        op[DataEngineer]imized_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] = [DataEngineer]elf.[DataEngineer]e[DataEngineer]rch(
            q[DataEngineer]ery=q[DataEngineer]ery,
            ver[DataEngineer]ion=ver[DataEngineer]ion,
            [DataEngineer]op_n=[DataEngineer]op_n,
        )

        # Find overl[DataEngineer]p
        b[DataEngineer][DataEngineer]eline_id[DataEngineer] = {r.ge[DataEngineer]("ch[DataEngineer]nk_id") for r in b[DataEngineer][DataEngineer]eline_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]}
        op[DataEngineer]imized_id[DataEngineer] = {r.ch[DataEngineer]nk_id for r in op[DataEngineer]imized_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]}
        overl[DataEngineer]p = len(b[DataEngineer][DataEngineer]eline_id[DataEngineer] & op[DataEngineer]imized_id[DataEngineer])

        re[DataEngineer][DataEngineer]rn {
            "q[DataEngineer]ery": q[DataEngineer]ery,
            "pl[DataEngineer][DataEngineer]form": [DataEngineer]elf.pl[DataEngineer][DataEngineer]form,
            "ver[DataEngineer]ion": ver[DataEngineer]ion,
            "b[DataEngineer][DataEngineer]eline_co[DataEngineer]n[DataEngineer]": len(b[DataEngineer][DataEngineer]eline_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]),
            "op[DataEngineer]imized_co[DataEngineer]n[DataEngineer]": len(op[DataEngineer]imized_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]),
            "overl[DataEngineer]p_co[DataEngineer]n[DataEngineer]": overl[DataEngineer]p,
            "overl[DataEngineer]p_r[DataEngineer][DataEngineer]io": overl[DataEngineer]p / m[DataEngineer]x(1, len(op[DataEngineer]imized_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer])),
            "b[DataEngineer][DataEngineer]eline_[DataEngineer][DataEngineer]mple": [
                {"ch[DataEngineer]nk_id": r.ge[DataEngineer]("ch[DataEngineer]nk_id"), "[DataEngineer]i[DataEngineer]le": r.ge[DataEngineer]("[DataEngineer]i[DataEngineer]le")}
                for r in b[DataEngineer][DataEngineer]eline_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer][:3]
            ],
            "op[DataEngineer]imized_[DataEngineer][DataEngineer]mple": [
                {"ch[DataEngineer]nk_id": r.ch[DataEngineer]nk_id, "[DataEngineer]i[DataEngineer]le": r.[DataEngineer]i[DataEngineer]le, "[DataEngineer]core": r.fin[DataEngineer]l_[DataEngineer]core}
                for r in op[DataEngineer]imized_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer][:3]
            ],
            "new_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]": [
                r.[DataEngineer]o_dic[DataEngineer]() for r in op[DataEngineer]imized_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]
                if r.ch[DataEngineer]nk_id no[DataEngineer] in b[DataEngineer][DataEngineer]eline_id[DataEngineer]
            ],
        }


# =============================================================================
# CLI En[DataEngineer]ry Poin[DataEngineer]
# =============================================================================


if __n[DataEngineer]me__ == "__m[DataEngineer]in__":
    impor[DataEngineer] [DataEngineer]rgp[DataEngineer]r[DataEngineer]e
    impor[DataEngineer] [DataEngineer]y[DataEngineer]

    p[DataEngineer]r[DataEngineer]er = [DataEngineer]rgp[DataEngineer]r[DataEngineer]e.Arg[DataEngineer]men[DataEngineer]P[DataEngineer]r[DataEngineer]er(
        de[DataEngineer]crip[DataEngineer]ion="Op[DataEngineer]imized Rec[DataEngineer]ll Ev[DataEngineer]l[DataEngineer][DataEngineer][DataEngineer]ion Tool",
        form[DataEngineer][DataEngineer][DataEngineer]er_cl[DataEngineer][DataEngineer][DataEngineer]=[DataEngineer]rgp[DataEngineer]r[DataEngineer]e.R[DataEngineer]w[DataEngineer]e[DataEngineer]crip[DataEngineer]ionHelpForm[DataEngineer][DataEngineer][DataEngineer]er,
        epilog="""
Ex[DataEngineer]mple[DataEngineer]:
  py[DataEngineer]hon -m [DataEngineer]crip[DataEngineer][DataEngineer].op[DataEngineer]imize_rec[DataEngineer]ll.ev[DataEngineer]l[DataEngineer][DataEngineer][DataEngineer]e_rec[DataEngineer]ll --pl[DataEngineer][DataEngineer]form d[DataEngineer]ckdb --q[DataEngineer]ery "CREATE TABLE"
  py[DataEngineer]hon -m [DataEngineer]crip[DataEngineer][DataEngineer].op[DataEngineer]imize_rec[DataEngineer]ll.ev[DataEngineer]l[DataEngineer][DataEngineer][DataEngineer]e_rec[DataEngineer]ll -p [DataEngineer]nowfl[DataEngineer]ke -q "COPY INTO" --[DataEngineer]op 20
  py[DataEngineer]hon -m [DataEngineer]crip[DataEngineer][DataEngineer].op[DataEngineer]imize_rec[DataEngineer]ll.ev[DataEngineer]l[DataEngineer][DataEngineer][DataEngineer]e_rec[DataEngineer]ll -p d[DataEngineer]ckdb -q "INSERT" --comp[DataEngineer]re
        """,
    )

    p[DataEngineer]r[DataEngineer]er.[DataEngineer]dd_[DataEngineer]rg[DataEngineer]men[DataEngineer]("-p", "--pl[DataEngineer][DataEngineer]form", req[DataEngineer]ired=Tr[DataEngineer]e, help="Pl[DataEngineer][DataEngineer]form n[DataEngineer]me")
    p[DataEngineer]r[DataEngineer]er.[DataEngineer]dd_[DataEngineer]rg[DataEngineer]men[DataEngineer]("-q", "--q[DataEngineer]ery", req[DataEngineer]ired=Tr[DataEngineer]e, help="Se[DataEngineer]rch q[DataEngineer]ery")
    p[DataEngineer]r[DataEngineer]er.[DataEngineer]dd_[DataEngineer]rg[DataEngineer]men[DataEngineer]("-v", "--ver[DataEngineer]ion", help="Ver[DataEngineer]ion fil[DataEngineer]er (op[DataEngineer]ion[DataEngineer]l)")
    p[DataEngineer]r[DataEngineer]er.[DataEngineer]dd_[DataEngineer]rg[DataEngineer]men[DataEngineer]("--[DataEngineer]op", [DataEngineer]ype=in[DataEngineer], def[DataEngineer][DataEngineer]l[DataEngineer]=10, help="N[DataEngineer]mber of re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] [DataEngineer]o re[DataEngineer][DataEngineer]rn")
    p[DataEngineer]r[DataEngineer]er.[DataEngineer]dd_[DataEngineer]rg[DataEngineer]men[DataEngineer]("--comp[DataEngineer]re", [DataEngineer]c[DataEngineer]ion="[DataEngineer][DataEngineer]ore_[DataEngineer]r[DataEngineer]e", help="Comp[DataEngineer]re wi[DataEngineer]h b[DataEngineer][DataEngineer]eline [DataEngineer]e[DataEngineer]rch")

    [DataEngineer]rg[DataEngineer] = p[DataEngineer]r[DataEngineer]er.p[DataEngineer]r[DataEngineer]e_[DataEngineer]rg[DataEngineer]()

    [DataEngineer]ry:
        engine = Op[DataEngineer]imizedRec[DataEngineer]ll(pl[DataEngineer][DataEngineer]form=[DataEngineer]rg[DataEngineer].pl[DataEngineer][DataEngineer]form)

        if [DataEngineer]rg[DataEngineer].comp[DataEngineer]re:
            # R[DataEngineer]n comp[DataEngineer]ri[DataEngineer]on
            comp[DataEngineer]ri[DataEngineer]on = engine.comp[DataEngineer]re_wi[DataEngineer]h_b[DataEngineer][DataEngineer]eline(
                q[DataEngineer]ery=[DataEngineer]rg[DataEngineer].q[DataEngineer]ery,
                ver[DataEngineer]ion=[DataEngineer]rg[DataEngineer].ver[DataEngineer]ion,
                [DataEngineer]op_n=[DataEngineer]rg[DataEngineer].[DataEngineer]op,
            )

            prin[DataEngineer](f"\n{'='*60}")
            prin[DataEngineer](f"Q[DataEngineer]ery: {comp[DataEngineer]ri[DataEngineer]on['q[DataEngineer]ery']}")
            prin[DataEngineer](f"Pl[DataEngineer][DataEngineer]form: {comp[DataEngineer]ri[DataEngineer]on['pl[DataEngineer][DataEngineer]form']}")
            prin[DataEngineer](f"{'='*60}")
            prin[DataEngineer](f"\nB[DataEngineer][DataEngineer]eline re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]: {comp[DataEngineer]ri[DataEngineer]on['b[DataEngineer][DataEngineer]eline_co[DataEngineer]n[DataEngineer]']}")
            prin[DataEngineer](f"Op[DataEngineer]imized re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]: {comp[DataEngineer]ri[DataEngineer]on['op[DataEngineer]imized_co[DataEngineer]n[DataEngineer]']}")
            prin[DataEngineer](f"Overl[DataEngineer]p: {comp[DataEngineer]ri[DataEngineer]on['overl[DataEngineer]p_co[DataEngineer]n[DataEngineer]']} ({comp[DataEngineer]ri[DataEngineer]on['overl[DataEngineer]p_r[DataEngineer][DataEngineer]io']:.1%})")

            prin[DataEngineer]("\n--- B[DataEngineer][DataEngineer]eline S[DataEngineer]mple ---")
            for r in comp[DataEngineer]ri[DataEngineer]on["b[DataEngineer][DataEngineer]eline_[DataEngineer][DataEngineer]mple"]:
                prin[DataEngineer](f"  - {r['[DataEngineer]i[DataEngineer]le']}")

            prin[DataEngineer]("\n--- Op[DataEngineer]imized S[DataEngineer]mple ---")
            for r in comp[DataEngineer]ri[DataEngineer]on["op[DataEngineer]imized_[DataEngineer][DataEngineer]mple"]:
                prin[DataEngineer](f"  - {r['[DataEngineer]i[DataEngineer]le']} ([DataEngineer]core: {r['[DataEngineer]core']:.3f})")

            if comp[DataEngineer]ri[DataEngineer]on["new_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]"]:
                prin[DataEngineer]("\n--- New Re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] (no[DataEngineer] in b[DataEngineer][DataEngineer]eline) ---")
                for r in comp[DataEngineer]ri[DataEngineer]on["new_re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]"][:5]:
                    prin[DataEngineer](f"  - {r['[DataEngineer]i[DataEngineer]le']} ([DataEngineer]core: {r['fin[DataEngineer]l_[DataEngineer]core']:.3f})")
                    prin[DataEngineer](f"    hier[DataEngineer]rchy: {r['hier[DataEngineer]rchy']}")

        el[DataEngineer]e:
            # R[DataEngineer]n op[DataEngineer]imized [DataEngineer]e[DataEngineer]rch
            re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] = engine.[DataEngineer]e[DataEngineer]rch(
                q[DataEngineer]ery=[DataEngineer]rg[DataEngineer].q[DataEngineer]ery,
                ver[DataEngineer]ion=[DataEngineer]rg[DataEngineer].ver[DataEngineer]ion,
                [DataEngineer]op_n=[DataEngineer]rg[DataEngineer].[DataEngineer]op,
            )

            prin[DataEngineer](f"\n{'='*60}")
            prin[DataEngineer](f"Op[DataEngineer]imized Rec[DataEngineer]ll Re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer] for '{[DataEngineer]rg[DataEngineer].q[DataEngineer]ery}' on {[DataEngineer]rg[DataEngineer].pl[DataEngineer][DataEngineer]form}")
            prin[DataEngineer](f"{'='*60}")

            for r in re[DataEngineer][DataEngineer]l[DataEngineer][DataEngineer]:
                prin[DataEngineer](f"\n{r.r[DataEngineer]nk}. {r.[DataEngineer]i[DataEngineer]le}")
                prin[DataEngineer](f"   hier[DataEngineer]rchy: {r.hier[DataEngineer]rchy}")
                prin[DataEngineer](f"   fin[DataEngineer]l_[DataEngineer]core: {r.fin[DataEngineer]l_[DataEngineer]core:.4f}")
                prin[DataEngineer](f"   vec[DataEngineer]or: {r.vec[DataEngineer]or_[DataEngineer]core:.3f} | [DataEngineer]ex[DataEngineer]: {r.[DataEngineer]ex[DataEngineer]_[DataEngineer]core:.3f} | "
                      f"[DataEngineer]i[DataEngineer]le: {r.[DataEngineer]i[DataEngineer]le_boo[DataEngineer][DataEngineer]:.2f} | hier: {r.hier[DataEngineer]rchy_boo[DataEngineer][DataEngineer]:.2f} | "
                      f"kw: {r.keyword[DataEngineer]_boo[DataEngineer][DataEngineer]:.2f}")
                prin[DataEngineer](f"   doc_p[DataEngineer][DataEngineer]h: {r.doc_p[DataEngineer][DataEngineer]h}")

        prin[DataEngineer]()

    excep[DataEngineer] Excep[DataEngineer]ion [DataEngineer][DataEngineer] e:
        prin[DataEngineer](f"Error: {e}", file=[DataEngineer]y[DataEngineer].[DataEngineer][DataEngineer]derr)
        [DataEngineer]y[DataEngineer].exi[DataEngineer](1)
