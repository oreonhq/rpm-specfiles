%global source0_hash 0409e2ce4bfdb2dacb2c193d0fedfc49bb975cb057c5c6b0ffcca603a1188da7

Summary: Displays who is logged in to local network machines
Name: rwho
Version: 0.17
Release: 81%{?dist}
# part of rwhod is under GPL+, other parts are under BSD
# Automatically converted from old format: BSD and GPL+ - review is highly recommended.
License: LicenseRef-Callaway-BSD AND GPL-1.0-or-later
Source: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/netkit-rwho-%{version}.tar.gz
Source1: rwhod.service
Patch0: rwho-0.15-alpha.patch
Patch1: rwho-0.17-bug22014.patch
Patch2: rwho-0.17-fixbcast.patch
Patch3: rwho-0.17-fixhostname.patch
Patch4: rwho-0.17-strip.patch
Patch5: rwho-0.17-include.patch
Patch6: rwho-0.17-wd_we.patch
Patch7: rwho-0.17-time.patch
Patch8: rwho-0.17-gcc4.patch
Patch9: rwho-0.17-waitchild.patch
Patch10: rwho-0.17-neighbours.patch
Patch11: rwho-0.17-hostnamelen.patch
Patch12: rwho-0.17-stderr.patch
Patch13: rwho-c99.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires: gcc
BuildRequires: systemd, perl-interpreter

%description
The rwho command displays output similar to the output of the who
command (it shows who is logged in) for all machines on the local
network running the rwho daemon.

Install the rwho command if you need to keep track of the users who
are logged in to your local network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n netkit-rwho-%{version}
%patch -P0 -p1 -b .alpha
%patch -P1 -p1 -b .bug22014
%patch -P2 -p1 -b .fixbcast
%patch -P3 -p1 -b .fixhostname
%patch -P4 -p1 -b .strip
%patch -P5 -p1 -b .include
%patch -P6 -p1 -b .wd_we
%patch -P7 -p1 -b .time
%patch -P8 -p1 -b .gcc4
%patch -P9 -p1 -b .waitchild
%patch -P10 -p1 -b .neighbours
%patch -P11 -p1 -b .hostnamelen
%patch -P12 -p1 -b .stderr
%patch -P13 -p1

%{__perl} -pi -e '
    s|^LDFLAGS=|LDFLAGS="-pie -Wl,-z,relro,-z,now"|;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' configure

%build
%ifarch s390 s390x
CFLAGS="$RPM_OPT_FLAGS -I../include -fPIC" \
%else
CFLAGS="$RPM_OPT_FLAGS -I../include -fpic" \
%endif
sh configure --with-c-compiler=gcc
make %{?_smp_mflags}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,8}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}/var/spool/rwho

make INSTALLROOT=${RPM_BUILD_ROOT} install
make INSTALLROOT=${RPM_BUILD_ROOT} install -C ruptime

install -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_unitdir}/rwhod.service

%post
%systemd_post rwhod.service

%preun
%systemd_preun rwhod.service

%postun
%systemd_postun_with_restart rwhod.service

%files
%doc README
%{_bindir}/ruptime
%{_mandir}/man1/ruptime.1*
%{_bindir}/rwho
%{_mandir}/man1/rwho.1*
%{_sbindir}/rwhod
%{_mandir}/man8/rwhod.8*
/var/spool/rwho
%{_unitdir}/*

%changelog
%autochangelog
