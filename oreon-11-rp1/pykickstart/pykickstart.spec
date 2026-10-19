%global source1_hash d3f1b4657120a5054f47280826c8724e08906b08ba70402bd3eba79c524f5ffd
%global source0_hash f9752920e48408a21588cf734a49cab6f4bdf7ab80c3262099a775bc9abb1895
%bcond_without runtests
%bcond_with signed
Name:      pykickstart
Version:   3.78
Release:        1%{?dist}
License:   GPL-2.0-only
Summary:        Python utilities for manipulating kickstart files.
Url:       http://fedoraproject.org/wiki/pykickstart
Source0:        https://github.com/pykickstart/%{name}/releases/download/r%{version}/%{name}-%{version}.tar.gz
%if %{with signed}
Source1:        https://github.com/pykickstart/%{name}/releases/download/r%{version}/%{name}-%{version}.tar.gz.asc
%endif
BuildArch: noarch
%if %{with runtests}
%endif
Requires: python3-kickstart = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description
Python utilities for manipulating kickstart files.

%package -n python3-kickstart
Summary:  Python 3 library for manipulating kickstart files.
Requires: python3-requests
%description -n python3-kickstart
Python 3 library for manipulating kickstart files.  The binaries are found in
the pykickstart package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

make PYTHON=%{__python3}
%install
make PYTHON=%{__python3} DESTDIR=%{buildroot} install
%oreon_autofiles python3-kickstart usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with runtests}
LC_ALL=C make PYTHON=%{__python3} test-no-coverage
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-kickstart -f %{oreon_filedir}/python3-kickstart.list

%changelog

%autochangelog
