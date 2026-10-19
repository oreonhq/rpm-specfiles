%global source0_hash 6e8512fb86523ada1f94fd1b14e280f924e379064bb8a29ee399950e513eeccd
Name:           python-expecttest
Version:        0.3.0
Release:        1%{?dist}
Summary:        ...
License:        MIT
URL:            https://github.com/ezyang/expecttest
Source0:        https://files.pythonhosted.org/packages/source/e/expecttest/expecttest-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-expecttest = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-expecttest
Summary:        ...
%description -n python3-expecttest

%prep
%global oreon_srcdir expecttest-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-expecttest usr/lib/python3*/site-packages/expecttest* usr/lib64/python3*/site-packages/expecttest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/expecttest* usr/lib64/python3*/site-packages/expecttest* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-expecttest -f %{oreon_filedir}/python3-expecttest.list

%changelog

%autochangelog
