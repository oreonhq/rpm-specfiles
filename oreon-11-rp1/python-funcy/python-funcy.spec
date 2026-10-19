%global source0_hash 8979feb3de7120afd1d00e5a8eae810c1942e4bfbc91697151e9ee1e49f79284
Name:           python-funcy
Version:        2.1
Release:        1%{?dist}
Summary:        A fancy and practical functional tools
License:        ...
URL:            https://github.com/Suor/funcy
Source0:        https://files.pythonhosted.org/packages/source/f/funcy/funcy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-funcy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-funcy
Summary:        A fancy and practical functional tools
%description -n python3-funcy

%prep
%global oreon_srcdir funcy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-funcy usr/lib/python3*/site-packages/funcy* usr/lib64/python3*/site-packages/funcy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/funcy* usr/lib64/python3*/site-packages/funcy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-funcy -f %{oreon_filedir}/python3-funcy.list

%changelog

%autochangelog
