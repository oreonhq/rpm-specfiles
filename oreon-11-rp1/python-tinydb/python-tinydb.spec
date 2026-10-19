%global source0_hash 6928b1fa785186bda7952a0ba05aaeedc883ede565ca9c7d608de44e5e75de70
Name:           python-tinydb
Version:        4.9.0
Release:        1%{?dist}
Summary:        TinyDB is a tiny, document oriented database optimized for your happiness :_
License:        MIT
URL:            https://github.com/msiemens/tinydb
Source0:        https://files.pythonhosted.org/packages/source/t/tinydb/tinydb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tinydb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tinydb
Summary:        TinyDB is a tiny, document oriented database optimized for your happiness :_
%description -n python3-tinydb

%prep
%global oreon_srcdir tinydb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tinydb usr/lib/python3*/site-packages/tinydb* usr/lib64/python3*/site-packages/tinydb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tinydb* usr/lib64/python3*/site-packages/tinydb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tinydb -f %{oreon_filedir}/python3-tinydb.list

%changelog

%autochangelog
