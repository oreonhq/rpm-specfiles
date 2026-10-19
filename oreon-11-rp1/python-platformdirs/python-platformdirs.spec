%global source0_hash eab5f70271a490ef74618bb314fbb86e3c7e82fa3b9c922c2ea0e0a1a155d329
Name:           python-platformdirs
Version:        4.12.2
Release:        1%{?dist}
Summary:        A small Python package for determining appropriate platform-specific dirs, e.g. a _user data dir_.
License:        MIT
URL:            https://github.com/tox-dev/platformdirs
Source0:        https://files.pythonhosted.org/packages/source/p/platformdirs/platformdirs-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) >= 0.5
BuildRequires:  python3dist(hatchling) >= 1.29
Requires:       python3-platformdirs = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-platformdirs
Summary:        A small Python package for determining appropriate platform-specific dirs, e.g. a _user data dir_.
%description -n python3-platformdirs

%prep
%global oreon_srcdir platformdirs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-platformdirs usr/lib/python3*/site-packages/platformdirs* usr/lib64/python3*/site-packages/platformdirs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/platformdirs* usr/lib64/python3*/site-packages/platformdirs* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-platformdirs -f %{oreon_filedir}/python3-platformdirs.list

%changelog

%autochangelog
