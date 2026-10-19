%global source0_hash 1091cd919806a3ce05d2276729f79be4ecbd0a939500a8899026c3ef5769c650
Name:           python-pyqt6-charts
Version:        6.11.0
Release:        1%{?dist}
Summary:        Python bindings for the Qt Charts library
License:        GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/pyqtchart/
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt6_charts/pyqt6_charts-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyqt-builder) < 2
BuildRequires:  python3dist(pyqt-builder) >= 1.19
BuildRequires:  python3dist(sip) < 7
BuildRequires:  python3dist(sip) >= 6.15
Requires:       python3-pyqt6-charts = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyqt6-charts
Summary:        Python bindings for the Qt Charts library
# oreon:reqs
Requires:       python3dist(pyqt6) (>=6.2.0)
# /oreon:reqs
%description -n python3-pyqt6-charts

%prep
%global oreon_srcdir pyqt6_charts-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyqt6-charts usr/lib/python3*/site-packages/pyqt6_charts* usr/lib64/python3*/site-packages/pyqt6_charts* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyqt6_charts* usr/lib64/python3*/site-packages/pyqt6_charts* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyqt6-charts -f %{oreon_filedir}/python3-pyqt6-charts.list

%changelog

%autochangelog
