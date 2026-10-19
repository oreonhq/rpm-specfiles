%global source0_hash 571930928b11e43db690073ad8228162eca8a3f8fd3a87acdeae07df7dd57068
Name:           python-virtualenv
Version:        21.14.2
Release:        1%{?dist}
Summary:        Virtual Python Environment builder
License:        MIT
URL:            https://github.com/pypa/virtualenv
Source0:        https://files.pythonhosted.org/packages/source/v/virtualenv/virtualenv-%{version}.tar.gz
BuildArch:      noarch
Patch:          rpm-wheels.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-vcs) >= 0.4
BuildRequires:  python3dist(hatchling) < 1.28
BuildRequires:  python3dist(hatchling) >= 1.27
BuildRequires:  python3dist(hatchling) >= 1.28
Requires:       python3-virtualenv = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-virtualenv
Summary:        Virtual Python Environment builder
# oreon:reqs
Requires:       python3dist(distlib) < 1
Requires:       python3dist(distlib) >= 0.3.7
Requires:       python3dist(filelock) < 5
Requires:       python3dist(filelock) <= 3.19.1
Requires:       python3dist(filelock) >= 3.16.1
Requires:       python3dist(filelock) >= 3.24.2
Requires:       python3dist(packaging) >= 23.1
Requires:       python3dist(platformdirs) < 5
Requires:       python3dist(platformdirs) >= 3.9.1
Requires:       python3dist(python-discovery) >= 1.6
Requires:       python3dist(typing-extensions) >= 4.13.2
# /oreon:reqs
%description -n python3-virtualenv

%prep
%global oreon_srcdir virtualenv-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-virtualenv usr/lib/python3*/site-packages/virtualenv* usr/lib64/python3*/site-packages/virtualenv* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/virtualenv* usr/lib64/python3*/site-packages/virtualenv* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-virtualenv -f %{oreon_filedir}/python3-virtualenv.list

%changelog

%autochangelog
