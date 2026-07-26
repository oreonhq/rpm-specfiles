%global source0_hash f73508a40b093caea8ac20431c19b1e89627311bbd8ff49063ec987378a46a7c

Name:           bpfmon
Version:        2.53
Release:        6%{?dist}
Summary:        Traffic monitor for BPF expression/iptables rule

License:        GPL-2.0-or-later
URL:            https://github.com/bbonev/bpfmon/
Source0:        %{url}releases/download/v%{version}/bpfmon-%{version}.tar.xz
Source1:        %{url}releases/download/v%{version}/bpfmon-%{version}.tar.xz.asc
Source2:        https://raw.githubusercontent.com/bbonev/bpfmon/v%{version}/debian/upstream/signing-key.asc
Patch1:         bpfmon-2.53-sbindir.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(yascreen)

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

%files
%license LICENSE
%{_sbindir}/bpfmon
%{_mandir}/man8/bpfmon.8*

%changelog
%autochangelog
