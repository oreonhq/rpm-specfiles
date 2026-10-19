%global source0_hash ef958f83da020629259afd41f793e6d10ef32139ce849ada8a9c3b9d3ef2e56b
%bcond tests %{undefined rhel}
%global distname requests-oauthlib
%global modname requests_oauthlib
Name:               python-requests-oauthlib
Version:            2.0.0
Release:        1%{?dist}
Summary:        OAuthlib authentication support for Requests.
License:            ISC
URL:                http://pypi.python.org/pypi/requests-oauthlib
Source0:        https://github.com/requests/requests-oauthlib/archive/refs/tags/v%{version}.tar.gz#/requests-oauthlib-%{version}.tar.gz
Patch0:             https://github.com/requests/requests-oauthlib/commit/b1dd93c5d024500b6236dea06734d6e6482c3565.patch
BuildArch:          noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-requests-oauthlib = %{version}-%{release}
# /oreon:deps
%description
This project provides first-class OAuth library support for python-request.

%package -n python3-%{distname}
%{?python_provide:%python_provide python3-%{distname}}
Summary:            OAuthlib authentication support for Requests.
BuildRequires:      python3-devel
%if %{with tests}
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-mock
BuildRequires:      python3-requests-mock
BuildRequires:      python3-selenium, selenium-manager
%endif
%description -n python3-%{distname}
This project provides first-class OAuth library support for python-request.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{distname}-%{version} -p1
# Requires python-selenium fix from unmerged https://src.fedoraproject.org/rpms/python-selenium/pull-request/9
# Furthermore then throws error on insisting on only chrome-146 but fedora has 148
rm tests/examples/test_native_spa_pkce_auth0.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/requests_oauthlib* usr/lib64/python3*/site-packages/requests_oauthlib* usr/bin/*

%check

%if %{with tests}
%pytest -k "not testCanPostBinaryData and not test_content_type_override and not test_url_is_native_str"
%else
%pyproject_check_import
%endif
%files
%files -n python3-requests-oauthlib -f %{oreon_filedir}/python3-requests-oauthlib.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Import
