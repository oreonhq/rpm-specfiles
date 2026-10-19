%global source0_hash ebd13154be1c8515e665de70bd2d303ae9ddc3ef47e44afd5116441ca0283a26
Name:           python-reportlab
Version:        5.0.1
Release:        1%{?dist}
Summary:        The Reportlab Toolkit
License:        ...
URL:            https://www.reportlab.com/
Source0:        https://files.pythonhosted.org/packages/source/r/reportlab/reportlab-%{version}.tar.gz
BuildArch:      noarch
Patch0:         %{name}-fix_python_3.15.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-reportlab = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-reportlab
Summary:        The Reportlab Toolkit
%description -n python3-reportlab

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir reportlab-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-reportlab usr/lib/python3*/site-packages/reportlab* usr/lib64/python3*/site-packages/reportlab* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/reportlab* usr/lib64/python3*/site-packages/reportlab* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-reportlab -f %{oreon_filedir}/python3-reportlab.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4.10-1
- Prepare for Oreon 11 (RP1)
