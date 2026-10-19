%global source0_hash ff6b113f50bc066a698db5d944d2c6dc7507168dd3341e255a8892fd0715a558
Name:           python-propcache
Version:        0.5.4
Release:        1%{?dist}
Summary:        Accelerated property cache
License:        Apache-2.0
URL:            https://matrix.to/#/#aio-libs:matrix.org
Source0:        https://files.pythonhosted.org/packages/source/p/propcache/propcache-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 47
Requires:       python3-propcache = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-propcache
Summary:        Accelerated property cache
%description -n python3-propcache

%prep
%global oreon_srcdir propcache-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-propcache usr/lib/python3*/site-packages/propcache* usr/lib64/python3*/site-packages/propcache* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/propcache* usr/lib64/python3*/site-packages/propcache* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-propcache -f %{oreon_filedir}/python3-propcache.list

%changelog

%autochangelog
