%global source0_hash d31e7109b6ef3559067e53e520870eafed7c9534d00db9728814b6df03fa4a5e
%{?mingw_package_header}
%global pkgname spirv-tools
%global srcname SPIRV-Tools
Name:          mingw-%{pkgname}
Epoch:         1
Version:       1.4.357.0
Release:        1%{?dist}
Summary:        MinGW Windows spirv-tools
License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:        https://github.com/KhronosGroup/%{srcname}/archive/vulkan-sdk-%{version}/%{srcname}-vulkan-sdk-%{version}.tar.gz
Patch0:        spirv-tool_cmake-install.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-spirv-headers
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw32-winpthreads-static
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-spirv-headers
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw64-winpthreads-static
BuildRequires:  ninja-build
# /oreon:deps
%description
MinGW Windows %{pkgname}.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}
%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}
%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version}

%build

MINGW32_CMAKE_ARGS="-DSPIRV-Headers_SOURCE_DIR=%{mingw32_prefix}" \
MINGW64_CMAKE_ARGS="-DSPIRV-Headers_SOURCE_DIR=%{mingw64_prefix}" \
%mingw_cmake -G Ninja -DSPIRV_TOOLS_BUILD_STATIC=OFF -DSPIRV_WERROR=OFF
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-spirv-tools -f %{oreon_filedir}/mingw32-spirv-tools.list
%files -n mingw64-spirv-tools -f %{oreon_filedir}/mingw64-spirv-tools.list

%changelog

%autochangelog
