%global source0_hash 1e117ee4574366a2d7376b8c858433ad724b0a29e4036d9f1a9fda4372180267
Name:           python-androguard
Version:        4.1.4
Release:        1%{?dist}
Summary:        Androguard is a full python tool to play with Android files.
License:        ...
URL:            https://github.com/androguard/androguard
Source0:        https://files.pythonhosted.org/packages/source/a/androguard/androguard-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-androguard = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-androguard
Summary:        Androguard is a full python tool to play with Android files.
%description -n python3-androguard

%prep
%global oreon_srcdir androguard-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-androguard usr/lib/python3*/site-packages/androguard* usr/lib64/python3*/site-packages/androguard* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/androguard* usr/lib64/python3*/site-packages/androguard* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-androguard -f %{oreon_filedir}/python3-androguard.list

%changelog

%autochangelog
