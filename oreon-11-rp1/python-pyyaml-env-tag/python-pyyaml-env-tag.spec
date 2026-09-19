%global source0_hash dc81e3334fed22f7a977ecac46e4d7e4580e33445b4c2a059ea812c44548af38

Name:           python-pyyaml-env-tag
Version:        1.1
Release:        6%{?dist}
Summary:        A custom YAML tag for referencing environment variables in YAML files
BuildArch:      noarch

License:        MIT
URL:            https://github.com/waylan/pyyaml-env-tag
Source0:        https://github.com/waylan/pyyaml-env-tag/archive/%{version}/pyyaml_env_tag-%{version}.tar.gz

BuildRequires:  python3-devel

%description
A custom YAML tag for referencing environment variables in YAML files.

%package -n python3-pyyaml-env-tag
Summary:        %{summary}

%description -n python3-pyyaml-env-tag
A custom YAML tag for referencing environment variables in YAML files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyyaml-env-tag-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files yaml_env_tag

%check
PYTHONPATH=$PWD %{python3} tests/test_yaml_env_tag.py

%files -n python3-pyyaml-env-tag -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
