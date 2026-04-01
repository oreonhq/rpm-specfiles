#!/usr/bin/env python3
"""Rebuild grub2.spec inlined sections from grub.macros and grub.patches."""

from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parent
    spec_path = base / "grub2.spec"
    macros_path = base / "grub.macros"
    patches_path = base / "grub.patches"

    spec = spec_path.read_text()
    macros = macros_path.read_text()
    patches = patches_path.read_text()
    lines = spec.splitlines(keepends=True)

    idx_inc1 = idx_inc11 = None
    for i, ln in enumerate(lines):
        if ln.strip() == "%include %{SOURCE1}":
            idx_inc1 = i
        if ln.strip() == "%include %{SOURCE11}":
            idx_inc11 = i

    if idx_inc1 is not None and idx_inc11 is not None:
        # Legacy layout: split and rebuild (used if spec reverted to %%include style).
        head_end = None
        for i, ln in enumerate(lines):
            if ln.startswith("Source0:"):
                head_end = i
                break
        assert head_end is not None
        head = "".join(lines[:head_end])
        new_sources = (
            "Source0:\thttps://ftp.gnu.org/gnu/grub/grub-%{tarversion}.tar.xz\n"
            "Source1:\thttps://git.savannah.gnu.org/cgit/gnulib.git/snapshot/"
            "gnulib-%{gnulibversion}.tar.gz\n"
            "Source2:\t99-grub-mkconfig.install\n"
            "Source3:\thttp://unifoundry.com/pub/unifont/"
            "unifont-13.0.06/font-builds/unifont-13.0.06.pcf.gz\n"
            "Source4:\tgitignore\n"
            "Source5:\tbootstrap\n"
            "Source6:\tbootstrap.conf\n"
            "Source7:\tstrtoull_test.c\n"
            "Source8:\t20-grub.install\n"
            "Source9:\tsbat.csv.in\n"
            "Source10:\tgen_grub_cfgstub\n"
            "Source11:\t95-set-boot-entry.install\n\n"
        )
        repl_macros = macros
        middle = "".join(lines[idx_inc1 + 1 : idx_inc11])
        tail = "".join(lines[idx_inc11 + 1 :])
        banner_m = (
            "# Inlined from grub.macros "
            "(parse-time %%include removed for spectool)\n"
        )
        banner_p = "# Inlined from grub.patches\n"
        out = (
            head
            + new_sources
            + "\n"
            + banner_m
            + repl_macros
            + "\n"
            + middle
            + banner_p
            + patches
            + "\n"
            + tail
        )
        spec_path.write_text(out)
        return

    # Already inlined: swap macro + Patch* bodies using grub.macros / grub.patches
    # from disk. Middle (BuildRequires, etc.) sits between embedded macros and the
    # patches banner, so we size the old macro block by line count, not by scanning
    # for the patches banner.
    start_m = "# Inlined from grub.macros"
    start_p = "# Inlined from grub.patches"
    try:
        i_m = next(i for i, ln in enumerate(lines) if ln.startswith(start_m))
        i_p = next(i for i, ln in enumerate(lines) if ln.startswith(start_p))
    except StopIteration as e:
        raise SystemExit(
            "grub2.spec: expected inlined banners or %%include SOURCE1/11"
        ) from e

    n_m = len(macros.splitlines())
    if i_m + 1 + n_m > i_p:
        raise SystemExit(
            "grub2.spec: embedded macros longer than expected (past patches banner)"
        )
    macro_from_spec = "".join(lines[i_m + 1 : i_m + 1 + n_m])
    if macro_from_spec.rstrip() != macros.rstrip():
        raise SystemExit(
            "grub2.spec: embedded grub.macros out of sync with ./grub.macros "
            "(edit grub.macros or fix spec by hand, then retry)"
        )

    middle = "".join(lines[i_m + 1 + n_m : i_p])

    tail_start = i_p + 1
    while tail_start < len(lines) and lines[tail_start].startswith("Patch"):
        tail_start += 1

    repl_macros = macros

    if not patches.endswith("\n"):
        patches = patches + "\n"

    new_spec = (
        "".join(lines[: i_m + 1])
        + repl_macros
        + ("\n" if not repl_macros.endswith("\n") else "")
        + middle
        + lines[i_p]
        + patches
        + "".join(lines[tail_start:])
    )
    spec_path.write_text(new_spec)


if __name__ == "__main__":
    main()
