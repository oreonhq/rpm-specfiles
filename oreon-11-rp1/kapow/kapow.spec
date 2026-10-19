%global source0_hash 437a9f33c4ad8eb5b01b68f3d4d650dad930df2a414a6257f955eee7b8a83a06
Name:           kapow
Version:        1.7.1
Release:        1%{?dist}
Summary:        A punch clock program
License:        GPL-3.0-or-later
URL:            http://gottcode.org/%{name}
Source0:        https://github.com/gottcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
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
%oreon_prep
%build

%{cmake}
%{cmake_build}
%install
%{cmake_install}
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
