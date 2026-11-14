# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 392f4801409aad9c4f1b77745f179952fd6264e4c8bd0fc1bc45dfa6807bf6d0

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global commit 04fd3caa1e8267e4d95c806cad901181728e1006
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spirv-headers
Version:        1.5.5
Release:        1%{?dist}
Summary:        Header files from the SPIR-V registry

License:        MIT
URL:            https://github.com/KhronosGroup/SPIRV-Headers
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
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
* The XML registry file

%prep
%oreon_sha256

%autosetup -n SPIRV-Headers-%{commit} -p1
chmod a-x include/spirv/1.2/spirv.py

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -GNinja
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/spirv/
%{_datadir}/cmake/SPIRV-Headers/*.cmake
%{_datadir}/pkgconfig/SPIRV-Headers.pc

%changelog
%autochangelog
