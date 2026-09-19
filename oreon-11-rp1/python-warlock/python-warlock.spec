%global source0_hash 82319ba017341e7fcdc81efc2be9dd2f8237a0da07c71476b5425651b317b1c9

%global github_name warlock

Name:           python-warlock
Version:        2.1.0
Release:        6%{?dist}
Summary:        Python object model built on top of JSON schema

License:        Apache-2.0
URL:            http://pypi.python.org/pypi/warlock
Source0:        %{pypi_source %{github_name}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
Build self-validating python objects using JSON schemas}

%description %_description

%package -n python3-%{github_name}
Summary:        Python object model built on top of JSON schema
%{?python_provide:%python_provide python3-%{github_name}}

%description -n python3-%{github_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{github_name}-%{version}

sed -i 's/\(jsonschema\).*"^\(.*\)"/\1 = ">= \2"/' pyproject.toml
sed -i 's/\(jsonpatch\).*"^\(.*\)"/\1 = ">= \2"/' pyproject.toml
cat pyproject.toml | grep -e json

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files warlock

%check
%pyproject_check_import warlock

%files -n python3-%{github_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
