%global source0_hash 8ee295b26b608450bc0c47ba199b34cf92f7f9ec4c81a62363e6450da76b6739

%global forgeurl https://github.com/oracle/ktls-utils
%global baseversion 1.3.0

Name:           ktls-utils
Version:        %{baseversion}
Release:        %{autorelease}
Summary:        TLS handshake agent for kernel sockets

%forgemeta

License:        GPL-2.0-only AND (GPL-2.0-only OR BSD-3-Clause)
URL:            %{forgeurl}

# FIXME: is this a bug in the tagging scheme or forgesource macro?
Source0:        https://github.com/oracle/ktls-utils/releases/download/ktls-utils-1.3.0/ktls-utils-1.3.0.tar.gz

BuildRequires:  bash systemd-rpm-macros
BuildRequires:  gcc make coreutils
BuildRequires:  pkgconfig(gnutls) >= 3.3.0
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(glib-2.0) >= 2.6
BuildRequires:  pkgconfig(libnl-3.0) >= 3.1

%description
In-kernel TLS consumers need a mechanism to perform TLS handshakes
on a connected socket to negotiate TLS session parameters that can
then be programmed into the kernel's TLS record protocol engine.

This package of software provides a TLS handshake user agent that
listens for kernel requests and then materializes a user space
socket endpoint on which to perform these handshakes. The resulting
negotiated session parameters are passed back to the kernel via
standard kTLS socket options.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{baseversion}

%build
./autogen.sh
%configure --with-systemd
%make_build

%install
%make_install

%files
%config(noreplace) %{_sysconfdir}/tlshd/config
%{_sbindir}/tlshd
%{_mandir}/man5/tlshd.conf.5.gz
%{_mandir}/man8/tlshd.8.gz
%{_unitdir}/tlshd.service
%license COPYING
%doc README.md
%doc SECURITY.md

%post
%systemd_post tlshd.service

%preun
%systemd_preun tlshd.service

%postun
%systemd_postun_with_restart tlshd.service

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{baseversion}-1
- Prepare for Oreon 11 (RP1)
