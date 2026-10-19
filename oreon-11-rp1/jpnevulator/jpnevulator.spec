%global source0_hash 4f9e1c38a23f7b15794731ee31f873f33371b9d9ea412f5404d9f008a85e803d
Summary:        Serial line sniffer including very simple terminal emulator
Name: jpnevulator
Version: 2.3.6
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://jpnevulator.snarl.nl/
Source0:        http://jpnevulator.snarl.nl/download/%{name}-%{version}.tgz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Jpnevulator is a handy serial sniffer. You can use it to send data on a serial
device too. You can read or write from/to one or more serial devices at the
same time.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make %{?_smp_mflags} CFLAGS="%{optflags}" %{?__global_ldflags: LDFLAGS="%{__global_ldflags}"}
%install
make DESTDIR=%{buildroot} INSTALL="install -p" install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
