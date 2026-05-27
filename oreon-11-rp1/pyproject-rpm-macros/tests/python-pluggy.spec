%global source0_hash none

%global pypi_name pluggy
Name:           python-%{pypi_name}
Version:        1.5.0
Release:        1%{?dist}
Summary:        The plugin manager stripped of pytest specific details

License:        MIT
URL:            https://github.com/pytest-dev/pluggy
Source0:        https://files.pythonhosted.org/packages/source/p/pluggy/pluggy-1.5.0.tar.gz

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
# we don't BR python3-devel here just for test purposes, but we recommend you do it

%description
A pure Python library. The package contains tox.ini. Does not contain executables.
Building this tests:
- generating runtime and testing dependencies
- running tests with %%tox
- the %%pyproject_save_files +auto option works without actual executables
- pyproject.toml with the setuptools backend and setuptools-scm


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{pypi_name}-%{version}
# internal check for our macros: insert a subprocess echo to setup.py
# to ensure it's not generated as BuildRequires
echo 'import os; os.system("echo if-this-is-generated-the-build-will-fail")' >> setup.py


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
# There are no executables, but we are allowed to pass +auto anyway
%pyproject_save_files pluggy +auto -l


%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
