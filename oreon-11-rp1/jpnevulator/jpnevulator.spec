%global source0_hash 6daf3d9b5a7e0a17c1939c423c74ba116cbddce89a3dffb2ddd1859cdd175e62

Summary: Serial line sniffer including very simple terminal emulator
Name: jpnevulator
Version: 2.3.6
Release: 15%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://jpnevulator.snarl.nl/
Source: http://jpnevulator.snarl.nl/download/%{name}-%{version}.tgz
BuildRequires: gcc
BuildRequires: make

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

%files
%doc AUTHORS BUGS COPYING Changelog FAQ README TODO

%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
