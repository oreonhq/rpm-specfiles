%global source0_hash ab7058b96d5d6c563183529243052a4d7241b0829dfac517f1ce3c3c5503afc6

Name:           ganyremote
Version:        8.1.1
Release:        %autorelease
Summary:        GTK frontend for anyRemote
License:        GPL-3.0-or-later
URL:            https://anyremote.sourceforge.net/
Source:         https://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  make

Requires:       anyremote >= 6.7
Requires:       bluez-deprecated
Requires:       gdk-pixbuf2
Requires:       gtk3
Requires:       python3-bluez >= 0.9.1
Requires:       python3-gobject
Recommends:     libappindicator-gtk3

%description
gAnyRemote package is GTK GUI frontend for anyRemote 
(https://anyremote.sourceforge.net/) - remote control software for applications 
using Bluetooth or Wi-Fi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure

%install
%make_install

desktop-file-install \
  --add-category="System"                     \
  --delete-original                           \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

find %{buildroot}%{_docdir} -delete
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.png

%changelog
%autochangelog
