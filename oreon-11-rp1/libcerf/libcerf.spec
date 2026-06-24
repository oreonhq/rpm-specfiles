%global source0_hash none

Name:           libcerf
Version:        3.3
%global         sover 3
Release:        2%{?dist}
Summary:        A library that provides complex error functions

License:        MIT
URL:            https://jugit.fz-juelich.de/mlz/libcerf
Source0:        https://jugit.fz-juelich.de/mlz/libcerf/-/archive/v%{version}/%{name}-v%{version}.tar.gz

%if (0%{?rhel} || (0%{?fedora} && 0%{?fedora} < 33))
%undefine __cmake_in_source_build
%endif

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake
# Required to build the documentation
BuildRequires:  perl-podlators
BuildRequires:  perl-Pod-Html

%description
libcerf is a self-contained numeric library that provides an efficient
and accurate implementation of complex error functions, along with
Dawson, Faddeeva, and Voigt functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}

%build
# avoid non-portable default build flags (-march=native -O3), by setting overwrite
# CERF_COMPILE_OPTIONS to a harmless flags like -Wall and let cmake do its thing
%cmake -DCERF_COMPILE_OPTIONS='-Wall' \
    %{nil}
%cmake_build


%install
%cmake_install
# Move the documentation to the devel package
mv $RPM_BUILD_ROOT/%{_datadir}/doc/cerf/html $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-devel


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.%{sover}*

%files devel
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/doc/%{name}-devel/
%{_libdir}/cmake/cerf


%changelog
%autochangelog

