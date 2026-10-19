%global source0_hash 0f7b910a399d985437564af8c5d81d6dcf22b96b26b01488d72baa6a6fdb5c2c
Name:           KoboDeluxe
Version:        0.5.1
Release:        48%{?dist}
Summary:        Third person scrolling 2D shooter
License:        GPL-2.0-or-later
URL:            http://olofson.net/kobodl/
Source0:        http://olofson.net/kobodl/download/%{name}-%{version}.tar.bz2
Source1:        %{name}-32.png
Source2:        %{name}-64.png
Source3:        %{name}-128.png
Source4:        %{name}.desktop
Source5:        %{name}.appdata.xml
Patch1:         KoboDeluxe-defaults.patch
Patch2:         KoboDeluxe-0.5.1-avoid-unistd-pipe-collision.patch
Patch3:         KoboDeluxe-0.5.1-gcc44.patch
Patch4:         KoboDeluxe-0.5.1-midi-crash-fix.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Kobo Deluxe is a 3'rd person  scrolling 2D shooter with a simple
and responsive control system  - which you'll need to tackle the
tons of enemy ships that shoot at you,  chase you, circle around
you shooting,  or even  launch other ships at you,  while you're
trying to  destroy the  labyrinth  shaped  bases.  There  are 50
action packed  levels with  smoothly increasing  difficulty, and
different combinations of enemies that require different tactics
to be dealt with successfully.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's|$(sharedstatedir)/kobo-deluxe/scores|%{_var}/games/kobo-deluxe|g' \
  configure
iconv -f ISO-8859-1 -t UTF8 README > tmp;         mv tmp README
iconv -f ISO-8859-1 -t UTF8 ChangeLog > tmp;      mv tmp ChangeLog
iconv -f ISO2022JP -t UTF8 README.jp > tmp;       mv tmp README.jp
iconv -f ISO2022JP -t UTF8 README.xkobo.jp > tmp; mv tmp README.xkobo.jp

# Create a sysusers.d config file
cat >kobodeluxe.sysusers.conf <<EOF
g kobodl -
EOF

%build

%configure --disable-dependency-tracking --enable-opengl
%make_build
%install
%make_install INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
install -m0644 -D kobodeluxe.sysusers.conf %{buildroot}%{_sysusersdir}/kobodeluxe.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
