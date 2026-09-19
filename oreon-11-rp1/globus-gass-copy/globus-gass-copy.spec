%global source0_hash f8b301b99de8f236733486767409d952024e16ff44ccfa8627063eefcbc8fe45

Name:		globus-gass-copy
%global _name %(tr - _ <<< %{name})
Version:	10.13
Release:	5%{?dist}
Summary:	Grid Community Toolkit - Globus Gass Copy

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-ftp-client-devel >= 7
BuildRequires:	globus-ftp-control-devel >= 4
BuildRequires:	globus-gsi-sysconfig-devel >= 4
BuildRequires:	globus-gass-transfer-devel >= 7
BuildRequires:	globus-io-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 9
BuildRequires:	globus-gssapi-error-devel >= 4
BuildRequires:	openssl-devel
BuildRequires:	doxygen
#		Additional requirements for make check
BuildRequires:	globus-gridftp-server-devel >= 7
BuildRequires:	globus-gridftp-server-progs >= 7
BuildRequires:	openssl
BuildRequires:	perl-interpreter
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

%package progs
Summary:	Grid Community Toolkit - Globus Gass Copy Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package devel
Summary:	Grid Community Toolkit - Globus Gass Copy Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Globus Gass Copy Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus Gass Copy

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Globus Gass Copy Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus Gass Copy Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus Gass Copy Documentation Files

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
%{_libdir}/libglobus_gass_copy.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_bindir}/globus-url-copy
%doc %{_mandir}/man1/globus-url-copy.1*

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_gass_copy.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
