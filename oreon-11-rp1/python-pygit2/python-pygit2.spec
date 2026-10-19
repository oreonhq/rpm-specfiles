%global source0_hash 36dff84d237f2b8f18b0b146d6e7c3f99a7bce2da98cc4103a14387f53319f95
Name:           python-pygit2
Version:        1.20.1
Release:        1%{?dist}
Summary:        Python bindings for libgit2.
License:        ...
URL:            https://www.pygit2.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pygit2/pygit2-%{version}.tar.gz
Patch:          python-pygit2-network-tests.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 2.0
Requires:       python3-pygit2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygit2
Summary:        Python bindings for libgit2.
%description -n python3-pygit2

%prep
%global oreon_srcdir pygit2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygit2 usr/lib/python3*/site-packages/pygit2* usr/lib64/python3*/site-packages/pygit2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygit2* usr/lib64/python3*/site-packages/pygit2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygit2 -f %{oreon_filedir}/python3-pygit2.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.19.1-1
- Prepare for Oreon 11 (RP1)
