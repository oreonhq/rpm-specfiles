%global source0_hash 34de77cec1250e0f00a1a50c1b9252c2a1a7fe4768b8d31fb95289d9ebdde991
Name:           python-pdir2
Version:        1.1.2
Release:        1%{?dist}
Summary:        Pretty dir printing with joy
License:        MIT
URL:            https://github.com/laike9m/pdir2
Source0:        https://files.pythonhosted.org/packages/source/p/pdir2/pdir2-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python313.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pdir2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pdir2
Summary:        Pretty dir printing with joy
# oreon:reqs
Requires:       python3dist(typing-extensions) == 4.*
# /oreon:reqs
%description -n python3-pdir2

%prep
%global oreon_srcdir pdir2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pdir2 usr/lib/python3*/site-packages/pdir2* usr/lib64/python3*/site-packages/pdir2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pdir2* usr/lib64/python3*/site-packages/pdir2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pdir2 -f %{oreon_filedir}/python3-pdir2.list

%changelog

%autochangelog
