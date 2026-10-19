%global source0_hash 3d7e980292bb0107abaa79c68dd3eee3c561b83a0f89ae482860b181c8bd412d
Name:           python-questionary
Version:        2.1.1
Release:        1%{?dist}
Summary:        Python library to build pretty command line user prompts ⭐️
License:        MIT
URL:            https://github.com/tmbo/questionary
Source0:        https://files.pythonhosted.org/packages/source/q/questionary/questionary-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-questionary = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-questionary
Summary:        Python library to build pretty command line user prompts ⭐️
%description -n python3-questionary

%prep
%global oreon_srcdir questionary-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-questionary usr/lib/python3*/site-packages/questionary* usr/lib64/python3*/site-packages/questionary* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/questionary* usr/lib64/python3*/site-packages/questionary* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-questionary -f %{oreon_filedir}/python3-questionary.list

%changelog

%autochangelog
