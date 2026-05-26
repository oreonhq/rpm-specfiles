%bcond docs %{undefined rhel}

Name:           python-netaddr
Version:        1.3.0
Release:        11%{?dist}
Summary:        A pure Python network address representation and manipulation library

License:        BSD-3-Clause
URL:            https://github.com/netaddr/netaddr
Source0:        https://pypi.python.org/packages/source/n/netaddr/netaddr-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 5c3c3d9895b551b763779ba7db7a03487dc1f8e3b385af819af341ae9ef6e48a
%global source0_file netaddr-1.3.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-issues
BuildRequires:  python3-furo
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

%global _description\
%{desc}

%description %_description

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/netaddr-1.3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5c3c3d9895b551b763779ba7db7a03487dc1f8e3b385af819af341ae9ef6e48a" || { echo "oreon: Source0 SHA256 mismatch for netaddr-1.3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n netaddr-%{version} -p1

# Make rpmlint happy, rip out python shebang lines from most python
# modules
find netaddr -name "*.py" | \
  xargs sed -i -e '1 {/^#!\//d}'

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

#docs
%if %{with docs}
pushd docs
PYTHONPATH='../' sphinx-build-%{python3_version} -b html -d build/doctrees source python3/html
rm -f python3/html/.buildinfo
popd
%endif


%install
%pyproject_install
%pyproject_save_files netaddr

%check
%pytest

%files -n python3-netaddr -f %{pyproject_files}
%license COPYRIGHT.rst
%doc AUTHORS.rst CHANGELOG.rst README.rst THANKS.rst
%if %{with docs}
%doc docs/python3/html
%endif

%files -n python3-netaddr-shell
%{_bindir}/netaddr

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-11
- Prepare for Oreon 11 (RP1)
