%global source0_hash 5bce2cfa1d21aaca82622c68fb0deb233ca334b0c28749f104b983563f28f004
%global pypi_name uri-template
%global pypi_version 1.3.0
Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        RFC 6570 URI Template Processor
License:        MIT
URL:            https://github.com/plinss/uri_template/
Source0:        https://github.com/plinss/uri_template//archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-uri-template = %{version}-%{release}
# /oreon:deps
%package -n       python3-uri-template+dev
Summary:        Metapackage for python3-uri-template dev extras
Requires:       python3-uri-template = %{version}-%{release}
Provides:       python3dist(uri-template[dev]) = %{version}-%{release}

%description -n python3-uri-template+dev
Metapackage for python3-uri-template dev extras.

%description
An implementation of RFC 6570 URI Templates.This packages implements
URI Template expansion in strict adherence to RFC 6570, but adds a
few extensions.

%package -n     python3-%{pypi_name}
Summary:        RFC 6570 URI Template Processor
%description -n python3-%{pypi_name}
An implementation of RFC 6570 URI Templates.This packages implements
URI Template expansion in strict adherence to RFC 6570, but adds a
few extensions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version}

%build

export SETUPTOOLS_SCM_PRETEND_VERSION="%{pypi_version}"
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/uri_template* usr/lib64/python3*/site-packages/uri_template* usr/bin/*

%check

%{python3} test.py
%files
%files -n python3-uri-template -f %{oreon_filedir}/python3-uri-template.list

%changelog

%autochangelog
