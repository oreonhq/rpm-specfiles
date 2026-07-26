%global source0_hash 29a7ebaee4830d65d0b5cefa6d497887d4f23f34659876dfe944f3a020cf33ff

Name:           intel-undervolt
Version:        1.7
Release:        %autorelease
Summary:        Intel CPU undervolting and throttling configuration tool

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/kitsunyan/intel-undervolt
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# intel-undervolt.service: wanted by suspend-then-hibernate
# https://github.com/kitsunyan/intel-undervolt/pull/41
# https://bugzilla.redhat.com/show_bug.cgi?id=2427927
Patch:          https://github.com/kitsunyan/intel-undervolt/pull/41.patch
ExclusiveArch:  i386 x86_64

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
%{?systemd_requires}

%description
intel-undervolt is a tool for undervolting and throttling limits alteration for
Intel CPUs.

Undervolting works on Haswell and newer CPUs and based on the content of this
article https://github.com/mihic/linux-intel-undervolt

This tool may damage your hardware since it uses reverse engineered methods of
MSR usage. Use it on your own risk.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Cant build with proper build flags on Fedora
# * https://github.com/kitsunyan/intel-undervolt/issues/31
sed -i 's|CFLAGS =|CFLAGS =%{build_cflags}|' \
    Makefile.in

%build
%set_build_flags
%configure \
    --enable-systemd
%make_build

%install
%make_install

%post
%systemd_post %{name}.service %{name}-loop.service

%preun
%systemd_preun %{name}.service %{name}-loop.service

%postun
%systemd_postun_with_restart %{name}.service %{name}-loop.service

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/*.service
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
%autochangelog
