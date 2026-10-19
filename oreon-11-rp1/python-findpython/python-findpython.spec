%global source0_hash 53b32264874dfa5990bd09d717819386d8db3149d89fe20f88fe1078de286bae
Name:           python-findpython
Version:        0.8.0
Release:        1%{?dist}
Summary:        A utility to find python versions on your system
License:        MIT
URL:            https://github.com/frostming/findpython
Source0:        https://files.pythonhosted.org/packages/source/f/findpython/findpython-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-findpython = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-findpython
Summary:        A utility to find python versions on your system
# oreon:reqs
Requires:       python3dist(packaging) >= 20
Requires:       python3dist(platformdirs) >= 4.3.6
# /oreon:reqs
%description -n python3-findpython

%prep
%global oreon_srcdir findpython-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-findpython usr/lib/python3*/site-packages/findpython* usr/lib64/python3*/site-packages/findpython* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/findpython* usr/lib64/python3*/site-packages/findpython* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-findpython -f %{oreon_filedir}/python3-findpython.list

%changelog

%autochangelog
