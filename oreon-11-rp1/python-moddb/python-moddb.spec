%global source0_hash 1f561aae2de737bb70f113178dae2bfd1c3a58864499b786e0b7c216668e89c4
Name:           python-moddb
Version:        0.15.0
Release:        1%{?dist}
Summary:        A scrapper for ModDB Mod and Game pages
License:        ...
URL:            https://github.com/ClementJ18/moddb
Source0:        https://files.pythonhosted.org/packages/source/m/moddb/moddb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-moddb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-moddb
Summary:        A scrapper for ModDB Mod and Game pages
%description -n python3-moddb

%prep
%global oreon_srcdir moddb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-moddb usr/lib/python3*/site-packages/moddb* usr/lib64/python3*/site-packages/moddb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/moddb* usr/lib64/python3*/site-packages/moddb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-moddb -f %{oreon_filedir}/python3-moddb.list

%changelog

%autochangelog
