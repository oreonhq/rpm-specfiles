%global source0_hash a7c390b826e8bd76611a39b6f0e8af73c55871767c674fcd8373a25b2bcdd1c2

%global pypi_name resumable-urlretrieve

%global desc %{expand: \
Small library to fetch files over HTTP and resume their download.}

Name:           python-%{pypi_name}
Version:        0.1.6
Release:        26%{?dist}
Summary:        Small library to fetch files over HTTP and resume their download

License:        MIT
URL:            https://github.com/berdario/resumable-urlretrieve
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%?python_enable_dependency_generator

BuildRequires: python3-devel
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(requests)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(rangehttpserver)

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=. pytest-3

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/resumable
%{python3_sitelib}/resumable_urlretrieve-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
