Name:       lpsolve
Version:    5.5.2.14
Release:    2%{?dist}
Summary:    Mixed Integer Linear Programming (MILP) solver
# bfp/bfp_LUSOL/lp_LUSOL.c:             LGPL-2.1-or-later
# LICENSE:          LGPL-2.1 text
# lp_crash.c:       LGPL-2.1-or-later
# lp_lib.c:         LGPL-2.1-or-later
# lp_lib.h:         LGPL-2.1-or-later
# lp_matrix.c:      LGPL-2.1-or-later
# lp_MDO.c:         LGPL-2.1-or-later
# lp_mipbb.c:       LGPL-2.1-or-later
# lp_presolve.c:    LGPL-2.1-or-later
# lp_price.c:       LGPL-2.1-or-later
# lp_pricePSE.c:    LGPL-2.1-or-later
# lp_report.c:      LGPL-2.1-or-later
# lp_rlp.c:         GPL-2.0-or-later WITH Bison-exception-2.2
# lp_scale.c:       LGPL-2.1-or-later
# lp_simplex.c:     LGPL-2.1-or-later
# lp_SOS.c:         LGPL-2.1-or-later
# lp_utils.c:       LGPL-2.1-or-later
# README.txt:       LGPL-2.1-or-later
# lp_solve-5.5.2.11-Rebase-COLAMD-to-3.0.4.patch:   BSD-3-clause
## Unused and nonpackaged
# bfp/bfp_LUSOL/LUSOL/hbio.c:           xlock-like
License:    LGPL-2.1-or-later AND GPL-2.0-or-later WITH Bison-exception-2.2 AND BSD-3-clause
# There is a mailing list at <https://groups.google.com/g/lp_solve>.
URL:        https://lp-solve.github.io/
# A separate documention at
# <https://github.com/lp-solve/lp_solve/releases/download/%%{version}/lp_solve_%%{version}_doc.tar.gz>
# contains proprietary JavaScript files and javascript trackers.
#
# This is a repackaged source tar ball from
# <https://github.com/lp-solve/lp_solve/releases/download/%%{version}/lp_solve_%%{version}_source.tar.gz>.
# Original archive contained a nonfree COLAMD code (colamd/colamd.{c,h}),
# <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/230>.
# A new upstream COLAMD code with an acceptable code is supplied in
# Rebase-COLAMD-to-3.0.4.patch.
Source:     lp_solve_%{version}_source-repackaged.tar.gz
# Use system-wide compiler, compiler and linker flags
Patch0:     lp_solve-5.5.2.14-Respect-CC-CFLAGS-and-LDFLAGS.patch
# Do not duplicate library code in the the tool
Patch1:     lp_solve-5.5.2.11-Link-a-tool-to-a-shared-library.patch
# 1/2 Rebase bundled COLAMD to 3.0.4, proposed to the upstream.
Patch2:     lp_solve-5.5.2.11-Rebase-COLAMD-to-3.0.4.patch
# 2/2 Rebase bundled COLAMD to 3.0.4, proposed to the upstream.
Patch3:     lp_solve-5.5.2.11-Port-lp_MDO-to-colamd-3.0.4.patch
BuildRequires:  bash
# binutils for ar and ranlib
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc
# Tests:
BuildRequires:  grep
Provides:       bundled(colamd) = 3.0.4

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
%autosetup -p1 -n lp_solve
mv colamd/License.txt colamd/colamd_license
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

%check
LP_PATH="$(echo lpsolve55/bin/ux*)"
# Verify lp_solve tool works
echo 'max: x; x < 42;' | \
    LD_LIBRARY_PATH="$LP_PATH" ./lp_solve/bin/ux*/lp_solve -S1 | \
    grep -e ': 42\.0*$'
# Verify a demo code is buildable
%set_build_flags
${CC} ${CFLAGS} -I. demo/demo.c ${LDFLAGS} -L"$LP_PATH" -llpsolve55
LD_LIBRARY_PATH="$LP_PATH" ./a.out </dev/null

%files
%license colamd/colamd_license LICENSE
%doc README.txt
%{_bindir}/lp_solve
%{_libdir}/liblpsolve55.so

%files devel
%doc demo/demo.c
%{_includedir}/lpsolve

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.5.2.14-2
- Prepare for Oreon 11 (RP1)
