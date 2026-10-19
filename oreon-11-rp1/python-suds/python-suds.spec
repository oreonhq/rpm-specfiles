%global source0_hash 5c8752020826c8bc93fd6422b347ae3cfa2aeb76b477868644e5630c70d6d644
Name:           python-suds
Version:        1.2.0
Release:        1%{?dist}
Summary:        A python SOAP client
License:        LGPL-3.0-or-later
URL:            https://github.com/suds-community/suds
Source0:        https://github.com/suds-community/suds/archive/v1.2.0.tar.gz#/suds-1.2.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-suds = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-suds
Summary:        A python SOAP client
%description -n python3-suds

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir suds-%{version}
%oreon_prep
%build

export SUDS_PACKAGE=suds
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-suds usr/lib/python3*/site-packages/suds* usr/lib64/python3*/site-packages/suds* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/suds* usr/lib64/python3*/site-packages/suds* usr/bin/*

%check

%pytest
%files
%files -n python3-suds -f %{oreon_filedir}/python3-suds.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-7
- Prepare for Oreon 11 (RP1)
