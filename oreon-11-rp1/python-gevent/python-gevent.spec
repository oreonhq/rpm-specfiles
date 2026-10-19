%global source0_hash 4dd4703d71737a456c1c9df5cd43a82934e5b10c87549caa02495f487d1ef0b1
Name:           python-gevent
Version:        26.9.0
Release:        1%{?dist}
Summary:        Coroutine-based network library
License:        MIT
URL:            https://github.com/gevent/gevent/
Source0:        https://files.pythonhosted.org/packages/source/g/gevent/gevent-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 2.1.1
BuildRequires:  python3dist(cython) >= 3.2.4
BuildRequires:  python3dist(greenlet) >= 3.2.2
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-gevent = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-gevent
Summary:        Coroutine-based network library
%description -n python3-gevent

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir gevent-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gevent usr/lib/python3*/site-packages/gevent* usr/lib64/python3*/site-packages/gevent* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gevent* usr/lib64/python3*/site-packages/gevent* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gevent -f %{oreon_filedir}/python3-gevent.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.9.1-1
- Prepare for Oreon 11 (RP1)
