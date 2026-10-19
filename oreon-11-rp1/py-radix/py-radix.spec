%global source0_hash 969a3bb057d298c9b4dd537d70ce15143089fc20cd896c9f91b044691985b143
Name: py-radix
Summary:        Radix tree data structure for Python
Version: 1.1.0
Release:        1%{?dist}
URL: https://github.com/mjschultz/py-radix
Source0:        https://github.com/mjschultz/py-radix/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1: https://github.com/mjschultz/py-radix/pull/55.patch#/py-radix-0.10.0-py_ssize_t_clean.patch
Patch2: https://github.com/mjschultz/py-radix/pull/44.patch#/py-radix-0.10.0-assertequal.patch
Patch3: https://github.com/mjschultz/py-radix/pull/58.patch#/py-radix-0.10.0-pyobject-type.patch
License: BSD-4-Clause AND ISC
# oreon:deps
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# /oreon:deps
%description
py-radix is an implementation of a radix tree for Python, which
supports storage and lookups of IPv4 and IPv6 networks.

The radix tree (a.k.a Patricia tree) is the data structure most
commonly used for routing table lookups. It efficiently stores
network prefixes of varying lengths and allows fast lookups of
containing networks. py-radix's implementation is built solely
for networks (the data structure itself is more general).

%package -n python3-%{name}
Summary: Radix tree data structure for Python
BuildRequires: python3-devel
BuildRequires: python3-pytest
%description -n python3-%{name}
py-radix is an implementation of a radix tree for Python, which
supports storage and lookups of IPv4 and IPv6 networks.

The radix tree (a.k.a Patricia tree) is the data structure most
commonly used for routing table lookups. It efficiently stores
network prefixes of varying lengths and allows fast lookups of
containing networks. py-radix's implementation is built solely
for networks (the data structure itself is more general).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -f inet_ntop.c strlcpy.c
touch inet_ntop.c strlcpy.c

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-py-radix -f %{oreon_filedir}/python3-py-radix.list

%changelog

%autochangelog
