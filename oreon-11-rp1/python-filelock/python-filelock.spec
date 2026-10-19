%global source0_hash da5915714a70b55d167fdc7e251ad91302b0a36816fb574dfafae8f4f2c9bb21
Name:           python-filelock
Version:        4.0.7
Release:        1%{?dist}
Summary:        A platform independent file lock.
License:        MIT
URL:            https://github.com/tox-dev/py-filelock
Source0:        https://files.pythonhosted.org/packages/source/f/filelock/filelock-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) >= 0.5
BuildRequires:  python3dist(hatchling) >= 1.29
Requires:       python3-filelock = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-filelock
Summary:        A platform independent file lock.
%description -n python3-filelock

%prep
%global oreon_srcdir filelock-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-filelock usr/lib/python3*/site-packages/filelock* usr/lib64/python3*/site-packages/filelock* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/filelock* usr/lib64/python3*/site-packages/filelock* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-filelock -f %{oreon_filedir}/python3-filelock.list

%changelog

%autochangelog
