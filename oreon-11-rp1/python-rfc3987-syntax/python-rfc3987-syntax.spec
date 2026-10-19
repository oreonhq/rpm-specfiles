%global source0_hash dd8847eae35ca0668231026b64a32ea9b5bbb03c0aa3c8d02a4daa86de460dfc
Name:           python-rfc3987-syntax
Version:        1.1.0
Release:        1%{?dist}
Summary:        Helper functions to syntactically validate strings according to RFC 3987
License:        MIT
URL:            https://github.com/willynilly/rfc3987-syntax
Source0:        https://github.com/willynilly/rfc3987-syntax/archive/v%{version}/rfc3987-syntax-%{version}.tar.gz
Patch:          %{url}/pull/13.patch
Patch:          %{url}/pull/9.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rfc3987-syntax = %{version}-%{release}
# /oreon:deps
%package -n       python3-rfc3987-syntax+testing
Summary:        Metapackage for python3-rfc3987-syntax testing extras
Requires:       python3-rfc3987-syntax = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.3.5
Provides:       python3dist(rfc3987-syntax[testing]) = %{version}-%{release}

%description -n python3-rfc3987-syntax+testing
Metapackage for python3-rfc3987-syntax testing extras.

%description

%package -n     python3-rfc3987-syntax
Summary:        Helper functions to syntactically validate strings according to RFC 3987
# oreon:reqs
Requires:       python3dist(lark) >= 1.2.2
# /oreon:reqs
%description -n python3-rfc3987-syntax

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rfc3987-syntax usr/lib/python3*/site-packages/rfc3987_syntax* usr/lib64/python3*/site-packages/rfc3987_syntax* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rfc3987_syntax* usr/lib64/python3*/site-packages/rfc3987_syntax* usr/bin/*

%check

%pytest -v
%files
%files -n python3-rfc3987-syntax -f %{oreon_filedir}/python3-rfc3987-syntax.list

%changelog

%autochangelog
