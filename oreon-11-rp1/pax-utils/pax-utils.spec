%global source0_hash aa01db76341e64c9c6895d83f6b5f835a3cc9efdf1c21c72b8e45f1b0add32c7
%bcond check 0
Summary:        ELF utils that can check files for security relevant properties
Name: pax-utils
Version: 1.3.11
Release:        1%{?dist}
URL: https://wiki.gentoo.org/wiki/Hardened/PaX_Utilities
Source0:        https://github.com/gentoo/pax-utils/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: %{name}-py3shebang.patch
License: GPL-2.0-only AND LGPL-2.1-or-later AND Beerware
%if %{with check}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libcap-devel
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  python3-pyelftools
BuildRequires:  xmlto
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main
%if %{with check}
%check

export LD_LIBRARY_PATH=%{_libdir}
%meson_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
