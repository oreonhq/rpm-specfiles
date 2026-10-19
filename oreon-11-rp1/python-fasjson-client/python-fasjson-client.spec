%global source0_hash 47607c9f3bd39ad78ab0b2c4f31d34a8ea7f6b0fb407bd86a8e3b622eb2d7055
%bcond_without tests
Name:           python-fasjson-client
Version:        1.1.0
Release:        1%{?dist}
Summary:        An OpenAPI client for FASJSON
License:        LGPL-3.0-or-later
URL:            https://github.com/fedora-infra/fasjson-client
Source0:        https://files.pythonhosted.org/packages/source/f/fasjson_client/fasjson_client-%{version}.tar.gz
Patch:          0001-Update-dependency-bravado-to-v12-686.patch
Patch:          0002-Adjust-test_sign_bad_pkey-to-work-with-cryptography-45.patch
Patch:          0003-Only-package-support-files-in-the-sdist.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-fasjson-client = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-fasjson-client
Summary:        An OpenAPI client for FASJSON
%description -n python3-fasjson-client

%package -n     fasjson-client
Summary:        An OpenAPI client for FASJSON - CLI
Requires:       python3-fasjson-client+cli = %{version}-%{release}
%description -n fasjson-client
A command line interface for the FASJSON API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir fasjson_client-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-fasjson-client usr/lib/python3*/site-packages/fasjson_client* usr/lib64/python3*/site-packages/fasjson_client* usr/bin/*
%oreon_autofiles fasjson-client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/fasjson_client* usr/lib64/python3*/site-packages/fasjson_client* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%pytest -v fasjson_client/tests/unit
%else
%pyproject_check_import -e 'fasjson_client.tests*'
%endif
%files
%files -n python3-fasjson-client -f %{oreon_filedir}/python3-fasjson-client.list
%files -n fasjson-client -f %{oreon_filedir}/fasjson-client.list

%changelog

%autochangelog
