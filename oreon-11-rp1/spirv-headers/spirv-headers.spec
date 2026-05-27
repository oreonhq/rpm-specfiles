%global source0_hash 1b220e3eec1714f0451b0e3652979bd280edf10893f617837b88e6359a804ded

%global commit 04f10f650d514df88b76d25e83db360142c7b174
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:           spirv-headers
Version:        1.5.5
Release:        %autorelease
Summary:        Header files from the SPIR-V registry

License:        MIT
URL:            https://github.com/KhronosGroup/SPIRV-Headers/
Source0:        https://github.com/KhronosGroup/SPIRV-Headers//archive/04f10f650d514df88b76d25e83db360142c7b174/spirv-headers-04f10f6.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
%{summary}

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file

%package        devel
Summary:        Development files for %{name}

%description    devel
%{summary}

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry fil

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n SPIRV-Headers-%{commit} -p1
chmod a-x include/spirv/1.2/spirv.py


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -GNinja
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/spirv/
%{_datadir}/cmake/SPIRV-Headers/*.cmake
%{_datadir}/pkgconfig/SPIRV-Headers.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.5-1
- Prepare for Oreon 11 (RP1)
