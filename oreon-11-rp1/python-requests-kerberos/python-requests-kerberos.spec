%global source0_hash 2846bbca9ed5bd4c12ace11863c63d605684a5d327235ba95ff63b856bfb9e0c
Name:           python-requests-kerberos
Version:        0.15.0
Release:        1%{?dist}
Summary:        A Kerberos authentication handler for python-requests
License:        ISC
URL:            https://github.com/requests/requests-kerberos
Source0:        https://github.com/requests/requests-kerberos/archive/v%{version}/requests-kerberos-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-requests-kerberos = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-requests-kerberos
Summary:        A Kerberos authentication handler for python-requests
%description -n python3-requests-kerberos

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n requests-kerberos-%{version}
# avoid unnecessary coverage dependency
sed -i '/pytest-cov/d' requirements-test.txt

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requests-kerberos usr/lib/python3*/site-packages/requests_kerberos* usr/lib64/python3*/site-packages/requests_kerberos* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requests_kerberos* usr/lib64/python3*/site-packages/requests_kerberos* usr/bin/*

%check

%pytest -v tests
%files
%files -n python3-requests-kerberos -f %{oreon_filedir}/python3-requests-kerberos.list

%changelog

%autochangelog
