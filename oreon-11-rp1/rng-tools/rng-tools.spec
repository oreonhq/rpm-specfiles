%global source0_hash 4aa50994232da74499b60b3ebf79118e30a1943be375b7d931dcf18df5442fd3
%global _hardened_build 1
%bcond_without pkcs11
%bcond_without rtlsdr
Summary:        Random number generator related utilities
Name:           rng-tools
Version:        6.17
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/nhorman/rng-tools
Source0:        https://github.com/nhorman/rng-tools/archive/refs/tags/v6.17.tar.gz#/rng-tools-6.17.tar.gz
Source1:        rngd.service
Source2:        rngd.sysconfig
%if %{with rtlsdr}
%endif
%if %{with pkcs11}
Suggests: opensc
%endif
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: (selinux-policy >= 36.5 if selinux-policy)
Patch0: 1-rt-comment-out-have-aesni.patch
Patch1: 2-rt-revert-build-randstat.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  jansson-devel
BuildRequires:  jitterentropy-devel
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libp11-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  rtl-sdr-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This is a random number generator daemon and its tools. It monitors
a set of entropy sources present on a system (like /dev/hwrng, RDRAND,
TPM, jitter) and supplies entropy from them to a kernel entropy pool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p0

%build

%if !%{with pkcs11}
%define _without_pkcs11 --without-pkcs11
%endif
%if !%{with rtlsdr}
%define _without_rtlsdr --without-rtlsdr
%endif
./autogen.sh
%ifarch i386 i686
sed -i -e '/^#define RDRAND_RETRY_LIMIT\t10/a#define __PIC__ 1' rdrand_asm.S
%endif
sed -i -e 's/$(libdarn_impl_a_CFLAGS) $(CFLAGS)/$(CFLAGS) $(libdarn_impl_a_CFLAGS)/' Makefile.in
%configure %{?_without_pkcs11} %{?_without_rtlsdr}
%make_build
%install
%make_install
install -Dt %{buildroot}%{_unitdir} -m0644 %{SOURCE1}
install -D %{SOURCE2} -m0644 %{buildroot}%{_sysconfdir}/sysconfig/rngd
%oreon_autofiles main

%post

%systemd_post rngd.service
%preun

%systemd_preun rngd.service
%postun

%systemd_postun_with_restart rngd.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.17-8
- Prepare for Oreon 11 (RP1)
