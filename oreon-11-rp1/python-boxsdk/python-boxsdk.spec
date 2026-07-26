%global source0_hash d14b2ab39f0b24ac3a5dfe4bb1c64cee423e2cc097658056f27f121960c70885

%global modname boxsdk

%bcond_with tests

Name:               python-boxsdk
Version:            10.3.0
Release:            2%{?dist}
Summary:            Python wrapper for the Box API

License:            Apache-2.0 
URL:                https://github.com/box/box-python-sdk
Source0:            %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-requests
BuildRequires:      python%{python3_pkgversion}-six
BuildRequires:      python%{python3_pkgversion}-wrapt
BuildRequires:      python%{python3_pkgversion}-requests-toolbelt
BuildRequires:      python%{python3_pkgversion}-attrs
# Tests don't pass at the moment.
# https://github.com/box/box-python-sdk/issues/494
%if %{with tests}
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-bottle
BuildRequires:      python%{python3_pkgversion}-redis
BuildRequires:      python%{python3_pkgversion}-mock
BuildRequires:      python%{python3_pkgversion}-sqlalchemy
BuildRequires:      python%{python3_pkgversion}-jsonpatch
BuildRequires:      python%{python3_pkgversion}-cryptography
BuildRequires:      python%{python3_pkgversion}-pytz
BuildRequires:      python%{python3_pkgversion}-jwt
%endif

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n box-python-sdk-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l box_sdk_gen

%if %{with tests}
%check
%pyproject_check_import

pytest-3
%endif

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc *.md

%changelog
%autochangelog
