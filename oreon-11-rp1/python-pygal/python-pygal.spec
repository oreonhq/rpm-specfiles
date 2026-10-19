%global source0_hash dd119c14cdeb56beb85282e3e2687ece30561225d410a822e6bb68699aa6e7b1
Name:           python-pygal
Version:        3.1.3
Release:        1%{?dist}
Summary:        A Python svg graph plotting library
License:        LGPL-3.0-or-later
URL:            https://www.pygal.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pygal/pygal-%{version}.tar.gz
BuildArch:      noarch
Patch:              https://github.com/Kozea/pygal/pull/578.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pygal = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygal
Summary:        A Python svg graph plotting library
%description -n python3-pygal

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pygal-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygal usr/lib/python3*/site-packages/pygal* usr/lib64/python3*/site-packages/pygal* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygal* usr/lib64/python3*/site-packages/pygal* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygal -f %{oreon_filedir}/python3-pygal.list

%changelog

%autochangelog
