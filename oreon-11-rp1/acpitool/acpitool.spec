%global source0_hash 004fb6cd43102918b6302cf537a2db7ceadda04aef2e0906ddf230f820dad34f

Summary: Command line ACPI client
Name: acpitool
Version: 0.5.1
Release: 39%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://sourceforge.net/projects/acpitool/
BuildRequires: gcc-c++
BuildRequires: make

Source0:	https://sourceforge.net/projects/acpitool/files/acpitool/%{version}/acpitool-%{version}.tar.bz2
Patch0:		ac_adapter.patch
Patch1:		battery.patch
Patch2:		kernel3.patch
Patch3:		wakeup.patch
Patch4:		var-line.patch
Patch5:		typos.patch
Patch6:		cleanup.patch
Patch7:		cache-size.patch

%description
AcpiTool is a Linux ACPI client. It's a small command line application, 
intended to be a replacement for the apm tool. Besides "basic" ACPI 
information like battery status, AC presence, putting the laptop to
sleep, Acpitool also supports various extensions for Toshiba, Asus and 
IBM Thinkpad laptops, allowing you to change the LCD brightness level, 
toggle fan on/off, and more. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .ac_adapter
%patch -P1 -p1 -b .battery
%patch -P2 -p1 -b .kernel3
%patch -P3 -p1 -b .wakeup
%patch -P4 -p1 -b .var-line
%patch -P5 -p1 -b .typos
%patch -P6 -p1 -b .cleanup
%patch -P7 -p1 -b .cache-size

%build
%configure
make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/acpitool
%{_mandir}/man1/acpitool*

%changelog
%autochangelog
