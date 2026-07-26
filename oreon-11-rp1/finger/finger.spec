%global source0_hash 84885d668d117ef50e01c7034a45d8343d747cec6212e40e8d08151bc18e13fa

%global _hardened_build 1

Summary: The finger client
Name: finger
Version: 0.17
Release: 83%{?dist}
License: BSD-4-Clause-UC

Source0: ftp://ftp.uk.linux.org/pub/linux/Networking/netkit/bsd-finger-%{version}.tar.gz
Source1: finger.socket
Source2: finger@.service
#BSD license text from sources
Source3: COPYING

Patch1: bsd-finger-0.16-pts.patch
Patch2: bsd-finger-0.17-exact.patch
Patch3: bsd-finger-0.16-allocbroken.patch
Patch4: bsd-finger-0.17-rfc742.patch
Patch5: bsd-finger-0.17-time.patch
Patch6: bsd-finger-0.17-usagi-ipv6.patch
Patch7: bsd-finger-0.17-typo.patch
Patch8: bsd-finger-0.17-strip.patch
Patch9: bsd-finger-0.17-utmp.patch
Patch10: bsd-finger-wide-char-support5.patch
Patch11: bsd-finger-0.17-init-realname.patch
Patch12: bsd-finger-0.17-host-info.patch
Patch13: bsd-finger-0.17-match_sigsegv.patch
Patch14: bsd-finger-0.17-man_page_systemd.patch
Patch15: bsd-finger-0.17-coverity-bugs.patch

# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses make
BuildRequires: make
# uses autosetup
BuildRequires: git-core

BuildRequires: glibc-devel, systemd
BuildRequires: %{__perl}

%description
Finger is a utility which allows users to see information about system
users (login name, home directory, name, how long they've been logged
in to the system, etc.).  The finger package includes a standard
finger client.

You should install finger if you'd like to retrieve finger information
from other systems.

%package server
Summary: The finger daemon
Requires:         finger
Requires:         systemd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description server
Finger is a utility which allows users to see information about system
users (login name, home directory, name, how long they've been logged
in to the system, etc.).  The finger-server package includes a standard
finger server. The server daemon (fingerd) must be started using 
systemctl to receive finger requests.

You should install finger-server if your system is used by multiple users
and you'd like finger information to be available.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n bsd-finger-%{version} -S git

install -m 644 %{SOURCE3} COPYING

%build
%set_build_flags
sh configure --enable-ipv6
%{__perl} -pi -e '
	s,^CC=.*$,CC=gcc,;
	s,^CFLAGS=.*,CFLAGS=\$(RPM_OPT_FLAGS),;
	s,^BINDIR=.*$,BINDIR=%{_bindir},;
	s,^MANDIR=.*$,MANDIR=%{_mandir},;
	s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
	s,^LDFLAGS=.*$,LDFLAGS=\$(RPM_LD_FLAGS),;
	' MCONFIG

%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man{1,8}
mkdir -p %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}

%make_install INSTALLROOT=%{buildroot}

%post server
%systemd_post finger.socket

%preun server
%systemd_preun finger.socket

%postun server
%systemd_postun_with_restart finger.socket

%files
%doc COPYING
%attr(0755,root,root) %{_bindir}/finger
%{_mandir}/man1/finger.1*

%files server
%doc COPYING
%{_unitdir}/finger.socket
%{_unitdir}/finger@.service
%attr(0755,root,root) %{_sbindir}/in.fingerd
%{_mandir}/man8/in.fingerd.8*
%{_mandir}/man8/fingerd.8*

%changelog
%autochangelog
