%global source0_hash 68bd3137439941e6253a97c7dcd27b553ce4d76c8c38e7f8db63db4d6cc7000b

Name:    cool-retro-term
Summary: Terminal emulator mimicking a CRT display
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later

Version: 1.2.0
Release: 12%{?dist}

URL: https://github.com/Swordfish90/%{name}
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtquickcontrols2-devel

Requires: hicolor-icon-theme
Requires: qt5-qtbase
Requires: qt5-qtbase-gui
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtdeclarative
Requires: qt5-qtquickcontrols
Requires: qt5-qtquickcontrols2

# Version requirement includes a release number as well,
# since we want a fresher git snapshot, not the original v0.2.0
%global qtw_version 0.2.0-9.20220109git6322802
BuildRequires: qmltermwidget >= %{qtw_version}
Requires: qmltermwidget >= %{qtw_version}

%description
%{name} is a terminal emulator which tries to mimic the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# qmltermwidget is included in the project via a git submodule.
# Since we serve it as a separate package, we modify
# the project file so it doesn't try to compile the bundled library.
rm -rf ./qmltermwidget
sed -e "s/SUBDIRS += qmltermwidget//" -i %{name}.pro

%build
%qmake_qt5 CONFIG+=force_debug_info
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

desktop-file-install                         \
  --dir=%{buildroot}%{_datadir}/applications \
  %{name}.desktop

install -m 755 -d %{buildroot}%{_datadir}/metainfo/
install -m 644 packaging/appdata/%{name}.appdata.xml %{buildroot}%{_datadir}/metainfo/

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 packaging/debian/%{name}.1 %{buildroot}%{_mandir}/man1/

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%doc README.md
%license gpl-3.0.txt
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
%autochangelog
