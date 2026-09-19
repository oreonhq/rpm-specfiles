%global source0_hash 9b7c52b375081883738cf049ecabc103b97d094b19c6544fb241267905d88881

Summary: Bluetooth HCI protocol analyser
Name: bluez-hcidump
Version: 2.5
Release: 31%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
URL: http://www.bluez.org/
Requires: glibc >= 2.2.4
Requires: bluez-libs >= 3.14
BuildRequires:  gcc
BuildRequires: glibc-devel >= 2.2.4
BuildRequires: bluez-libs-devel >= 3.14
BuildRequires: pkgconfig
BuildRequires: make
ExcludeArch: s390 s390x

%description
Protocol analyser for Bluetooth traffic.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README
%{_sbindir}/hcidump
%{_mandir}/man8/hcidump.8.gz

%changelog
%autochangelog
