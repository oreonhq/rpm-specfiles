%global source0_hash eb1a594161c84a4e67df7db1c269a3392a645bd50e4c82e1298892db0cdb0965
Name:           python-pyspellchecker
Version:        0.9.0
Release:        1%{?dist}
Summary:        Pure python spell checker based on work by Peter Norvig
License:        MIT
URL:            https://github.com/barrust/pyspellchecker
Source0:        https://files.pythonhosted.org/packages/source/p/pyspellchecker/pyspellchecker-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-pyspellchecker = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyspellchecker
Summary:        Pure python spell checker based on work by Peter Norvig
%description -n python3-pyspellchecker

%prep
%global oreon_srcdir pyspellchecker-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyspellchecker usr/lib/python3*/site-packages/pyspellchecker* usr/lib64/python3*/site-packages/pyspellchecker* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyspellchecker* usr/lib64/python3*/site-packages/pyspellchecker* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyspellchecker -f %{oreon_filedir}/python3-pyspellchecker.list

%changelog

%autochangelog
