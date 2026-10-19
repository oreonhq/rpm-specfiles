%global source0_hash 6625288b760d38a15c295051ecf66c556fcad21dd1516d6d661c2a582421ee0e
%global fullname org.xfce.Parole
%global minorversion 4.18
Name:           parole
Version:        4.18.2
Release:        1%{?dist}
Summary:        Media player for the Xfce desktop
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/applications/parole
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
Requires:       gstreamer1-plugins-good
Obsoletes:      %{name}-mozplugin <= 2.0.2-7
# oreon:deps
BuildRequires:  clutter-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libnotify-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  libxfce4util-devel
BuildRequires:  make
BuildRequires:  taglib-devel
BuildRequires:  xfconf-devel
# /oreon:deps
%description
Parole is a modern simple media player based on the GStreamer framework and 
written to fit well in the Xfce desktop. Parole features playback of local 
media files, DVD/CD and live streams. Parole is extensible via plugins.

The project still in its early developments stage, but already contains the 
following features:
* Audio playback
* Video playback with optional subtitle
* Playback of live sources

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains header files for developing plugins for 
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static --enable-gtk-doc --enable-clutter
%{make_build}
%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}
desktop-file-install                                    \
  --delete-original                                     \
  --remove-mime-type=video/x-totem-stream               \
  --dir=%{buildroot}%{_datadir}/applications            \
  %{buildroot}/%{_datadir}/applications/%{fullname}.desktop
sed -i 's/<\/em>//' %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
sed -i 's/<em>//' %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n parole-devel -f %{oreon_filedir}/parole-devel.list

%changelog

%autochangelog
