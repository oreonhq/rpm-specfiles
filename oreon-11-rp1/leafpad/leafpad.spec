%global source0_hash 07d3f712f4dbd0a33251fd1dee14e21afdc9f92090fc768c11ab0ac556adbe97

Name:           leafpad
Version:        0.8.19
Release:        %autorelease

Summary:        GTK+ based simple text editor

License:        GPL-2.0-or-later
URL:            http://tarot.freeshell.org/leafpad/
Source0:        http://savannah.nongnu.org/download/leafpad/%{name}-%{version}.tar.gz
Patch0:         01-gcc-format.patch

BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel >= 2.4
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make

%description
Leafpad is a GTK+ based simple text editor. The user interface is similar to
Notepad. It aims to be lighter than GEdit and KWrite, and to be as useful as
them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/main.c
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/dnd.c
sed -i 's/g_strcasecmp/g_ascii_strcasecmp/g' src/selector.c
%patch -P0

%build
%configure --enable-chooser
%make_build

%install
%make_install

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/leafpad.desktop

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/leafpad.*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
