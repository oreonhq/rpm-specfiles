%global source0_hash f84f31f00a58fb9a1215a4699c12ed2262b697054752cf6eebf5c79896773216

Name:           clanbomber
Version:        1.05
Release:        52%{?dist}
Summary:        Lay bombs and Blast the other players of the field game using ClanLib
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://clanbomber.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        clanbomber.desktop
Source2:        clanbomber.png
Source3:        clanbomber.appdata.xml
Patch0:         clanbomber-1.05-debian.patch
Patch1:         clanbomber-1.05-namespace.patch
Patch2:         clanbomber-1.05-make.patch
Patch3:         clanbomber-1.05-gcc6.patch
Patch4:         %{name}-gcc11.patch
BuildRequires:  gcc-c++
BuildRequires:  ClanLib06-devel zlib-devel desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme

%description
ClanBomber is a free multiplayer game, using ClanLib, where the "purpose"
is to Blast the other players of the gamefield by laying bombs close to them.
While at the same time you must avoid being blown up yourself. It
is fully playable and features Computer controlled bombers, however, it is
recommended to play ClanBomber with friends (3-8 players are really fun).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -z .deb
%patch -P1 -p1 -z .namespace
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%configure --disable-dependency-tracking
make

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS ChangeLog IDEAS QUOTES README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
%autochangelog
