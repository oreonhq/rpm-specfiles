%global source0_hash 602364ab7bf404a7f352df7da5c645f1c4558a9c92616f8ee33422b04d5e35b7

%{?mingw_package_header}

%global pkgname spirv-headers
%global srcname SPIRV-Headers

Name:          mingw-%{pkgname}
Epoch:         1
Version:       1.4.328.1
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       MIT
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       %url/archive/vulkan-sdk-%{version}/%{srcname}-vulkan-sdk-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++

%description
MinGW Windows %{pkgname}

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname}

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-vulkan-sdk-%{version}

%build
%mingw_cmake -G Ninja
%mingw_ninja

%install
%mingw_ninja_install

%files -n mingw32-%{pkgname}
%{mingw32_includedir}/spirv/
%{mingw32_datadir}/cmake/SPIRV-Headers/
%{mingw32_datadir}/pkgconfig/SPIRV-Headers.pc

%files -n mingw64-%{pkgname}
%{mingw64_includedir}/spirv/
%{mingw64_datadir}/cmake/SPIRV-Headers/
%{mingw64_datadir}/pkgconfig/SPIRV-Headers.pc

%changelog
%autochangelog
