%global source0_hash 4eaeaa99ed91163ed8f9aac132c70a81f25bc4c12f3cd54dba329fc26c6739b5

%global srcname pytest-astropy
%global modname pytest_astropy
%global sum The py.test astropy plugin

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        %{sum}

License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-astropy
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
This package provides a plugin for the pytest framework that is used for
testing Astropy and its affiliated packages. 

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
This package provides a plugin for the pytest framework that is used for
testing Astropy and its affiliated packages. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst

%changelog
%autochangelog
