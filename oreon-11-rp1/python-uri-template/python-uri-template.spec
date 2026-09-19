%global source0_hash 5bce2cfa1d21aaca82622c68fb0deb233ca334b0c28749f104b983563f28f004

%global pypi_name uri-template
%global pypi_version 1.3.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        6%{?dist}
Summary:        RFC 6570 URI Template Processor

License:        MIT
URL:            https://github.com/plinss/uri_template/
Source:         %{url}/archive/refs/tags/v%{pypi_version}.tar.gz#/%{name}-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
An implementation of RFC 6570 URI Templates.This packages implements
URI Template expansion in strict adherence to RFC 6570, but adds a
few extensions.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
An implementation of RFC 6570 URI Templates.This packages implements
URI Template expansion in strict adherence to RFC 6570, but adds a
few extensions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%{pypi_version}"
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{pypi_version}"
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l uri_template

%check
%{python3} test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
