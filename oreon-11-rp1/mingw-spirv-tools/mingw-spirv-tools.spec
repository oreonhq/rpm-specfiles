%global source0_hash d00dc47df7163c2bacd70f090441e8fad96234f0e3b96c54ee9091a49e627adb

%{?mingw_package_header}

%global pkgname spirv-tools
%global srcname SPIRV-Tools

Name:          mingw-%{pkgname}
Epoch:         1
Version:       1.4.328.1
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname}

License:       Apache-2.0
BuildArch:     noarch
URL:           https://github.com/KhronosGroup/%{srcname}
Source0:       %url/archive/vulkan-sdk-%{version}/%{srcname}-vulkan-sdk-%{version}.tar.gz

# Fix installation dir for cmake modules
Patch0:        spirv-tool_cmake-install.patch

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-spirv-headers
BuildRequires: mingw32-winpthreads
BuildRequires: mingw32-winpthreads-static

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-spirv-headers
BuildRequires: mingw64-winpthreads
BuildRequires: mingw64-winpthreads-static

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

%files -n mingw32-%{pkgname}
%{mingw32_bindir}/libSPIRV-Tools-diff.dll
%{mingw32_bindir}/libSPIRV-Tools-link.dll
%{mingw32_bindir}/libSPIRV-Tools-lint.dll
%{mingw32_bindir}/libSPIRV-Tools-opt.dll
%{mingw32_bindir}/libSPIRV-Tools-reduce.dll
%{mingw32_bindir}/libSPIRV-Tools-shared.dll
%{mingw32_bindir}/libSPIRV-Tools.dll
%{mingw32_bindir}/spirv-as.exe
%{mingw32_bindir}/spirv-cfg.exe
%{mingw32_bindir}/spirv-diff.exe
%{mingw32_bindir}/spirv-dis.exe
%{mingw32_bindir}/spirv-lesspipe.sh
%{mingw32_bindir}/spirv-link.exe
%{mingw32_bindir}/spirv-lint.exe
%{mingw32_bindir}/spirv-objdump.exe
%{mingw32_bindir}/spirv-opt.exe
%{mingw32_bindir}/spirv-reduce.exe
%{mingw32_bindir}/spirv-val.exe
%{mingw32_includedir}/spirv-tools/
%{mingw32_libdir}/libSPIRV-Tools-diff.dll.a
%{mingw32_libdir}/libSPIRV-Tools-link.dll.a
%{mingw32_libdir}/libSPIRV-Tools-lint.dll.a
%{mingw32_libdir}/libSPIRV-Tools-opt.dll.a
%{mingw32_libdir}/libSPIRV-Tools-reduce.dll.a
%{mingw32_libdir}/libSPIRV-Tools-shared.dll.a
%{mingw32_libdir}/libSPIRV-Tools.dll.a
%{mingw32_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{mingw32_libdir}/pkgconfig/SPIRV-Tools.pc
%{mingw32_libdir}/cmake/*

%files -n mingw64-%{pkgname}
%{mingw64_bindir}/libSPIRV-Tools-diff.dll
%{mingw64_bindir}/libSPIRV-Tools-link.dll
%{mingw64_bindir}/libSPIRV-Tools-lint.dll
%{mingw64_bindir}/libSPIRV-Tools-opt.dll
%{mingw64_bindir}/libSPIRV-Tools-reduce.dll
%{mingw64_bindir}/libSPIRV-Tools-shared.dll
%{mingw64_bindir}/libSPIRV-Tools.dll
%{mingw64_bindir}/spirv-as.exe
%{mingw64_bindir}/spirv-cfg.exe
%{mingw64_bindir}/spirv-diff.exe
%{mingw64_bindir}/spirv-dis.exe
%{mingw64_bindir}/spirv-lesspipe.sh
%{mingw64_bindir}/spirv-link.exe
%{mingw64_bindir}/spirv-lint.exe
%{mingw64_bindir}/spirv-objdump.exe
%{mingw64_bindir}/spirv-opt.exe
%{mingw64_bindir}/spirv-reduce.exe
%{mingw64_bindir}/spirv-val.exe
%{mingw64_includedir}/spirv-tools/
%{mingw64_libdir}/libSPIRV-Tools-diff.dll.a
%{mingw64_libdir}/libSPIRV-Tools-link.dll.a
%{mingw64_libdir}/libSPIRV-Tools-lint.dll.a
%{mingw64_libdir}/libSPIRV-Tools-opt.dll.a
%{mingw64_libdir}/libSPIRV-Tools-reduce.dll.a
%{mingw64_libdir}/libSPIRV-Tools-shared.dll.a
%{mingw64_libdir}/libSPIRV-Tools.dll.a
%{mingw64_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{mingw64_libdir}/pkgconfig/SPIRV-Tools.pc
%{mingw64_libdir}/cmake/*

%changelog
%autochangelog
