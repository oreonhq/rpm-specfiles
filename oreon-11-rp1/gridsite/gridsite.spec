%global source0_hash 36a0f4ad06e132349cd2a998ac6c219e277127d37b704a895fc4995c1fca1b93
%global aprversion 1
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}
%global commit 7a7b7646b2a36d16c18591bc5b27c91b4dd26161
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           gridsite
Version:        3.0.0
Release:        1%{?dist}
Summary:        Grid Security for the Web, Web platforms for Grids
License:        Apache-2.0 AND BSD-2-Clause
URL:            http://www.gridsite.org
Source0:        https://github.com/CESNET/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        gridsite-httpd.conf
Source2:        gridsitehead.txt
Source3:        gridsitefoot.txt
Source4:        root-level.gacl
Source5:        gridsitelogo.png
Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       mod_ssl
Requires:       gridsite-libs = %{version}-%{release}
Provides:       gridsite-apache = %{version}-%{release}
Obsoletes:      gridsite-apache <= 1.7.20
Provides:       gridsite-services = %{version}-%{release}
Obsoletes:      gridsite-services <= 1.7.20
# oreon:deps
BuildRequires:  canl-c-devel
BuildRequires:  doxygen
BuildRequires:  gsoap-devel
BuildRequires:  httpd-devel
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/gridsite/cgi-bin
mv %{buildroot}%{_usr}/sbin/*.cgi %{buildroot}%{_libexecdir}/gridsite/cgi-bin
rmdir %{buildroot}%{_usr}/sbin
rm  %{buildroot}/%{_libdir}/libgridsite.a
rm -rf %{buildroot}/%{_defaultdocdir}
rm  %{buildroot}/%{_libdir}/libgridsite_globus.*
mkdir -p %{buildroot}%{_var}/lib/gridsite
install -p -m 0644 gridsitehead.txt %{buildroot}%{_var}/lib/gridsite/gridsitehead.txt
install -p -m 0644 gridsitefoot.txt %{buildroot}%{_var}/lib/gridsite/gridsitefoot.txt
install -p -m 0644 root-level.gacl  %{buildroot}%{_var}/lib/gridsite/.gacl
mkdir -p %{buildroot}%{_sysconfdir}/grid-security/dn-lists
mkdir -p %{buildroot}%{_var}/cache/mod_gridsite
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m 0644 gridsite-httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/zgridsite.conf
mkdir -p %{buildroot}%{_var}/www/icons
install -p -m 0644 gridsitelogo.png %{buildroot}%{_var}/www/icons
rm -f %{buildroot}%{_libdir}/libgridsite_nossl*
mkdir -p %{buildroot}%{_sysconfdir}/grid-security/vomsdir
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gridsite-libs -f %{oreon_filedir}/gridsite-libs.list
%files -n gridsite-clients -f %{oreon_filedir}/gridsite-clients.list
%files -n gridsite-devel -f %{oreon_filedir}/gridsite-devel.list
%files -n gridsite-doc -f %{oreon_filedir}/gridsite-doc.list

%changelog

%autochangelog
