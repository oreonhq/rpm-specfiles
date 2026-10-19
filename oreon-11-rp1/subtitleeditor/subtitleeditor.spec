%global source0_hash 333598a35facfc2c1d6b9c53f9e722c21044c7025bfc02d596ac40a853f976b3
Name:           subtitleeditor
Version:        0.56.2
Release:        1%{?dist}
Summary:        GTK+3 tool to edit subtitles for GNU/Linux/*BSD
License:        GPL-3.0-or-later
URL:            https://subtitleeditor.github.io/subtitleeditor/
Source0:        https://github.com/subtitleeditor/subtitleeditor/archive/%{version}/%{name}-%{version}.tar.gz
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*/lib.*\\.so$
# oreon:deps
BuildRequires:  ccache
BuildRequires:  desktop-file-utils
BuildRequires:  enchant2-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glibmm24-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  gstreamermm-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  libxml++-devel
BuildRequires:  make
# /oreon:deps
%description
Subtitle Editor is a GTK+3 tool to edit subtitles for GNU/Linux/*BSD. It can be
used for new subtitles or as a tool to transform, edit, correct and refine
existing subtitle. This program also shows sound waves, which makes it easier
to synchronize subtitles to voices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

autoreconf -fiv
%configure \
       --disable-debug \
       --disable-static \
       --disable-gl \
       --enable-ccache
%make_build
%install
%make_install
find %{buildroot} -name "*.la" | xargs rm -v
rm -v %{buildroot}%{_libdir}/lib%{name}.so
%find_lang %{name}
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.kitone.%{name}.desktop
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kitone.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
