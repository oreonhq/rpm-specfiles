%global source0_hash 4f7a55408e439741b74e18f81fe34a7dc4e4e5126cef47ca5e9e093a5a82e01c
%bcond_with bootstrap
Name:           python-ruamel-yaml
Version:        0.19.1
Release:        1%{?dist}
Summary:        YAML 1.2 loader/dumper package for Python
License:        MIT
URL:            https://sourceforge.net/projects/ruamel-yaml
Source0:        https://yaml.dev/ruamel-dl-tagged-releases/ruamel.yaml-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ruamel-yaml = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ruamel-yaml
Summary:        YAML 1.2 loader/dumper package for Python
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%py_provides python3-ruamel.yaml
%if !%{with bootstrap}
Requires:       python3-ruamel-yaml+oldlibyaml = %{version}-%{release}
%endif
%description -n python3-ruamel-yaml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ruamel.yaml-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ruamel-yaml usr/lib/python3*/site-packages/ruamel_yaml* usr/lib64/python3*/site-packages/ruamel_yaml* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ruamel_yaml* usr/lib64/python3*/site-packages/ruamel_yaml* usr/bin/*

%check

%if %{with bootstrap}
k="${k-}${k+ and }not test_load_cyaml"
k="${k-}${k+ and }not test_load_cyaml_1_2"
k="${k-}${k+ and }not test_dump_cyaml_1_2"
%endif
%pytest -k "${k-}" _test/test_*.py
%files
%files -n python3-ruamel-yaml -f %{oreon_filedir}/python3-ruamel-yaml.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.1-1
- Prepare for Oreon 11 (RP1)
