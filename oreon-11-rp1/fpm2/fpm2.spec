%global source0_hash 85b2a996bdbf65028b92a8c1d7ceed62787560562344a3f66397e7cd85d72030

Summary: Password manager with GTK3 GUI
Name: fpm2
Version: 0.90.2
Release: 2%{?dist}
License: GPL-2.0-or-later
Source: https://als.regnet.cz/%{name}/download/%{name}-%{version}.tar.xz
URL: https://als.regnet.cz/fpm2/
BuildRequires: meson
BuildRequires: gcc, desktop-file-utils, gettext
BuildRequires: gtk3-devel, libxml2-devel, nettle-devel

%description
Figaro's Password Manager 2 is a program that allows you to securely store the
passwords using GTK3 interface. Features include:
- Passwords are encrypted with the AES-256-GCM algorithm.
- Copy passwords or user names to the clipboard/primary selection.
- If the password is for a web site, FPM2 can keep track of the URLs of your
  login screens and can automatically launch your browser. In this capacity,
  FPM2 acts as a kind of bookmark manager.
- Combine all three features: you can configure FPM2 to bring you to a web
  login screen, copy your user name to the clipboard and your password to the
  primary selection, all with a single button click.
- FPM2 also has a password generator that can choose passwords for you. It
  allows you to determine how long the password should be, and what types of
  characters (lower case, upper case, numbers and symbols) should be used.
  You can even have it avoid ambiguous characters such as a capital O or the
  number zero.
- Auto-minimize and/or auto-locking passwords database after configurable time
  to the tray icon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
%meson

%build
%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-install \
  --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/fpm2
%{_datadir}/pixmaps/fpm2
%{_mandir}/man1/fpm2.1.gz
%{_datadir}/applications/fpm2.desktop
%{_datadir}/icons/hicolor/*/apps/fpm2.png
%{_datadir}/metainfo/fpm2.metainfo.xml

%check
# No tests available for this package

%changelog
%autochangelog
