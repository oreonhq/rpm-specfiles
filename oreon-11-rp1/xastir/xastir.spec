%global source0_hash 4d1844a5c9f31407d34fa0339a2b462f8c53991d41045ad16b39ded5dcdfb2fe

Summary: Amateur Station Tracking and Reporting system for amateur radio
Name:    xastir
Epoch:   1
Version: 2.2.0
Release: 6%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: https://github.com/Xastir/Xastir/archive/Release-%{version}.tar.gz
Source1: %{name}.desktop
Source2: %{name}.png
Source3: %{name}.svg
Source4: org.xastir.Xastir.metainfo.xml
URL:     http://www.xastir.org
Requires: wget
Requires: hicolor-icon-theme
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: wget, libXt-devel, GraphicsMagick-devel
%if 0%{?fedora} >= 24
BuildRequires: motif-devel
%else
BuildRequires: lesstif-devel
%endif
BuildRequires: dos2unix, libax25-devel, curl-devel, proj-devel, libXpm-devel
BuildRequires: python3-devel, gpsman, gdal-devel, libdb-devel
BuildRequires: desktop-file-utils, xfontsel, hdf5-devel
BuildRequires: autoconf, automake, shapelib-devel

%description
Xastir is a graphical application that interfaces HAM radio
and internet access to realtime mapping software.

Install XASTIR if you are interested in APRS(tm) and HAM radio
software.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Xastir-Release-%{version}
touch -r configure.ac aclocal.m4 Makefile.in config.h.in

%build
./bootstrap.sh
%configure --with-geotiff=/usr/include/libgeotiff
make %{?_smp_mflags}
for f in README ChangeLog ; do
    mv $f $f.iso88591
    iconv -o $f -f iso88591 -t utf8 $f.iso88591
    touch -r $f.iso88591 $f
    rm -f $f.iso88591
done
dos2unix -k scripts/toporama250k.pl

%install
rm -rf %{buildroot}
make install DESTDIR="%{buildroot}" INSTALL="install -p"
#fix wrong doc-path instalation in make install target
#or else we'll get unpacked files
rm -rf %{buildroot}/usr/share/doc
#remove gpx2shape because of unsupported dependency Geo::Shapelib
rm %{buildroot}/usr/share/xastir/scripts/gpx2shape
#strip exec bit from .pm files
find %{buildroot} -type f -name '*.pm' -exec chmod -x {} 2>/dev/null ';'
install -D -p -m644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -D -p -m644 %{SOURCE4} %{buildroot}%{_metainfodir}/org.xastir.Xastir.metainfo.xml

%files
%{_bindir}/xastir
%{_bindir}/xastir_udp_client
%{_bindir}/callpass
%{_bindir}/testdbfawk
%{_mandir}/man1/xastir*.*
%{_mandir}/man1/callpass.*
%{_mandir}/man1/testdbfawk.*
%{_datadir}/xastir
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/org.xastir.Xastir.metainfo.xml
%doc AUTHORS ChangeLog COPYING DEBUG_LEVELS FAQ LICENSE
%doc README
%doc README.MAPS UPGRADE

%changelog
%autochangelog
