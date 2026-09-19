%global source0_hash 7ebabb67a4d7b70cc6362ae692efeb609206e8b8c60714ba274533414d859f33

Summary: Simple DirectMedia Layer - MNG Loading Library
Name: SDL_mng
Version: 0.2.8
Release: 15%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: https://github.com/dulsi/SDL_mng
Source0: http://www.identicalsoftware.com/btbuilder/%{name}-%{version}.tgz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: SDL2-devel
BuildRequires: libpng-devel
BuildRequires: SDL2_image-devel
BuildRequires: cmake

%description
This is a simple library to load mng animations as SDL surfaces.

%package devel
Summary: Libraries and includes for SDL MNG development
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: SDL2-devel%{?_isa}
Requires: pkgconfig

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README ChangeLog
%license LICENSE
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/SDL2/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
