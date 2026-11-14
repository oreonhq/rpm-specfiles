# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cda24ec765e6d2845d106b7caa593f34127195a88524cf87821ff0088fb6edec

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global sdkver 1.4.363.0

Name:           glslang
Version:        16.6.0
Release:        1%{?dist}
Summary:        OpenGL and OpenGL ES shader front end and validator

License:        BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/KhronosGroup/%{name}
Source0:        %{url}/archive/vulkan-sdk-%{sdkver}.tar.gz#/%{name}-sdk-%{sdkver}.tar.gz
Patch3:         0001-pkg-config-compatibility.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  spirv-tools-devel
BuildRequires:  python3
BuildRequires:  diffutils

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
%oreon_sha256

%autosetup -p1 -n %{name}-vulkan-sdk-%{sdkver}
find . -name '*.h' -or -name '*.cpp' -or -name '*.hpp'| xargs chmod a-x

%build
%cmake -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%{cmake_install}

rm -rf %{buildroot}%{_includedir}/SPIRV

%ifnarch s390x ppc64
%check
pushd Test
./runtests localResults ../%{_vpath_builddir}/StandAlone/glslangValidator ../%{_vpath_builddir}/StandAlone/spirv-remap
popd
%endif

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/glslang
%{_bindir}/glslangValidator

%files devel
%{_includedir}/glslang/
%{_libdir}/libOSDependent.a
%{_libdir}/libSPIRV.a
%{_libdir}/libglslang.a
%{_libdir}/libGenericCodeGen.a
%{_libdir}/libMachineIndependent.a
%{_libdir}/libglslang-default-resource-limits.a
%{_libdir}/pkgconfig/glslang.pc
%{_libdir}/pkgconfig/spirv.pc
%{_libdir}/cmake/*

%changelog
%autochangelog
