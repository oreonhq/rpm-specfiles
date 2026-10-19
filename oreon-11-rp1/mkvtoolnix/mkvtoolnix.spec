%global source2_hash 9ff6e67aa8d37ad67e6e6078067d109ece948fccc8aad3bd157e2f57ee71c562
%global source1_hash 6baadd7038f9e06a7389c5eb7c1bc6d004c055d0c175372c58cc720ca661d21d
%global source0_hash f638b299e49cdd4efc4ab3c68dbb593ed6a61bd01bf8862da74ef7fb4d181ce8
Summary:        Matroska container manipulation utilities
Name: mkvtoolnix
Version: 101.0
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Source0:        https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz
Source1: https://mkvtoolnix.download/sources/mkvtoolnix-%{version}.tar.xz.sig
Source2: https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt
Patch0: mkvtoolnix-gcc16.patch
URL: https://mkvtoolnix.download/
Requires: libebml%{_isa} >= 1.4.4
Requires: libmatroska%{_isa} >= 1.7.1
Provides: bundled(avilib) = 0.6.10
Provides: bundled(librmff) = 0.6.0
# oreon:deps
BuildRequires:  /usr/bin/qmake6
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  boost-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  gnupg2
BuildRequires:  gtest-devel
BuildRequires:  json-devel
BuildRequires:  libappstream-glib
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libebml)
BuildRequires:  pkgconfig(libmatroska)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  po4a
BuildRequires:  rubygem-drake
BuildRequires:  rubygem-json
BuildRequires:  utf8cpp-devel
# /oreon:deps
%description
Mkvtoolnix is a set of utilities to mux and demux audio, video and subtitle
streams into and from Matroska containers.

%package gui
Summary: QT Graphical interface for Matroska container manipulation
Requires: %{name} = %{version}-%{release}
Requires: hicolor-icon-theme
%description gui
Mkvtoolnix is a set of utilities to mux and demux audio, video and subtitle
streams into and from Matroska containers.

This package contains the QT graphical interface for these utilities.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q
%patch 0 -p1
rm -rf lib/{fmt,libebml,libmatroska,nlohmann-json,pugixml,utf8-cpp}
rm -rf rake.d/vendor drake

%build

%configure \
  --disable-optimization \
  --disable-update-check \
  --with-boost-libdir=%{_libdir} \
  || cat config.log
drake %{?_smp_mflags} V=1
%install
drake DESTDIR=$RPM_BUILD_ROOT TOOLS=1 install
desktop-file-validate %{buildroot}%{_datadir}/applications/org.bunkus.mkvtoolnix-gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.bunkus.mkvtoolnix-gui.appdata.xml
install -pm 755 \
    src/tools/{base64tool,bluray_dump,diracparser,dovic_dump,dts_dump,ebml_validator,hevcc_dump,pgs_dump,vc1parser,xyzvc_dump}\
    $RPM_BUILD_ROOT%{_bindir}
%find_lang %{name}
%find_lang mkvextract --with-man
%find_lang mkvmerge --with-man
%find_lang mkvpropedit --with-man
%find_lang mkvinfo --with-man
cat mkv{extract,info,merge,propedit}.lang >> mkvtoolnix.lang
%find_lang mkvtoolnix-gui --with-man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

drake tests:run_unit
%files -f %{oreon_filedir}/main.list
%files -n mkvtoolnix-gui -f %{oreon_filedir}/mkvtoolnix-gui.list

%changelog

%autochangelog
