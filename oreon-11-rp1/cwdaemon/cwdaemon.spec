%global source0_hash 93b002ca409372a72520ce9d67a58dd49f43d04d4b38cdcedc2358ee72334283
%global forgeurl https://github.com/acerion/cwdaemon
Version:  0.13.0
%forgemeta
Name:           cwdaemon
Release:        1%{?dist}
Summary:        Morse daemon for the parallel or serial port
License:        GPL-2.0-only
URL:            http://cwdaemon.sourceforge.net
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        cwdaemon.sysconfig
Source2:        cwdaemon.service
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd-rpm-macros
BuildRequires:  unixcw-devel
# /oreon:deps
%description
cwdaemon is a small daemon which uses the pc parallel or serial port and a
simple transistor switch to output morse code to a transmitter from a text
message sent to it via udp port 6789. The program also uses the soundcard or PC
speaker (console buzzer) to generate a sidetone.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%configure
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_unitdir}
install -pDm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/cwdaemon
install -pDm644 %{SOURCE2} %{buildroot}%{_unitdir}/cwdaemon.service
%oreon_autofiles main

%check

make check
%post

%systemd_post cwdaemon.service
%preun

%systemd_preun cwdaemon.service
%postun

%systemd_postun_with_restart cwdaemon.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
