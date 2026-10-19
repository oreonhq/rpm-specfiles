%global source0_hash f80ca88a2c52586e31225493ad5eaf4c29a74c6105283decee6c3717afbf8326
%{?mingw_package_header}
%global pkgname glslang
Name:          mingw-%{pkgname}
Epoch:         1
Version:       1.4.328.1
Release:        1%{?dist}
Summary:        MinGW Windows glslang library
License:       BSD-3-clause AND GPL-3.0-or-later AND Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{pkgname}
Source0:        https://github.com/KhronosGroup/%{pkgname}/archive/vulkan-sdk-%{version}/%{pkgname}-vulkan-sdk-%{version}.tar.gz
Patch0:        glslang_debug-suffix.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-winpthreads-static
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-winpthreads-static
BuildRequires:  ninja-build
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-vulkan-sdk-%{version}

%build

%mingw_cmake -G Ninja -DBUILD_SHARED_LIBS=OFF -DENABLE_OPT=OFF
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-glslang -f %{oreon_filedir}/mingw32-glslang.list
%files -n mingw64-glslang -f %{oreon_filedir}/mingw64-glslang.list

%changelog

%autochangelog
