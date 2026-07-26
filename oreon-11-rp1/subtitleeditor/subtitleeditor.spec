%global source0_hash 1bfcd00efb1d0aeae55ac32129d5007a29697cd32351a52306675eabfda7dbb1

Name:           subtitleeditor
Version:        0.55.0
Release:        2%{?dist}
Summary:        GTK+3 tool to edit subtitles for GNU/Linux/*BSD

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://subtitleeditor.github.io/subtitleeditor/
Source0:        https://github.com/subtitleeditor/subtitleeditor/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtkmm30-devel
BuildRequires:  glibmm24-devel >= 2.16.3
BuildRequires:  libappstream-glib
BuildRequires:  libxml++-devel >= 2.20
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  ccache
BuildRequires:  gstreamermm-devel

# For spell checking (Optional)
BuildRequires:  enchant2-devel >= 2.2.0
# ISO-CODES 639 + 3166 (Optional)
BuildRequires:  iso-codes-devel

%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/.*/lib.*\\.so$

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

#remove .la's
find %{buildroot} -name "*.la" | xargs rm -v

#remove useless development files
rm -v %{buildroot}%{_libdir}/lib%{name}.so

%find_lang %{name}

desktop-file-validate \
  %{buildroot}%{_datadir}/applications/org.kitone.%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kitone.%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.kitone.%{name}.appdata.xml
%{_datadir}/applications/org.kitone.%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_libdir}/lib%{name}.so.*
%{_libdir}/%{name}/

%changelog
%autochangelog
