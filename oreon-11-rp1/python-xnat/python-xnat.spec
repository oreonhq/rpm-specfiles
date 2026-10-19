%global source0_hash da153e7d4bb4e7c1becff79c9dc4097750f56f77bef4aa5b9c2c446fe54f59ad
Name:           python-xnat
Version:        0.8.1
Release:        1%{?dist}
Summary:        An XNAT client that exposes the XNAT REST interface as python objects. Part of the interface is automatically generated based on the servers data model as defined by the xnat schema.
License:        ...
URL:            https://gitlab.com/radiology/infrastructure/xnatpy
Source0:        https://files.pythonhosted.org/packages/source/x/xnat/xnat-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-xnat = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xnat
Summary:        An XNAT client that exposes the XNAT REST interface as python objects. Part of the interface is automatically generated based on the servers data model as defined by the xnat schema.
# oreon:reqs
Requires:       python3dist(click) >= 8.0
Requires:       python3dist(click-option-group) >= 0.5.6
Requires:       python3dist(importlib-metadata) >= 6.8
Requires:       python3dist(isodate) >= 0.6
Requires:       python3dist(progressbar2) >= 4.2
Requires:       python3dist(pydicom) >= 2.3
Requires:       python3dist(python-dateutil) >= 2.8.2
Requires:       python3dist(pyyaml) >= 6.0
Requires:       python3dist(requests) >= 2.30
# /oreon:reqs
%description -n python3-xnat

%prep
%global oreon_srcdir xnat-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xnat usr/lib/python3*/site-packages/xnat* usr/lib64/python3*/site-packages/xnat* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xnat* usr/lib64/python3*/site-packages/xnat* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xnat -f %{oreon_filedir}/python3-xnat.list

%changelog

%autochangelog
