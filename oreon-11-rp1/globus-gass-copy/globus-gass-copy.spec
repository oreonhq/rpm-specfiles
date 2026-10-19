%global source0_hash f8b301b99de8f236733486767409d952024e16ff44ccfa8627063eefcbc8fe45
Name:		globus-gass-copy
%global _name %(tr - _ <<< %{name})
Version:	10.13
Release:        5%{?dist}
Summary:        Grid Community Toolkit - Globus Gass Copy
License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source0:        https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-ftp-client-devel
BuildRequires:  globus-ftp-control-devel
BuildRequires:  globus-gass-transfer-devel
BuildRequires:  globus-gridftp-server-devel
BuildRequires:  globus-gridftp-server-progs
BuildRequires:  globus-gsi-sysconfig-devel
BuildRequires:  globus-gssapi-error-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  globus-io-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-interpreter
# /oreon:deps
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

export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"
export GLOBUS_VERSION=6.2
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

GLOBUS_HOSTNAME=localhost %make_build check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n globus-gass-copy-progs -f %{oreon_filedir}/globus-gass-copy-progs.list
%files -n globus-gass-copy-devel -f %{oreon_filedir}/globus-gass-copy-devel.list
%files -n globus-gass-copy-doc -f %{oreon_filedir}/globus-gass-copy-doc.list

%changelog

%autochangelog
