%global source0_hash a969a4516b194895de72c875ece355f17c0d272146f7fda346ef74f93cf4d5ba
Name:           python-aenum
Version:        3.1.17
Release:        1%{?dist}
Summary:        Advanced Enumerations _compatible with Python_s stdlib Enum_, NamedTuples, and NamedConstants
License:        ...
URL:            https://github.com/ethanfurman/aenum
Source0:        https://files.pythonhosted.org/packages/source/a/aenum/aenum-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aenum = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aenum
Summary:        Advanced Enumerations _compatible with Python_s stdlib Enum_, NamedTuples, and NamedConstants
%description -n python3-aenum

%prep
%global oreon_srcdir aenum-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aenum usr/lib/python3*/site-packages/aenum* usr/lib64/python3*/site-packages/aenum* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aenum* usr/lib64/python3*/site-packages/aenum* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aenum -f %{oreon_filedir}/python3-aenum.list

%changelog

%autochangelog
