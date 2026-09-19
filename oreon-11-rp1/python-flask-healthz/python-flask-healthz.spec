%global source0_hash 3b25bfd8606950a77632925cfbbf19cac20650be51fc0efbe78c387e559e2541

%global pypi_name flask-healthz
%global srcname flask_healthz
%global mod_name flask_healthz

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        10%{?dist}
Summary:        Module to easily add health endpoints to a Flask application

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/fedora-infra/%{pypi_name}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This module allows you to define endpoints in your Flask application
that can be used as liveness and readiness probes.

%package -n python3-%{pypi_name}
Summary:        Module to easily add health endpoints to a Flask application
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module allows you to define endpoints in your Flask application
that can be used as liveness and readiness probes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
