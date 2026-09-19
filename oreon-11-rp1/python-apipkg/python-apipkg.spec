%global source0_hash 67345fd0446e5a24b50f42f2fc3e6a2cd5612379cd6944f68529886f188184ba

%global srcname apipkg

Name:           python-%{srcname}
Version:        3.0.2
Release:        11%{?dist}
Summary:        A Python namespace control and lazy-import mechanism

License:        MIT
URL:            https://github.com/pytest-dev/apipkg
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
With apipkg you can control the exported namespace of a Python package and
greatly reduce the number of imports for your users. It is a small pure Python
module that works on CPython 2.7 and 3.4+, Jython and PyPy. It cooperates well
with Python's help() system, custom importers (PEP302) and common command-line
completion tools.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# https://github.com/pytest-dev/apipkg/issues/43
sed -i '/distribution_version("py")/d' test_apipkg.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -t

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files apipkg

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG README.rst
%license LICENSE

%changelog
%autochangelog
