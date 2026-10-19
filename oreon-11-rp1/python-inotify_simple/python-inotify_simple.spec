%global source0_hash f010bbbd8283bd71a9f4eb2de94765804ede24bd47320b0e6ef4136e541cdc2c
Name:           python-inotify-simple
Version:        2.0.1
Release:        1%{?dist}
Summary:        A simple wrapper around inotify. No fancy bells and whistles, just a literal wrapper with ctypes. Under 100 lines of code!
License:        BSD-2-Clause
URL:            https://github.com/chrisjbillington/inotify_simple.git
Source0:        https://files.pythonhosted.org/packages/source/i/inotify_simple/inotify_simple-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-inotify-simple = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-inotify-simple
Summary:        A simple wrapper around inotify. No fancy bells and whistles, just a literal wrapper with ctypes. Under 100 lines of code!
%description -n python3-inotify-simple

%prep
%global oreon_srcdir inotify_simple-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-inotify-simple usr/lib/python3*/site-packages/inotify_simple* usr/lib64/python3*/site-packages/inotify_simple* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/inotify_simple* usr/lib64/python3*/site-packages/inotify_simple* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-inotify-simple -f %{oreon_filedir}/python3-inotify-simple.list

%changelog

%autochangelog
