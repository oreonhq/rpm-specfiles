%global source0_hash 82c62146083fd558735a3171cf97cfc47903ca7d368482e87f94bd44883c0f00

%undefine __cmake_in_source_build

%global commit ef96ed763b43b59b33b31b362f09a02b729fa1c9

Name:           spirv-tools
Version:        2026.4
Release:        1.20260927git%{lua:print(string.sub(rpm.expand("%{commit}"), 1, 7))}%{?dist}
Summary:        API and commands for processing SPIR-V modules

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/SPIRV-Tools
Source0:        https://github.com/KhronosGroup/SPIRV-Tools/archive/%{commit}.tar.gz#/SPIRV-Tools-%{commit}.tar.gz

Patch0: fix-gcc12-build.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
%if 0%{?rhel} == 7
BuildRequires:  python36-devel
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  python3-rpm-macros
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-headers-commit(496543121ce6419f23d6fa5d7194ba66c36212d2)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V..

%package        libs
%if 0%{?__isa_bits} == 64
Provides:       libSPIRV-Tools.so()(64bit)
Provides:       libSPIRV-Tools-opt.so()(64bit)
%else
Provides:       libSPIRV-Tools.so()
Provides:       libSPIRV-Tools-opt.so()
%endif
Summary:        Library files for %{name}
Provides:       %{name}-libs%{?_isa} = %{version}

%description    libs
library files for %{name}

%package        devel
Provides:       spirv-tools-commit(%{commit})
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n SPIRV-Tools-%{commit}

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DSPIRV-Headers_SOURCE_DIR=%{_prefix} \
       -DPYTHON_EXECUTABLE=%{__python3} \
       -DSPIRV_TOOLS_BUILD_STATIC=OFF \
       -GNinja
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets libs

%files
%license LICENSE
%doc README.md CHANGES
%{_bindir}/spirv-as
%{_bindir}/spirv-cfg
%{_bindir}/spirv-dis
%{_bindir}/spirv-diff
%{_bindir}/spirv-lesspipe.sh
%{_bindir}/spirv-link
%{_bindir}/spirv-lint
%{_bindir}/spirv-objdump
%{_bindir}/spirv-opt
%{_bindir}/spirv-reduce
%{_bindir}/spirv-val

%files libs
%license LICENSE
%{_libdir}/libSPIRV-Tools-diff.so
%{_libdir}/libSPIRV-Tools-link.so
%{_libdir}/libSPIRV-Tools-lint.so
%{_libdir}/libSPIRV-Tools-opt.so
%{_libdir}/libSPIRV-Tools.so
%{_libdir}/libSPIRV-Tools-reduce.so
%{_libdir}/libSPIRV-Tools-shared.so

%files devel
%{_includedir}/spirv-tools/
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/SPIRV-Tools-shared.pc
%{_libdir}/pkgconfig/SPIRV-Tools.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2026.1-1
- Prepare for Oreon 11 (RP1)
