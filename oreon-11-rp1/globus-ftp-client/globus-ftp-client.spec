%global source0_hash 3ac4c2f9a50bed8e17b590c37363110c7b34bb44bb4dd356dca7cc6273c87db6

Name:		globus-ftp-client
%global _name %(tr - _ <<< %{name})
Version:	9.9
Release:	2%{?dist}
Summary:	Grid Community Toolkit - GridFTP Client Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-ftp-control-devel >= 4
BuildRequires:	globus-gsi-callback-devel >= 4
BuildRequires:	globus-gsi-credential-devel >= 5
BuildRequires:	globus-gsi-sysconfig-devel >= 5
BuildRequires:	globus-gssapi-gsi-devel >= 10
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-xio-popen-driver-devel >= 2
BuildRequires:	openssl-devel
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	globus-gridftp-server-devel >= 7
BuildRequires:	globus-gridftp-server-progs >= 7
BuildRequires:	openssl
BuildRequires:	perl-interpreter
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(lib)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)

Requires:	globus-xio-popen-driver%{?_isa} >= 2

%package devel
Summary:	Grid Community Toolkit - GridFTP Client Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - GridFTP Client Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GridFTP Client Library

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GridFTP Client Library Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
GridFTP Client Library Documentation Files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

export GLOBUS_VERSION=6.2
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

%check
GLOBUS_HOSTNAME=localhost %make_build check

%ldconfig_scriptlets

%files
%{_libdir}/libglobus_ftp_client.so.*
%dir %{_datadir}/globus
%{_datadir}/globus/gridftp-ssh
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_ftp_client.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
