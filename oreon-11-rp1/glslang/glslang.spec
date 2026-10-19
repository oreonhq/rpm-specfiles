%global source0_hash 18cdf7d40a39001dde842c6a1338b2c9321ac5e487139b9d52b4b9c666da3c86
%global sdkver 1.4.341.0
Name:           glslang
Version:        16.6.0
Release:        1%{?dist}
Summary:        OpenGL and OpenGL ES shader front end and validator
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/KhronosGroup/%{name}
Source0:        https://github.com/KhronosGroup/glslang/archive/vulkan-sdk-1.4.341.0.tar.gz#/glslang-sdk-1.4.341.0.tar.gz
Patch3:         0001-pkg-config-compatibility.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  spirv-tools-devel
# /oreon:deps
%description
%{name} is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{name} is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-vulkan-sdk-%{sdkver}
# Fix rpmlint warning on debuginfo
find . -name '*.h' -or -name '*.cpp' -or -name '*.hpp'| xargs chmod a-x

%build

%cmake -DBUILD_SHARED_LIBS=OFF
%cmake_build
%install
%{cmake_install}
rm -rf %{buildroot}%{_includedir}/SPIRV
%ifnarch s390x ppc64
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd Test
./runtests localResults ../%{_vpath_builddir}/StandAlone/glslangValidator ../%{_vpath_builddir}/StandAlone/spirv-remap
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n glslang-devel -f %{oreon_filedir}/glslang-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.2.0-1
- Prepare for Oreon 11 (RP1)
