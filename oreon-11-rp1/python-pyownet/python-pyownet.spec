%global source0_hash 4f2fa4471c2f806b35090bdc6c092305c6eded3ff3736f8b586d35bdb157de62
Name:		python-pyownet
Version:	0.10.0.post1
Release:        1%{?dist}
Summary:        Pure python client library for accessing OWFS via owserver protocol
License:	LGPL-3.0-or-later
URL:		https://github.com/miccoli/pyownet
Source0:        https://files.pythonhosted.org/packages/source/p/pyownet/pyownet-%{version}.tar.gz
Patch0:		python-pyownet-001-declarative-build.patch
Patch1:		python-pyownet-002-remove-www.google.com-from-tests.patch
Patch2:		python-pyownet-003-2to3.patch
Patch3:		python-pyownet-004-pyproject-remove-pin-on-setuptools.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyownet = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pyownet
Summary:	Pure python client library for accessing OWFS via owserver protocol
%description -n python3-pyownet

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyownet-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyownet usr/lib/python3*/site-packages/pyownet* usr/lib64/python3*/site-packages/pyownet* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyownet* usr/lib64/python3*/site-packages/pyownet* usr/bin/*

%check

%pytest
%files
%files -n python3-pyownet -f %{oreon_filedir}/python3-pyownet.list

%changelog

%autochangelog
