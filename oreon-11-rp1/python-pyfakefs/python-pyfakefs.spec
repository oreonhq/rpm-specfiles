%global source0_hash 8ae0e5421e08de4e433853a4609a06a1835f4bc2a3ce13b54f36713a897474ba

%global package_name pyfakefs

Name:           python-%{package_name}
Version:        5.10.2
Release:        2%{?dist}
Summary:        pyfakefs implements a fake file system that mocks the Python file system modules.
License:        Apache-2.0
URL:            http://pyfakefs.org
Source0:        https://pypi.io/packages/source/p/%{package_name}/%{package_name}-%{version}.tar.gz
BuildArch:      noarch

%description
pyfakefs implements a fake file system that mocks the Python file system
modules.
Using pyfakefs, your tests operate on a fake file system in memory without
touching the real disk. The software under test requires no modification to
work with pyfakefs.

%package -n python3-%{package_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{package_name}}

BuildRequires:  git-core
BuildRequires:  python3-devel
# For import check
BuildRequires:  python3-pytest

Requires:       python3-pytest

%description -n python3-%{package_name}
pyfakefs implements a fake file system that mocks the Python file system
modules.
Using pyfakefs, your tests operate on a fake file system in memory without
touching the real disk. The software under test requires no modification to
work with pyfakefs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{package_name}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{package_name}

%check
%pyproject_check_import

%files -n python3-%{package_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
