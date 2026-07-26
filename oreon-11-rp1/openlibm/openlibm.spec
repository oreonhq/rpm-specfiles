%global source0_hash be983b9e1e40e696e8bbb7eb8f6376d3ca0ae675ae6d82936540385b0eeec15b

%bcond_with static_libs # don't build static libraries

Summary:        High quality system independent, open source libm
Name:           openlibm
Version:        0.7.5
Release:        13%{?dist}
# Automatically converted from old format: BSD and MIT and ISC and Public Domain - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND ISC AND LicenseRef-Callaway-Public-Domain
Source0:        https://github.com/JuliaLang/openlibm/archive/v%{version}.tar.gz
URL:            https://github.com/JuliaLang/openlibm/
ExclusiveArch:  %{arm} %{ix86} x86_64 aarch64 %{power64}

BuildRequires: make
BuildRequires: gcc
%description
OpenLIBM is an effort to have a high quality standalone LIBM library.
It is meant to be used standalone in applications and programming language
implementations. The OpenLIBM code derives from the FreeBSD msun implementation,
which in turn derives from FDLIBM 5.3. As a result, it has a number of fixes
and updates that have accumulated over the years in msun, and also optimized
assembly versions of many functions.

%package devel
Summary:    High quality system independent, open source libm
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains header files for developing applications that use the %{name}
library.

%package static
Summary:    High quality system independent, open source libm
Requires:   %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# File under the Apple Public Source License Version 1.1
rm -f test/ieeetestnew.c
# File under the Apple Public Source License Version 2.0
rm -f i387/osx_asm.h

%build
make %{?_smp_mflags} \
      FFLAGS="%{optflags}" \
      CFLAGS="%{optflags}"

%check
# Tests still fail on ARM because of floating-point exceptions
# which are not set correctly (but other tests are fine)
%ifnarch %{arm}
make test
%endif

%install
make install prefix=%{_prefix} \
             libdir=%{_libdir} \
             includedir=%{_includedir} \
             DESTDIR=%{buildroot}

%if ! %{with static_libs}
rm %{buildroot}/%{_libdir}/libopenlibm.a
%endif

%ldconfig_scriptlets

%files
%doc LICENSE.md README.md
%{_libdir}/libopenlibm.so.3*

%files devel
%{_libdir}/libopenlibm.so
%{_libdir}/pkgconfig/openlibm.pc
%{_includedir}/openlibm/

%if %{with static_libs}
%files static
%{_libdir}/libopenlibm.a
%endif

%changelog
%autochangelog
