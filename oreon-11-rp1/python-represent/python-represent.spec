%global source0_hash 403daa7f8360390b84b143b7bf1dd720965a3e93a234994923c7123cc55d5fe1
Name:           python-represent
Version:        2.2.0
Release:        1%{?dist}
Summary:        Create __repr__ automatically or declaratively.
License:        MIT
URL:            https://github.com/RazerM/represent
Source0:        https://files.pythonhosted.org/packages/source/r/represent/represent-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-represent = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-represent
Summary:        Create __repr__ automatically or declaratively.
%description -n python3-represent

%prep
%global oreon_srcdir represent-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-represent usr/lib/python3*/site-packages/represent* usr/lib64/python3*/site-packages/represent* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/represent* usr/lib64/python3*/site-packages/represent* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-represent -f %{oreon_filedir}/python3-represent.list

%changelog

%autochangelog
