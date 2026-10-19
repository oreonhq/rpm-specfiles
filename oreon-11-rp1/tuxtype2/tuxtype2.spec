%global source0_hash f821f75c7d32ffc2c105e842b70b8c87299949b44adcd6d110556122615e92fa
Name:           tuxtype2
Version:        1.8.1
Release:        37%{?dist}
Summary:        Tux Typing, an educational typing tutor for children
License:        GPL-2.0-or-later
URL:            https://github.com/tux4kids/tuxtype/
Source0:        https://github.com/tux4kids/tuxtype/archive/1.8.1-7/tuxtype_w_fonts-%{version}.tar.gz
Patch0:         tuxtype2-1.8.1-chown.patch
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  librsvg2-devel
BuildRequires:  make
BuildRequires:  t4k_common-devel
# /oreon:deps
%description
Tux Typing is an educational typing tutor for children. It features several
different types of game-play, at a variety of difficulty levels.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n tuxtype_w_fonts-1.8.1
%patch -P0 -p1
rm -rf data/fonts/*.ttf
# fix wrong end of line encoding
sed -i -e 's|\r||g' doc/en/TuxType_port_Mac.txt
#unknow lang
pushd po
mv zh_N.gmo zh_CN.gmo
mv zh_N.po zh_CN.po
popd

%build

%configure --localstatedir=%{_localstatedir}/games --sysconfdir=%{_sysconfdir}
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc
rm -rf $RPM_BUILD_ROOT/%{_usr}/doc
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/games/tuxtype
cat << EOF > %{name}.desktop
[Desktop Entry]
Name=Tux Typing
Comment=An educational typing tutor for children.
Exec=tuxtype
Icon=tuxtype
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Game;Application;
EOF
convert -size 48x48 tuxtype.ico $RPM_BUILD_ROOT/%{_datadir}/pixmaps/tuxtype.png
desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications/ \
                     --add-category X-Fedora \
                     %{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<application>
  <id type="desktop">tuxtype2.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      TuxTyping is an educational typing tutor for kids starring Tux, the Linux
      penguin.
    </p>
    <p>
      This educational game comes with two different games for practicing your
      typing, and having a great time doing it.
    </p>
  </description>
  <url type="homepage">http://tux4kids.alioth.debian.org/tuxtype/index.php</url>
  <screenshots>
    <screenshot type="default">http://tux4kids.alioth.debian.org/tuxtype/screenshots/tux_eat_fish.jpg</screenshot>
    <screenshot>http://tux4kids.alioth.debian.org/tuxtype/screenshots/tux_waiting.jpg</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
%find_lang tuxtype
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
