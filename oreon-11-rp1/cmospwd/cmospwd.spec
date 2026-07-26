%global source0_hash 97f48eb0770b7341e267c65bf40f145c08fc000a2387b9af920287e662c2ef32

Name:           cmospwd
Version:        5.0
Release:        33%{?dist}
Summary:        BIOS password cracker utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.cgsecurity.org/wiki/CmosPwd
Source0:        http://www.cgsecurity.org/%{name}-%{version}.tar.bz2

# Fails to build on other arches and not useful there either, I think
ExclusiveArch:  %{ix86} x86_64

BuildRequires:  gcc
BuildRequires:  dos2unix
BuildRequires: make

%description
CmosPwd decrypts password stored in cmos used to access BIOS SETUP.
Works with the following BIOSes

    * ACER/IBM BIOS
    * AMI BIOS
    * AMI WinBIOS 2.5
    * Award 4.5x/4.6x/6.0
    * Compaq (1992)
    * Compaq (New version)
    * IBM (PS/2, Activa, Thinkpad)
    * Packard Bell
    * Phoenix 1.00.09.AC0 (1994), a486 1.03, 1.04, 1.10 A03, 4.05 rev 1.02.943,
      4.06 rev 1.13.1107
    * Phoenix 4 release 6 (User)
    * Gateway Solo - Phoenix 4.0 release 6
    * Toshiba
    * Zenith AMI

With CmosPwd, you can also backup, restore and erase/kill cmos.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

rm src/%{name}

dos2unix %{name}.txt
iconv -f iso-8859-1 -t utf-8 %{name}.txt > %{name}.new
touch -r %{name}.txt %{name}.new
mv %{name}.new %{name}.txt

%build
cd src
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 src/%{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}

%files
%doc COPYING %{name}.txt
%{_sbindir}/%{name}

%changelog
%autochangelog
