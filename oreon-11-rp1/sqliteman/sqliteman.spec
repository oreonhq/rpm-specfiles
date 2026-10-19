%global source0_hash 2229e627528ec02a9cf7aba3a65bef8999272fc25eb22112dc3f8ee583eb5dfb
Summary:        Manager for sqlite - Sqlite Databases Made Easy
Name:          sqliteman
Version:       1.2.2
Release:        1%{?dist}
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://sqliteman.yarpen.cz/
Patch:         sqliteman-1.2.2-desktop.patch
Patch:         sqliteman-1.2.2-cmake4.patch
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:       sqliteman.png
Requires:      qt-sqlite
Requires:      sqlite
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  qt4-devel
# /oreon:deps
%description
If you are looking for a tool for tuning SQL statements, manage
tables, views, or triggers, administrate the database space and index
statistics then Sqliteman is the perfect choice.

If you are looking for a graphical queries creation wizards, user
interface designers for your database, or an universal report tool try
the applications designed for tasks such this (Kexi, knoda).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DWANT_INTERNAL_QSCINTILLA=1
%cmake_build
%install
%cmake_install
desktop-file-install   \
    --delete-original  \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
rm %{buildroot}%{_datadir}/icons/hicolor/%{name}.png
install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -rf %{buildroot}%{_datadir}/icons
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
