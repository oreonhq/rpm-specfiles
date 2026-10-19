%global source0_hash d39cfd15c1a1c3bd4d705c82252fa9edb8e4f5e8cc039f8e39afac7b1b47e92c
Name:           python-boltons
Version:        26.2.0
Release:        1%{?dist}
Summary:        When they_re not builtins, they_re boltons.
License:        ...
URL:            https://github.com/mahmoud/boltons
Source0:        https://files.pythonhosted.org/packages/source/b/boltons/boltons-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-boltons = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-boltons
Summary:        When they_re not builtins, they_re boltons.
%description -n python3-boltons

%prep
%global oreon_srcdir boltons-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-boltons usr/lib/python3*/site-packages/boltons* usr/lib64/python3*/site-packages/boltons* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/boltons* usr/lib64/python3*/site-packages/boltons* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-boltons -f %{oreon_filedir}/python3-boltons.list

%changelog

%autochangelog
