%global source0_hash 3eef8bebea6c8f3f084a5593bff91807cd4424d400e95fcb41609b5e497c4a89

%global commit 5ae309f1048c863f4745cd50c8cd81f98340b1d4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: vdrift
Version:  20141020
Release:  35.git%{shortcommit}%{?dist}
Summary: Driving/drift racing simulation

License: GPL-3.0-or-later
URL: http://vdrift.net
Source0: https://github.com/VDrift/vdrift/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1: vdrift.desktop
Source2: vdrift.png
# Data
# svn checkout https://svn.code.sf.net/p/vdrift/code/ vdrift-code
# mv vdrift-code/vdrift-data data
# tar cvfJ vdrift-data-20210211.tar.xz data
Source3: vdrift-data-20210211.tar.xz

Patch1: vdrift-20071226-paths.patch
Patch4:	vdrift-20090215-joepack-includes.patch
BuildRequires: mesa-libGL-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL_gfx-devel
BuildRequires: python3-scons
BuildRequires: libvorbis-devel
BuildRequires: desktop-file-utils
BuildRequires: glew-devel
BuildRequires: boost-devel
BuildRequires: asio-devel
BuildRequires: bullet-devel
BuildRequires: libarchive-devel
BuildRequires: libcurl-devel
BuildRequires: python3-devel
BuildRequires: gcc-c++
BuildRequires: subversion

Requires: vdrift-data = %{version}

%description
VDrift is a cross-platform, open source driving simulation made with drift 
racing in mind. It's powered by the excellent Vamos physics engine. It is
released under the GNU General Public License (GPL) v2. It is currently
available for Linux, FreeBSD, Mac OS X and Windows (Cygwin).

%package data
Summary: Driving/drift racing simulation data
Requires: vdrift = %{version}
BuildArch: noarch

%description data
VDrift is a cross-platform, open source driving simulation made with drift 
racing in mind. It's powered by the excellent Vamos physics engine. It is
released under the GNU General Public License (GPL) v2. It is currently
available for Linux, FreeBSD, Mac OS X and Windows (Cygwin).

These are the data files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn vdrift-%{commit} -a 3
# unbundling
rm -rf bullet

%ifarch ppc ppc64
sed -i 's/linuxx86/linuxppc/' src/SConscript
%endif

%patch -P 1 -p0
%patch -P 4 -p0
%py3_shebang_fix .

/bin/chmod -x src/main.cpp
/bin/chmod -x src/game.cpp

%build
scons %{?_smp_mflags}

%install
# As described in the README scons install is broken so DIY
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}
install -m 755 build/vdrift %{buildroot}%{_bindir}
cp -pr data %{buildroot}%{_datadir}/vdrift
rm `find %{buildroot}%{_datadir}/vdrift -name "SConscript*"`

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install           \
  --dir %{buildroot}%{_datadir}/applications \
 %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

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
<!-- Copyright 2014 Luya Tshimbalanga <luya@fedoraproject.org> -->
<!--
BugReportURL: https://github.com/VDrift/vdrift/issues/122
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">vdrift.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Drifting oriented racing simulation</summary>
  <description>
    <p>
      VDrift is a racing simulation oriented to drifting.
    </p>
    <p>
      It features over 45 tracks based on famous real-world circuits and 45 cars
      based on real-world vehicles.
    </p>
  </description>
  <url type="homepage">http://vdrift.net</url>
  <screenshots>
    <screenshot type="default"><!--screenshot url here--></screenshot>
    <screenshot><!--screenshot url here--></screenshot>
    <screenshot><!--screenshot url here--></screenshot>
  </screenshots>
</application>
EOF

%files
%license LICENSE
%doc README.md
%{_bindir}/vdrift
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/vdrift.desktop
%{_datadir}/icons/hicolor/32x32/apps/vdrift.png

%files data
%{_datadir}/vdrift

%changelog
%autochangelog
