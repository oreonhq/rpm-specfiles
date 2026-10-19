%global source0_hash e388c86203532e3934ffc64a2128835288b8209d82bca4f8f73ce0adef9795ff
Name:           python-exabgp
Version:        5.0.13
Release:        1%{?dist}
Summary:        BGP swiss army knife
License:        BSD-3-Clause
URL:            https://github.com/Exa-Networks/exabgp
Source0:        https://files.pythonhosted.org/packages/source/e/exabgp/exabgp-%{version}.tar.gz
BuildArch:      noarch
Patch0100:      0100-Adjust-python-versions.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-exabgp = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-exabgp
Summary:        BGP swiss army knife
%description -n python3-exabgp

%prep
%global oreon_srcdir exabgp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-exabgp usr/lib/python3*/site-packages/exabgp* usr/lib64/python3*/site-packages/exabgp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/exabgp* usr/lib64/python3*/site-packages/exabgp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-exabgp -f %{oreon_filedir}/python3-exabgp.list

%changelog

%autochangelog
