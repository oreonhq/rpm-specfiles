%global source0_hash 2ddd32fd6343ec9b6ed0da729b212362d0e6b1208c0162633c90cb6f94a05877
Name:           python-knack
Version:        0.14.0
Release:        1%{?dist}
Summary:        A Command-Line Interface framework
License:        MIT
URL:            https://github.com/microsoft/knack
Source0:        https://files.pythonhosted.org/packages/source/k/knack/knack-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-knack = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-knack
Summary:        A Command-Line Interface framework
%description -n python3-knack

%prep
%global oreon_srcdir knack-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-knack usr/lib/python3*/site-packages/knack* usr/lib64/python3*/site-packages/knack* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/knack* usr/lib64/python3*/site-packages/knack* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-knack -f %{oreon_filedir}/python3-knack.list

%changelog

%autochangelog
