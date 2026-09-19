%global source0_hash 2229e627528ec02a9cf7aba3a65bef8999272fc25eb22112dc3f8ee583eb5dfb

Summary:       Manager for sqlite - Sqlite Databases Made Easy
Name:          sqliteman
Version:       1.2.2
Release:       43%{?dist}
# src is GPLv2+, icons are LGPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://sqliteman.yarpen.cz/
Patch:         sqliteman-1.2.2-desktop.patch
Patch:         sqliteman-1.2.2-cmake4.patch
Source:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# converted from logo_design/logo-original.ai by gimp
Source1:       sqliteman.png
Requires:      qt-sqlite
Requires:      sqlite
BuildRequires: cmake
BuildRequires: qt4-devel >= 4.2.0
BuildRequires: desktop-file-utils
%description
If you are looking for a tool for tuning SQL statements, manage
tables, views, or triggers, administrate the database space and index
statistics then Sqliteman is the perfect choice.

If you are looking for a graphical queries creation wizards, user
interface designers for your database, or an universal report tool try
the applications designed for tasks such this (Kexi, knoda).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DWANT_INTERNAL_QSCINTILLA=1
%cmake_build

%install
%cmake_install
desktop-file-install   \
    --delete-original  \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

# fix location of desktop icon
rm %{buildroot}%{_datadir}/icons/hicolor/%{name}.png
install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -rf %{buildroot}%{_datadir}/icons

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
%autochangelog
