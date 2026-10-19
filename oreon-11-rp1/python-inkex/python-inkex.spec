%global source0_hash 2f9803154806ebae8a40b33ef2c691806a472857adc90303eaa32482bd8c19ed
Name:           python-inkex
Version:        1.4.1
Release:        1%{?dist}
Summary:        Python extensions for Inkscape core, separated out from main repository.
License:        GPL-2.0-or-later
URL:            https://gitlab.com/inkscape/extensions
Source0:        https://files.pythonhosted.org/packages/source/i/inkex/inkex-%{version}.tar.gz
Patch:          fix-pyproject-lxml-constraint.patch
Patch:          fix-pyproject-scour-constraint.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-inkex = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-inkex
Summary:        Python extensions for Inkscape core, separated out from main repository.
%description -n python3-inkex

%prep
%global oreon_srcdir inkex-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-inkex usr/lib/python3*/site-packages/inkex* usr/lib64/python3*/site-packages/inkex* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/inkex* usr/lib64/python3*/site-packages/inkex* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-inkex -f %{oreon_filedir}/python3-inkex.list

%changelog

%autochangelog
