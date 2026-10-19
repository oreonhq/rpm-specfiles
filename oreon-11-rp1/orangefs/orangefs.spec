%global source0_hash a945e33b824220b6b97d3d036dabea7c56a1392155b86d741d75a55427814d42
%define         _legacy_common_support 1
%global         _hardened_build 1
Name:           orangefs
Version:        2.10.1
Release:        1%{?dist}
Summary:        Parallel network file system client
URL:            https://www.orangefs.org/
License:       LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND Zlib
Source0:        https://github.com/waltligon/orangefs/archive/refs/tags/2.10.1.tar.gz
Source1:       orangefs-server.service
Source2:       orangefs-client.service
Source3:       orangefs.conf
Source4:       pvfs2tab
Patch:         orangefs-genconfig.patch
Patch:         orangefs-lmdb.patch
Patch:         orangefs-no-start-stop.patch
Patch:         orangefs-configure-c99.patch
Patch:         orangefs-2.10.1-disable-ib-exp.patch
%ifnarch armv7hl
%endif
# oreon:deps
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  latex2html
BuildRequires:  libattr-devel
BuildRequires:  libibverbs-devel
BuildRequires:  libselinux-devel
BuildRequires:  lmdb-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  systemd
BuildRequires:  texlive
BuildRequires:  texlive-charter
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips
BuildRequires:  texlive-times
# /oreon:deps
%description
OrangeFS (formerly PVFS2) is a high-performance parallel
network file system designed for use on high performance computing
systems.  It provides very high performance access to disk storage for
parallel applications.  It is accessible through a variety of
interfaces, including the native OrangeFS library, the kernel, FUSE,
and MPI-IO.

This package provides the pvfs2-client-core which is required to use
he kernel module.

%package       server
Summary:       Parallel network file system server
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      perl(Math::BigInt)
%description   server
This package contains the Parallel network file system server

%package       fuse
Summary:       Parallel network file system FUSE client
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   fuse
This package contains the Parallel network file system FUSE client

%package       devel
Summary:       Parallel network file system development libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   devel
This package contains the headers and libraries necessary for client
development of the Parallel network file system

%package       docs
Summary:       Documentation for the  Parallel network file system
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   docs
This package contains documentation of the Parallel network file system

%prep

%autosetup -p1 -n orangefs-%{version}
rm -r src/apps/devel/lmdb
rm -r src/common/lmdb
mv doc/man/pvfs2.conf.5 doc/man/orangefs.conf.5

# autotools
autoupdate -I maint/config
autoreconf -vif -I maint/config

%build

export LDFLAGS="%{optflags} -Wl,--as-needed"
%configure --enable-external-lmdb \
           --enable-shared        \
           --disable-static       \
           --enable-fuse          \
           --disable-usrint-cwd   \
           --with-db-backend=lmdb \
%ifnarch armv7hl
           --with-openib=/usr     \
%endif
           --disable-olib         \
           --with-ib=no           \
           --with-experimental-ib=no
%make_build V=1
make docs V=1
%install
%make_install
mkdir -p %{buildroot}%{_docdir}/orangefs
install -p -m 644 doc/*.pdf %{buildroot}%{_docdir}/orangefs
mkdir -p %{buildroot}%{_docdir}/orangefs/coding
install -p -m 644 doc/coding/*.pdf %{buildroot}%{_docdir}/orangefs/coding
mkdir -p %{buildroot}%{_docdir}/orangefs/design
install -p -m 644 doc/design/*.pdf %{buildroot}%{_docdir}/orangefs/design
mkdir -p %{buildroot}%{_docdir}/orangefs/random
install -p -m 644 doc/random/*.pdf %{buildroot}%{_docdir}/orangefs/random
install -p -m 644 COPYING %{buildroot}%{_docdir}/orangefs
mkdir -p %{buildroot}%{_unitdir}
install  -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sharedstatedir}/orangefs
mkdir -p %{buildroot}%{_sysconfdir}/orangefs
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/orangefs
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n orangefs-server -f %{oreon_filedir}/orangefs-server.list
%files -n orangefs-fuse -f %{oreon_filedir}/orangefs-fuse.list
%files -n orangefs-devel -f %{oreon_filedir}/orangefs-devel.list
%files -n orangefs-docs -f %{oreon_filedir}/orangefs-docs.list

%changelog

%autochangelog
