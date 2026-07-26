%global source0_hash 49fb61d146c1c00be3f46280ba230ed7ddd2c13c0bbe1d06ac9f41c995f5ebb7

%define prever pre2

Name:           atomorun
Version:        1.1
Release:        0.48.%{prever}%{?dist}
Summary:        Jump & Run game where you have to flee an exploding nuclear bomb
License:        GPL-1.0-or-later
URL:            http://atomorun.whosme.de/index.php
# the file seems to be gone from upstreams server so no URL
Source0:        %{name}-%{version}_%{prever}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         atomorun-1.1-missing-protos.patch
Patch1:         atomorun-1.1-fcommon-fix.patch
Patch2:         atomorun-1.1-warnings-fix.patch
Patch3:         atomorun-1.1-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  SDL_mixer-devel SDL_image-devel libtiff-devel libvorbis-devel
BuildRequires:  alsa-lib-devel desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Atomorun is a OpenGL Jump&Run game where you have to flee an exploding
nuclear bomb.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}_%{prever}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign"
%configure
make %{?_smp_mflags}

%install
%make_install
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps/atomorun_winicon.ico
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pixmaps/%{name}_icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
