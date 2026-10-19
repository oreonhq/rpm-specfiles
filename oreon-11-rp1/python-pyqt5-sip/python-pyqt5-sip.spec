%global source0_hash 71cacf1879da2cd3e50cb239e21673cfe02d358af70ab6768817c960428868c3
Name:           python-pyqt5-sip
Version:        12.19.0
Release:        1%{?dist}
Summary:        The sip module support for PyQt5
License:        BSD-2-Clause
URL:            https://github.com/Python-SIP/sip
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt5_sip/pyqt5_sip-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75.8.1
Requires:       python3-pyqt5-sip = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyqt5-sip
Summary:        The sip module support for PyQt5
%description -n python3-pyqt5-sip

%prep
%global oreon_srcdir pyqt5_sip-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyqt5-sip usr/lib/python3*/site-packages/pyqt5_sip* usr/lib64/python3*/site-packages/pyqt5_sip* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyqt5_sip* usr/lib64/python3*/site-packages/pyqt5_sip* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyqt5-sip -f %{oreon_filedir}/python3-pyqt5-sip.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.17.1-2
- Prepare for Oreon 11 (RP1)
