%global source0_hash 819e98bc7dad7cf7e67c9ddb592f44545c300de143fe30bc29ca1b422b55306a
Name:           mpfi
Version:        1.5.4
Release:        11%{?dist}
Summary:        An interval arithmetic library based on MPFR
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://perso.ens-lyon.fr/nathalie.revol/software.html
VCS:            git:https://gitlab.inria.fr/mpfi/mpfi.git
Source0:        https://perso.ens-lyon.fr/nathalie.revol/softwares/%{name}-%{version}.tar.xz
Patch:          %{name}-uninit.patch
Patch:          %{name}-mismatched-type.patch
Patch:          %{name}-bad-ref.patch
Patch:          %{name}-test.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  mpfr-devel
# /oreon:deps
%description
MPFI is intended to be a portable library written in C for arbitrary precision
interval arithmetic with intervals represented using MPFR reliable
floating-point numbers.  It is based on the GNU MP library and on the MPFR
library and is part of the latter.  The purpose of an arbitrary precision
interval arithmetic is on the one hand to get "guaranteed" results, thanks to
interval computation, and on the other hand to obtain accurate results, thanks
to multiple precision arithmetic.  The MPFI library is built upon MPFR in
order to benefit from the correct roundings provided by MPFR.  Further
advantages of using MPFR are its portability and compliance with the IEEE 754
standard for floating-point arithmetic.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Obsoletes:      %{name}-static < 1.5.4-11
Provides:       %{name}-static = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# In the 1.5.4 release, these two tests try to call functions with mismatched
# signatures, then segfault.  It is not clear to me how to fix them.
sed -i 's/ tdiv_ext\$(EXEEXT)//;s/ trec_sqrt\$(EXEEXT)//' tests/Makefile.in

# In the 1.5.4 release, the data file needed by this test is missing.
sed -i 's/texp10\$(EXEEXT) //' tests/Makefile.in

# Fix the pkgconfig file
sed -i 's/ -lmpfr -lgmp/\nLibs.private:&/' mpfi.pc.in

%configure --disable-static

%build

%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm %{buildroot}%{_docdir}/mpfi/COPYING*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n mpfi-devel -f %{oreon_filedir}/mpfi-devel.list

%changelog

%autochangelog
