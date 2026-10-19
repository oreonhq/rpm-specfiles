%global source0_hash d7af3984a99d243c131aa1a828331e7630f4a88a9741fd05c927b204bcf92261
Name:           python-click-plugins
Version:        1.1.1.2
Release:        1%{?dist}
Summary:        Click extension to register CLI commands via setuptools
License:        BSD-3-Clause
URL:            https://github.com/click-contrib/click-plugins
Source0:        https://files.pythonhosted.org/packages/source/c/click_plugins/click_plugins-%{version}.tar.gz
BuildArch:      noarch
Patch:          fix-click-8.2-tests.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-click-plugins = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-click-plugins
Summary:        Click extension to register CLI commands via setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
Provides: deprecated()
%description -n python3-click-plugins

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir click_plugins-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-click-plugins usr/lib/python3*/site-packages/click_plugins* usr/lib64/python3*/site-packages/click_plugins* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/click_plugins* usr/lib64/python3*/site-packages/click_plugins* usr/bin/*

%check

export LANG=C.UTF-8
%{pytest} -ra
%files
%files -n python3-click-plugins -f %{oreon_filedir}/python3-click-plugins.list

%changelog

%autochangelog
