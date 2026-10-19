%global source0_hash c982176754e8274f5aec00eaa65986cf205cb5fc898c2f917eead00d221f2adc
Name:           python-requests-exoscale-auth
Version:        1.1.2
Release:        19%{?dist}
Summary:        Exoscale APIs support for Python-Requests
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/exoscale/requests-exoscale-auth
Source0:        https://github.com/exoscale/requests-exoscale-auth/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-requests-exoscale-auth = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-requests-exoscale-auth
Summary:        Exoscale APIs support for Python-Requests
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
%description -n python3-requests-exoscale-auth

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir requests-exoscale-auth-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requests-exoscale-auth usr/lib/python3*/site-packages/requests_exoscale_auth* usr/lib64/python3*/site-packages/requests_exoscale_auth* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requests_exoscale_auth* usr/lib64/python3*/site-packages/requests_exoscale_auth* usr/bin/*

%check

%pytest
%files
%files -n python3-requests-exoscale-auth -f %{oreon_filedir}/python3-requests-exoscale-auth.list

%changelog

%autochangelog
