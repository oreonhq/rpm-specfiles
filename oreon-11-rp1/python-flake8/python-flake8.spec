%global source0_hash fe044858146b9fc69b551a4b490d69cf960fcb78ad1edcb84e7fbb1b4a8e3872
Name:           python-flake8
Version:        7.3.0
Release:        1%{?dist}
Summary:        the modular source code checker: pep8 pyflakes and co
License:        MIT
URL:            https://github.com/pycqa/flake8
Source0:        https://files.pythonhosted.org/packages/source/f/flake8/flake8-%{version}.tar.gz
BuildArch:      noarch
Patch:            Support-Python-3.14.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flake8 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flake8
Summary:        the modular source code checker: pep8 pyflakes and co
%description -n python3-flake8

%prep
%global oreon_srcdir flake8-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flake8 usr/lib/python3*/site-packages/flake8* usr/lib64/python3*/site-packages/flake8* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flake8* usr/lib64/python3*/site-packages/flake8* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flake8 -f %{oreon_filedir}/python3-flake8.list

%changelog

%autochangelog
