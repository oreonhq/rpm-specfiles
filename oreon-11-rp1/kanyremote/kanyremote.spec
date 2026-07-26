%global source0_hash 0ce1344802112baf28da7f727913e20f58af8495d92d6340f72d7f91da345c7a

Summary: KDE frontend for anyRemote
Name: kanyremote
Version: 8.1.1
Release: 6%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Source0: http://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
Requires: python3-qt5-base, python3-bluez >= 0.22, bluez >= 4.64, anyremote >= 6.5
BuildRequires: gcc, desktop-file-utils
BuildRequires: make
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://anyremote.sourceforge.net/
BuildArch: noarch

%description
kAnyRemote package is KDE GUI frontend for anyRemote
(http://anyremote.sourceforge.net/) - remote control software for applications 
using Bluetooth or Wi-Fi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
desktop-file-install --vendor="" \
  --add-category="System" \
  --delete-original \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ \
  $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
%autochangelog
