%global source0_hash 3d3ab91dd0a0f0922713f2d3f4fd5fad66ec97cc2d944fb9e5ed4dbb9b953e46
Name:           qtpass
Version:        1.8.1
Release:        1%{?dist}
Summary:        Cross-platform GUI for pass
License:        GPL-3.0-only
URL:            https://qtpass.org/
Source0:        https://github.com/IJHack/qtpass/archive/v%{version}.tar.gz
Source1:        qtpass.sh.in
Patch1:         0001-Fix-build-with-Qt6.patch
Patch2:         0002-Update-new-TLDs.patch
Patch3:         0003-Fix-multiple-profiles-issue-for-Qt6.patch
Patch4:         0004-getRecipientListSplitByHash.patch
Patch5:         0005-fix-add-missing-QDirIterator-include.patch
Requires:       hicolor-icon-theme
Requires:       qt6-qtsvg
Requires:       pass
Recommends:     git
Recommends:     gpg2
Recommends:     pwgen
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  sed
# /oreon:deps
%description
QtPass is a cross-platform GUI for pass, the standard Unix password manager.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n QtPass-%{version}
sed -i "s|#include <QDir>|#include <QDir>\n#if QT_VERSION >= QT_VERSION_CHECK(6, 0, 0)\n#include <QStringDecoder>\n#endif|" src/executor.cpp

%build

%qmake_qt6 PREFIX=%{_prefix}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
desktop-file-install %{name}.desktop
install -Dpm 644 artwork/icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/qtpass-icon.svg
install -Dpm 644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm 755 %{buildroot}%{_bindir}/qtpass %{buildroot}%{_libexecdir}/qtpass
sed -e 's,/__PREFIX__,%{_libexecdir},g' %{SOURCE1} > %{buildroot}%{_bindir}/qtpass
chmod 755 %{buildroot}%{_bindir}/qtpass
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
