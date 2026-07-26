%global source0_hash 444080f0554a1d65db32231ee18f9a662bfa6148a15cb006eba838c2463e7a2f

Name:           kcheckers
Version:        0.8.1
Release:        38%{?dist}
Summary:        Checkers board game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://qcheckers.sourceforge.net/
Source0:        http://downloads.sourceforge.net/qcheckers/%{name}-%{version}.tar.gz
# Desktop file and patches are taken from ALT Linux package
Source1:        kcheckers.desktop
# Fedora specific prefix
Patch0:         kcheckers-0.8.1-prefix.patch
# Patch is committed into upstream CVS
Patch1:         kcheckers-0.8.1-qt-translator.patch

Requires:       hicolor-icon-theme
BuildRequires:  qt4-devel desktop-file-utils
BuildRequires: make

%description
The Qt version of the classic board game checkers. This game is also
known as draughts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{qmake_qt4}
make %{?_smp_mflags}
lrelease-qt4 i18n/*.ts

%install
rm -rf $RPM_BUILD_ROOT

install -Dp -m 755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
install -Dp -m 644 icons/biglogo.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/
install -p -m 644 i18n/*.qm $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -p -r themes $RPM_BUILD_ROOT/%{_datadir}/%{name}/
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog FAQ README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes

%changelog
%autochangelog
