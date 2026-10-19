%global source0_hash 5c3c3d9895b551b763779ba7db7a03487dc1f8e3b385af819af341ae9ef6e48a
%bcond docs %{undefined rhel}
Name:           python-netaddr
Version:        1.3.0
Release:        11%{?dist}
Summary:        A pure Python network address representation and manipulation library
License:        BSD-3-Clause
URL:            https://github.com/netaddr/netaddr
Source0:        https://pypi.python.org/packages/source/n/netaddr/netaddr-%{version}.tar.gz
BuildArch:      noarch
%if %{with docs}
%endif
%global desc A network address manipulation library for Python\
\
Provides support for:\
\
Layer 3 addresses\
\
 * IPv4 and IPv6 addresses, subnets, masks, prefixes\
 * iterating, slicing, sorting, summarizing and classifying IP networks\
 * dealing with various ranges formats (CIDR, arbitrary ranges and globs, nmap)\
 * set based operations (unions, intersections etc) over IP addresses and\
   subnets\
 * parsing a large variety of different formats and notations\
 * looking up IANA IP block information\
 * generating DNS reverse lookups\
 * supernetting and subnetting\
\
Layer 2 addresses\
\
 * representation and manipulation MAC addresses and EUI-64 identifiers\
 * looking up IEEE organisational information (OUI, IAB)\
 * generating derived IPv6 addresses
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-netaddr = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-netaddr
Summary: A pure Python network address representation and manipulation library
%description -n python3-netaddr
%{desc}

%package -n python3-netaddr-shell
Summary: An interactive shell environment for the netaddr library
Requires:  python3-netaddr = %{version}-%{release}
%description -n python3-netaddr-shell
An interactive shell environment for the netaddr library

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n netaddr-%{version} -p1

# Make rpmlint happy, rip out python shebang lines from most python
# modules
find netaddr -name "*.py" | \
  xargs sed -i -e '1 {/^#!\//d}'

%build

%pyproject_wheel
%if %{with docs}
pushd docs
PYTHONPATH='../' sphinx-build-%{python3_version} -b html -d build/doctrees source python3/html
rm -f python3/html/.buildinfo
popd
%endif
%install
%pyproject_install
%oreon_autofiles python3-netaddr usr/lib/python3*/site-packages/netaddr* usr/lib64/python3*/site-packages/netaddr* usr/bin/*
%oreon_autofiles python3-netaddr-shell usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/netaddr* usr/lib64/python3*/site-packages/netaddr* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-netaddr -f %{oreon_filedir}/python3-netaddr.list
%files -n python3-netaddr-shell -f %{oreon_filedir}/python3-netaddr-shell.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-11
- Prepare for Oreon 11 (RP1)
