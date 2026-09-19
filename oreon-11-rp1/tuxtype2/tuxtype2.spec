%global source0_hash 2687b858679b4f0b4f42204211d162234568198544bd95a9b71ec96e788d1481

Name:           tuxtype2
Version:        1.8.1
Release:        37%{?dist}

Summary:        Tux Typing, an educational typing tutor for children
License:        GPL-2.0-or-later
URL:            https://github.com/tux4kids/tuxtype/
Source0:        https://github.com/tux4kids/tuxtype/archive/1.8.1-7/tuxtype_w_fonts-%{version}.tar.gz
Patch0:         tuxtype2-1.8.1-chown.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL-devel >= 1.2.5 SDL_image-devel SDL_mixer-devel SDL_Pango-devel
BuildRequires:  SDL_ttf-devel ImageMagick desktop-file-utils t4k_common-devel
BuildRequires:  automake autoconf
BuildRequires:  librsvg2-devel

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

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
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

%files -f tuxtype.lang
%doc AUTHORS COPYING ChangeLog README TODO doc/en/howtotheme.html doc/en/TuxType_port_Mac.txt
%attr(-,root,games) %{_bindir}/tuxtype
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_datadir}/tuxtype
%config(noreplace) %{_sysconfdir}/tuxtype
%attr(0755,root,games) %config(noreplace) %{_localstatedir}/games/tuxtype

%changelog
%autochangelog
