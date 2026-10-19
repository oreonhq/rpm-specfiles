%global source0_hash dc14867ed15b4529d6e69b1d07df3fb29c91ccf7ab174de3f9100b90a95cc826
Name:           python-aw-core
Version:        0.5.18
Release:        1%{?dist}
Summary:        Core library for ActivityWatch
License:        MPL-2.0
URL:            https://activitywatch.net/
Source0:        https://files.pythonhosted.org/packages/source/a/aw_core/aw_core-%{version}.tar.gz
BuildArch:      noarch
Patch:          https://github.com/ActivityWatch/aw-core/pull/127.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aw-core = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aw-core
Summary:        Core library for ActivityWatch
%description -n python3-aw-core

%prep
%global oreon_srcdir aw_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aw-core usr/lib/python3*/site-packages/aw_core* usr/lib64/python3*/site-packages/aw_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aw_core* usr/lib64/python3*/site-packages/aw_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aw-core -f %{oreon_filedir}/python3-aw-core.list

%changelog

%autochangelog
