%global source0_hash 7900d9d20139c5407d3cb65e560c11b021767ae21054536cc919f9924e67a21e
%global srcname pyramid_sawing
%global desc A Pyramid framework plugin for configuring logging via YAML. This uses\
the Python standard-library's logging (initialized using\
logging.config.dictConfig).
Name: python-%{srcname}
Version: 1.1.3
Release:        1%{?dist}
BuildArch: noarch
Summary:        Pyramid plugin for YAML logging configuration
License: AGPL-3.0-only
URL:     https://github.com/openstax/pyramid_sawing
Source0:        https://github.com/openstax/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch0:  0000-Use-yaml.safe_load-instead-of-load.patch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pyramid
BuildRequires:  python3-pyyaml
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{desc}

%package -n python3-%{srcname}
Summary:        Pyramid plugin for YAML logging configuration
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n python3-pyramid_sawing -f %{oreon_filedir}/python3-pyramid_sawing.list

%changelog

%autochangelog
