%global source0_hash ac174808dbf61d35d9da804bf33baac74bc6f2be0c108594ae93c79cd15ddc36
Name:           python-xkbcommon
Version:        1.5.1
Release:        1%{?dist}
Summary:        Bindings for libxkbcommon using cffi
License:        MIT
URL:            https://github.com/sde1000/python-xkbcommon
Source0:        https://files.pythonhosted.org/packages/source/x/xkbcommon/xkbcommon-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45.0
Requires:       python3-xkbcommon = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xkbcommon
Summary:        Bindings for libxkbcommon using cffi
%description -n python3-xkbcommon

%prep
%global oreon_srcdir xkbcommon-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xkbcommon usr/lib/python3*/site-packages/xkbcommon* usr/lib64/python3*/site-packages/xkbcommon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xkbcommon* usr/lib64/python3*/site-packages/xkbcommon* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xkbcommon -f %{oreon_filedir}/python3-xkbcommon.list

%changelog

%autochangelog
