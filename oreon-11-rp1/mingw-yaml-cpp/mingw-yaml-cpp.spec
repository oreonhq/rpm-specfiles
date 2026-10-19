%global source0_hash fbe74bbdcee21d656715688706da3c8becfd946d92cd44705cc6098bb23b3a16
%{?mingw_package_header}
%global pkgname yaml-cpp
Name:           mingw-%{pkgname}
Version:        0.9.0
Release:        1%{?dist}
Summary:        A YAML parser and emitter for C++
License:        MIT
URL:            https://github.com/jbeder/yaml-cpp
Source0:        https://github.com/jbeder/yaml-cpp/archive/%{version}/yaml-cpp-%{version}.tar.gz
Patch0:         yaml-cpp-includes.patch
Patch1:         yaml-cpp-cmakever.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package -n mingw32-%{pkgname}
Summary:        A YAML parser and emitter for C++
%description -n mingw32-%{pkgname}
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%package -n mingw64-%{pkgname}
Summary:        A YAML parser and emitter for C++
%description -n mingw64-%{pkgname}
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

%mingw_cmake -DYAML_CPP_BUILD_TESTS=OFF -DYAML_CPP_BUILD_TOOLS=OFF -DCMAKE_DLL_NAME_WITH_SOVERSION=ON
%mingw_make_build
%install
%mingw_make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-yaml-cpp -f %{oreon_filedir}/mingw32-yaml-cpp.list
%files -n mingw64-yaml-cpp -f %{oreon_filedir}/mingw64-yaml-cpp.list

%changelog

%autochangelog
