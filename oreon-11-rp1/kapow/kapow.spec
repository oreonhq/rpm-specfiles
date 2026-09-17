%global source0_hash f65e73bdfadbb53734cf8b4d165adad13c2cc2d8447187c0a6be048e9e0db0d5

Name:           kapow
Version:        1.6.4
Release:        3%{?dist}
Summary:        A punch clock program

License:        GPL-3.0-or-later
URL:            http://gottcode.org/%{name}
Source0:        https://github.com/gottcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  qt6-linguist
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  gettext-devel
Requires:       hicolor-icon-theme

%description
Kapow is a punch clock program designed to easily keep track of your hours,
whether you're working on one project or many. Simply clock in and out with the
Start/Stop button. If you make a mistake in your hours, you can go back and
edit any of the entries by double-clicking on the session in question. Kapow
also allows you to easily keep track of the hours since you last billed a
client, by providing a helpful "Billed" check box--the totals will reflect your
work after the last billed session.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc CREDITS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
%autochangelog
