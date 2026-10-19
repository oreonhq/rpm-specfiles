%global source0_hash 992de8d1d6c1a0c4edccd798084b6a7f8b93155ba7ae110d836dc248a2f7005a
Name:		globus-io
%global _name %(tr - _ <<< %{name})
Version:	12.4
Release:        10%{?dist}
Summary:        Grid Community Toolkit - uniform I/O interface
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
Requires:	globus-xio-gsi-driver%{?_isa} >= 2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-error-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  globus-xio-devel
BuildRequires:  globus-xio-gsi-driver-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl-interpreter
# /oreon:deps
%package devel
Summary:	Grid Community Toolkit - uniform I/O interface Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
uniform I/O interface to stream and datagram style communications

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
uniform I/O interface Development Files

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build

export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

GLOBUS_HOSTNAME=localhost %make_build check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n globus-io-devel -f %{oreon_filedir}/globus-io-devel.list

%changelog

%autochangelog
