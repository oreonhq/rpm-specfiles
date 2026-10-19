%global source0_hash 902bd9a95a12f195f15753a1080075d4eca7a2cb934fac7ac03c9e362b50796a
Name:           python-interface-meta
Version:        2.0.1
Release:        1%{?dist}
Summary:        _interface_meta_ provides a convenient way to expose an extensible API with enforced method signatures and consistent documentation.
License:        MIT
URL:            https://github.com/matthewwardrop/interface_meta
Source0:        https://files.pythonhosted.org/packages/source/i/interface_meta/interface_meta-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-interface-meta = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-interface-meta
Summary:        _interface_meta_ provides a convenient way to expose an extensible API with enforced method signatures and consistent documentation.
%description -n python3-interface-meta

%prep
%global oreon_srcdir interface_meta-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-interface-meta usr/lib/python3*/site-packages/interface_meta* usr/lib64/python3*/site-packages/interface_meta* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/interface_meta* usr/lib64/python3*/site-packages/interface_meta* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-interface-meta -f %{oreon_filedir}/python3-interface-meta.list

%changelog

%autochangelog
