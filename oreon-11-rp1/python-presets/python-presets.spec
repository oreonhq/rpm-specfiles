%global source0_hash 8eb49a436c5ddf7109167da7f3c15da7e7c5ca38bd1aae0ff6c013eb92d7c950
Name:           python-presets
Version:        1.0.0
Release:        1%{?dist}
Summary:        A python module to manipulate default parameters of a module_s functions
License:        ISC
URL:            http://github.com/bmcfee/presets
Source0:        https://files.pythonhosted.org/packages/source/p/presets/presets-%{version}.tar.gz
BuildArch:      noarch
Patch0:         importlib.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-presets = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-presets
Summary:        A python module to manipulate default parameters of a module_s functions
%description -n python3-presets

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir presets-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-presets usr/lib/python3*/site-packages/presets* usr/lib64/python3*/site-packages/presets* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/presets* usr/lib64/python3*/site-packages/presets* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-presets -f %{oreon_filedir}/python3-presets.list

%changelog

%autochangelog
