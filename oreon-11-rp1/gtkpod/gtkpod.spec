%global source0_hash a57dc8ae9138e0cb4cee98691e7a95001130c9ea7823e6a75cc72503facd3a76

Name:           gtkpod
Version:        2.1.5
Release:        34%{?dist}
Summary:        Graphical song management program for Apple's iPod

License:        GPL-2.0-or-later
URL:            http://www.gtkpod.org/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gtkpod-m4a-copy.patch
Patch1:         includes.patch
Patch2:         gtkpod-snprintf.patch

BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  curl-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  anjuta-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flac-devel
BuildRequires:  flex
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libgpod-devel >= 0.7.0
BuildRequires:  libid3tag-devel
BuildRequires:  libvorbis-devel
BuildRequires:  perl-generators
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  libmusicbrainz5-devel
BuildRequires:  automake autoconf libtool
BuildRequires:  python3-devel
BuildRequires: make

# some of the scripts in %%{_datadir}/%%{name}/scripts use which
Requires:       which
Requires:       hicolor-icon-theme

%description
gtkpod is a platform independent Graphical User Interface for Apple's
iPod using GTK3. It supports all current iPod models, including
the Mini, Photo, Shuffle, Nano, Video, Classic, Touch, and iPhone.

%package devel
Summary: Development files for the gtkpod
Requires: %{name} = %{version}-%{release}

%description devel
The gtkpod-devel package contains libraries and header files for
developing extensions for gtkpod.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pni "%{__python2} %{py2_shbang_opts}" .
%setup -q
%patch -P 0 -p1
%patch -P 1 -p0
%patch -P 2 -p0

%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

desktop-file-install \
    --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    --add-category="Audio" \
    --add-category="Video" \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

# delete libtool files
find %{buildroot} -name '*.la' -exec rm -f {} \;

%py3_shebang_fix %{buildroot}/usr/share/gtkpod/scripts/*

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog* README TODO TROUBLESHOOTING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}*
%dir %{_libdir}/gtkpod
%{_libdir}/gtkpod/*.plugin
%{_libdir}/gtkpod/*.so
%{_libdir}/*.so.*
%{_datadir}/glib-2.0/schemas/org.gtkpod.gschema.xml

%files devel
%{_includedir}/gtkpod
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
