%global source0_hash 15cf49efbbbd4c6bc87653b2c4ae80d6049f800e31620b336734ae2e37cbedae
Name:           python-pyqt6-webengine
Version:        6.11.0
Release:        1%{?dist}
Summary:        Python bindings for the Qt WebEngine framework
License:        GPL-3.0-only
URL:            https://www.riverbankcomputing.com/software/pyqtwebengine/
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt6_webengine/pyqt6_webengine-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyqt-builder) < 2
BuildRequires:  python3dist(pyqt-builder) >= 1.19
BuildRequires:  python3dist(sip) < 7
BuildRequires:  python3dist(sip) >= 6.15
Requires:       python3-pyqt6-webengine = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyqt6-webengine
Summary:        Python bindings for the Qt WebEngine framework
# oreon:reqs
Requires:       python3dist(pyqt6) (>=6.2.0)
# /oreon:reqs
%description -n python3-pyqt6-webengine

%prep
%global oreon_srcdir pyqt6_webengine-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyqt6-webengine usr/lib/python3*/site-packages/pyqt6_webengine* usr/lib64/python3*/site-packages/pyqt6_webengine* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyqt6_webengine* usr/lib64/python3*/site-packages/pyqt6_webengine* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyqt6-webengine -f %{oreon_filedir}/python3-pyqt6-webengine.list

%changelog

%autochangelog
