# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4f7a55408e439741b74e18f81fe34a7dc4e4e5126cef47ca5e9e093a5a82e01c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond_with bootstrap

Name:           python-ruamel-yaml
Version:        0.19.1
Release:        1%{?dist}
Summary:        YAML 1.2 loader/dumper package for Python

License:        MIT
URL:            https://sourceforge.net/projects/ruamel-yaml
Source0:        https://yaml.dev/ruamel-dl-tagged-releases/ruamel.yaml-%{version}.tar.xz

BuildArch:      noarch

%global _description %{expand:
ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of
comments, seq/map flow style, and map key order.}

%description %{_description}

%package -n     python3-ruamel-yaml
Summary:        YAML 1.2 loader/dumper package for Python

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%py_provides python3-ruamel.yaml

%if !%{with bootstrap}
Requires:       python3-ruamel-yaml+oldlibyaml = %{version}-%{release}
%endif

%description -n python3-ruamel-yaml %{_description}

%prep
%oreon_sha256
%autosetup -n ruamel.yaml-%{version}

%generate_buildrequires
%pyproject_buildrequires %{!?with_bootstrap:-x oldlibyaml}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l ruamel

%check
%if %{with bootstrap}
k="${k-}${k+ and }not test_load_cyaml"
k="${k-}${k+ and }not test_load_cyaml_1_2"
k="${k-}${k+ and }not test_dump_cyaml_1_2"
%endif
%pytest -k "${k-}" _test/test_*.py

%files -n python3-ruamel-yaml -f %{pyproject_files}
%doc README.md

%pyproject_extras_subpkg -n python3-ruamel-yaml oldlibyaml

%changelog
%autochangelog
