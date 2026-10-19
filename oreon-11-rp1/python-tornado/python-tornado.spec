%global source0_hash a6b1ccd08c04b4a06fb5aeb381be99de5ad1e5375c1785e31d78c880feb57687
Name:           python-tornado
Version:        6.5.10
Release:        1%{?dist}
Summary:        Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
License:        Apache-2.0
URL:            https://github.com/tornadoweb/tornado
Source0:        https://files.pythonhosted.org/packages/source/t/tornado/tornado-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tornado = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-tornado
Summary:        Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed.
%description -n python3-tornado

%prep
%global oreon_srcdir tornado-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tornado usr/lib/python3*/site-packages/tornado* usr/lib64/python3*/site-packages/tornado* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tornado* usr/lib64/python3*/site-packages/tornado* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tornado -f %{oreon_filedir}/python3-tornado.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.5.2-1
- Prepare for Oreon 11 (RP1)
