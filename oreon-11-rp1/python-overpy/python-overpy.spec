%global source0_hash 05ba0aa23455cdddb8679e0476bd1d9cbf7380f3136ef2785f836733a68c4468

%global github_name python-overpy
%global pretty_name overpy

%global _description %{expand:
overpy is a wrapper written in Python to access the Overpass API.}

Name:           python-%{pretty_name}
Version:        0.7
Release:        12%{?dist}
Summary:        Python Wrapper to access the Overpass API

# SPDX
License:        MIT
URL:            https://github.com/DinoTools/python-overpy
Source0:        %{url}/archive/%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

#for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis

#for docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)

%description -n python3-%{pretty_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{github_name}-%{version}
rm -rf %{pretty_name}.egg-info

%build
%py3_build

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%pytest

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.rst CHANGELOG.rst examples/
%{python3_sitelib}/%{pretty_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pretty_name}

%files -n python-%{pretty_name}-doc
%license LICENSE
%doc html/

%changelog
%autochangelog
