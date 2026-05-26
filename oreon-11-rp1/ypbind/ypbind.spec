Summary: The NIS daemon which binds NIS clients to an NIS domain
Name: ypbind
Epoch: 3
Version: 2.7.2
Release: 17%{?dist}
License: GPL-2.0-only
Url: https://www.thkukuk.de/nis/nis/ypbind-mt/

Source0: https://github.com/thkukuk/ypbind-mt/archive/v%{version}.tar.gz#/ypbind-mt-%{version}.tar.gz
#Source1: ypbind.init
Source2: nis.sh
Source3: ypbind.service
Source4: ypbind-pre-setdomain
Source5: ypbind-post-waitbind

# Fedora-specific patch. Renaming 'ypbind' package to proper
# 'ypbind-mt' would allow us to drop it.
Patch1: ypbind-1.11-gettextdomain.patch
# Not sent to upstream.
Patch2: ypbind-2.5-helpman.patch
# oreon url source checksums begin
%global source0_sha256 3d20741ba04d9d421a5462555177e1b88aefd279b4f882b0f0083077a557f51f
%global source0_file v2.7.2.tar.gz
# oreon url source checksums end

# This is for /bin/systemctl
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: rpcbind
Requires: yp-tools >= 4.2.2-2
# New nss_nis package in F25+
Requires: nss_nis
BuildRequires: make
BuildRequires:  gcc
BuildRequires: dbus-glib-devel, docbook-style-xsl
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: autoconf, automake
BuildRequires: gettext-devel
BuildRequires: libtirpc-devel
BuildRequires: libnsl2-devel
BuildRequires: libxslt

%description
The Network Information Service (NIS) is a system that provides
network information (login names, passwords, home directories, group
information) to all of the machines on a network. NIS can allow users
to log in on any machine on the network, as long as the machine has
the NIS client programs running and the user's password is recorded in
the NIS passwd database. NIS was formerly known as Sun Yellow Pages
(YP).

This package provides the ypbind daemon. The ypbind daemon binds NIS
clients to an NIS domain. Ypbind must be running on any machines
running NIS client programs.

Install the ypbind package on any machines running NIS client programs
(included in the yp-tools package). If you need an NIS server, you
also need to install the ypserv package to a machine on your network.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v2.7.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3d20741ba04d9d421a5462555177e1b88aefd279b4f882b0f0083077a557f51f" || { echo "oreon: Source0 SHA256 mismatch for v2.7.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n ypbind-mt-%{version}

autoreconf -fiv

%build
%ifarch s390 s390x
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif
export LDFLAGS="$LDFLAGS -pie -Wl,-z,relro,-z,now"

#export CFLAGS="$CFLAGS -H"

%configure
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/yp/binding
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dhcp/dhclient.d
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
install -m 644 etc/yp.conf $RPM_BUILD_ROOT%{_sysconfdir}/yp.conf
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/dhcp/dhclient.d/nis.sh
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/ypbind.service
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_libexecdir}/ypbind-pre-setdomain
install -m 755 %{SOURCE5} $RPM_BUILD_ROOT%{_libexecdir}/ypbind-post-waitbind

%{find_lang} %{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files -f %{name}.lang
%{_sbindir}/*
%{_mandir}/*/*
%{_libexecdir}/*
%{_unitdir}/*
%{_sysconfdir}/dhcp/dhclient.d/*
%config(noreplace) %{_sysconfdir}/yp.conf
%dir %{_localstatedir}/yp/binding
%doc README NEWS
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7.2-17
- Prepare for Oreon 11 (RP1)
