%global source0_hash 30e01c0217d5bf8b94ff68c6f517df7319254e1f62c1796919f8a7f5512b4725
Name:           python-goocalendar
Version:        1.0.0
Release:        1%{?dist}
Summary:        A calendar widget for GTK
License:        GPL-2.0-or-later
URL:            https://www.tryton.org/
Source0:        https://files.pythonhosted.org/packages/source/g/goocalendar/goocalendar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1
Requires:       python3-goocalendar = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-goocalendar
Summary:        A calendar widget for GTK
%description -n python3-goocalendar

%prep
%global oreon_srcdir goocalendar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-goocalendar usr/lib/python3*/site-packages/goocalendar* usr/lib64/python3*/site-packages/goocalendar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/goocalendar* usr/lib64/python3*/site-packages/goocalendar* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-goocalendar -f %{oreon_filedir}/python3-goocalendar.list

%changelog

%autochangelog
