%global source0_hash d1f535a6ca4827c087e0a2a173dd74621d6e1688c740c8dd44e0377480020431
Name:           python-tox
Version:        4.61.5
Release:        1%{?dist}
Summary:        tox is a generic virtualenv management and test command line tool
License:        MIT
URL:            https://tox.wiki
Source0:        https://files.pythonhosted.org/packages/source/t/tox/tox-%{version}.tar.gz
BuildArch:      noarch
Patch:          fix-tests.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tox = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tox
Summary:        tox is a generic virtualenv management and test command line tool
%description -n python3-tox

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tox-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tox usr/lib/python3*/site-packages/tox* usr/lib64/python3*/site-packages/tox* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tox* usr/lib64/python3*/site-packages/tox* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tox -f %{oreon_filedir}/python3-tox.list

%changelog

%autochangelog
