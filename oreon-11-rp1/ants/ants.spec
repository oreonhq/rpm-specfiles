%global source0_hash 3089d82759ce7f62bb53c4bb82bf6c330bfa168fe6ff03d6c510ac49b10ea055

Name:           ants
Version:        1.4
Release:        43%{?dist}
Summary:        Guide the insects safely home before they drop of the cliff
License:        LicenseRef-Fedora-Public-Domain
URL:            http://www.allegro.cc/depot/Ants
Source0:        http://games.linux.sk/files/ants-1.4.tar.gz
Source1:        ants.desktop
Source2:        ants-level-editor.desktop
Source3:        ants.png
Source4:        license-info
Patch0:         ants-1.4-fixes.patch
BuildRequires:  gcc-c++
BuildRequires:  allegro-devel desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

%description
You take command in the game of a bunch of small ants and have to guide them
around in levels. Since the ants walk on their own, the player can only
influence them by giving them commands, like build a bridge, dig a hole or
redirect all ants in the other direction. The goal of each level is to
reach the exit, for which multiple combination of commands are necessary.
The game is presented in a 2D side view.

%package        level-editor
Summary:        Ants level editor
Requires:       %{name} = %{version}-%{release}

%description    level-editor
This package contains a level editor for ants, notice that you must run this
at root, or change the owner of the files under %{_datadir}/%{name}, as the
level editor edits the files directly under %{_datadir}/%{name} .

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -z .fix
sed -i 's/\r//g' ants.txt
cp %{SOURCE4} .

%build
make %{?_smp_mflags} EXTRA_CFLAGS="-std=c++14 $RPM_OPT_FLAGS"

%install
#no make install target, DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{name} %{name}_le $RPM_BUILD_ROOT%{_bindir}
cp -a %{name}.dat levels1 levels2 $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/

%files
%doc Changelog ants.txt license-info
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files level-editor
%{_bindir}/%{name}_le
%{_datadir}/applications/%{name}-level-editor.desktop

%changelog
%autochangelog
