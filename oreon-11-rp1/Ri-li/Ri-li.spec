%global source0_hash f71ccc20c37c601358d963e087ac0d524de8c68e96df09c3aac1ae65edd38dbd

Name:           Ri-li
Version:        2.0.1
Release:        45%{?dist}
Summary:        Arcade game where you drive a toy wood engine
# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            http://ri-li.sourceforge.net/index.html
Source0:        http://dl.sf.net/sourceforge/ri-li/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         Ri-li-2.0.1-build-fix.patch
Patch1:         Ri-li-2.0.1-gcc43.patch
Patch2:         Ri-li-gcc11.patch
Patch3:         Ri-li-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
You drive a toy wood engine in many levels and you must collect all the coaches
to win. Full-featured: 18 languages, Colorful animated wood engine, 50 levels,
3 beautiful music tracks and many sound effects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
sed -i 's/\r//g' README COPYING AUTHORS NEWS

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -m 644 data/Ri-li-icon-16x16.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 data/Ri-li-icon-32x32.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 data/Ri-li-icon-48x48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.xml

%files
%doc README AUTHORS NEWS
%license COPYING
%{_bindir}/Ri_li
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
