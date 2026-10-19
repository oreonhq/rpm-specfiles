%global source0_hash a7ad45c1e3cec3a2473d37ea9870b6c3baeccc560298623c8eb59265714c06e2
Name:           python-pyqt6-sip
Version:        13.12.0
Release:        1%{?dist}
Summary:        The sip module support for PyQt6
License:        BSD-2-Clause
URL:            https://github.com/Python-SIP/sip
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt6_sip/pyqt6_sip-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 75.8.1
Requires:       python3-pyqt6-sip = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyqt6-sip
Summary:        The sip module support for PyQt6
%description -n python3-pyqt6-sip

%prep
%global oreon_srcdir pyqt6_sip-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyqt6-sip usr/lib/python3*/site-packages/pyqt6_sip* usr/lib64/python3*/site-packages/pyqt6_sip* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyqt6_sip* usr/lib64/python3*/site-packages/pyqt6_sip* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyqt6-sip -f %{oreon_filedir}/python3-pyqt6-sip.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.11.0-2
- Prepare for Oreon 11 (RP1)
