%global source0_hash bd4e6366529841b04ebca98387ccb2e0e07d556739feea1220e7194be20a9a19

Name:		globus-xio-gridftp-driver
%global _name %(tr - _ <<< %{name})
Version:	3.6
Release:	10%{?dist}
Summary:	Grid Community Toolkit - Globus XIO GridFTP Driver

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-ftp-client-devel >= 7
BuildRequires:	globus-xio-gsi-driver-devel >= 2
BuildRequires:	doxygen
BuildRequires:	perl-interpreter
BuildRequires:	perl(strict)
#		Additional requirements for make check
BuildRequires:	globus-gridftp-server-devel >= 7
BuildRequires:	globus-gridftp-server-progs >= 7
BuildRequires:	openssl
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(lib)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

Requires:	globus-xio-gsi-driver%{?_isa} >= 2

%package devel
Summary:	Grid Community Toolkit - Globus XIO GridFTP Driver Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Globus XIO GridFTP Driver Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus XIO GridFTP Driver

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus XIO GridFTP Driver Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Globus XIO GridFTP Driver Documentation Files

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

%check
GLOBUS_HOSTNAME=localhost %make_build check

%ldconfig_scriptlets

%files
# This is a loadable module (plugin)
%{_libdir}/libglobus_xio_gridftp_driver.so
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
%autochangelog
