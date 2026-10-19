%global source0_hash af0a5035f3f3df876ca15aea13486bfed6b3ef5409dee016db0be67755c35fcc
%bcond_without  php
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh8)}
%{!?tcl_sitearch: %global tcl_sitearch %{_prefix}/%{_lib}/tcl%{tcl_version}}
Name:		owfs
Version:	3.2p4
Release:        1%{?dist}
Summary:        1-Wire Virtual File System
License:	GPL-2.0-only
URL:		http://www.owfs.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	owserver.xml
Patch0:		owfs-0001-install-into-vendor-perl-directories.patch
Patch1: 	owfs-configure-c99.patch
Patch2:		owfs-0002-configure-deal-with-colons-in-TCL_PACKAGE_PATH.patch
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  firewalld-filesystem
BuildRequires:  fuse-devel
BuildRequires:  libftdi-devel
BuildRequires:  libtool
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  php-devel
BuildRequires:  swig
BuildRequires:  systemd
BuildRequires:  tcl8-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
OWFS is a user-space virtual file-system providing access to 1-Wire networks.

%package libs
Summary: Core library providing base functions to other OWFS modules
Requires: libusb-compat-0.1
Requires: libftdi
BuildRequires: automake autoconf libtool
BuildRequires: libusb-compat-0.1-devel libusb1-devel
%description libs
%{name}-libs is a core library providing base functions to other OWFS modules.

%package capi
Summary: C-API to develop third-part applications which access 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description capi
%{name}-capi library on top of libow providing an easy API to develop third-party
applications to access to 1-Wire networks.

%package devel
Summary: Files for development of OWFS applications
Requires: %{name}-libs%{?_isa} = %{version}
Requires: %{name}-capi%{?_isa} = %{version}
%description devel
This package contains the libraries and header files that are needed for
developing OWFS applications.

%package ownet
Summary: C-API to develop third-part applications which access 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description ownet
%{name}-ownet library provides an easy API to develop third-party applications
to access to 1-Wire networks. It doesn't depend on owlib, and only supports
remote-server connections. This library doesn't include any 1-wire adapter
support, except server connections.

%package fs
Summary: Virtual file-system on top of %{name}-libs providing access to 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: fuse >= 1.0
Requires: %{name}-server
BuildRequires: fuse-devel >= 1.0
%description fs
%{name}-fs is a virtual file-system on top of %{name}-libs providing
access to 1-Wire networks.

%package httpd
Summary: HTTP daemon providing access to 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-server
%description httpd
%{name}-httpd is a HTTP daemon on top of %{name} providing
access to 1-Wire networks.

%package ftpd
Summary: FTP daemon providing access to 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-server
%description ftpd
%{name}-ftpd is a FTP daemon on top of %{name} providing access to 1-Wire networks.

%package server
Summary: Back-end server (daemon) for 1-wire control
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: firewalld-filesystem
BuildRequires: firewalld-filesystem
BuildRequires: libftdi-devel
%description server
%{name}-server is the back-end component of the OWFS 1-wire bus control system.
owserver arbitrates access to the bus from multiple client processes. The
physical bus is usually connected to a serial or USB port, and other processes
connect to owserver over network sockets (TCP port). Communication can be local
or over a network.

%package tap
Summary: Packet sniffer for the owserver protocol
Requires: tcl >= 8.1
Requires: %{name}-tcl%{?_isa} = %{version}-%{release}
BuildRequires: zlib-devel
%description tap
%{name}-tap is a packet sniffer for the owserver protocol

%package mon
Summary: Statistics and settings monitor for owserver
Requires: tcl >= 8.1
Requires: %{name}-tcl%{?_isa} = %{version}-%{release}
%description mon
%{name}-mon is a graphical monitor of owserver’s status

%if %{with php}
%package php
Summary: PHP interface for the 1-wire file-system
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Requires: php-cli >= 4.3.0
BuildRequires: swig
BuildRequires: php-devel >= 4.3.0
%description php
%{name}-php is a php interface for the 1-wire file-system
%endif

%package tcl
Summary: Tcl interface for the 1-wire file-system
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: tcl >= 8.1
BuildRequires: tcl8-devel >= 8.1
%description tcl
%{name}-tcl is a Tcl interface for the 1-wire file-system

%package shell
License: MIT
Summary: Light weight shell access to owserver and the 1-wire file-system
%description shell
%{name}-shell is 5 small programs to easily access owserver (and thus
the 1-wire system) from shell scripts. owdir, owread, owwrite, owget
and owpresent.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i -e 's/) Makefile.PL/& INSTALLDIRS=vendor/' \
	module/swig/perl5/Makefile.am \
	module/ownet/perl5/Makefile.am

# Create a sysusers.d config file
cat >owfs.sysusers.conf <<EOF
u ow - '1-wire file-system (OWFS) utilities account' /var/empty -
EOF

%build

./bootstrap
%configure --disable-rpath \
%if %{without php}
  --disable-owphp \
%endif
  --disable-owperl
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
rm -f %{buildroot}%{perl_archlib}/auto/OW/.packlist
rm -f %{buildroot}%{perl_archlib}/auto/OWNet/.packlist
rm -f %{buildroot}%{_libdir}/libow.la
rm -f %{buildroot}%{_libdir}/libowcapi.la
rm -f %{buildroot}%{_libdir}/libownet.la
rm -f %{buildroot}%{php_extdir}/libowphp.la
rm -f %{buildroot}%{tcl_sitearch}/ow.la
rm -f %{buildroot}/usr/local/lib64/perl5/auto/OWNet/.packlist
install -Dm 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/owserver.xml
install -m0644 -D owfs.sysusers.conf %{buildroot}%{_sysusersdir}/owfs.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post fs

%systemd_post owfs.service
%post httpd

%systemd_post owhttpd.service
%post ftpd

%systemd_post owftpd.service
%post server

%systemd_post owserver.service owserver.socket
%firewalld_reload
%preun fs

%systemd_preun owfs.service
%preun httpd

%systemd_preun owhttpd.service
%preun ftpd

%systemd_preun owftpd.service
%preun server

%systemd_preun owserver.service owserver.socket
%postun fs

%systemd_postun_with_restart owfs.service
%postun httpd

%systemd_postun_with_restart owhttpd.service
%postun ftpd

%systemd_postun_with_restart owftpd.service
%postun server

%systemd_postun_with_restart owserver.service owserver.socket
%firewalld_reload
%files -f %{oreon_filedir}/main.list
%files -n owfs-libs -f %{oreon_filedir}/owfs-libs.list
%files -n owfs-capi -f %{oreon_filedir}/owfs-capi.list
%files -n owfs-devel -f %{oreon_filedir}/owfs-devel.list
%files -n owfs-ownet -f %{oreon_filedir}/owfs-ownet.list
%files -n owfs-fs -f %{oreon_filedir}/owfs-fs.list
%files -n owfs-httpd -f %{oreon_filedir}/owfs-httpd.list
%files -n owfs-ftpd -f %{oreon_filedir}/owfs-ftpd.list
%files -n owfs-server -f %{oreon_filedir}/owfs-server.list
%files -n owfs-tap -f %{oreon_filedir}/owfs-tap.list
%files -n owfs-mon -f %{oreon_filedir}/owfs-mon.list
%files -n owfs-php -f %{oreon_filedir}/owfs-php.list
%files -n owfs-tcl -f %{oreon_filedir}/owfs-tcl.list
%files -n owfs-shell -f %{oreon_filedir}/owfs-shell.list

%changelog

%autochangelog
