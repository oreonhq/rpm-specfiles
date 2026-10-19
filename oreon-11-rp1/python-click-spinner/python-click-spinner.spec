%global source0_hash 01371550596bc18f1e1546bb2956745eed387235235e664bc96f8cc675b7d6e8
Name:           python-click-spinner
Version:        0.2.0
Release:        1%{?dist}
Summary:        Spinner for Click
License:        MIT
URL:            https://github.com/click-contrib/click-spinner
Source0:        https://files.pythonhosted.org/packages/source/c/click_spinner/click_spinner-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-click-spinner = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-click-spinner
Summary:        Spinner for Click
%description -n python3-click-spinner

%prep
%global oreon_srcdir click_spinner-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-click-spinner usr/lib/python3*/site-packages/click_spinner* usr/lib64/python3*/site-packages/click_spinner* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/click_spinner* usr/lib64/python3*/site-packages/click_spinner* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-click-spinner -f %{oreon_filedir}/python3-click-spinner.list

%changelog

%autochangelog
