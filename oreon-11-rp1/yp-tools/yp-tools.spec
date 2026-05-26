Summary: NIS (or YP) client programs
Name: yp-tools
Version: 4.2.3
Release: 22%{?dist}
License: GPL-2.0-only

URL: https://www.thkukuk.de/nis/nis/yp-tools/
Source: https://github.com/thkukuk/yp-tools/archive/v%{version}.tar.gz

Patch1: yp-tools-2.12-hash.patch
Patch2: yp-tools-2.12-crypt.patch
Patch3: yp-tools-2.12-adjunct.patch
Patch4: yp-tools-4.2.2-strict-prototypes.patch
Patch5: yp-tools-4.2.3-yppasswd.patch
Patch6: yp-tools-4.2.3-yppasswd-exclamation_mark.patch
# oreon url source checksums begin
%global source0_sha256 62b2278d0277c1dad122ae4a20f7a25857265904edbe0a264f9bf25b7fe50dd8
%global source0_file v4.2.3.tar.gz
# oreon url source checksums end

BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires: autoconf, automake, gettext-devel, libtool, libtirpc-devel, libnsl2-devel
Requires: ypbind >= 3:2.4-2
Requires: glibc

%global __filter_GLIBC_PRIVATE 1

%description
The Network Information Service (NIS) is a system which provides
network information (login names, passwords, home directories, groupinformation) to all of the machines on a network.  NIS can enable
information) to all of the machines on a network.  NIS can enable
users to login on any machine on the network, as long as the machine
has the NIS client programs running and the user's password is
recorded in the NIS passwd database.  NIS was formerly known as Sun
Yellow Pages (YP).

This package's NIS implementation is based on FreeBSD's YP and is a
special port for glibc 2.x and libc versions 5.4.21 and later.  This
package only provides the NIS client programs.  In order to use the
clients, you'll need to already have an NIS server running on your
network. An NIS server is provided in the ypserv package.

Install the yp-tools package if you need NIS client programs for machines
on your network.  You will also need to install the ypbind package on
every machine running NIS client programs.  If you need an NIS server,
you'll need to install the ypserv package on one machine on the network.

%package devel
Summary: NIS (or YP) client programs
Requires: yp-tools

%description devel
Install yp-tools-devel package for developing applications that use yp-tools


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v4.2.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "62b2278d0277c1dad122ae4a20f7a25857265904edbe0a264f9bf25b7fe50dd8" || { echo "oreon: Source0 SHA256 mismatch for v4.2.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{name}-%{version} -p1

autoreconf -i -f -v

%build

export CFLAGS="$CFLAGS %{optflags} -Wno-cast-function-type"

# If needed the yppasswd can be deprecated by --enable-call-passwd
%configure --disable-domainname

%make_build

%install
make DESTDIR="$RPM_BUILD_ROOT" INSTALL_PROGRAM=install install

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog NEWS etc/nsswitch.conf
%doc THANKS
%{_bindir}/*


%{_mandir}/*/*
%{_sbindir}/*
/var/yp/nicknames

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2.3-22
- Prepare for Oreon 11 (RP1)
