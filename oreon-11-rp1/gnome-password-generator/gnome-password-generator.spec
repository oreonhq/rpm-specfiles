%global source0_hash 84bd5416c187de5ce69acb53591927981f8cc2c18fc1ce993a257e7a20f9852d

%global project_owner Jenselme

Summary:        Graphical secure password generator
Name:           gnome-password-generator
Version:        2.2.3
Release:        3%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/%{project_owner}/%{name}
Source0:        https://github.com/%{project_owner}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires: make
Requires:       python3-gobject
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
Gnome Password Generator is a GUI based secure password generator. It allows
the user to generate a specified number of random passwords of a specified
length.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%make_build

%install
%make_install

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%files
%license COPYING
%license AUTHORS
%doc ChangeLog.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
%autochangelog
