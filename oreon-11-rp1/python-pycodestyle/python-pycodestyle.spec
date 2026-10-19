%global source0_hash c4b5b517d278089ff9d0abdec919cd97262a3367449ea1c8b49b91529167b783
Name:           python-pycodestyle
Version:        2.14.0
Release:        1%{?dist}
Summary:        Python style guide checker
License:        MIT
URL:            https://pycodestyle.pycqa.org/en/latest/developer.html#changes
Source0:        https://files.pythonhosted.org/packages/source/p/pycodestyle/pycodestyle-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pycodestyle = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pycodestyle
Summary:        Python style guide checker
%description -n python3-pycodestyle

%prep
%global oreon_srcdir pycodestyle-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pycodestyle usr/lib/python3*/site-packages/pycodestyle* usr/lib64/python3*/site-packages/pycodestyle* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pycodestyle* usr/lib64/python3*/site-packages/pycodestyle* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pycodestyle -f %{oreon_filedir}/python3-pycodestyle.list

%changelog

%autochangelog
