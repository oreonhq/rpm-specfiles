%global source0_hash c4081548c05acdd92df4d721c556f6f2c18a60e2bf5c513cb18690ad9d769980

Name:           alienblaster
Version:        1.1.0
Release:        42%{?dist}
Summary:        Action-loaded 2D arcade shooter game
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.schwardtnet.de/alienblaster/
Source0:        http://www.schwardtnet.de/%{name}/archives/%{name}-%{version}.tgz
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        %{name}-16x16.png
Source4:        %{name}-32x32.png
Source5:        %{name}-48x48.png
Patch0:         alienblaster-1.1.0-64bit.patch
Patch1:         alienblaster-1.1.0-fullscreen.patch
BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Alien Blaster is an action-loaded 2D arcade shooter game. Your mission in the 
game is simple: stop the invasion of the aliens by blasting them. 
Simultaneous two-player mode is available.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1 -z .64bit
%patch -P1 -p1 -z .fs

%build
make %{?_smp_mflags} OPTIMIZATION="$RPM_OPT_FLAGS"

%install
# no make install, DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 755 alienBlaster $RPM_BUILD_ROOT%{_bindir}/%{name}.bin
cp -a images sound cfg $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 %{SOURCE5} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files
%doc LICENSE CHANGELOG AUTHORS
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
