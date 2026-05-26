Name:          zenity
Version:       4.2.1
Release:       2%{?dist}
Summary:       Display dialog boxes from shell scripts

License:       LGPL-2.1-or-later
URL:           https://wiki.gnome.org/Projects/Zenity
Source:        https://download.gnome.org/sources/%{name}/4.2/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 5a9fd8d8316f90cb2e1a5a8f0d411eb9fcaf85957a8229ea3e803e81004a1ebd
%global source0_file zenity-4.2.1.tar.xz
# oreon url source checksums end

BuildRequires: pkgconfig(libadwaita-1) >= 1.2
BuildRequires: /usr/bin/help2man
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: meson
BuildRequires: which
# Tests
BuildRequires: xwayland-run
BuildRequires: mutter
BuildRequires: mesa-dri-drivers
BuildRequires: mesa-libEGL

%description
Zenity lets you display Gtk+ dialog boxes from the command line and through
shell scripts. It is similar to gdialog, but is intended to be saner. It comes
from the same family as dialog, Xdialog, and cdialog.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/zenity-4.2.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5a9fd8d8316f90cb2e1a5a8f0d411eb9fcaf85957a8229ea3e803e81004a1ebd" || { echo "oreon: Source0 SHA256 mismatch for zenity-4.2.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%build
%meson
# Man page generation requires running the in-tree zenity command.
%{shrink:xwfb-run -c mutter -w 10 -- %meson_build}


%install
%meson_install

# we don't want a perl dependency just for this
rm -f %{buildroot}/%{_bindir}/gdialog

%find_lang zenity --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Zenity.desktop


%files -f zenity.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/zenity
%{_datadir}/applications/org.gnome.Zenity.desktop
%{_datadir}/icons/hicolor/48*48/apps/zenity.png
%{_mandir}/man1/zenity.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.2.1-2
- Prepare for Oreon 11 (RP1)
