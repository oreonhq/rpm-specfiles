%global source2_hash c459c03d0ae871d59b60255303bb972a3ece8ff4a4a63a1f8c90229f64234ecf
%global source0_hash cf970afb6426e7f035be369948656fa91a048dce5ce306e2219483b48b82415a
Name:           bpfmon
Version:        2.60
Release:        1%{?dist}
Summary:        Traffic monitor for BPF expression/iptables rule
License:        GPL-2.0-or-later
URL:            https://github.com/bbonev/bpfmon/
Source0:        https://github.com/bbonev/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}releases/download/v%{version}/bpfmon-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/bbonev/bpfmon/v%{version}/debian/upstream/signing-key.asc
Patch1:         bpfmon-2.53-sbindir.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(yascreen)
# /oreon:deps
%description
While tcpdump shows what packets are going through the
network, bpfmon will show how much in terms
of bytes per second and packets per second in a
nice pseudo-graphical terminal interface.

bpfmon also supports monitoring an iptables rule that
is selected by command line option or selected from a
menu.

%global _hardened_build 1

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%set_build_flags
NO_FLTO=1 %make_build PREFIX=%{_usr} STRIP=: bpfmon
%install
V=1 STRIP=: BINDIR=$RPM_BUILD_ROOT%{_bindir} %make_install
install -TD -m 0644 bpfmon.8 $RPM_BUILD_ROOT/%{_mandir}/man8/bpfmon.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
