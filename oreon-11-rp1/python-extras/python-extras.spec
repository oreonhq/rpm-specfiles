%global source0_hash 132e36de10b9c91d5d4cc620160a476e0468a88f16c9431817a6729611a81b4e
%bcond bootstrap 0
Name:           python-extras
Version:        1.0.0
Release:        43%{?dist}
Summary:        Useful extra bits for Python
License:        MIT
URL:            https://github.com/testing-cabal/extras
Source0:        https://files.pythonhosted.org/packages/source/e/extras/extras-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-extras = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-extras
Summary:        Useful extra bits for Python
BuildRequires:  python3-devel
%if %{without bootstrap}
BuildRequires:  python3-testtools
%endif
%description -n python3-extras

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n extras-%{version}
# don't include extras.tests
sed -e '/extras\.tests/d' -i setup.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-extras usr/lib/python3*/site-packages/extras* usr/lib64/python3*/site-packages/extras* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/extras* usr/lib64/python3*/site-packages/extras* usr/bin/*

%check

%if %{with bootstrap}
%pyproject_check_import
%else
%{py3_test_envvars} %{python3} -m testtools.run extras.tests.test_suite
%endif
%files
%files -n python3-extras -f %{oreon_filedir}/python3-extras.list

%changelog

%autochangelog
