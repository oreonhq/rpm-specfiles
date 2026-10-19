%global source0_hash 8c9d72ddd6d38aa48545c4b486932e3f7008354131ae1be27db863dfd7b11aaf
Summary:        The NIS (Network Information Service) server
Name: ypserv
Version: 4.2
Release:        16%{?dist}
License: GPL-2.0-only
URL: https://www.thkukuk.de/nis/nis/ypserv/
Source0:        https://github.com/thkukuk/%{name}/archive/refs/tags/v%{version}.tar.gz#/ypserv-4.2.tar.gz
Source1: ypserv.service
Source2: yppasswdd.service
Source3: ypxfrd.service
Source4: rpc.yppasswdd.env
Source5: yppasswdd-pre-setdomain
Requires: gawk, make, portmap, bash >= 2.0
Requires: tokyocabinet
Requires(pre): hostname
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Patch0: ypserv-2.5-redhat.patch
Patch2: ypserv-2.5-nfsnobody2.patch
Patch3: ypserv-2.13-ypxfr-zeroresp.patch
Patch4: ypserv-2.13-nonedomain.patch
Patch5: ypserv-2.19-slp-warning.patch
Patch6: ypserv-4.0-manfix.patch
Patch7: ypserv-2.24-aliases.patch
Patch8: ypserv-2.27-confpost.patch
Patch10: ypserv-2.31-netgrprecur.patch
Patch12: ypserv-4.0-headers.patch
Patch14: ypserv-4.0-selinux-context.patch
Patch15: ypserv-4.2-implicit-int.patch
Patch16: ypserv-4.2-uninitialized-int.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  libnsl2-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  tokyocabinet-devel
# /oreon:deps
%description
The Network Information Service (NIS) is a system that provides
network information (login names, passwords, home directories, group
information) to all of the machines on a network. NIS can allow users
to log in on any machine on the network, as long as the machine has
the NIS client programs running and the user's password is recorded in
the NIS passwd database. NIS was formerly known as Sun Yellow Pages
(YP).

This package provides the NIS server, which will need to be running on
your network. NIS clients do not need to be running the server.

Install ypserv if you need an NIS server for your network. You also
need to install the yp-tools and ypbind packages on any NIS client
machines.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1

# Delete generated man pages. They will be generated later from source.
rm makedbm/makedbm.8
rm mknetid/mknetid.8
rm etc/netgroup.5
rm etc/ypserv.conf.5

autoreconf -i

%build

cp etc/README etc/README.etc
%ifarch s390 s390x
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif
export CFLAGS="$CFLAGS -Wno-format-overflow"
%configure \
    --enable-checkroot \
    --enable-fqdn \
    --libexecdir=%{_libdir}/yp \
    --with-dbmliborder=tokyocabinet \
    --localstatedir=%{_localstatedir} \
    --with-selinux
make
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
install -m 644 etc/ypserv.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/ypserv.service
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/yppasswdd.service
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/ypxfrd.service
install -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_libexecdir}/yppasswdd-pre-setdomain
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
cat >$RPM_BUILD_ROOT/etc/sysconfig/yppasswdd <<EOF
YPPASSWDD_ARGS=
EOF
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_libexecdir}/rpc.yppasswdd.env
%oreon_autofiles main

%post

%systemd_post ypserv.service
%systemd_post ypxfrd.service
%systemd_post yppasswdd.service
%preun

%systemd_preun ypserv.service
%systemd_preun ypxfrd.service
%systemd_preun yppasswdd.service
%postun

%systemd_postun_with_restart ypserv.service
%systemd_postun_with_restart ypxfrd.service
%systemd_postun_with_restart yppasswdd.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2-16
- Prepare for Oreon 11 (RP1)
