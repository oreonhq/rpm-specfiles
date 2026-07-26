%global source0_hash 2dfb9e112bb298e122ec0afd1bc54068c02c0c786237b3ddc17c4d2872a2d2cc

%global gitdate 20220906
%global commit0 2cc2a06148604b2f118ef460527b03d27530f6d4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           seahorse-nautilus
Version:        3.11.92
%global         release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Release:        31%{?gitdate:.%{gitdate}git%{shortcommit0}}%{?dist}
Summary:        PGP encryption and signing for nautilus
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Seahorse
%if 0%{?gitdate}
Source0:        https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.bz2
%else
Source0:        https://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz
%endif
Patch0:         seahorse-nautilus-fix_gnupg2_ver.patch
Patch1:         seahorse-fix-building-w-gpgme2.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  gpgme-devel >= 1.0
BuildRequires:  meson
BuildRequires:  pkgconfig(cryptui-0.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:  pkgconfig(libnotify)

%description
Seahorse nautilus is an extension for nautilus which allows encryption
and decryption of OpenPGP files using GnuPG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{?gitdate:%{name}-%{commit0}}%{!?gitdate:%{name}-%{tarball_version}}

%build
%meson
%meson_build

%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/seahorse-pgp-encrypted.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/seahorse-pgp-keys.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/seahorse-pgp-signature.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_bindir}/seahorse-tool
%{_libdir}/nautilus/extensions-4/libnautilus-seahorse.so
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.*gschema.xml
%{_mandir}/man1/seahorse-tool.1*

%changelog
%autochangelog
