%global source0_hash 7900d9d20139c5407d3cb65e560c11b021767ae21054536cc919f9924e67a21e

%global srcname pyramid_sawing
%global desc A Pyramid framework plugin for configuring logging via YAML. This uses\
the Python standard-library's logging (initialized using\
logging.config.dictConfig).

Name: python-%{srcname}
Version: 1.1.3
Release: 28%{?dist}
BuildArch: noarch

Summary: Pyramid plugin for YAML logging configuration
# Automatically converted from old format: AGPLv3
License: AGPL-3.0-only
URL:     https://github.com/openstax/pyramid_sawing
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/openstax/pyramid_sawing/pull/3
Patch0:  0000-Use-yaml.safe_load-instead-of-load.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pyramid
BuildRequires: python3-pyyaml

%description
%{desc}

%package -n python3-%{srcname}
Summary: %{summary}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
# This package used setup.py test which doesn't work anymore
# upstream is dead, but we still need it as it is used in Bodhi

%files -n python3-%{srcname}
%license LICENSE.txt
%doc CHANGES.rst
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/*.egg-info

%changelog
%autochangelog
