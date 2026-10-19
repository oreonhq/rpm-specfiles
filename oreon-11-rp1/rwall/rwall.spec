%global source0_hash 97bd59f787d19bc3dff633d35eeb627176574aa7adf65b64a6a4d8dc08f752ed
Summary:        Client for sending messages to a host's logged in users
Name: rwall
Version: 0.17
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
Url: ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/
Source0:        ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-rwall-%{version}.tar.gz
Source1: rwalld.service
Patch1: netkit-rwalld-0.10-banner.patch
Patch2: netkit-rwall-0.17-strip.patch
Patch3: netkit-rwall-0.17-netgroup.patch
Patch4: netkit-rwall-0.17-droppriv.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libnsl2-devel
BuildRequires:  libtirpc-devel
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  rpcgen
BuildRequires:  systemd-units
# /oreon:deps
%description
The rwall command sends a message to all of the users logged into a
specified host.  Actually, your machine's rwall client sends the
message to the rwall daemon running on the specified host, and the
rwall daemon relays the message to all of the users logged in to that
host.

Install rwall if you'd like the ability to send messages to users
logged in to a specified host machine.

%package server
Summary: Server for sending messages to a host's logged in users
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: portmap
BuildRequires: systemd-units
%description server
The rwall command sends a message to all of the users logged into
a specified host.  The rwall-server package contains the daemon for
receiving such messages, and is disabled by default on Red Hat Linux
systems (it can be very annoying to keep getting all those messages
when you're trying to play Quake--I mean, trying to get some work done).

Install rwall-server if you'd like the ability to receive messages
from users on remote hosts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n netkit-rwall-%{version}
%patch -P1 -p1 -b .banner
%patch -P2 -p1 -b .strip
%patch -P3 -p1 -b .netgroup
%patch -P4 -p1 -b .droppriv

%{__perl} -pi -e '
    s|^LDFLAGS=|LDFLAGS="-pie -Wl,-z,relro,-z,now -ltirpc"|;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' configure

%build

export CFLAGS="$CFLAGS -I/usr/include/tirpc"
%ifarch s390 s390x
CFLAGS="$CFLAGS $RPM_OPT_FLAGS -fPIC" \
%else
CFLAGS="$CFLAGS $RPM_OPT_FLAGS -fpic" \
%endif
sh configure --with-c-compiler=gcc
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}
%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,8}
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}/
make INSTALLROOT=${RPM_BUILD_ROOT} install
install -m 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_unitdir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post rwalld.service
%preun server

%systemd_preun rwalld.service
%postun server

%systemd_postun_with_restart rwalld.service
%files -f %{oreon_filedir}/main.list
%files -n rwall-server -f %{oreon_filedir}/rwall-server.list

%changelog

%autochangelog
