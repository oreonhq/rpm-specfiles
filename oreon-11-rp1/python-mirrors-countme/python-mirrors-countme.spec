%global source0_hash f2a01c8c3009ec635476af431991f6c1c785d6a5f53eb1da2f3646f455cc89a6
Name:           python-mirrors-countme
Version:        0.1.5
Release:        1%{?dist}
Summary:        Parse access logs and count hosts for DNF mirrors
License:        GPL-3.0-or-later
URL:            http://github.com/fedora-infra/mirrors-countme
Source0:        https://files.pythonhosted.org/packages/source/m/mirrors_countme/mirrors_countme-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mirrors-countme = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mirrors-countme
Summary:        Parse access logs and count hosts for DNF mirrors
%description -n python3-mirrors-countme

%prep
%global oreon_srcdir mirrors_countme-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mirrors-countme usr/lib/python3*/site-packages/mirrors_countme* usr/lib64/python3*/site-packages/mirrors_countme* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mirrors_countme* usr/lib64/python3*/site-packages/mirrors_countme* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mirrors-countme -f %{oreon_filedir}/python3-mirrors-countme.list

%changelog

%autochangelog
