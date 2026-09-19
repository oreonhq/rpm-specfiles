%global source0_hash 47607c9f3bd39ad78ab0b2c4f31d34a8ea7f6b0fb407bd86a8e3b622eb2d7055

%bcond_without tests

Name:           python-fasjson-client
Version:        1.1.0
Release:        %autorelease
Summary:        An OpenAPI client for FASJSON

License:        LGPL-3.0-or-later
URL:            https://github.com/fedora-infra/fasjson-client
Source:         %{pypi_source fasjson_client}
# https://github.com/fedora-infra/fasjson-client/commit/9806fa5022502fae3f5e8d58599791b9f3d4e07e
Patch:          0001-Update-dependency-bravado-to-v12-686.patch
# https://github.com/fedora-infra/fasjson-client/pull/694
Patch:          0002-Adjust-test_sign_bad_pkey-to-work-with-cryptography-45.patch
# https://github.com/fedora-infra/fasjson-client/commit/0cd6106581d9cf85e790b3c9fa2842070c46113b
Patch:          0003-Only-package-support-files-in-the-sdist.patch
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-requests-mock
%endif

%global _description %{expand:
A python client library for the FASJSON API.}

%description %_description

%package -n     python3-fasjson-client
Summary:        %{summary}

%description -n python3-fasjson-client %_description

%pyproject_extras_subpkg -n python3-fasjson-client cli

%package -n     fasjson-client
Summary:        %{summary} - CLI
Requires:       python3-fasjson-client+cli = %{version}-%{release}

%description -n fasjson-client
A command line interface for the FASJSON API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fasjson_client-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires -x cli

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fasjson_client

%check
%if %{with tests}
# upstream runs pytest from within tox, but that includes lots of coverage
# flags we don't want
%pytest -v fasjson_client/tests/unit
%else
# even when tests are skipped, make sure the module imports correctly
%pyproject_check_import -e 'fasjson_client.tests*'
%endif

%files -n python3-fasjson-client -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n fasjson-client
%{_bindir}/fasjson-client

%changelog
%autochangelog
