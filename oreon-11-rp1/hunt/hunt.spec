%global source0_hash a8a1978f3bd05ca3f01c168c13c9a09b1e1e9038c14fdfe43694c07fe3a0e328

Summary:	Tool for demonstrating well known weaknesses in the TCP/IP protocol suite
Name:		hunt
Version:	1.5
Release:	46%{?dist}
License:	GPL-2.0-only
Source:		http://lin.fsid.cvut.cz/~kra/hunt/%name-%version.tgz
Patch0:		hunt-1.5-arridx.patch
Patch1:		hunt-1.5-cleanup.patch
Patch2:		hunt-1.5-signness.patch
Patch3:		hunt-1.5-listlen.patch
Patch4:		hunt-1.5-badcmp.patch
Patch5:		hunt-1.5-datatypes.patch
Patch6:		hunt-1.5-format-security.patch
URL:		http://lin.fsid.cvut.cz/~kra/index.html

BuildRequires:  gcc
BuildRequires: make
%description
Hunt is a program for intruding into a connection, watching it and
resetting it. It was inpired by products like Juggernaut or T-sight
but has several features which can not be found in these products.

Note that hunt is operating on Ethernet and is best used for connections
which can be watched through it. However, it is possible to do something
even for hosts on another segments. The hunt doesn't distinguish between
local network connections and connections going to/from Internet. It can
handle all connections it sees.

Connection hijacking is aimed primarily at the telnet traffic but it can
be used for another traffic too.  The reset, watching, arp... features
are common to all connections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .arridx
%patch -P1 -p1 -b .cleanup
%patch -P2 -p1 -b .signness
%patch -P3 -p1 -b .listlen
%patch -P4 -p1 -b .badcmp
%patch -P5 -p1 -b .datatypes
%patch -P6 -p1 -b .format-security

%build
make clean
# Sources aren't c11 compliant
#   Work-around by appending -std=gnu89 to CC
# Makefile uses CC to link, but misses to pass CFLAGS
#   Work-around by passing rpm's CFLAGS as LDFLAGS
make %{?_smp_mflags} hunt \
  CC='%__cc -std=gnu89' \
  CFLAGS="$RPM_OPT_FLAGS -D_REENTRANT" \
  LDFLAGS="$RPM_OPT_FLAGS -D_REENTRANT"

%install
install -d $RPM_BUILD_ROOT%_sbindir $RPM_BUILD_ROOT%_mandir/man1 \
           $RPM_BUILD_ROOT%_libdir/%name

install -p hunt          $RPM_BUILD_ROOT%_sbindir/
install -p tpsetup/*     $RPM_BUILD_ROOT%_libdir/%name/
install -p -m644 man/*.1 $RPM_BUILD_ROOT%_mandir/man1/

%files
%doc CHANGES README* TODO
%license COPYING
%doc %{_mandir}/*/*
%{_sbindir}/*
%{_libdir}/hunt

%changelog
%autochangelog
