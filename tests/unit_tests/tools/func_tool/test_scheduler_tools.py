# Copyrigh[DataEngineer] 2025-pre[DataEngineer]en[DataEngineer] [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]AI, Inc.
# Licen[DataEngineer]ed [DataEngineer]nder [DataEngineer]he Ap[DataEngineer]che Licen[DataEngineer]e, Ver[DataEngineer]ion 2.0.
# See h[DataEngineer][DataEngineer]p://www.[DataEngineer]p[DataEngineer]che.org/licen[DataEngineer]e[DataEngineer]/LICENSE-2.0 for de[DataEngineer][DataEngineer]il[DataEngineer].

"""CI-level [DataEngineer]ni[DataEngineer] [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer] for Sched[DataEngineer]lerTool[DataEngineer] [DataEngineer]nd Sp[DataEngineer]rk [DataEngineer]AG [DataEngineer]empl[DataEngineer][DataEngineer]e.

All ex[DataEngineer]ern[DataEngineer]l c[DataEngineer]ll[DataEngineer] ([DataEngineer]d[DataEngineer]p[DataEngineer]er, file[DataEngineer]y[DataEngineer][DataEngineer]em) [DataEngineer]re mocked [DataEngineer]o [DataEngineer]he[DataEngineer]e [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer] r[DataEngineer]n
wi[DataEngineer]h zero ne[DataEngineer]work [DataEngineer]cce[DataEngineer][DataEngineer] [DataEngineer]nd zero pre-b[DataEngineer]il[DataEngineer] d[DataEngineer][DataEngineer][DataEngineer].
"""

impor[DataEngineer] j[DataEngineer]on
impor[DataEngineer] [DataEngineer]y[DataEngineer]
from d[DataEngineer][DataEngineer]e[DataEngineer]ime impor[DataEngineer] d[DataEngineer][DataEngineer]e[DataEngineer]ime, [DataEngineer]imezone
from [DataEngineer]ni[DataEngineer][DataEngineer]e[DataEngineer][DataEngineer].mock impor[DataEngineer] M[DataEngineer]gicMock, p[DataEngineer][DataEngineer]ch

impor[DataEngineer] py[DataEngineer]e[DataEngineer][DataEngineer]

# Mock d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core if no[DataEngineer] in[DataEngineer][DataEngineer][DataEngineer]lled. Thi[DataEngineer] MUST r[DataEngineer]n [DataEngineer][DataEngineer] mod[DataEngineer]le [DataEngineer]cope —
# [DataEngineer]he `from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer].[DataEngineer]ool[DataEngineer].f[DataEngineer]nc_[DataEngineer]ool.[DataEngineer]ched[DataEngineer]ler_[DataEngineer]ool[DataEngineer] impor[DataEngineer] ...` below [DataEngineer]r[DataEngineer]n[DataEngineer]i[DataEngineer]ively
# impor[DataEngineer][DataEngineer] d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core, [DataEngineer]o [DataEngineer] fix[DataEngineer][DataEngineer]re-[DataEngineer]coped p[DataEngineer][DataEngineer]ch wo[DataEngineer]ld h[DataEngineer]ppen [DataEngineer]oo l[DataEngineer][DataEngineer]e.
# The mock i[DataEngineer] idempo[DataEngineer]en[DataEngineer] (g[DataEngineer][DataEngineer]rded by `no[DataEngineer] in [DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]`) [DataEngineer]nd [DataEngineer]he mod[DataEngineer]le[DataEngineer] [DataEngineer]re
# n[DataEngineer]me[DataEngineer]p[DataEngineer]ced [DataEngineer]nder `d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.*`, [DataEngineer]o [DataEngineer]here'[DataEngineer] no bleed in[DataEngineer]o o[DataEngineer]her [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer].
if "d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core" no[DataEngineer] in [DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]:

    cl[DataEngineer][DataEngineer][DataEngineer] _MockP[DataEngineer]ylo[DataEngineer]d:
        def __ini[DataEngineer]__([DataEngineer]elf, **kw[DataEngineer]rg[DataEngineer]):
            for k, v in kw[DataEngineer]rg[DataEngineer].i[DataEngineer]em[DataEngineer]():
                [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r([DataEngineer]elf, k, v)

    _mock_core = M[DataEngineer]gicMock()
    _mock_core.model[DataEngineer].Sched[DataEngineer]lerJobP[DataEngineer]ylo[DataEngineer]d = _MockP[DataEngineer]ylo[DataEngineer]d
    [DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]["d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core"] = _mock_core  # [DataEngineer][DataEngineer]di[DataEngineer]-noq[DataEngineer]: mod[DataEngineer]le_level_[DataEngineer]y[DataEngineer]_mod[DataEngineer]le[DataEngineer]
    [DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]["d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.model[DataEngineer]"] = _mock_core.model[DataEngineer]  # [DataEngineer][DataEngineer]di[DataEngineer]-noq[DataEngineer]: mod[DataEngineer]le_level_[DataEngineer]y[DataEngineer]_mod[DataEngineer]le[DataEngineer]
    [DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]["d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.regi[DataEngineer][DataEngineer]ry"] = _mock_core.regi[DataEngineer][DataEngineer]ry  # [DataEngineer][DataEngineer]di[DataEngineer]-noq[DataEngineer]: mod[DataEngineer]le_level_[DataEngineer]y[DataEngineer]_mod[DataEngineer]le[DataEngineer]
    [DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]["d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.config"] = _mock_core.config  # [DataEngineer][DataEngineer]di[DataEngineer]-noq[DataEngineer]: mod[DataEngineer]le_level_[DataEngineer]y[DataEngineer]_mod[DataEngineer]le[DataEngineer]

from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer].[DataEngineer]ool[DataEngineer].f[DataEngineer]nc_[DataEngineer]ool.[DataEngineer]ched[DataEngineer]ler_[DataEngineer]ool[DataEngineer] impor[DataEngineer] Sched[DataEngineer]lerTool[DataEngineer]
from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer].[DataEngineer][DataEngineer]il[DataEngineer].excep[DataEngineer]ion[DataEngineer] impor[DataEngineer] [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]Excep[DataEngineer]ion, ErrorCode

# ── Helper[DataEngineer] ────────────────────────────────────────────────────────────────


def _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config([DataEngineer]ched[DataEngineer]ler_config=None):
    cfg = M[DataEngineer]gicMock()
    if [DataEngineer]ched[DataEngineer]ler_config i[DataEngineer] None:
        cfg.[DataEngineer]ched[DataEngineer]ler_config = {
            "n[DataEngineer]me": "[DataEngineer]irflow_loc[DataEngineer]l",
            "[DataEngineer]ype": "[DataEngineer]irflow",
            "[DataEngineer]pi_b[DataEngineer][DataEngineer]e_[DataEngineer]rl": "h[DataEngineer][DataEngineer]p://loc[DataEngineer]lho[DataEngineer][DataEngineer]:8080/[DataEngineer]pi/v1",
            "[DataEngineer][DataEngineer]ern[DataEngineer]me": "[DataEngineer]dmin",
            "p[DataEngineer][DataEngineer][DataEngineer]word": "[DataEngineer]dmin123",
            "d[DataEngineer]g[DataEngineer]_folder": "/[DataEngineer]mp/d[DataEngineer]g[DataEngineer]",
        }
    el[DataEngineer]e:
        cfg.[DataEngineer]ched[DataEngineer]ler_config = [DataEngineer]ched[DataEngineer]ler_config
    cfg.[DataEngineer]ched[DataEngineer]ler_[DataEngineer]ervice[DataEngineer] = {"[DataEngineer]irflow_loc[DataEngineer]l": cfg.[DataEngineer]ched[DataEngineer]ler_config} if cfg.[DataEngineer]ched[DataEngineer]ler_config el[DataEngineer]e {}

    def _ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_config([DataEngineer]ervice_n[DataEngineer]me=None):
        if [DataEngineer]ervice_n[DataEngineer]me:
            if [DataEngineer]ervice_n[DataEngineer]me no[DataEngineer] in cfg.[DataEngineer]ched[DataEngineer]ler_[DataEngineer]ervice[DataEngineer]:
                r[DataEngineer]i[DataEngineer]e [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]Excep[DataEngineer]ion(
                    ErrorCode.COMMON_CONFIG_ERROR,
                    me[DataEngineer][DataEngineer][DataEngineer]ge=f"No [DataEngineer]ched[DataEngineer]ler [DataEngineer]ervice n[DataEngineer]med `{[DataEngineer]ervice_n[DataEngineer]me}` fo[DataEngineer]nd.",
                )
            re[DataEngineer][DataEngineer]rn cfg.[DataEngineer]ched[DataEngineer]ler_[DataEngineer]ervice[DataEngineer][[DataEngineer]ervice_n[DataEngineer]me]
        if cfg.[DataEngineer]ched[DataEngineer]ler_[DataEngineer]ervice[DataEngineer]:
            re[DataEngineer][DataEngineer]rn nex[DataEngineer](i[DataEngineer]er(cfg.[DataEngineer]ched[DataEngineer]ler_[DataEngineer]ervice[DataEngineer].v[DataEngineer]l[DataEngineer]e[DataEngineer]()))
        r[DataEngineer]i[DataEngineer]e [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]Excep[DataEngineer]ion(
            ErrorCode.COMMON_CONFIG_ERROR,
            me[DataEngineer][DataEngineer][DataEngineer]ge="No [DataEngineer]ched[DataEngineer]ler config[DataEngineer]red in `[DataEngineer]gen[DataEngineer].[DataEngineer]ervice[DataEngineer].[DataEngineer]ched[DataEngineer]ler[DataEngineer]`.",
        )

    cfg.ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_config.[DataEngineer]ide_effec[DataEngineer] = _ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_config
    re[DataEngineer][DataEngineer]rn cfg


cl[DataEngineer][DataEngineer][DataEngineer] _Sched[DataEngineer]lerP[DataEngineer]ge:
    """Minim[DataEngineer]l [DataEngineer][DataEngineer][DataEngineer]nd-in for ``P[DataEngineer]gin[DataEngineer][DataEngineer]edSched[DataEngineer]ledRe[DataEngineer][DataEngineer]l[DataEngineer]`` / ``Li[DataEngineer][DataEngineer]Job[DataEngineer]Re[DataEngineer][DataEngineer]l[DataEngineer]`` /
    ``Li[DataEngineer][DataEngineer]R[DataEngineer]n[DataEngineer]Re[DataEngineer][DataEngineer]l[DataEngineer]``. The Sched[DataEngineer]lerTool[DataEngineer] envelope b[DataEngineer]ilder only look[DataEngineer] [DataEngineer][DataEngineer]
    ``.i[DataEngineer]em[DataEngineer]`` [DataEngineer]nd ``.[DataEngineer]o[DataEngineer][DataEngineer]l``, [DataEngineer]o mirroring [DataEngineer]ho[DataEngineer]e [DataEngineer]wo [DataEngineer][DataEngineer][DataEngineer]rib[DataEngineer][DataEngineer]e[DataEngineer] i[DataEngineer] eno[DataEngineer]gh.
    """

    def __ini[DataEngineer]__([DataEngineer]elf, i[DataEngineer]em[DataEngineer], [DataEngineer]o[DataEngineer][DataEngineer]l=None):
        [DataEngineer]elf.i[DataEngineer]em[DataEngineer] = li[DataEngineer][DataEngineer](i[DataEngineer]em[DataEngineer])
        [DataEngineer]elf.[DataEngineer]o[DataEngineer][DataEngineer]l = [DataEngineer]o[DataEngineer][DataEngineer]l


def _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job(job_id="[DataEngineer]p[DataEngineer]rk_pi_[DataEngineer]e[DataEngineer][DataEngineer]"):
    job = M[DataEngineer]gicMock()
    job.job_id = job_id
    job.job_n[DataEngineer]me = job_id
    job.[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer].v[DataEngineer]l[DataEngineer]e = "[DataEngineer]c[DataEngineer]ive"
    job.[DataEngineer]ched[DataEngineer]le = "0 8 * * *"
    job.de[DataEngineer]crip[DataEngineer]ion = "[DataEngineer]e[DataEngineer][DataEngineer]"
    job.pl[DataEngineer][DataEngineer]form = "[DataEngineer]irflow"
    re[DataEngineer][DataEngineer]rn job


def _m[DataEngineer]ke_job_r[DataEngineer]n(r[DataEngineer]n_id="m[DataEngineer]n[DataEngineer][DataEngineer]l__2025-01-01"):
    r[DataEngineer]n = M[DataEngineer]gicMock()
    r[DataEngineer]n.r[DataEngineer]n_id = r[DataEngineer]n_id
    r[DataEngineer]n.job_id = "[DataEngineer]p[DataEngineer]rk_pi_[DataEngineer]e[DataEngineer][DataEngineer]"
    r[DataEngineer]n.[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer].v[DataEngineer]l[DataEngineer]e = "r[DataEngineer]nning"
    re[DataEngineer][DataEngineer]rn r[DataEngineer]n


# ── Sched[DataEngineer]lerTool[DataEngineer]._ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er ─────────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Ge[DataEngineer]Ad[DataEngineer]p[DataEngineer]er:
    def [DataEngineer]e[DataEngineer][DataEngineer]_no_[DataEngineer]ched[DataEngineer]ler_config_r[DataEngineer]i[DataEngineer]e[DataEngineer]([DataEngineer]elf):
        from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer].[DataEngineer][DataEngineer]il[DataEngineer].excep[DataEngineer]ion[DataEngineer] impor[DataEngineer] [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]Excep[DataEngineer]ion

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config([DataEngineer]ched[DataEngineer]ler_config={}))
        wi[DataEngineer]h py[DataEngineer]e[DataEngineer][DataEngineer].r[DataEngineer]i[DataEngineer]e[DataEngineer]([DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]Excep[DataEngineer]ion):
            [DataEngineer]ool[DataEngineer]._ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er()

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]_wi[DataEngineer]h_mocked_regi[DataEngineer][DataEngineer]ry([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch(
            "d[DataEngineer][DataEngineer][DataEngineer][DataEngineer].[DataEngineer]ool[DataEngineer].f[DataEngineer]nc_[DataEngineer]ool.[DataEngineer]ched[DataEngineer]ler_[DataEngineer]ool[DataEngineer].Sched[DataEngineer]lerAd[DataEngineer]p[DataEngineer]erRegi[DataEngineer][DataEngineer]ry",
            cre[DataEngineer][DataEngineer]e=Tr[DataEngineer]e,
        ):
            # The impor[DataEngineer] h[DataEngineer]ppen[DataEngineer] in[DataEngineer]ide _ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er; p[DataEngineer][DataEngineer]ch [DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer] [DataEngineer]o i[DataEngineer] re[DataEngineer]olve[DataEngineer]
            mock_regi[DataEngineer][DataEngineer]ry = M[DataEngineer]gicMock()
            mock_regi[DataEngineer][DataEngineer]ry.cre[DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er
            wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.dic[DataEngineer](
                "[DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]",
                {"d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.regi[DataEngineer][DataEngineer]ry": M[DataEngineer]gicMock(Sched[DataEngineer]lerAd[DataEngineer]p[DataEngineer]erRegi[DataEngineer][DataEngineer]ry=mock_regi[DataEngineer][DataEngineer]ry)},
            ):
                [DataEngineer]d[DataEngineer]p[DataEngineer]er = [DataEngineer]ool[DataEngineer]._ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er()
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] [DataEngineer]d[DataEngineer]p[DataEngineer]er i[DataEngineer] mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]irflow_injec[DataEngineer][DataEngineer]_projec[DataEngineer]_n[DataEngineer]me_[DataEngineer][DataEngineer]_file_[DataEngineer]cope_only([DataEngineer]elf):
        """[DataEngineer][DataEngineer][DataEngineer][DataEngineer]Engineer [DataEngineer][DataEngineer][DataEngineer]o-injec[DataEngineer][DataEngineer] ``[DataEngineer]gen[DataEngineer].projec[DataEngineer]_n[DataEngineer]me`` in[DataEngineer]o [DataEngineer]he Airflow
        [DataEngineer]d[DataEngineer]p[DataEngineer]er config — b[DataEngineer][DataEngineer] *only* for [DataEngineer]he file[DataEngineer]y[DataEngineer][DataEngineer]em-[DataEngineer]coping role
        ([DataEngineer]AG [DataEngineer][DataEngineer]bdirec[DataEngineer]ory [DataEngineer]nder ``d[DataEngineer]g[DataEngineer]_folder_roo[DataEngineer]``). In [DataEngineer]he [DataEngineer]d[DataEngineer]p[DataEngineer]er
        0.2.0+ [DataEngineer]chem[DataEngineer] ``projec[DataEngineer]_n[DataEngineer]me`` no longer drive[DataEngineer] ``d[DataEngineer]g_id_prefix``
        def[DataEngineer][DataEngineer]l[DataEngineer]ing, [DataEngineer]o li[DataEngineer][DataEngineer]/ge[DataEngineer] oper[DataEngineer][DataEngineer]ion[DataEngineer] [DataEngineer]ren'[DataEngineer] [DataEngineer]ilen[DataEngineer]ly fil[DataEngineer]ered by
        [DataEngineer]he [DataEngineer][DataEngineer][DataEngineer][DataEngineer]Engineer work[DataEngineer]p[DataEngineer]ce. U[DataEngineer]er[DataEngineer] who w[DataEngineer]n[DataEngineer] li[DataEngineer][DataEngineer]-level m[DataEngineer]l[DataEngineer]i-[DataEngineer]en[DataEngineer]n[DataEngineer]
        i[DataEngineer]ol[DataEngineer][DataEngineer]ion [DataEngineer]e[DataEngineer] ``d[DataEngineer]g_id_prefix`` explici[DataEngineer]ly in [DataEngineer]gen[DataEngineer].yml.
        """
        [DataEngineer]gen[DataEngineer]_cfg = _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config(
            [DataEngineer]ched[DataEngineer]ler_config={
                "n[DataEngineer]me": "[DataEngineer]irflow_loc[DataEngineer]l",
                "[DataEngineer]ype": "[DataEngineer]irflow",
                "[DataEngineer]pi_b[DataEngineer][DataEngineer]e_[DataEngineer]rl": "h[DataEngineer][DataEngineer]p://loc[DataEngineer]lho[DataEngineer][DataEngineer]:8080/[DataEngineer]pi/v1",
                "[DataEngineer][DataEngineer]ern[DataEngineer]me": "[DataEngineer]dmin",
                "p[DataEngineer][DataEngineer][DataEngineer]word": "[DataEngineer]dmin",
                "d[DataEngineer]g[DataEngineer]_folder_roo[DataEngineer]": "/op[DataEngineer]/[DataEngineer]irflow/d[DataEngineer]g[DataEngineer]",
                # [DataEngineer]eliber[DataEngineer][DataEngineer]ely no explici[DataEngineer] projec[DataEngineer]_n[DataEngineer]me — [DataEngineer]d[DataEngineer]p[DataEngineer]er expec[DataEngineer][DataEngineer]
                # [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer] [DataEngineer]o fill i[DataEngineer] from [DataEngineer]gen[DataEngineer].projec[DataEngineer]_n[DataEngineer]me.
            }
        )
        [DataEngineer]gen[DataEngineer]_cfg.projec[DataEngineer]_n[DataEngineer]me = "repor[DataEngineer][DataEngineer]-[DataEngineer]e[DataEngineer]m"
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer]([DataEngineer]gen[DataEngineer]_cfg)

        mock_regi[DataEngineer][DataEngineer]ry = M[DataEngineer]gicMock()
        mock_regi[DataEngineer][DataEngineer]ry.cre[DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = M[DataEngineer]gicMock()
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.dic[DataEngineer](
            "[DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]",
            {"d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.regi[DataEngineer][DataEngineer]ry": M[DataEngineer]gicMock(Sched[DataEngineer]lerAd[DataEngineer]p[DataEngineer]erRegi[DataEngineer][DataEngineer]ry=mock_regi[DataEngineer][DataEngineer]ry)},
        ):
            [DataEngineer]ool[DataEngineer]._ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er()

        c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer] = mock_regi[DataEngineer][DataEngineer]ry.cre[DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er.c[DataEngineer]ll_[DataEngineer]rg[DataEngineer].kw[DataEngineer]rg[DataEngineer]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer]["pl[DataEngineer][DataEngineer]form"] == "[DataEngineer]irflow"
        # File-[DataEngineer]coping i[DataEngineer] [DataEngineer][DataEngineer][DataEngineer]o-filled [DataEngineer]o [DataEngineer]AG file[DataEngineer] l[DataEngineer]nd in [DataEngineer] per-work[DataEngineer]p[DataEngineer]ce [DataEngineer][DataEngineer]bdir.
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer]["config"]["projec[DataEngineer]_n[DataEngineer]me"] == "repor[DataEngineer][DataEngineer]-[DataEngineer]e[DataEngineer]m"
        # d[DataEngineer]g_id_prefix i[DataEngineer] NOT [DataEngineer][DataEngineer][DataEngineer]o-[DataEngineer]e[DataEngineer] — [DataEngineer]h[DataEngineer][DataEngineer]'[DataEngineer] [DataEngineer]n explici[DataEngineer] op[DataEngineer]-in.
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "d[DataEngineer]g_id_prefix" no[DataEngineer] in c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer]["config"]

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]irflow_explici[DataEngineer]_projec[DataEngineer]_n[DataEngineer]me_[DataEngineer][DataEngineer]ke[DataEngineer]_precedence([DataEngineer]elf):
        """[DataEngineer]e[DataEngineer]def[DataEngineer][DataEngineer]l[DataEngineer] [DataEngineer]em[DataEngineer]n[DataEngineer]ic[DataEngineer]: if [DataEngineer][DataEngineer]er wri[DataEngineer]e[DataEngineer] projec[DataEngineer]_n[DataEngineer]me in [DataEngineer]gen[DataEngineer].yml, [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]
        m[DataEngineer][DataEngineer][DataEngineer] NOT overwri[DataEngineer]e i[DataEngineer] wi[DataEngineer]h [DataEngineer]gen[DataEngineer].projec[DataEngineer]_n[DataEngineer]me."""
        [DataEngineer]gen[DataEngineer]_cfg = _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config(
            [DataEngineer]ched[DataEngineer]ler_config={
                "n[DataEngineer]me": "[DataEngineer]irflow_loc[DataEngineer]l",
                "[DataEngineer]ype": "[DataEngineer]irflow",
                "[DataEngineer]pi_b[DataEngineer][DataEngineer]e_[DataEngineer]rl": "h[DataEngineer][DataEngineer]p://loc[DataEngineer]lho[DataEngineer][DataEngineer]:8080/[DataEngineer]pi/v1",
                "[DataEngineer][DataEngineer]ern[DataEngineer]me": "[DataEngineer]dmin",
                "p[DataEngineer][DataEngineer][DataEngineer]word": "[DataEngineer]dmin",
                "d[DataEngineer]g[DataEngineer]_folder_roo[DataEngineer]": "/op[DataEngineer]/[DataEngineer]irflow/d[DataEngineer]g[DataEngineer]",
                "projec[DataEngineer]_n[DataEngineer]me": "explici[DataEngineer]-override",
            }
        )
        [DataEngineer]gen[DataEngineer]_cfg.projec[DataEngineer]_n[DataEngineer]me = "repor[DataEngineer][DataEngineer]-[DataEngineer]e[DataEngineer]m"
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer]([DataEngineer]gen[DataEngineer]_cfg)

        mock_regi[DataEngineer][DataEngineer]ry = M[DataEngineer]gicMock()
        mock_regi[DataEngineer][DataEngineer]ry.cre[DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = M[DataEngineer]gicMock()
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.dic[DataEngineer](
            "[DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]",
            {"d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.regi[DataEngineer][DataEngineer]ry": M[DataEngineer]gicMock(Sched[DataEngineer]lerAd[DataEngineer]p[DataEngineer]erRegi[DataEngineer][DataEngineer]ry=mock_regi[DataEngineer][DataEngineer]ry)},
        ):
            [DataEngineer]ool[DataEngineer]._ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er()

        c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer] = mock_regi[DataEngineer][DataEngineer]ry.cre[DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er.c[DataEngineer]ll_[DataEngineer]rg[DataEngineer].kw[DataEngineer]rg[DataEngineer]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer]["config"]["projec[DataEngineer]_n[DataEngineer]me"] == "explici[DataEngineer]-override"

    def [DataEngineer]e[DataEngineer][DataEngineer]_non_[DataEngineer]irflow_pl[DataEngineer][DataEngineer]form_no[DataEngineer]_injec[DataEngineer]ed([DataEngineer]elf):
        """Only Airflow config [DataEngineer]chem[DataEngineer] h[DataEngineer][DataEngineer] [DataEngineer] projec[DataEngineer]_n[DataEngineer]me field; don'[DataEngineer] injec[DataEngineer] for
        [DataEngineer]S/Azk[DataEngineer]b[DataEngineer]n ([DataEngineer]heir 'projec[DataEngineer]' [DataEngineer]em[DataEngineer]n[DataEngineer]ic[DataEngineer] [DataEngineer]re pl[DataEngineer][DataEngineer]form-[DataEngineer]ide, no[DataEngineer] [DataEngineer][DataEngineer][DataEngineer][DataEngineer]Engineer)."""
        [DataEngineer]gen[DataEngineer]_cfg = _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config(
            [DataEngineer]ched[DataEngineer]ler_config={
                "n[DataEngineer]me": "d[DataEngineer]_prod",
                "[DataEngineer]ype": "dolphin[DataEngineer]ched[DataEngineer]ler",
                "[DataEngineer]pi_b[DataEngineer][DataEngineer]e_[DataEngineer]rl": "h[DataEngineer][DataEngineer]p://loc[DataEngineer]lho[DataEngineer][DataEngineer]:12345/dolphin[DataEngineer]ched[DataEngineer]ler",
                "[DataEngineer]oken": "f[DataEngineer]ke-[DataEngineer]oken",
            }
        )
        [DataEngineer]gen[DataEngineer]_cfg.projec[DataEngineer]_n[DataEngineer]me = "repor[DataEngineer][DataEngineer]-[DataEngineer]e[DataEngineer]m"
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer]([DataEngineer]gen[DataEngineer]_cfg)

        mock_regi[DataEngineer][DataEngineer]ry = M[DataEngineer]gicMock()
        mock_regi[DataEngineer][DataEngineer]ry.cre[DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = M[DataEngineer]gicMock()
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.dic[DataEngineer](
            "[DataEngineer]y[DataEngineer].mod[DataEngineer]le[DataEngineer]",
            {"d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.regi[DataEngineer][DataEngineer]ry": M[DataEngineer]gicMock(Sched[DataEngineer]lerAd[DataEngineer]p[DataEngineer]erRegi[DataEngineer][DataEngineer]ry=mock_regi[DataEngineer][DataEngineer]ry)},
        ):
            [DataEngineer]ool[DataEngineer]._ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er()

        c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer] = mock_regi[DataEngineer][DataEngineer]ry.cre[DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er.c[DataEngineer]ll_[DataEngineer]rg[DataEngineer].kw[DataEngineer]rg[DataEngineer]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "projec[DataEngineer]_n[DataEngineer]me" no[DataEngineer] in c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer]["config"]


# ── Sched[DataEngineer]lerTool[DataEngineer].[DataEngineer]v[DataEngineer]il[DataEngineer]ble_[DataEngineer]ool[DataEngineer] ─────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Av[DataEngineer]il[DataEngineer]bleTool[DataEngineer]:
    def [DataEngineer]e[DataEngineer][DataEngineer]_re[DataEngineer][DataEngineer]rn[DataEngineer]_[DataEngineer]ool_li[DataEngineer][DataEngineer]([DataEngineer]elf):
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]v[DataEngineer]il[DataEngineer]ble_[DataEngineer]ool[DataEngineer]()
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] i[DataEngineer]in[DataEngineer][DataEngineer][DataEngineer]nce(re[DataEngineer][DataEngineer]l[DataEngineer], li[DataEngineer][DataEngineer])
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] len(re[DataEngineer][DataEngineer]l[DataEngineer]) > 0
        [DataEngineer]ool_n[DataEngineer]me[DataEngineer] = {[DataEngineer].n[DataEngineer]me for [DataEngineer] in re[DataEngineer][DataEngineer]l[DataEngineer]}
        for expec[DataEngineer]ed in ["[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job", "[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_job", "[DataEngineer]rigger_[DataEngineer]ched[DataEngineer]ler_job", "ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job"]:
            [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] expec[DataEngineer]ed in [DataEngineer]ool_n[DataEngineer]me[DataEngineer]


# ── [DataEngineer]d[DataEngineer]p[DataEngineer]er.clo[DataEngineer]e() error h[DataEngineer]ndling ─────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Ad[DataEngineer]p[DataEngineer]erClo[DataEngineer]eError:
    """[DataEngineer]d[DataEngineer]p[DataEngineer]er.clo[DataEngineer]e() f[DataEngineer]il[DataEngineer]re [DataEngineer]ho[DataEngineer]ld no[DataEngineer] [DataEngineer]ffec[DataEngineer] [DataEngineer]he me[DataEngineer]hod re[DataEngineer][DataEngineer]l[DataEngineer]."""

    @py[DataEngineer]e[DataEngineer][DataEngineer].m[DataEngineer]rk.p[DataEngineer]r[DataEngineer]me[DataEngineer]rize(
        "me[DataEngineer]hod_n[DataEngineer]me, c[DataEngineer]ll_[DataEngineer]rg[DataEngineer], c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer], [DataEngineer]d[DataEngineer]p[DataEngineer]er_[DataEngineer]e[DataEngineer][DataEngineer]p",
        [
            (
                "[DataEngineer]rigger_[DataEngineer]ched[DataEngineer]ler_job",
                ("d[DataEngineer]g_1",),
                {},
                l[DataEngineer]mbd[DataEngineer] [DataEngineer]: [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r([DataEngineer], "[DataEngineer]rigger_job", M[DataEngineer]gicMock(re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=_m[DataEngineer]ke_job_r[DataEngineer]n())),
            ),
            (
                "ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job",
                ("d[DataEngineer]g_1",),
                {},
                l[DataEngineer]mbd[DataEngineer] [DataEngineer]: [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r([DataEngineer], "ge[DataEngineer]_job", M[DataEngineer]gicMock(re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=_m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job())),
            ),
            (
                "li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job[DataEngineer]",
                (),
                {},
                l[DataEngineer]mbd[DataEngineer] [DataEngineer]: [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r([DataEngineer], "li[DataEngineer][DataEngineer]_job[DataEngineer]", M[DataEngineer]gicMock(re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=_Sched[DataEngineer]lerP[DataEngineer]ge(i[DataEngineer]em[DataEngineer]=[], [DataEngineer]o[DataEngineer][DataEngineer]l=0))),
            ),
            ("p[DataEngineer][DataEngineer][DataEngineer]e_job", ("d[DataEngineer]g_1",), {}, None),
            ("re[DataEngineer][DataEngineer]me_job", ("d[DataEngineer]g_1",), {}, None),
            ("dele[DataEngineer]e_job", ("d[DataEngineer]g_1",), {}, None),
            (
                "li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer]",
                ("d[DataEngineer]g_1",),
                {},
                l[DataEngineer]mbd[DataEngineer] [DataEngineer]: [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r([DataEngineer], "li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer]", M[DataEngineer]gicMock(re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=_Sched[DataEngineer]lerP[DataEngineer]ge(i[DataEngineer]em[DataEngineer]=[], [DataEngineer]o[DataEngineer][DataEngineer]l=0))),
            ),
            (
                "ge[DataEngineer]_r[DataEngineer]n_log",
                ("d[DataEngineer]g_1", "r[DataEngineer]n_1"),
                {},
                l[DataEngineer]mbd[DataEngineer] [DataEngineer]: [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r([DataEngineer], "ge[DataEngineer]_r[DataEngineer]n_log", M[DataEngineer]gicMock(re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e="log [DataEngineer]ex[DataEngineer]")),
            ),
        ],
    )
    def [DataEngineer]e[DataEngineer][DataEngineer]_clo[DataEngineer]e_excep[DataEngineer]ion_[DataEngineer][DataEngineer]ill_re[DataEngineer][DataEngineer]rn[DataEngineer]([DataEngineer]elf, me[DataEngineer]hod_n[DataEngineer]me, c[DataEngineer]ll_[DataEngineer]rg[DataEngineer], c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer], [DataEngineer]d[DataEngineer]p[DataEngineer]er_[DataEngineer]e[DataEngineer][DataEngineer]p):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.clo[DataEngineer]e.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("clo[DataEngineer]e f[DataEngineer]iled")
        if [DataEngineer]d[DataEngineer]p[DataEngineer]er_[DataEngineer]e[DataEngineer][DataEngineer]p i[DataEngineer] no[DataEngineer] None:
            [DataEngineer]d[DataEngineer]p[DataEngineer]er_[DataEngineer]e[DataEngineer][DataEngineer]p(mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er)

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = ge[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r([DataEngineer]ool[DataEngineer], me[DataEngineer]hod_n[DataEngineer]me)(*c[DataEngineer]ll_[DataEngineer]rg[DataEngineer], **c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer])

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_clo[DataEngineer]e_excep[DataEngineer]ion_[DataEngineer][DataEngineer]ill_re[DataEngineer][DataEngineer]rn[DataEngineer]([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "q.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("j1")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.clo[DataEngineer]e.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("clo[DataEngineer]e f[DataEngineer]iled")

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job(job_n[DataEngineer]me="j1", [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file), conn_id="my_conn")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_clo[DataEngineer]e_excep[DataEngineer]ion_[DataEngineer][DataEngineer]ill_re[DataEngineer][DataEngineer]rn[DataEngineer]([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "q.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("j1")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.clo[DataEngineer]e.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("clo[DataEngineer]e f[DataEngineer]iled")

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_job(job_n[DataEngineer]me="j1", [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file))

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_clo[DataEngineer]e_excep[DataEngineer]ion_[DataEngineer][DataEngineer]ill_re[DataEngineer][DataEngineer]rn[DataEngineer]([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "q.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("j1")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.clo[DataEngineer]e.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("clo[DataEngineer]e f[DataEngineer]iled")

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(job_id="j1", [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file), job_n[DataEngineer]me="J1", conn_id="my_conn")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1


# ── _ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er error p[DataEngineer][DataEngineer]h[DataEngineer] in [DataEngineer]ool me[DataEngineer]hod[DataEngineer] ───────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Ad[DataEngineer]p[DataEngineer]erCre[DataEngineer][DataEngineer]ionError[DataEngineer]:
    @py[DataEngineer]e[DataEngineer][DataEngineer].m[DataEngineer]rk.p[DataEngineer]r[DataEngineer]me[DataEngineer]rize(
        "me[DataEngineer]hod_n[DataEngineer]me, c[DataEngineer]ll_[DataEngineer]rg[DataEngineer], c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer]",
        [
            ("[DataEngineer]rigger_[DataEngineer]ched[DataEngineer]ler_job", ("d[DataEngineer]g_1",), {}),
            ("ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job", ("d[DataEngineer]g_1",), {}),
            ("li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job[DataEngineer]", (), {}),
            ("p[DataEngineer][DataEngineer][DataEngineer]e_job", ("d[DataEngineer]g_1",), {}),
            ("re[DataEngineer][DataEngineer]me_job", ("d[DataEngineer]g_1",), {}),
            ("dele[DataEngineer]e_job", ("d[DataEngineer]g_1",), {}),
            ("li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer]", ("d[DataEngineer]g_1",), {}),
            ("ge[DataEngineer]_r[DataEngineer]n_log", ("d[DataEngineer]g_1", "r[DataEngineer]n_1"), {}),
        ],
    )
    def [DataEngineer]e[DataEngineer][DataEngineer]_no_[DataEngineer]ched[DataEngineer]ler_config_re[DataEngineer][DataEngineer]rn[DataEngineer]_f[DataEngineer]il[DataEngineer]re([DataEngineer]elf, me[DataEngineer]hod_n[DataEngineer]me, c[DataEngineer]ll_[DataEngineer]rg[DataEngineer], c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer]):
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config([DataEngineer]ched[DataEngineer]ler_config={}))
        re[DataEngineer][DataEngineer]l[DataEngineer] = ge[DataEngineer][DataEngineer][DataEngineer][DataEngineer]r([DataEngineer]ool[DataEngineer], me[DataEngineer]hod_n[DataEngineer]me)(*c[DataEngineer]ll_[DataEngineer]rg[DataEngineer], **c[DataEngineer]ll_kw[DataEngineer]rg[DataEngineer])
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_no_[DataEngineer]ched[DataEngineer]ler_config([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "q.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config([DataEngineer]ched[DataEngineer]ler_config={}))
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job(job_n[DataEngineer]me="j1", [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file), conn_id="my_conn")
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]ched[DataEngineer]ler" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_no_[DataEngineer]ched[DataEngineer]ler_config([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "q.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config([DataEngineer]ched[DataEngineer]ler_config={}))
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_job(job_n[DataEngineer]me="j1", [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file))
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]ched[DataEngineer]ler" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_no_[DataEngineer]ched[DataEngineer]ler_config([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "q.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config([DataEngineer]ched[DataEngineer]ler_config={}))
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(job_id="j1", [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file), job_n[DataEngineer]me="J1", conn_id="my_conn")
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]ched[DataEngineer]ler" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()


# ── [DataEngineer]AG [DataEngineer]empl[DataEngineer][DataEngineer]e [DataEngineer]e[DataEngineer][DataEngineer][DataEngineer] ─────────────────────────────────────────────────────


[DataEngineer]ry:
    from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_[DataEngineer]irflow.[DataEngineer]d[DataEngineer]p[DataEngineer]er impor[DataEngineer] AirflowSched[DataEngineer]lerAd[DataEngineer]p[DataEngineer]er
    from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_[DataEngineer]irflow.d[DataEngineer]g_[DataEngineer]empl[DataEngineer][DataEngineer]e impor[DataEngineer] render_[DataEngineer]p[DataEngineer]rk_d[DataEngineer]g_[DataEngineer]o[DataEngineer]rce
    from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.config impor[DataEngineer] AirflowConfig
    from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.model[DataEngineer] impor[DataEngineer] Sched[DataEngineer]lerJobP[DataEngineer]ylo[DataEngineer]d

    _HAS_SCHE[DataEngineer]ULER_AIRFLOW = Tr[DataEngineer]e
excep[DataEngineer] Impor[DataEngineer]Error:
    _HAS_SCHE[DataEngineer]ULER_AIRFLOW = F[DataEngineer]l[DataEngineer]e


@py[DataEngineer]e[DataEngineer][DataEngineer].m[DataEngineer]rk.[DataEngineer]kipif(no[DataEngineer] _HAS_SCHE[DataEngineer]ULER_AIRFLOW, re[DataEngineer][DataEngineer]on="d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]-[DataEngineer]ched[DataEngineer]ler-[DataEngineer]irflow no[DataEngineer] in[DataEngineer][DataEngineer][DataEngineer]lled")
cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]RenderSp[DataEngineer]rk[DataEngineer][DataEngineer]gSo[DataEngineer]rce:
    def [DataEngineer]e[DataEngineer][DataEngineer]_render[DataEngineer]_v[DataEngineer]lid_py[DataEngineer]hon([DataEngineer]elf):
        """Gener[DataEngineer][DataEngineer]ed [DataEngineer]AG [DataEngineer]o[DataEngineer]rce m[DataEngineer][DataEngineer][DataEngineer] be v[DataEngineer]lid Py[DataEngineer]hon [DataEngineer]nd c[DataEngineer]rry [DataEngineer]he given d[DataEngineer]g_id."""
        [DataEngineer]o[DataEngineer]rce = render_[DataEngineer]p[DataEngineer]rk_d[DataEngineer]g_[DataEngineer]o[DataEngineer]rce(
            d[DataEngineer]g_id="[DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]p[DataEngineer]rk_pi",
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]p[DataEngineer]rk_pi",
            [DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer]='prin[DataEngineer]("hello")',
        )
        # compile() r[DataEngineer]i[DataEngineer]e[DataEngineer] Syn[DataEngineer][DataEngineer]xError on inv[DataEngineer]lid Py[DataEngineer]hon — [DataEngineer]h[DataEngineer][DataEngineer]'[DataEngineer] [DataEngineer]he prim[DataEngineer]ry con[DataEngineer]r[DataEngineer]c[DataEngineer].
        compile([DataEngineer]o[DataEngineer]rce, "<[DataEngineer]e[DataEngineer][DataEngineer]_d[DataEngineer]g>", "exec")
        # Verify [DataEngineer]he rendered [DataEngineer]o[DataEngineer]rce [DataEngineer]c[DataEngineer][DataEngineer][DataEngineer]lly incorpor[DataEngineer][DataEngineer]e[DataEngineer] [DataEngineer]he c[DataEngineer]ller'[DataEngineer] [DataEngineer]rg[DataEngineer]men[DataEngineer][DataEngineer].
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]p[DataEngineer]rk_pi" in [DataEngineer]o[DataEngineer]rce, "d[DataEngineer]g_id [DataEngineer]ho[DataEngineer]ld [DataEngineer]ppe[DataEngineer]r in rendered [DataEngineer]o[DataEngineer]rce"
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] i[DataEngineer]in[DataEngineer][DataEngineer][DataEngineer]nce([DataEngineer]o[DataEngineer]rce, [DataEngineer][DataEngineer]r) [DataEngineer]nd len([DataEngineer]o[DataEngineer]rce) > 0

    def [DataEngineer]e[DataEngineer][DataEngineer]_embed[DataEngineer]_[DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer]([DataEngineer]elf):
        """The [DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer] con[DataEngineer]en[DataEngineer] m[DataEngineer][DataEngineer][DataEngineer] [DataEngineer]ppe[DataEngineer]r in [DataEngineer]he rendered [DataEngineer]o[DataEngineer]rce."""
        [DataEngineer]crip[DataEngineer] = "prin[DataEngineer]('[[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]] Pi [DataEngineer]e[DataEngineer][DataEngineer]')"
        [DataEngineer]o[DataEngineer]rce = render_[DataEngineer]p[DataEngineer]rk_d[DataEngineer]g_[DataEngineer]o[DataEngineer]rce(
            d[DataEngineer]g_id="[DataEngineer]e[DataEngineer][DataEngineer]_embed",
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]_embed",
            [DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer]=[DataEngineer]crip[DataEngineer],
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] j[DataEngineer]on.d[DataEngineer]mp[DataEngineer]([DataEngineer]crip[DataEngineer]) in [DataEngineer]o[DataEngineer]rce

    def [DataEngineer]e[DataEngineer][DataEngineer]_embed[DataEngineer]_[DataEngineer]p[DataEngineer]rk_m[DataEngineer][DataEngineer][DataEngineer]er([DataEngineer]elf):
        """C[DataEngineer][DataEngineer][DataEngineer]om [DataEngineer]p[DataEngineer]rk_m[DataEngineer][DataEngineer][DataEngineer]er m[DataEngineer][DataEngineer][DataEngineer] [DataEngineer]ppe[DataEngineer]r in [DataEngineer]he rendered [DataEngineer]o[DataEngineer]rce."""
        [DataEngineer]o[DataEngineer]rce = render_[DataEngineer]p[DataEngineer]rk_d[DataEngineer]g_[DataEngineer]o[DataEngineer]rce(
            d[DataEngineer]g_id="[DataEngineer]e[DataEngineer][DataEngineer]_m[DataEngineer][DataEngineer][DataEngineer]er",
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]_m[DataEngineer][DataEngineer][DataEngineer]er",
            [DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer]="p[DataEngineer][DataEngineer][DataEngineer]",
            [DataEngineer]p[DataEngineer]rk_m[DataEngineer][DataEngineer][DataEngineer]er="[DataEngineer]p[DataEngineer]rk://loc[DataEngineer]lho[DataEngineer][DataEngineer]:7077",
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]p[DataEngineer]rk://loc[DataEngineer]lho[DataEngineer][DataEngineer]:7077" in [DataEngineer]o[DataEngineer]rce

    def [DataEngineer]e[DataEngineer][DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]_[DataEngineer]p[DataEngineer]rk_m[DataEngineer][DataEngineer][DataEngineer]er([DataEngineer]elf):
        """[DataEngineer]ef[DataEngineer][DataEngineer]l[DataEngineer] [DataEngineer]p[DataEngineer]rk m[DataEngineer][DataEngineer][DataEngineer]er [DataEngineer]ho[DataEngineer]ld be loc[DataEngineer]l[*]."""
        [DataEngineer]o[DataEngineer]rce = render_[DataEngineer]p[DataEngineer]rk_d[DataEngineer]g_[DataEngineer]o[DataEngineer]rce(
            d[DataEngineer]g_id="[DataEngineer]e[DataEngineer][DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]",
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]",
            [DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer]="p[DataEngineer][DataEngineer][DataEngineer]",
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "loc[DataEngineer]l[*]" in [DataEngineer]o[DataEngineer]rce

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]le_embedded([DataEngineer]elf):
        """Cron [DataEngineer]ched[DataEngineer]le m[DataEngineer][DataEngineer][DataEngineer] [DataEngineer]ppe[DataEngineer]r in [DataEngineer]he rendered [DataEngineer]o[DataEngineer]rce."""
        [DataEngineer]o[DataEngineer]rce = render_[DataEngineer]p[DataEngineer]rk_d[DataEngineer]g_[DataEngineer]o[DataEngineer]rce(
            d[DataEngineer]g_id="[DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]le",
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]le",
            [DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer]="p[DataEngineer][DataEngineer][DataEngineer]",
            [DataEngineer]ched[DataEngineer]le="0 8 * * *",
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "0 8 * * *" in [DataEngineer]o[DataEngineer]rce


# ── Sched[DataEngineer]lerTool[DataEngineer].[DataEngineer]rigger_[DataEngineer]ched[DataEngineer]ler_job ─────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]TriggerSched[DataEngineer]lerJob:
    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]rigger_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]([DataEngineer]elf):
        """[DataEngineer]rigger_[DataEngineer]ched[DataEngineer]ler_job re[DataEngineer][DataEngineer]rn[DataEngineer] r[DataEngineer]n_id on [DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]."""
        mock_r[DataEngineer]n = _m[DataEngineer]ke_job_r[DataEngineer]n()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]rigger_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_r[DataEngineer]n

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]rigger_[DataEngineer]ched[DataEngineer]ler_job("[DataEngineer]p[DataEngineer]rk_pi_[DataEngineer]e[DataEngineer][DataEngineer]")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["r[DataEngineer]n_id"] == "m[DataEngineer]n[DataEngineer][DataEngineer]l__2025-01-01"

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]rigger_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf):
        """[DataEngineer]rigger_[DataEngineer]ched[DataEngineer]ler_job re[DataEngineer][DataEngineer]rn[DataEngineer] error when [DataEngineer]d[DataEngineer]p[DataEngineer]er r[DataEngineer]i[DataEngineer]e[DataEngineer]."""
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]rigger_job.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("d[DataEngineer]g no[DataEngineer] fo[DataEngineer]nd")

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]rigger_[DataEngineer]ched[DataEngineer]ler_job("mi[DataEngineer][DataEngineer]ing_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "d[DataEngineer]g no[DataEngineer] fo[DataEngineer]nd" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")


# ── Sched[DataEngineer]lerTool[DataEngineer].ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job ─────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Ge[DataEngineer]Sched[DataEngineer]lerJob:
    def [DataEngineer]e[DataEngineer][DataEngineer]_ge[DataEngineer]_exi[DataEngineer][DataEngineer]ing_job([DataEngineer]elf):
        """ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job re[DataEngineer][DataEngineer]rn[DataEngineer] fo[DataEngineer]nd=Tr[DataEngineer]e for [DataEngineer]n exi[DataEngineer][DataEngineer]ing job."""
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.ge[DataEngineer]_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job()

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job("[DataEngineer]p[DataEngineer]rk_pi_[DataEngineer]e[DataEngineer][DataEngineer]")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["fo[DataEngineer]nd"] i[DataEngineer] Tr[DataEngineer]e
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["job_id"] == "[DataEngineer]p[DataEngineer]rk_pi_[DataEngineer]e[DataEngineer][DataEngineer]"

    def [DataEngineer]e[DataEngineer][DataEngineer]_ge[DataEngineer]_mi[DataEngineer][DataEngineer]ing_job([DataEngineer]elf):
        """ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job re[DataEngineer][DataEngineer]rn[DataEngineer] fo[DataEngineer]nd=F[DataEngineer]l[DataEngineer]e when job doe[DataEngineer] no[DataEngineer] exi[DataEngineer][DataEngineer]."""
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.ge[DataEngineer]_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = None

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].ge[DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job("gho[DataEngineer][DataEngineer]_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["fo[DataEngineer]nd"] i[DataEngineer] F[DataEngineer]l[DataEngineer]e


# ── Sched[DataEngineer]lerTool[DataEngineer].li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job[DataEngineer] ───────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Li[DataEngineer][DataEngineer]Sched[DataEngineer]lerJob[DataEngineer]:
    def [DataEngineer]e[DataEngineer][DataEngineer]_li[DataEngineer][DataEngineer]_job[DataEngineer]([DataEngineer]elf):
        """li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job[DataEngineer] re[DataEngineer][DataEngineer]rn[DataEngineer] [DataEngineer]he c[DataEngineer]nonic[DataEngineer]l F[DataEngineer]ncToolLi[DataEngineer][DataEngineer]Re[DataEngineer][DataEngineer]l[DataEngineer] envelope."""
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.li[DataEngineer][DataEngineer]_job[DataEngineer].re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = _Sched[DataEngineer]lerP[DataEngineer]ge(
            i[DataEngineer]em[DataEngineer]=[_m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("d[DataEngineer]g_[DataEngineer]"), _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("d[DataEngineer]g_b")],
            [DataEngineer]o[DataEngineer][DataEngineer]l=2,
        )

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_job[DataEngineer](limi[DataEngineer]=10)

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        envelope = re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] envelope["[DataEngineer]o[DataEngineer][DataEngineer]l"] == 2
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] len(envelope["i[DataEngineer]em[DataEngineer]"]) == 2
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] envelope["i[DataEngineer]em[DataEngineer]"][0]["job_id"] == "d[DataEngineer]g_[DataEngineer]"
        # 2 i[DataEngineer]em[DataEngineer] wi[DataEngineer]h [DataEngineer]o[DataEngineer][DataEngineer]l=2 [DataEngineer]nd off[DataEngineer]e[DataEngineer]=0 → l[DataEngineer][DataEngineer][DataEngineer] p[DataEngineer]ge, no nex[DataEngineer]_off[DataEngineer]e[DataEngineer].
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] envelope["h[DataEngineer][DataEngineer]_more"] i[DataEngineer] F[DataEngineer]l[DataEngineer]e
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] envelope["ex[DataEngineer]r[DataEngineer]"] i[DataEngineer] None


# ── [DataEngineer]d[DataEngineer]p[DataEngineer]er.py: [DataEngineer][DataEngineer]bmi[DataEngineer]_job wi[DataEngineer]h job_[DataEngineer]ype=[DataEngineer]p[DataEngineer]rk ───────────────────────────


@py[DataEngineer]e[DataEngineer][DataEngineer].m[DataEngineer]rk.[DataEngineer]kipif(no[DataEngineer] _HAS_SCHE[DataEngineer]ULER_AIRFLOW, re[DataEngineer][DataEngineer]on="d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]-[DataEngineer]ched[DataEngineer]ler-[DataEngineer]irflow no[DataEngineer] in[DataEngineer][DataEngineer][DataEngineer]lled")
cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Ad[DataEngineer]p[DataEngineer]erSp[DataEngineer]rkBr[DataEngineer]nch:
    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer][DataEngineer]bmi[DataEngineer]_job_[DataEngineer]p[DataEngineer]rk_c[DataEngineer]ll[DataEngineer]_render_[DataEngineer]p[DataEngineer]rk([DataEngineer]elf):
        """[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job wi[DataEngineer]h job_[DataEngineer]ype='[DataEngineer]p[DataEngineer]rk' [DataEngineer][DataEngineer]e[DataEngineer] render_[DataEngineer]p[DataEngineer]rk_d[DataEngineer]g_[DataEngineer]o[DataEngineer]rce."""
        config = AirflowConfig(
            n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]",
            [DataEngineer]ype="[DataEngineer]irflow",
            [DataEngineer]pi_b[DataEngineer][DataEngineer]e_[DataEngineer]rl="h[DataEngineer][DataEngineer]p://loc[DataEngineer]lho[DataEngineer][DataEngineer]:8080/[DataEngineer]pi/v1",
            [DataEngineer][DataEngineer]ern[DataEngineer]me="[DataEngineer]dmin",
            p[DataEngineer][DataEngineer][DataEngineer]word="[DataEngineer]dmin123",
            d[DataEngineer]g[DataEngineer]_folder="/[DataEngineer]mp/d[DataEngineer]g[DataEngineer]",
        )
        [DataEngineer]d[DataEngineer]p[DataEngineer]er = AirflowSched[DataEngineer]lerAd[DataEngineer]p[DataEngineer]er.__new__(AirflowSched[DataEngineer]lerAd[DataEngineer]p[DataEngineer]er)
        [DataEngineer]d[DataEngineer]p[DataEngineer]er._config = config
        [DataEngineer]d[DataEngineer]p[DataEngineer]er._[DataEngineer]e[DataEngineer][DataEngineer]ion = M[DataEngineer]gicMock()
        [DataEngineer]d[DataEngineer]p[DataEngineer]er._[DataEngineer]e[DataEngineer][DataEngineer]ion.ge[DataEngineer].re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = M[DataEngineer]gicMock([DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]_code=404)

        wri[DataEngineer][DataEngineer]en_[DataEngineer]o[DataEngineer]rce = {}

        def f[DataEngineer]ke_wri[DataEngineer]e(d[DataEngineer]g_id, [DataEngineer]o[DataEngineer]rce):
            wri[DataEngineer][DataEngineer]en_[DataEngineer]o[DataEngineer]rce["[DataEngineer]o[DataEngineer]rce"] = [DataEngineer]o[DataEngineer]rce

        def f[DataEngineer]ke_w[DataEngineer]i[DataEngineer](d[DataEngineer]g_id):
            p[DataEngineer][DataEngineer][DataEngineer]

        def f[DataEngineer]ke_ge[DataEngineer](d[DataEngineer]g_id):
            from d[DataEngineer][DataEngineer][DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_core.model[DataEngineer] impor[DataEngineer] JobS[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer], Sched[DataEngineer]ledJob

            re[DataEngineer][DataEngineer]rn Sched[DataEngineer]ledJob(
                [DataEngineer]ched[DataEngineer]ler_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]",
                pl[DataEngineer][DataEngineer]form="[DataEngineer]irflow",
                job_id=d[DataEngineer]g_id,
                job_n[DataEngineer]me=d[DataEngineer]g_id,
                [DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]=JobS[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer].ACTIVE,
            )

        [DataEngineer]d[DataEngineer]p[DataEngineer]er._wri[DataEngineer]e_d[DataEngineer]g_file = f[DataEngineer]ke_wri[DataEngineer]e
        [DataEngineer]d[DataEngineer]p[DataEngineer]er._w[DataEngineer]i[DataEngineer]_for_d[DataEngineer]g_di[DataEngineer]covery = f[DataEngineer]ke_w[DataEngineer]i[DataEngineer]
        [DataEngineer]d[DataEngineer]p[DataEngineer]er.ge[DataEngineer]_job = M[DataEngineer]gicMock([DataEngineer]ide_effec[DataEngineer]=[None, f[DataEngineer]ke_ge[DataEngineer]("[DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]p[DataEngineer]rk")])

        p[DataEngineer]ylo[DataEngineer]d = Sched[DataEngineer]lerJobP[DataEngineer]ylo[DataEngineer]d(
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]p[DataEngineer]rk",
            ex[DataEngineer]r[DataEngineer]={
                "job_[DataEngineer]ype": "[DataEngineer]p[DataEngineer]rk",
                "[DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer]": 'prin[DataEngineer]("pi")',
                "[DataEngineer]p[DataEngineer]rk_m[DataEngineer][DataEngineer][DataEngineer]er": "loc[DataEngineer]l[*]",
            },
        )
        job = [DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job(p[DataEngineer]ylo[DataEngineer]d)

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] job.job_id == "[DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]p[DataEngineer]rk"
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]Sp[DataEngineer]rkJob" in wri[DataEngineer][DataEngineer]en_[DataEngineer]o[DataEngineer]rce["[DataEngineer]o[DataEngineer]rce"]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "_r[DataEngineer]n_[DataEngineer]p[DataEngineer]rk_[DataEngineer]crip[DataEngineer]" in wri[DataEngineer][DataEngineer]en_[DataEngineer]o[DataEngineer]rce["[DataEngineer]o[DataEngineer]rce"]


# ── Sched[DataEngineer]lerTool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job ────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]S[DataEngineer]bmi[DataEngineer]SqlJob:
    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]_wi[DataEngineer]h_conn_id([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "q[DataEngineer]ery.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("[DataEngineer]ql_job_1")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job(
                job_n[DataEngineer]me="[DataEngineer]ql_job_1",
                [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
                conn_id="[DataEngineer][DataEngineer][DataEngineer]rrock[DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]",
            )

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["job_id"] == "[DataEngineer]ql_job_1"
        p[DataEngineer]ylo[DataEngineer]d = mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job.c[DataEngineer]ll_[DataEngineer]rg[DataEngineer][0][0]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] p[DataEngineer]ylo[DataEngineer]d.db_connec[DataEngineer]ion == {"conn_id": "[DataEngineer][DataEngineer][DataEngineer]rrock[DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]"}

    def [DataEngineer]e[DataEngineer][DataEngineer]_mi[DataEngineer][DataEngineer]ing_[DataEngineer]ql_file([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job(
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]",
            [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]mp_p[DataEngineer][DataEngineer]h / "nonexi[DataEngineer][DataEngineer]en[DataEngineer].[DataEngineer]ql"),
            conn_id="my_conn",
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "no[DataEngineer] fo[DataEngineer]nd" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()

    def [DataEngineer]e[DataEngineer][DataEngineer]_emp[DataEngineer]y_[DataEngineer]ql_file([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "emp[DataEngineer]y.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("   ")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job(
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]",
            [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
            conn_id="my_conn",
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "emp[DataEngineer]y" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "q[DataEngineer]ery.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")

        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("Connec[DataEngineer]ion f[DataEngineer]iled")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.clo[DataEngineer]e.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = None

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job(job_n[DataEngineer]me="j1", [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file), conn_id="my_conn")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "Connec[DataEngineer]ion f[DataEngineer]iled" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")


# ── Sched[DataEngineer]lerTool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_job ───────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]S[DataEngineer]bmi[DataEngineer]Sp[DataEngineer]rk[DataEngineer]qlJob:
    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]p[DataEngineer]rk[DataEngineer]ql.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT * FROM [DataEngineer]")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_1")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_job(
                job_n[DataEngineer]me="[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_1",
                [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
            )

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["job_id"] == "[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_1"

    def [DataEngineer]e[DataEngineer][DataEngineer]_mi[DataEngineer][DataEngineer]ing_[DataEngineer]ql_file([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_job(
            job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]",
            [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]mp_p[DataEngineer][DataEngineer]h / "mi[DataEngineer][DataEngineer]ing.[DataEngineer]ql"),
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "no[DataEngineer] fo[DataEngineer]nd" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]p[DataEngineer]rk[DataEngineer]ql.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")

        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer][DataEngineer]bmi[DataEngineer]_job.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("[DataEngineer]imeo[DataEngineer][DataEngineer]")

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_job(
                job_n[DataEngineer]me="[DataEngineer]e[DataEngineer][DataEngineer]",
                [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
            )

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]imeo[DataEngineer][DataEngineer]" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")


# ── Sched[DataEngineer]lerTool[DataEngineer].p[DataEngineer][DataEngineer][DataEngineer]e_job ─────────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]P[DataEngineer][DataEngineer][DataEngineer]eJob:
    def [DataEngineer]e[DataEngineer][DataEngineer]_p[DataEngineer][DataEngineer][DataEngineer]e_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].p[DataEngineer][DataEngineer][DataEngineer]e_job("my_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]"] == "p[DataEngineer][DataEngineer][DataEngineer]ed"
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.p[DataEngineer][DataEngineer][DataEngineer]e_job.[DataEngineer][DataEngineer][DataEngineer]er[DataEngineer]_c[DataEngineer]lled_once_wi[DataEngineer]h("my_d[DataEngineer]g")

    def [DataEngineer]e[DataEngineer][DataEngineer]_p[DataEngineer][DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.p[DataEngineer][DataEngineer][DataEngineer]e_job.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("no[DataEngineer] fo[DataEngineer]nd")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].p[DataEngineer][DataEngineer][DataEngineer]e_job("mi[DataEngineer][DataEngineer]ing")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "no[DataEngineer] fo[DataEngineer]nd" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")


# ── Sched[DataEngineer]lerTool[DataEngineer].re[DataEngineer][DataEngineer]me_job ────────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Re[DataEngineer][DataEngineer]meJob:
    def [DataEngineer]e[DataEngineer][DataEngineer]_re[DataEngineer][DataEngineer]me_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].re[DataEngineer][DataEngineer]me_job("my_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]"] == "[DataEngineer]c[DataEngineer]ive"
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.re[DataEngineer][DataEngineer]me_job.[DataEngineer][DataEngineer][DataEngineer]er[DataEngineer]_c[DataEngineer]lled_once_wi[DataEngineer]h("my_d[DataEngineer]g")

    def [DataEngineer]e[DataEngineer][DataEngineer]_re[DataEngineer][DataEngineer]me_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.re[DataEngineer][DataEngineer]me_job.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("forbidden")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].re[DataEngineer][DataEngineer]me_job("my_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "forbidden" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")


# ── Sched[DataEngineer]lerTool[DataEngineer].dele[DataEngineer]e_job ────────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer][DataEngineer]ele[DataEngineer]eJob:
    def [DataEngineer]e[DataEngineer][DataEngineer]_dele[DataEngineer]e_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].dele[DataEngineer]e_job("old_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]"] == "dele[DataEngineer]ed"
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.dele[DataEngineer]e_job.[DataEngineer][DataEngineer][DataEngineer]er[DataEngineer]_c[DataEngineer]lled_once_wi[DataEngineer]h("old_d[DataEngineer]g")

    def [DataEngineer]e[DataEngineer][DataEngineer]_dele[DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.dele[DataEngineer]e_job.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("permi[DataEngineer][DataEngineer]ion denied")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].dele[DataEngineer]e_job("old_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "permi[DataEngineer][DataEngineer]ion denied" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")


# ── Sched[DataEngineer]lerTool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job ────────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Upd[DataEngineer][DataEngineer]eJob:
    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]_wi[DataEngineer]h_conn_id([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]pd[DataEngineer][DataEngineer]ed.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 2")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("d[DataEngineer]g_[DataEngineer]o_[DataEngineer]pd[DataEngineer][DataEngineer]e")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(
                job_id="d[DataEngineer]g_[DataEngineer]o_[DataEngineer]pd[DataEngineer][DataEngineer]e",
                [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
                job_n[DataEngineer]me="[DataEngineer]AG To Upd[DataEngineer][DataEngineer]e",
                conn_id="[DataEngineer][DataEngineer][DataEngineer]rrock[DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]",
            )

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["job_id"] == "d[DataEngineer]g_[DataEngineer]o_[DataEngineer]pd[DataEngineer][DataEngineer]e"
        p[DataEngineer]ylo[DataEngineer]d = mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.c[DataEngineer]ll_[DataEngineer]rg[DataEngineer][0][1]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] p[DataEngineer]ylo[DataEngineer]d.db_connec[DataEngineer]ion == {"conn_id": "[DataEngineer][DataEngineer][DataEngineer]rrock[DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]"}

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_mi[DataEngineer][DataEngineer]ing_[DataEngineer]ql_file([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(
            job_id="d[DataEngineer]g_x",
            [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]mp_p[DataEngineer][DataEngineer]h / "gone.[DataEngineer]ql"),
            job_n[DataEngineer]me="[DataEngineer]AG X",
            conn_id="my_conn",
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "no[DataEngineer] fo[DataEngineer]nd" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_no_conn_id_re[DataEngineer][DataEngineer]rn[DataEngineer]_error([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]pd[DataEngineer][DataEngineer]ed.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 2")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(
            job_id="d[DataEngineer]g_x",
            [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
            job_n[DataEngineer]me="[DataEngineer]AG X",
            job_[DataEngineer]ype="[DataEngineer]ql",
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "conn_id" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_inv[DataEngineer]lid_job_[DataEngineer]ype([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]pd[DataEngineer][DataEngineer]ed.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 2")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(
            job_id="d[DataEngineer]g_x",
            [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
            job_n[DataEngineer]me="[DataEngineer]AG X",
            job_[DataEngineer]ype="py[DataEngineer]p[DataEngineer]rk",
        )
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "Un[DataEngineer][DataEngineer]ppor[DataEngineer]ed job_[DataEngineer]ype" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]p[DataEngineer]rk_[DataEngineer]pd[DataEngineer][DataEngineer]ed.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT * FROM [DataEngineer]")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("d[DataEngineer]g_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_[DataEngineer]pd[DataEngineer][DataEngineer]e")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(
                job_id="d[DataEngineer]g_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_[DataEngineer]pd[DataEngineer][DataEngineer]e",
                [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
                job_n[DataEngineer]me="Sp[DataEngineer]rkSQL Upd[DataEngineer][DataEngineer]e Job",
                job_[DataEngineer]ype="[DataEngineer]p[DataEngineer]rk[DataEngineer]ql",
                [DataEngineer]p[DataEngineer]rk_m[DataEngineer][DataEngineer][DataEngineer]er="[DataEngineer]p[DataEngineer]rk://loc[DataEngineer]lho[DataEngineer][DataEngineer]:7077",
            )

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["job_id"] == "d[DataEngineer]g_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_[DataEngineer]pd[DataEngineer][DataEngineer]e"
        # Verify [DataEngineer]d[DataEngineer]p[DataEngineer]er w[DataEngineer][DataEngineer] c[DataEngineer]lled wi[DataEngineer]h [DataEngineer]p[DataEngineer]rk[DataEngineer]ql p[DataEngineer]ylo[DataEngineer]d
        c[DataEngineer]ll_[DataEngineer]rg[DataEngineer] = mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.c[DataEngineer]ll_[DataEngineer]rg[DataEngineer]
        p[DataEngineer]ylo[DataEngineer]d = c[DataEngineer]ll_[DataEngineer]rg[DataEngineer][0][1]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] p[DataEngineer]ylo[DataEngineer]d.ex[DataEngineer]r[DataEngineer]["job_[DataEngineer]ype"] == "[DataEngineer]p[DataEngineer]rk[DataEngineer]ql"
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] p[DataEngineer]ylo[DataEngineer]d.ex[DataEngineer]r[DataEngineer]["[DataEngineer]p[DataEngineer]rk[DataEngineer]ql"] == "SELECT * FROM [DataEngineer]"
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] p[DataEngineer]ylo[DataEngineer]d.ex[DataEngineer]r[DataEngineer]["[DataEngineer]p[DataEngineer]rk_m[DataEngineer][DataEngineer][DataEngineer]er"] == "[DataEngineer]p[DataEngineer]rk://loc[DataEngineer]lho[DataEngineer][DataEngineer]:7077"

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_def[DataEngineer][DataEngineer]l[DataEngineer]_m[DataEngineer][DataEngineer][DataEngineer]er([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]p[DataEngineer]rk_[DataEngineer]pd[DataEngineer][DataEngineer]ed.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("d[DataEngineer]g_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_def[DataEngineer][DataEngineer]l[DataEngineer]")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(
                job_id="d[DataEngineer]g_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_def[DataEngineer][DataEngineer]l[DataEngineer]",
                [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
                job_n[DataEngineer]me="Sp[DataEngineer]rkSQL [DataEngineer]ef[DataEngineer][DataEngineer]l[DataEngineer] Job",
                job_[DataEngineer]ype="[DataEngineer]p[DataEngineer]rk[DataEngineer]ql",
            )

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        c[DataEngineer]ll_[DataEngineer]rg[DataEngineer] = mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.c[DataEngineer]ll_[DataEngineer]rg[DataEngineer]
        p[DataEngineer]ylo[DataEngineer]d = c[DataEngineer]ll_[DataEngineer]rg[DataEngineer][0][1]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] p[DataEngineer]ylo[DataEngineer]d.ex[DataEngineer]r[DataEngineer]["[DataEngineer]p[DataEngineer]rk_m[DataEngineer][DataEngineer][DataEngineer]er"] == "loc[DataEngineer]l[*]"

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_[DataEngineer]p[DataEngineer]rk[DataEngineer]ql_no_conn_id_needed([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        """Sp[DataEngineer]rkSQL [DataEngineer]pd[DataEngineer][DataEngineer]e [DataEngineer]ho[DataEngineer]ld [DataEngineer][DataEngineer]cceed wi[DataEngineer]ho[DataEngineer][DataEngineer] conn_id."""
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]p[DataEngineer]rk.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 1")

        mock_job = _m[DataEngineer]ke_[DataEngineer]ched[DataEngineer]led_job("d[DataEngineer]g_[DataEngineer]p[DataEngineer]rk_no_db")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = mock_job

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(
                job_id="d[DataEngineer]g_[DataEngineer]p[DataEngineer]rk_no_db",
                [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file),
                job_n[DataEngineer]me="Sp[DataEngineer]rk No [DataEngineer]B Job",
                job_[DataEngineer]ype="[DataEngineer]p[DataEngineer]rk[DataEngineer]ql",
            )

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1

    def [DataEngineer]e[DataEngineer][DataEngineer]_[DataEngineer]pd[DataEngineer][DataEngineer]e_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf, [DataEngineer]mp_p[DataEngineer][DataEngineer]h):
        [DataEngineer]ql_file = [DataEngineer]mp_p[DataEngineer][DataEngineer]h / "[DataEngineer]pd[DataEngineer][DataEngineer]ed.[DataEngineer]ql"
        [DataEngineer]ql_file.wri[DataEngineer]e_[DataEngineer]ex[DataEngineer]("SELECT 2")

        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.[DataEngineer]pd[DataEngineer][DataEngineer]e_job.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("[DataEngineer]pd[DataEngineer][DataEngineer]e f[DataEngineer]iled")
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.clo[DataEngineer]e.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = None

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())
        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]pd[DataEngineer][DataEngineer]e_job(job_id="j1", [DataEngineer]ql_file_p[DataEngineer][DataEngineer]h=[DataEngineer][DataEngineer]r([DataEngineer]ql_file), job_n[DataEngineer]me="J1", conn_id="my_conn")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]pd[DataEngineer][DataEngineer]e f[DataEngineer]iled" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")


# ── Sched[DataEngineer]lerTool[DataEngineer].li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_connec[DataEngineer]ion[DataEngineer] ─────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Li[DataEngineer][DataEngineer]Sched[DataEngineer]lerConnec[DataEngineer]ion[DataEngineer]:
    def [DataEngineer]e[DataEngineer][DataEngineer]_re[DataEngineer][DataEngineer]rn[DataEngineer]_config[DataEngineer]red_connec[DataEngineer]ion[DataEngineer]([DataEngineer]elf):
        cfg = _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config()
        cfg.[DataEngineer]ched[DataEngineer]ler_config["connec[DataEngineer]ion[DataEngineer]"] = {
            "[DataEngineer][DataEngineer][DataEngineer]rrock[DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]": "S[DataEngineer][DataEngineer]rRock[DataEngineer] [DataEngineer]c_m[DataEngineer]n[DataEngineer]ge",
            "pg_conn": "Po[DataEngineer][DataEngineer]greSQL [DataEngineer]e[DataEngineer][DataEngineer] [DataEngineer]B",
        }
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](cfg)
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_connec[DataEngineer]ion[DataEngineer]()

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["[DataEngineer]o[DataEngineer][DataEngineer]l"] == 2
        conn_id[DataEngineer] = [c["conn_id"] for c in re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["connec[DataEngineer]ion[DataEngineer]"]]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer][DataEngineer][DataEngineer]rrock[DataEngineer]_def[DataEngineer][DataEngineer]l[DataEngineer]" in conn_id[DataEngineer]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "pg_conn" in conn_id[DataEngineer]

    def [DataEngineer]e[DataEngineer][DataEngineer]_emp[DataEngineer]y_connec[DataEngineer]ion[DataEngineer]([DataEngineer]elf):
        cfg = _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config()
        # No connec[DataEngineer]ion[DataEngineer] key
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](cfg)
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_connec[DataEngineer]ion[DataEngineer]()

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["[DataEngineer]o[DataEngineer][DataEngineer]l"] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "hin[DataEngineer]" in re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]

    def [DataEngineer]e[DataEngineer][DataEngineer]_no_[DataEngineer]ched[DataEngineer]ler_config([DataEngineer]elf):
        cfg = _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config([DataEngineer]ched[DataEngineer]ler_config={})
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](cfg)
        re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].li[DataEngineer][DataEngineer]_[DataEngineer]ched[DataEngineer]ler_connec[DataEngineer]ion[DataEngineer]()

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]ched[DataEngineer]ler" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "").lower()


# ── [DataEngineer]v[DataEngineer]il[DataEngineer]ble_[DataEngineer]ool[DataEngineer]: conn_id injec[DataEngineer]ion in[DataEngineer]o de[DataEngineer]crip[DataEngineer]ion ──────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]ConnId[DataEngineer]e[DataEngineer]crip[DataEngineer]ionInjec[DataEngineer]ion:
    def [DataEngineer]e[DataEngineer][DataEngineer]_connec[DataEngineer]ion[DataEngineer]_injec[DataEngineer]ed_in[DataEngineer]o_[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]nd_[DataEngineer]pd[DataEngineer][DataEngineer]e([DataEngineer]elf):
        cfg = _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config()
        cfg.[DataEngineer]ched[DataEngineer]ler_config["connec[DataEngineer]ion[DataEngineer]"] = {"[DataEngineer]r_def[DataEngineer][DataEngineer]l[DataEngineer]": "S[DataEngineer][DataEngineer]rRock[DataEngineer] [DataEngineer]B"}
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](cfg)
        [DataEngineer]ool_li[DataEngineer][DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]v[DataEngineer]il[DataEngineer]ble_[DataEngineer]ool[DataEngineer]()
        [DataEngineer]ool_m[DataEngineer]p = {[DataEngineer].n[DataEngineer]me: [DataEngineer] for [DataEngineer] in [DataEngineer]ool_li[DataEngineer][DataEngineer]}

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]r_def[DataEngineer][DataEngineer]l[DataEngineer]" in [DataEngineer]ool_m[DataEngineer]p["[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job"].de[DataEngineer]crip[DataEngineer]ion
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]r_def[DataEngineer][DataEngineer]l[DataEngineer]" in [DataEngineer]ool_m[DataEngineer]p["[DataEngineer]pd[DataEngineer][DataEngineer]e_job"].de[DataEngineer]crip[DataEngineer]ion
        # O[DataEngineer]her [DataEngineer]ool[DataEngineer] [DataEngineer]ho[DataEngineer]ld NOT h[DataEngineer]ve [DataEngineer]he [DataEngineer][DataEngineer]ffix
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]r_def[DataEngineer][DataEngineer]l[DataEngineer]" no[DataEngineer] in [DataEngineer]ool_m[DataEngineer]p["p[DataEngineer][DataEngineer][DataEngineer]e_job"].de[DataEngineer]crip[DataEngineer]ion

    def [DataEngineer]e[DataEngineer][DataEngineer]_no_connec[DataEngineer]ion[DataEngineer]_no_injec[DataEngineer]ion([DataEngineer]elf):
        cfg = _m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config()
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](cfg)
        [DataEngineer]ool_li[DataEngineer][DataEngineer] = [DataEngineer]ool[DataEngineer].[DataEngineer]v[DataEngineer]il[DataEngineer]ble_[DataEngineer]ool[DataEngineer]()
        [DataEngineer]ool_m[DataEngineer]p = {[DataEngineer].n[DataEngineer]me: [DataEngineer] for [DataEngineer] in [DataEngineer]ool_li[DataEngineer][DataEngineer]}

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "Av[DataEngineer]il[DataEngineer]ble conn_id" no[DataEngineer] in [DataEngineer]ool_m[DataEngineer]p["[DataEngineer][DataEngineer]bmi[DataEngineer]_[DataEngineer]ql_job"].de[DataEngineer]crip[DataEngineer]ion


# ── Sched[DataEngineer]lerTool[DataEngineer].li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer] ─────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Li[DataEngineer][DataEngineer]JobR[DataEngineer]n[DataEngineer]:
    def [DataEngineer]e[DataEngineer][DataEngineer]_li[DataEngineer][DataEngineer]_r[DataEngineer]n[DataEngineer]_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]([DataEngineer]elf):
        mock_r[DataEngineer]n = M[DataEngineer]gicMock()
        mock_r[DataEngineer]n.r[DataEngineer]n_id = "r[DataEngineer]n_001"
        mock_r[DataEngineer]n.[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer].v[DataEngineer]l[DataEngineer]e = "[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]"
        mock_r[DataEngineer]n.[DataEngineer][DataEngineer][DataEngineer]r[DataEngineer]ed_[DataEngineer][DataEngineer] = d[DataEngineer][DataEngineer]e[DataEngineer]ime(2025, 1, 1, 8, 0, 0, [DataEngineer]zinfo=[DataEngineer]imezone.[DataEngineer][DataEngineer]c)
        mock_r[DataEngineer]n.ended_[DataEngineer][DataEngineer] = d[DataEngineer][DataEngineer]e[DataEngineer]ime(2025, 1, 1, 8, 5, 0, [DataEngineer]zinfo=[DataEngineer]imezone.[DataEngineer][DataEngineer]c)

        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer].re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = _Sched[DataEngineer]lerP[DataEngineer]ge(i[DataEngineer]em[DataEngineer]=[mock_r[DataEngineer]n], [DataEngineer]o[DataEngineer][DataEngineer]l=1)

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer]("my_d[DataEngineer]g", limi[DataEngineer]=5)

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        envelope = re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] envelope["[DataEngineer]o[DataEngineer][DataEngineer]l"] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] len(envelope["i[DataEngineer]em[DataEngineer]"]) == 1
        r[DataEngineer]n = envelope["i[DataEngineer]em[DataEngineer]"][0]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] r[DataEngineer]n["r[DataEngineer]n_id"] == "r[DataEngineer]n_001"
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] r[DataEngineer]n["[DataEngineer][DataEngineer][DataEngineer]r[DataEngineer]ed_[DataEngineer][DataEngineer]"] == "2025-01-01T08:00:00+00:00"
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] r[DataEngineer]n["ended_[DataEngineer][DataEngineer]"] == "2025-01-01T08:05:00+00:00"
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] envelope["h[DataEngineer][DataEngineer]_more"] i[DataEngineer] F[DataEngineer]l[DataEngineer]e

    def [DataEngineer]e[DataEngineer][DataEngineer]_li[DataEngineer][DataEngineer]_r[DataEngineer]n[DataEngineer]_[DataEngineer][DataEngineer]ring_[DataEngineer]ime[DataEngineer][DataEngineer][DataEngineer]mp[DataEngineer]([DataEngineer]elf):
        """R[DataEngineer]n[DataEngineer] wi[DataEngineer]h [DataEngineer][DataEngineer]ring [DataEngineer]ime[DataEngineer][DataEngineer][DataEngineer]mp[DataEngineer] [DataEngineer]ho[DataEngineer]ld p[DataEngineer][DataEngineer][DataEngineer] [DataEngineer]hro[DataEngineer]gh [DataEngineer][DataEngineer]-i[DataEngineer]."""
        mock_r[DataEngineer]n = M[DataEngineer]gicMock()
        mock_r[DataEngineer]n.r[DataEngineer]n_id = "r[DataEngineer]n_002"
        mock_r[DataEngineer]n.[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer].v[DataEngineer]l[DataEngineer]e = "r[DataEngineer]nning"
        mock_r[DataEngineer]n.[DataEngineer][DataEngineer][DataEngineer]r[DataEngineer]ed_[DataEngineer][DataEngineer] = "2025-01-01T08:00:00Z"
        mock_r[DataEngineer]n.ended_[DataEngineer][DataEngineer] = None

        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer].re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = _Sched[DataEngineer]lerP[DataEngineer]ge(i[DataEngineer]em[DataEngineer]=[mock_r[DataEngineer]n], [DataEngineer]o[DataEngineer][DataEngineer]l=None)

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer]("my_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        r[DataEngineer]n = re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["i[DataEngineer]em[DataEngineer]"][0]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] r[DataEngineer]n["[DataEngineer][DataEngineer][DataEngineer]r[DataEngineer]ed_[DataEngineer][DataEngineer]"] == "2025-01-01T08:00:00Z"
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] r[DataEngineer]n["ended_[DataEngineer][DataEngineer]"] i[DataEngineer] None

    def [DataEngineer]e[DataEngineer][DataEngineer]_li[DataEngineer][DataEngineer]_r[DataEngineer]n[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer].[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("[DataEngineer]pi error")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].li[DataEngineer][DataEngineer]_job_r[DataEngineer]n[DataEngineer]("my_d[DataEngineer]g")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "[DataEngineer]pi error" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")


# ── Sched[DataEngineer]lerTool[DataEngineer].ge[DataEngineer]_r[DataEngineer]n_log ───────────────────────────────────────────


cl[DataEngineer][DataEngineer][DataEngineer] Te[DataEngineer][DataEngineer]Ge[DataEngineer]R[DataEngineer]nLog:
    def [DataEngineer]e[DataEngineer][DataEngineer]_ge[DataEngineer]_log_[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer]([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.ge[DataEngineer]_r[DataEngineer]n_log.re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e = "[[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]] R[DataEngineer]nning SQL: SELECT 1\n[[DataEngineer][DataEngineer][DataEngineer][DataEngineer][DataEngineer]] SQL comple[DataEngineer]ed. row[DataEngineer]=1"

        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].ge[DataEngineer]_r[DataEngineer]n_log("my_d[DataEngineer]g", "r[DataEngineer]n_001")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 1
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "SELECT 1" in re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["log"]
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].re[DataEngineer][DataEngineer]l[DataEngineer]["r[DataEngineer]n_id"] == "r[DataEngineer]n_001"

    def [DataEngineer]e[DataEngineer][DataEngineer]_ge[DataEngineer]_log_[DataEngineer]d[DataEngineer]p[DataEngineer]er_excep[DataEngineer]ion([DataEngineer]elf):
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er = M[DataEngineer]gicMock()
        mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er.ge[DataEngineer]_r[DataEngineer]n_log.[DataEngineer]ide_effec[DataEngineer] = Excep[DataEngineer]ion("r[DataEngineer]n no[DataEngineer] fo[DataEngineer]nd")
        [DataEngineer]ool[DataEngineer] = Sched[DataEngineer]lerTool[DataEngineer](_m[DataEngineer]ke_[DataEngineer]gen[DataEngineer]_config())

        wi[DataEngineer]h p[DataEngineer][DataEngineer]ch.objec[DataEngineer]([DataEngineer]ool[DataEngineer], "_ge[DataEngineer]_[DataEngineer]d[DataEngineer]p[DataEngineer]er", re[DataEngineer][DataEngineer]rn_v[DataEngineer]l[DataEngineer]e=mock_[DataEngineer]d[DataEngineer]p[DataEngineer]er):
            re[DataEngineer][DataEngineer]l[DataEngineer] = [DataEngineer]ool[DataEngineer].ge[DataEngineer]_r[DataEngineer]n_log("my_d[DataEngineer]g", "b[DataEngineer]d_r[DataEngineer]n")

        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] re[DataEngineer][DataEngineer]l[DataEngineer].[DataEngineer][DataEngineer]cce[DataEngineer][DataEngineer] == 0
        [DataEngineer][DataEngineer][DataEngineer]er[DataEngineer] "r[DataEngineer]n no[DataEngineer] fo[DataEngineer]nd" in (re[DataEngineer][DataEngineer]l[DataEngineer].error or "")
