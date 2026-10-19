%global source0_hash eb49a0f6862f7e75df4a40107f1c8c267cf8adfbd6d29a0dac29d17ac188c878
Name:           python-pebble
Version:        5.2.2
Release:        1%{?dist}
Summary:        Threading and multiprocessing eye-candy.
License:        ...
URL:            https://github.com/noxdafox/pebble
Source0:        https://files.pythonhosted.org/packages/source/p/pebble/pebble-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pebble = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pebble
Summary:        Threading and multiprocessing eye-candy.
%description -n python3-pebble

%prep
%global oreon_srcdir pebble-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pebble usr/lib/python3*/site-packages/pebble* usr/lib64/python3*/site-packages/pebble* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pebble* usr/lib64/python3*/site-packages/pebble* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pebble -f %{oreon_filedir}/python3-pebble.list

%changelog

%autochangelog
