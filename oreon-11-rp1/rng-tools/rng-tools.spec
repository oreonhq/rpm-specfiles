%global source0_hash 4aa50994232da74499b60b3ebf79118e30a1943be375b7d931dcf18df5442fd3

%global _hardened_build 1

# this is a correct if, bcond_with actually means without and vice versa
%if 0%{?rhel} && 0%{?rhel} >= 9
%bcond_with    pkcs11
%bcond_with    rtlsdr
%else
%bcond_without pkcs11
%bcond_without rtlsdr
%endif

Summary:        Random number generator related utilities
Name:           rng-tools
Version:        6.17
Release:        8%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/nhorman/rng-tools
Source0:        https://github.com/nhorman/rng-tools/archive/v6.17/rng-tools-6.17.tar.gz
Source1:        rngd.service
Source2:        rngd.sysconfig

BuildRequires: gcc make binutils
BuildRequires: gettext
BuildRequires: systemd systemd-rpm-macros
BuildRequires: autoconf >= 2.57, automake >= 1.7
BuildRequires: libgcrypt-devel libcurl-devel
BuildRequires: libxml2-devel openssl-devel
BuildRequires: jitterentropy-devel
BuildRequires: jansson-devel
BuildRequires: libcap-devel
%if %{with rtlsdr}
BuildRequires: rtl-sdr-devel
%endif
%if %{with pkcs11}
BuildRequires: libp11-devel
Suggests: opensc
%endif

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# This ensures that the selinux-policy package and all its dependencies
# are not pulled into containers and other systems that do not use SELinux.
Requires: (selinux-policy >= 36.5 if selinux-policy)

Patch0: 1-rt-comment-out-have-aesni.patch
Patch1: 2-rt-revert-build-randstat.patch

%description
This is a random number generator daemon and its tools. It monitors
a set of entropy sources present on a system (like /dev/hwrng, RDRAND,
TPM, jitter) and supplies entropy from them to a kernel entropy pool.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p0

%build
%if !%{with pkcs11}
%define _without_pkcs11 --without-pkcs11
%endif
%if !%{with rtlsdr}
%define _without_rtlsdr --without-rtlsdr
%endif

./autogen.sh
# a dirty hack to force PIC for a PIC-aware assembly code for i686
# /usr/lib/rpm/redhat/redhat-hardened-cc1 in Koji/Brew does not
# force PIC for assembly sources as of now
%ifarch i386 i686
sed -i -e '/^#define RDRAND_RETRY_LIMIT\t10/a#define __PIC__ 1' rdrand_asm.S
%endif
# a dirty hack so libdarn_impl_a_CFLAGS overrides common CFLAGS
sed -i -e 's/$(libdarn_impl_a_CFLAGS) $(CFLAGS)/$(CFLAGS) $(libdarn_impl_a_CFLAGS)/' Makefile.in
%configure %{?_without_pkcs11} %{?_without_rtlsdr}
%make_build

%install
%make_install

# install systemd unit file
install -Dt %{buildroot}%{_unitdir} -m0644 %{SOURCE1}
# install sysconfig file
install -D %{SOURCE2} -m0644 %{buildroot}%{_sysconfdir}/sysconfig/rngd

%post
%systemd_post rngd.service

%preun
%systemd_preun rngd.service

%postun
%systemd_postun_with_restart rngd.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS README.md
%{_bindir}/rngtest
%{_sbindir}/rngd
%{_mandir}/man1/rngtest.1.*
%{_mandir}/man8/rngd.8.*
%attr(0644,root,root)    %{_unitdir}/rngd.service
%config(noreplace) %attr(0644,root,root)    %{_sysconfdir}/sysconfig/rngd

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.17-8
- Prepare for Oreon 11 (RP1)
