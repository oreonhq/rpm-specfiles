%global source0_hash 0287daafc04da2ae70676f0cf6b6c7fbd8742183ce82d005afd078d0550f0f6c

%define new_ldlinux	0

Summary: Utility for creation bootable FAT disk
Name: makebootfat
Version: 1.4
Release: 44%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://advancemame.sourceforge.net/doc-makebootfat.html
Source0: http://downloads.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
Source1: makebootfat-README.usbboot
Patch0:  makebootfat-1.4-newioctl.patch
Patch1: makebootfat-configure-c99.patch

BuildRequires: make
BuildRequires: gcc

%if %{new_ldlinux}
#  Get syslinux-VERSION.tar.bz2 from
#	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/
#  or
#	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/Old/
#  Then
#	bunzip2 -cd syslinux-VERSION.tar.bz2 | tar -xvf -
#	cp syslinux-VERSION/ldlinux.bss ldlinux.bss-VERSION
#	cp syslinux-VERSION/ldlinux.sys ldlinux.sys-VERSION
#	rm -rf syslinux-VERSION
#
Source2: ldlinux.bss-3.36
Source3: ldlinux.sys-3.36
%endif

%description
This utility creates a bootable FAT filesystem and populates it
with files and boot tools.

It was mainly designed to create bootable USB and Fixed disk
for the AdvanceCD project (http://advancemame.sourceforge.net), but
can be successfully used separately for any purposes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

install -p -m644 %{SOURCE1} README.usbboot

%build

%configure
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/x86
install -p -m644 mbrfat.bin $RPM_BUILD_ROOT%{_datadir}/%{name}/x86
%if %{new_ldlinux}
install -p -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/x86/ldlinux.bss
install -p -m644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}/x86/ldlinux.sys
%else
install -p -m644 test/ldlinux.bss $RPM_BUILD_ROOT%{_datadir}/%{name}/x86
install -p -m644 test/ldlinux.sys $RPM_BUILD_ROOT%{_datadir}/%{name}/x86
%endif

%files
%doc AUTHORS COPYING HISTORY README README.usbboot
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/*/*

%changelog
%autochangelog
