Name:           libcerf
%global rname   cerf
Version:        3.8
%global         sover 3
Release:        %autorelease
Summary:        A library that provides complex error functions

License:        MIT
URL:            https://jugit.fz-juelich.de/mlz/lib/cerf
Source0:        %{url}/-/archive/v%{version}/%{rname}-v%{version}.tar.gz

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
%setup -q -n %{rname}-v%{version}

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
