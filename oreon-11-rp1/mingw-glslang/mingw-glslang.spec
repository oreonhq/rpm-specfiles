%global source0_hash f80ca88a2c52586e31225493ad5eaf4c29a74c6105283decee6c3717afbf8326

%{?mingw_package_header}

%global pkgname glslang

Name:          mingw-%{pkgname}
Epoch:         1
Version:       1.4.328.1
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD-3-clause AND GPL-3.0-or-later AND Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{pkgname}
Source0:       %url/archive/vulkan-sdk-%{version}/%{pkgname}-vulkan-sdk-%{version}.tar.gz
# Remove debug suffix for mingw builds
Patch0:        glslang_debug-suffix.patch

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-winpthreads-static

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-winpthreads-static

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

%files -n mingw32-%{pkgname}
%{mingw32_bindir}/glslang.exe
%{mingw32_bindir}/glslangValidator.exe
%{mingw32_includedir}/glslang/
%{mingw32_libdir}/libGenericCodeGen.a
%{mingw32_libdir}/libMachineIndependent.a
%{mingw32_libdir}/libOSDependent.a
%{mingw32_libdir}/libSPIRV.a
%{mingw32_libdir}/libglslang.a
%{mingw32_libdir}/libglslang-default-resource-limits.a
%{mingw32_libdir}/cmake/*

%files -n mingw64-%{pkgname}
%{mingw64_bindir}/glslang.exe
%{mingw64_bindir}/glslangValidator.exe
%{mingw64_includedir}/glslang/
%{mingw64_libdir}/libGenericCodeGen.a
%{mingw64_libdir}/libMachineIndependent.a
%{mingw64_libdir}/libOSDependent.a
%{mingw64_libdir}/libSPIRV.a
%{mingw64_libdir}/libglslang.a
%{mingw64_libdir}/libglslang-default-resource-limits.a
%{mingw64_libdir}/cmake/*

%changelog
%autochangelog
