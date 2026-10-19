%global source0_hash dc81e3334fed22f7a977ecac46e4d7e4580e33445b4c2a059ea812c44548af38
Name:           python-pyyaml-env-tag
Version:        1.1
Release:        6%{?dist}
Summary:        A custom YAML tag for referencing environment variables in YAML files
BuildArch:      noarch
License:        MIT
URL:            https://github.com/waylan/pyyaml-env-tag
Source0:        https://github.com/waylan/pyyaml-env-tag/archive/%{version}/pyyaml_env_tag-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-pyyaml-env-tag = %{version}-%{release}
# /oreon:deps
%description
A custom YAML tag for referencing environment variables in YAML files.

%package -n python3-pyyaml-env-tag
Summary:        A custom YAML tag for referencing environment variables in YAML files
%description -n python3-pyyaml-env-tag
A custom YAML tag for referencing environment variables in YAML files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyyaml-env-tag-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyyaml-env-tag usr/lib/python3*/site-packages/pyyaml_env_tag* usr/lib64/python3*/site-packages/pyyaml_env_tag* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyyaml_env_tag* usr/lib64/python3*/site-packages/pyyaml_env_tag* usr/bin/*

%check

PYTHONPATH=$PWD %{python3} tests/test_yaml_env_tag.py
%files
%files -n python3-pyyaml-env-tag -f %{oreon_filedir}/python3-pyyaml-env-tag.list

%changelog

%autochangelog
