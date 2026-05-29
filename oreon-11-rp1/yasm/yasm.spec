%global source0_hash none

%global git 1
%global commit 121ab150b3577b666c79a79f4a511798d7ad2432
%global date 20250625
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: Modular Assembler
Name: yasm
Version: 1.3.0^%{date}git%{shortcommit}
Release: 4%{?dist}
# See COPYING for the detail, there is quite a lot!
# Bitvect is (GPL-1.0-or-later AND GPL-2.0-or-later OR Artistic-1.0-Perl OR LGPL-2.0-or-later
# Everything else is BSD. Either 2 or 3 clause.
License: BSD-2-Clause AND BSD-3-Clause AND (GPL-1.0-or-later AND GPL-2.0-or-later OR Artistic-1.0-Perl OR LGPL-2.0-or-later)

URL: http://yasm.tortall.net/
%if 0%{?git}
Source:        https://github.com/yasm/yasm/archive/121ab150b3577b666c79a79f4a511798d7ad2432/yasm-%(c=121ab150b3577b666c79a79f4a511798d7ad2432;.tar.gz
# https://github.com/yasm/yasm/issues/270
Patch0: yasm-tests.patch
# https://github.com/yasm/yasm/issues/283
Patch1: yasm-gcc15.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: python3
%else
Source:        http://www.tortall.net/projects/yasm/releases/yasm-1.3.0^.tar.gz
%endif

BuildRequires: make
BuildRequires:  gcc
BuildRequires: bison
BuildRequires: byacc
BuildRequires: gettext-devel
BuildRequires: xmlto
Provides: bundled(md5-plumb)
Provides: deprecated()

%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.


%package devel
Summary: Header files and static libraries for the yasm Modular Assembler
Requires: %{name} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
Provides: bundled(md5-plumb)

%description devel
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.
Install this package if you need to rebuild applications that use yasm.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%if 0%{?git}
%setup -q -n %{name}-%{commit}
%ifarch i686
%patch 0 -p1
%endif
%patch 1 -p1
autoreconf -I m4 -fiv
%else
%setup -q
%endif


%build
%configure
%make_build


%install
%make_install


%check
# tests must be run sequentially
# https://github.com/yasm/yasm/issues/269
make check

%files
%license Artistic.txt BSD.txt COPYING GNU_GPL-2.0 GNU_LGPL-2.0
%doc AUTHORS
%{_bindir}/vsyasm
%{_bindir}/yasm
%{_bindir}/ytasm
%{_mandir}/man1/yasm.1*

%files devel
%{_includedir}/libyasm/
%{_includedir}/libyasm-stdint.h
%{_includedir}/libyasm.h
%{_libdir}/libyasm.a
%{_mandir}/man7/yasm_*.7*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0^%{date}git%{shortcommit}-4
- Prepare for Oreon 11 (RP1)
