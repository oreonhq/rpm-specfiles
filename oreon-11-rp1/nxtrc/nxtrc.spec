%global source0_hash d007b6d40c6d26e659731dac338d3c8c4d61c0fea0bd2042a07c94db1f5b1b3e

Summary: Program to interact with LEGO NXT via BlueTooth
Name: nxtrc
Version: 2.3
Release: 35%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Source0: http://www.scienzaludica.it/files/%{name}-%{version}.tar.gz
URL: http://www.scienzaludica.it/index.php?page=88

BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: bluez-libs-devel

%description
nxtrc (NXT  Remote  Command) is a small program that allows to send various
commands to a LEGO Mindstorm NXT Brick. It uses the Bluetooth protocol
through the Bluez libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's#^\."\ #.\\"\ #' nxtrc.1 #just correct the invalid prefix

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%doc COPYING Readme.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
