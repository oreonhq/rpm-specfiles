%global source0_hash 2362b685633caeaf45b9951a9b76ce359cd3581dd515b430c6c3f5dfb4d92a8c
Name:           python-codecov
Version:        2.1.13
Release:        1%{?dist}
Summary:        Hosted coverage reports for GitHub, Bitbucket and Gitlab
License:        ...
URL:            https://github.com/codecov/codecov-python
Source0:        https://files.pythonhosted.org/packages/source/c/codecov/codecov-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-codecov-rm-python-mock-usage.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-codecov = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-codecov
Summary:        Hosted coverage reports for GitHub, Bitbucket and Gitlab
%description -n python3-codecov

%prep
%global oreon_srcdir codecov-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-codecov usr/lib/python3*/site-packages/codecov* usr/lib64/python3*/site-packages/codecov* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/codecov* usr/lib64/python3*/site-packages/codecov* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-codecov -f %{oreon_filedir}/python3-codecov.list

%changelog

%autochangelog
