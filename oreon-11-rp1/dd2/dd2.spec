%global source0_hash 9cecf8c3ce264977c66b7f6c6aa1eee9a80564a5c9a479404c82cd96f1dea5cc

Name:           dd2
Version:        0.2.2
Release:        42%{?dist}
Summary:        Dodgin' Diamond 2 - Shoot'em up arcade game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.usebox.net/jjm/dd2/
Source0:        http://www.usebox.net/jjm/dd2/releases/dd2-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         dd2-0.2.1-glob-highscore.patch
Patch1:         dd2-0.2.1-640x480-fullscreen.patch
Patch2:         dd2-0.2.2-configure-c99.patch
Patch3:         dd2-0.2.2-c23.patch
Patch4:         dd2-0.2.2-quit.patch
BuildRequires:  gcc make
BuildRequires:  SDL_mixer-devel desktop-file-utils
Requires:       hicolor-icon-theme

%description
This is a little shoot'em up arcade game for one or two players. It aims to
be an 'old school' arcade game with low resolution graphics, top-down scroll
action, energy based gameplay and different weapons with several levels of
power.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
#stop autoxxx from rerunning
touch src/data/Makefile.in

%build
%configure
%make_build

%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/games
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-hiscore \
  $RPM_BUILD_ROOT%{_var}/games

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/%{name}.png

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%config(noreplace) %attr (0664,root,games) %{_var}/games/%{name}-hiscore

%changelog
%autochangelog
