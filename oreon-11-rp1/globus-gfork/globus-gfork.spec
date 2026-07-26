%global source0_hash db473317e2a74beaedbbf1a3ff581b3ef3ab0b18d3af2590c793b8caddcf89d3

Name:		globus-gfork
%global _name %(tr - _ <<< %{name})
Version:	5.0
Release:	19%{?dist}
Summary:	Grid Community Toolkit - GFork

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-xio-devel >= 3

%package progs
Summary:	Grid Community Toolkit - GFork Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package devel
Summary:	Grid Community Toolkit - GFork Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GFork Library

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
GFork Programs - GFork is user configurable super-server daemon very similar
to xinetd. It listens on a TCP port. When clients connect to a port it runs an
administrator defined program which services that client connection, just as
x/inetd do.

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GFork Development Files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

# Add empty default configuration file
mkdir -p %{buildroot}%{_sysconfdir}
echo "# This is the default gfork configuration file" > \
  %{buildroot}%{_sysconfdir}/gfork.conf

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_gfork.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_sbindir}/gfork
%config(noreplace) %{_sysconfdir}/gfork.conf
%doc %{_pkgdocdir}/README.txt

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gfork.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
