%global source0_hash 0895cfa3b5531fc65fe439c05eb65144f123bf7a394fcaa56aa423548d8e45c0
Name:           python-hpack
Version:        4.2.0
Release:        1%{?dist}
Summary:        Pure-Python HPACK header encoding
License:        MIT
URL:            https://github.com/python-hyper/hpack/
Source0:        https://files.pythonhosted.org/packages/source/h/hpack/hpack-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82
BuildRequires:  python3dist(wheel) >= 0.46.3
Requires:       python3-hpack = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-hpack
Summary:        Pure-Python HPACK header encoding
%description -n python3-hpack

%prep
%global oreon_srcdir hpack-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hpack usr/lib/python3*/site-packages/hpack* usr/lib64/python3*/site-packages/hpack* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hpack* usr/lib64/python3*/site-packages/hpack* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-hpack -f %{oreon_filedir}/python3-hpack.list

%changelog

%autochangelog
