%global source0_hash a4bbdc881128bdbe920a38e134c9add5db47f9aa814a0a018ba940b0f3c278c3
Name:       lpsolve
Version:    5.5.2.14
Release:        1%{?dist}
Summary:        Mixed Integer Linear Programming (MILP) solver
License:    LGPL-2.1-or-later AND GPL-2.0-or-later WITH Bison-exception-2.2 AND BSD-3-clause
URL:        https://lp-solve.github.io/
Source0:        https://github.com/lp-solve/lp_solve/releases/download/%{version}/lp_solve_%{version}_source.tar.gz#/lp_solve_%{version}_source-repackaged.tar.gz
Patch0:     lp_solve-5.5.2.14-Respect-CC-CFLAGS-and-LDFLAGS.patch
Patch1:     lp_solve-5.5.2.11-Link-a-tool-to-a-shared-library.patch
Provides:       bundled(colamd) = 3.0.4
# oreon:deps
BuildRequires:  bash
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  grep
# /oreon:deps
%description
Mixed Integer Linear Programming (MILP) solver lpsolve solves pure linear,
(mixed) integer/binary, semi-continuous and special ordered sets (SOS) models.

%package devel
License:    LGPL-2.1-or-later
Requires:   %{name}%{?_isa} = %{version}-%{release}
Summary:    Files for developing with lpsolve
%description devel
Header files for developing with lpsolve library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n lp_solve
chmod -x lp_lib.h

%build

%set_build_flags
pushd lpsolve55
sh -x ccc
rm bin/ux*/liblpsolve55.a
popd
pushd lp_solve
sh -x ccc
popd
%install
install -d %{buildroot}%{_bindir} %{buildroot}%{_libdir} %{buildroot}%{_includedir}/lpsolve
install -p -m 755 \
        lp_solve/bin/ux*/lp_solve %{buildroot}%{_bindir}
install -p -m 755 \
        lpsolve55/bin/ux*/liblpsolve55.so %{buildroot}%{_libdir}
install -p -m 644 \
        lp*.h yacc_read.h %{buildroot}%{_includedir}/lpsolve
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LP_PATH="$(echo lpsolve55/bin/ux*)"
echo 'max: x; x < 42;' | \
    LD_LIBRARY_PATH="$LP_PATH" ./lp_solve/bin/ux*/lp_solve -S1 | \
    grep -e ': 42\.0*$'
%set_build_flags
${CC} ${CFLAGS} -I. demo/demo.c ${LDFLAGS} -L"$LP_PATH" -llpsolve55
LD_LIBRARY_PATH="$LP_PATH" ./a.out </dev/null
%files -f %{oreon_filedir}/main.list
%files -n lpsolve-devel -f %{oreon_filedir}/lpsolve-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.5.2.14-2
- Import
