%global source0_hash 923d5db2fca10636b64e5529552edf1de8bd3da1da3cc7ac963ae6c3895a31ae
Name:           calceph
Version:        5.0.1
Release:        1%{?dist}
Summary:        Astronomical library to access planetary ephemeris files
License:        CECILL-2.0 OR CECILL-B OR CECILL-C
URL:            https://www.imcce.fr/inpop/calceph
Source0:        https://www.imcce.fr/content/medias/recherche/equipes/asd/%{name}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      calceph-docs < 4.0.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
# /oreon:deps
%description
This library is designed to access the binary planetary ephemeris files,
such INPOPxx, JPL DExxx and SPICE ephemeris files.

%package        libs
Summary:        %{name} shared libraries
License:        CECILL-2.0 OR CECILL-B OR CECILL-C
%description    libs
Calceph shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        fortran-devel
Summary:        Development files for using %{name} Fortran bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran
%description    fortran-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -DBUILD_SHARED_LIBS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles calceph-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calceph-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles calceph-fortran-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n calceph-libs -f %{oreon_filedir}/calceph-libs.list
%files -n calceph-devel -f %{oreon_filedir}/calceph-devel.list
%files -n calceph-fortran-devel -f %{oreon_filedir}/calceph-fortran-devel.list

%changelog

%autochangelog
