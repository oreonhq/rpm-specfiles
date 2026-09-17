%global source0_hash 4ee86899b0cb8b702f443908dc4e9e5e19a2bd870d0520cbae4066658c89df14

%bcond check 0

Summary: ELF utils that can check files for security relevant properties
Name: pax-utils
Version: 1.3.10
Release: 2%{?dist}
# http://packages.gentoo.org/package/app-misc/pax-utils
URL: https://wiki.gentoo.org/wiki/Hardened/PaX_Utilities
#Source0: https://distfiles.gentoo.org/distfiles/%{name}-%{version}.tar.xz
Source0: https://github.com/gentoo/pax-utils/archive/v%{version}/%{name}-%{version}.tar.gz
# fix python shebang in lddtree.py and pylint
Patch0: %{name}-py3shebang.patch
# elf.h is from glibc: LGPLv2.1+
# pspax.c is Beerware
License: GPL-2.0-only AND LGPL-2.1-or-later AND Beerware
BuildRequires:  gcc
BuildRequires: meson
BuildRequires: libcap-devel
BuildRequires: xmlto
%if %{with check}
BuildRequires: python3-pyelftools
BuildRequires: python3
%endif

%description
pax-utils is a small set of utilities for peforming Q/A (mostly security)
checks on systems (most notably, `scanelf`).  It is focused on the ELF
format, but does include a Mach-O helper too for OS X systems.

While heavily integrated into Gentoo's build system, it can be used on any
distro as it is a generic toolset.

Originally focused only on [PaX](https://pax.grsecurity.net/), it has been
expanded to be generally security focused.  It still has a good number of
PaX helpers for people interested in that.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson \
    -Duse_libcap=enabled \
    -Duse_seccomp=true \
    -Dbuild_manpages=enabled \
    -Dtests=true \
    -Duse_fuzzing=false \
    -Dlddtree_implementation=sh \

%meson_build

%install
%meson_install

%if %{with check}
%check
export LD_LIBRARY_PATH=%{_libdir}
%meson_test
%endif

%files
%license COPYING
%doc BUGS README.md TODO
%{_bindir}/dumpelf
%{_bindir}/lddtree
%{_bindir}/pspax
%{_bindir}/scanelf
%{_bindir}/scanmacho
%{_bindir}/symtree
%{_mandir}/man1/dumpelf.1*
%{_mandir}/man1/pspax.1*
%{_mandir}/man1/scanelf.1*
%{_mandir}/man1/scanmacho.1*

%changelog
%autochangelog
