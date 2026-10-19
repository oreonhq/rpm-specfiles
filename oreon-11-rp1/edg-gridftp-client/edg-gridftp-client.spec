%global source0_hash e77aec426cda4b7f35dfbebdfef9e9bcbb104aed6939268c62651b3e410935d7
Name:           edg-gridftp-client
Version:        1.2.9.2
Release:        1%{?dist}
Summary:        Command line clients to GridFTP libraries
License:        EUDatagrid
URL:            http://jra1mw.cvs.cern.ch:8180/cgi-bin/jra1mw.cgi/edg-gridftp-client/
Source0:        edg-gridftp-client-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  globus-ftp-client-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
The edg-gridftp-client package is a thin command line interface on top
of the GridFTP libraries supplied by Globus.  They do, however,
represent a useful set of commands to do basic management of files on
a GridFTP server.

The commands provided are:

  edg-gridftp-exists   test if a file/directory exists on the server
  edg-gridftp-mkdir    create a directory on the server
  edg-gridftp-rmdir    remove a directory from a server
  edg-gridftp-rm       remove a file from a server
  edg-gridftp-ls       list files/directories on a server
  edg-gridftp-rename   rename a file/directory on a server

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Adapt for flavourless globus
sed -i 's/_$(FLAVOR)//g' src/Makefile.am
# A library changed name.
sed -i 's/-lgssapi_error/-lglobus_gssapi_error/' src/Makefile.am

%build

./autogen.sh
CFLAGS="${CFLAGS:-%optflags} -I%{_includedir}/globus -I%{_libdir}/globus/include" ; export CFLAGS
%configure
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_defaultdocdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
