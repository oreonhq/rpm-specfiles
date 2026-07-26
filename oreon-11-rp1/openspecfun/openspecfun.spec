%global source0_hash 1505c7a45f9f39ffe18be36f7a985cb427873948281dbcd376a11c2cd15e41e7

%bcond_with static_libs # don't build static libraries

Summary:        Library providing a collection of special mathematical functions
Name:           openspecfun
Version:        0.5.3
Release:        25%{?dist}
# Automatically converted from old format: MIT and Public Domain - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
Source0:        https://github.com/JuliaLang/openspecfun/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL:            https://github.com/JuliaLang/openspecfun
BuildRequires: make
BuildRequires:  gcc-gfortran

%description
Currently provides AMOS and Faddeeva. AMOS (from Netlib) is a
portable package for Bessel Functions of a Complex Argument and
Nonnegative Order; it contains subroutines for computing Bessel
functions and Airy functions. Faddeeva allows computing the
various error functions of arbitrary complex arguments (Faddeeva
function, error function, complementary error function, scaled
complementary error function, imaginary error function, and Dawson function);
given these, one can also easily compute Voigt functions, Fresnel integrals,
and similar related functions as well.

%package devel
Summary:    Library providing a collection of special mathematical functions
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains header files for developing applications that use the %{name}
library.

%package static
Summary:    Library providing a collection of special mathematical functions
Requires:   %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q %{name}-%{version}

%build
make %{?_smp_mflags} \
      FFLAGS="%{optflags}" \
      CFLAGS="%{optflags}" \
      USE_OPENLIBM=0 \
      includedir=%{_includedir}

%install
make install prefix=%{_prefix} \
             libdir=%{_libdir} \
             includedir=%{_includedir} \
             DESTDIR=%{buildroot}

%if ! %{with static_libs}
rm %{buildroot}/%{_libdir}/libopenspecfun.a
%endif

%ldconfig_scriptlets

%files
%doc LICENSE.md README.md
%{_libdir}/libopenspecfun.so.1*

%files devel
%{_libdir}/libopenspecfun.so
%{_includedir}/Faddeeva.h

%if %{with static_libs}
%files static
%{_libdir}/libopenspecfun.a
%endif

%changelog
%autochangelog
