%global source0_hash 18ae978418813f292ddff4dcd1aec1c296b81e0a127c41bd77e2b78bfcf194ab
Name:           python-flexmock
Version:        0.13.0
Release:        1%{?dist}
Summary:        Testing library that makes it easy to create mocks, stubs and fakes
License:        BSD-2-Clause-Views
URL:            https://flexmock.readthedocs.org
Source0:        https://github.com/flexmock/flexmock/archive/v%{version}/flexmock-v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-flexmock = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-flexmock
Summary:        Testing library that makes it easy to create mocks, stubs and fakes
%{?python_provide:%python_provide python3-flexmock}
%description -n python3-flexmock

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n flexmock-%{version}
# teamcity-messages package not yet available in Fedora
sed -i "/teamcity-messages$/d" tox.ini
sed -i "/test_teamcity.py$/d" tox.ini
# Upstream manipulates PYTHONPATH which breaks testing
sed -i "/setenv = PYTHONPATH/d" tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flexmock usr/lib/python3*/site-packages/flexmock* usr/lib64/python3*/site-packages/flexmock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flexmock* usr/lib64/python3*/site-packages/flexmock* usr/bin/*

%check

PYTHONPATH=.:%{buildroot}/%{python3_sitelib} %tox
rm -rf %{buildroot}/%{python3_sitelib}/{LICENSE,docs,*.md,tests}
%files
%files -n python3-flexmock -f %{oreon_filedir}/python3-flexmock.list

%changelog

%autochangelog
