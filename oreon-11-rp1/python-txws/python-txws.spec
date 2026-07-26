%global source0_hash 7e91e570341756994ba6dd00bd1bb2329ad9966a77a17a7d6d5a904fb66f419d

# what it's called on pypi
%global srcname txWS
# what it's imported as
%global libname txws
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%bcond_without tests

Name:             python-%{pkgname}
Version:          0.9.1
Release:          41%{?dist}
Summary:          Twisted WebSockets wrapper

License:          MIT
URL:              https://github.com/MostAwesomeDude/txWS
# PyPI tarball doesn't have tests
Source0:          %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Downstream-only patch.  Make sure to update when the version changes!
Patch0:           0001-Drop-vcversioner.patch

# https://github.com/MostAwesomeDude/txWS/pull/34
Patch1:           python-txws-python39.patch

BuildArch:        noarch

%global common_description %{expand:
txWS (pronounced "Twisted WebSockets") is a small, short, simple library
for adding WebSockets server support to your favorite Twisted applications.}

%description %{common_description}

%package -n python3-%{pkgname}
Summary:          %{summary}
BuildRequires:    python3-devel
BuildRequires:    %{py3_dist setuptools}
%if %{with tests}
BuildRequires:    %{py3_dist Twisted six}
%endif
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=$(pwd) trial-3 tests
%endif

%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}.py
%{python3_sitelib}/__pycache__/%{libname}.cpython-%{python3_version_nodots}*.py*
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
