%global source0_hash 36a0f4ad06e132349cd2a998ac6c219e277127d37b704a895fc4995c1fca1b93

%global aprversion 1
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}

%global commit 7a7b7646b2a36d16c18591bc5b27c91b4dd26161
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gridsite
Version:        3.0.0
Release:        0.36.20260121git%{shortcommit}%{?dist}
Summary:        Grid Security for the Web, Web platforms for Grids

#  - src/gsexec.c ASL 2.0 (not used)
#  - src/gsexec.h ASL 2.0 (not used)
#  - src/mod_gridsite.c BSD but includes ASL 2.0 based code.
#  - src/mod_ssl-private.h BSD but includes ASL 2.0 based code.
# All other files are BSD
License:        Apache-2.0 AND BSD-2-Clause
URL:            http://www.gridsite.org
Source0:        https://github.com/CESNET/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        gridsite-httpd.conf
Source2:        gridsitehead.txt
Source3:        gridsitefoot.txt
Source4:        root-level.gacl
Source5:        gridsitelogo.png

BuildRequires:  make
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  httpd-devel
BuildRequires:  doxygen
BuildRequires:  openssl-devel >= 1.1
BuildRequires:  gsoap-devel
BuildRequires:  canl-c-devel >= 3.0.0
BuildRequires:  libtool

Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       mod_ssl
Requires:       gridsite-libs = %{version}-%{release}

Provides:       gridsite-apache = %{version}-%{release}
Obsoletes:      gridsite-apache <= 1.7.20
Provides:       gridsite-services = %{version}-%{release}
Obsoletes:      gridsite-services <= 1.7.20

%description
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for
Grid credentials, GACL access control lists and HTTP(S) protocol operations.

This package gridsite contains apache httpd modules for enabling
mod_gridsite.

%package  libs
Summary:  Run time libraries for mod_gridsite and gridsite-clients

%description libs
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for
Grid credentials, GACL access control lists and HTTP(S) protocol operations.

This package contains the runtime libraries.

%package  clients
Summary:  Clients to gridsite including htcp, htrm, htmv
Requires: gridsite-libs = %{version}-%{release}
Provides: gridsite-commands = %{version}-%{release}
Obsoletes:gridsite-commands <= 1.7.20

%description  clients
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for
Grid credentials, GACL access control lists and HTTP(S) protocol operations.

This package gridsite-clients, contains clients for using against gridsite,
htcp, htrm, ...

%package  devel
Summary:  Developers tools for gridsite
Requires: gridsite-libs = %{version}-%{release}
Requires: openssl-devel

%description  devel
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for

This package gridsite-devel, contains developer tools for using gridsite.

%package   doc
Summary:   Developers Documentation for gridsite
BuildArch: noarch

%description  doc
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for

This package gridsite-doc, contains developer documentation for gridsite.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
# Copy in apache configuration.
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p %{SOURCE4} .
cp -p %{SOURCE5} .

%build
(cd src && make prefix=%{_usr} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" HTTPD_FLAGS="-I%{_includedir}/httpd -I%{_includedir}/apr-%{aprversion}")

%install
(cd src && make install prefix=%{_usr} libdir=%{_lib} DESTDIR=%{buildroot})
(cd src && make install-ws prefix=%{_usr} libdir=%{_lib} DESTDIR=%{buildroot})

# change cgi scripts location
mkdir -p %{buildroot}%{_libexecdir}/gridsite/cgi-bin
mv %{buildroot}%{_usr}/sbin/*.cgi %{buildroot}%{_libexecdir}/gridsite/cgi-bin
rmdir %{buildroot}%{_usr}/sbin

# Remove static libs
rm  %{buildroot}/%{_libdir}/libgridsite.a
# Remove docs we don't want now but will move it in %%doc later.
rm -rf %{buildroot}/%{_defaultdocdir}
# Remove the built against globus-openssl libs since
# we don't actually do that.
rm  %{buildroot}/%{_libdir}/libgridsite_globus.*

# Set up a root area to serve files from.
mkdir -p %{buildroot}%{_var}/lib/gridsite
install -p -m 0644 gridsitehead.txt %{buildroot}%{_var}/lib/gridsite/gridsitehead.txt
install -p -m 0644 gridsitefoot.txt %{buildroot}%{_var}/lib/gridsite/gridsitefoot.txt
install -p -m 0644 root-level.gacl  %{buildroot}%{_var}/lib/gridsite/.gacl

mkdir -p %{buildroot}%{_sysconfdir}/grid-security/dn-lists

mkdir -p %{buildroot}%{_var}/cache/mod_gridsite
# Copy in apache configuration, we must name it zgridsite.conf
# so it is loaded after mod_ssl in ssl.conf.
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m 0644 gridsite-httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/zgridsite.conf

mkdir -p %{buildroot}%{_var}/www/icons
install -p -m 0644 gridsitelogo.png %{buildroot}%{_var}/www/icons

# These were work arounds for an old bug in some other
# software never ever in Fedora anyway.
rm -f %{buildroot}%{_libdir}/libgridsite_nossl*

# Add an empty /etc/grid-security/vomsdir since this gridsite version
# supports .lsc files.
mkdir -p %{buildroot}%{_sysconfdir}/grid-security/vomsdir

%ldconfig_scriptlets libs

%files
%{_libdir}/httpd/modules/mod_gridsite.so
%dir %{_libexecdir}/gridsite
%dir %{_libexecdir}/gridsite/cgi-bin
%{_libexecdir}/gridsite/cgi-bin/gridsite-delegation.cgi
%{_libexecdir}/gridsite/cgi-bin/real-gridsite-admin.cgi
%dir %{_var}/www/icons
%{_var}/www/icons/gridsitelogo.png
%dir %attr(0755,apache,apache) %{_var}/lib/gridsite
%dir %attr(0755,root,root) %{_sysconfdir}/grid-security
%dir %attr(0755,apache,apache) %{_sysconfdir}/grid-security/dn-lists
%dir %attr(0755,apache,apache) %{_var}/cache/mod_gridsite
%dir %{_sysconfdir}/grid-security/vomsdir

%{_mandir}/man8/mod_gridsite.8.*
%{_mandir}/man8/gridsite-*.8.*

%config(noreplace) %{_sysconfdir}/httpd/conf.d/zgridsite.conf
%config(noreplace) %attr(-,apache,apache) %{_var}/lib/gridsite/.gacl
%config(noreplace) %attr(-,apache,apache) %{_var}/lib/gridsite/gridsitehead.txt
%config(noreplace) %attr(-,apache,apache) %{_var}/lib/gridsite/gridsitefoot.txt

%license LICENSE

%doc doc/httpd-fileserver.conf doc/httpd-webserver.conf
%doc doc/httpd-storage.conf

%doc CHANGES

%files libs
%{_libdir}/libgridsite.so.6
%{_libdir}/libgridsite.so.6.*
%license LICENSE

%files  clients
%{_bindir}/findproxyfile
%{_bindir}/htcp
%{_bindir}/htfind
%{_bindir}/htll
%{_bindir}/htls
%{_bindir}/htmkdir
%{_bindir}/htmv
%{_bindir}/htping
%{_bindir}/htproxydestroy
%{_bindir}/htproxyinfo
%{_bindir}/htproxyput
%{_bindir}/htproxyrenew
%{_bindir}/htproxytime
%{_bindir}/htproxyunixtime
%{_bindir}/htrm
%{_bindir}/urlencode

%{_mandir}/man1/findproxyfile.1*
%{_mandir}/man1/htcp.1*
%{_mandir}/man1/htfind.1*
%{_mandir}/man1/htll.1*
%{_mandir}/man1/htls.1*
%{_mandir}/man1/htmkdir.1*
%{_mandir}/man1/htmv.1*
%{_mandir}/man1/htping.1*
%{_mandir}/man1/htproxydestroy.1*
%{_mandir}/man1/htproxyinfo.1*
%{_mandir}/man1/htproxyput.1*
%{_mandir}/man1/htproxyrenew.1*
%{_mandir}/man1/htproxytime.1*
%{_mandir}/man1/htproxyunixtime.1*
%{_mandir}/man1/htrm.1*
%{_mandir}/man1/urlencode.1*

%files devel
%{_includedir}/gridsite-gacl.h
%{_includedir}/gridsite.h
%{_libdir}/libgridsite.so
%{_libdir}/pkgconfig/*

%files doc
%license LICENSE
%doc src/doxygen

%changelog
%autochangelog
