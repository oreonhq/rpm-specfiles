%global source0_hash c739688dc3e8e7de6bd836886c827bddbed6ee3259831cf82f035f0d2c9c7636

Name:     gsequencer
Version:  8.0.13
Release:  2%{?dist}
Summary:  Audio processing engine
# Automatically converted from old format: GPLv3+ and AGPLv3+ and GFDL - review is highly recommended.
License:  GPL-3.0-or-later AND AGPL-3.0-or-later AND LicenseRef-Callaway-GFDL
URL:      http://nongnu.org/gsequencer
Source:   http://download.savannah.gnu.org/releases/gsequencer/8.0.x/%{name}-%{version}.tar.gz
ExcludeArch:        i686
BuildRequires:      make
BuildRequires:      libtool
BuildRequires:      chrpath
BuildRequires:      docbook-style-xsl
BuildRequires:      gettext-devel
BuildRequires:      libxcrypt-devel
BuildRequires:      gtk-doc
BuildRequires:      dblatex
BuildRequires:      fop
BuildRequires:      libstdc++-devel
BuildRequires:      nghttp2
BuildRequires:      pkgconfig(uuid)
BuildRequires:      pkgconfig(libxml-2.0)
BuildRequires:      pkgconfig(libsoup-3.0)
BuildRequires:      pkgconfig(alsa)
BuildRequires:      pkgconfig(fftw3)
BuildRequires:      ladspa-devel
BuildRequires:      dssi-devel
BuildRequires:      lv2-devel
BuildRequires:      gstreamer1-plugins-base
BuildRequires:      gstreamer1-plugins-good
BuildRequires:      pkgconfig(jack)
BuildRequires:      pkgconfig(samplerate)
BuildRequires:      pkgconfig(sndfile)
BuildRequires:      pkgconfig(libinstpatch-1.0)
BuildRequires:      pkgconfig(gtk4)
BuildRequires:      pkgconfig(json-glib-1.0)
BuildRequires:      pkgconfig(poppler-glib)
BuildRequires:      pkgconfig(gstreamer-1.0)
BuildRequires:      pkgconfig(gstreamer-app-1.0)
BuildRequires:      pkgconfig(gstreamer-video-1.0)
BuildRequires:      pkgconfig(gstreamer-audio-1.0)
BuildRequires:      pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:      pkgconfig(gobject-introspection-1.0)
BuildRequires:      pkgconfig(libpulse)
BuildRequires:      CUnit-devel
BuildRequires:      desktop-file-utils
BuildRequires:      xorg-x11-server-Xvfb
Requires:           xml-common

%description
Advanced Gtk+ Sequencer audio processing engine is an audio
sequencer application supporting LADPSA, DSSI and Lv2 plugin
format. It can output to Pulseaudio server, JACK audio connection
kit, ALSA and OSS4.

You may add multiple sinks, mix different sources by producing
sound with different sequencers. Further it features a pattern
and piano roll. Additional there is a automation editor to
automate ports.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N

%build
%undefine _strict_symbol_defs_build
autoreconf -fi
export CPPFLAGS='-DAGS_CSS_FILENAME=\"/usr/share/gsequencer/styles/ags.css\" -DAGS_ANIMATION_FILENAME=\"/usr/share/gsequencer/images/gsequencer-800x450.png\" -DAGS_LOGO_FILENAME=\"/usr/share/gsequencer/images/ags.png\" -DAGS_LICENSE_FILENAME=\"/usr/share/licenses/gsequencer/COPYING\" -DAGS_ONLINE_HELP_A4_PDF_FILENAME=\"/usr/share/doc/gsequencer/pdf/user-manual-a4.pdf\" -DAGS_ONLINE_HELP_LETTER_PDF_FILENAME=\"/usr/share/doc/gsequencer/pdf/user-manual-letter.pdf\"'
export CFLAGS="%{build_cflags} -Wno-error=incompatible-pointer-types"
export GSEQUENCER_LDFLAGS="%{build_ldflags} -L%{_libdir}"
export MIDI2XML_LDFLAGS="%{build_ldflags} -L%{_libdir}"
%configure FO_XSL="/usr/share/sgml/docbook/xsl-stylesheets/fo/docbook.xsl" HTMLHELP_XSL="/usr/share/sgml/docbook/xsl-stylesheets/htmlhelp/htmlhelp.xsl" --disable-upstream-gtk-doc --enable-introspection --disable-oss --enable-gtk-doc --enable-gtk-doc-html
%make_build
%make_build html
%make_build fix-local-html
%make_build pdf

%install
%make_install
%make_install install-compress-changelog
%make_install install-html-mkdir
%make_install install-html-mkdir-links
%make_install install-html
%make_install install-pdf-mkdir
%make_install install-pdf
chrpath --delete %{buildroot}%{_bindir}/gsequencer
chrpath --delete %{buildroot}%{_bindir}/midi2xml
chrpath --delete %{buildroot}%{_libdir}/libags.so*
chrpath --delete %{buildroot}%{_libdir}/libags_server.so*
chrpath --delete %{buildroot}%{_libdir}/libags_thread.so*
chrpath --delete %{buildroot}%{_libdir}/libags_gui.so*
chrpath --delete %{buildroot}%{_libdir}/libags_audio.so*
chrpath --delete %{buildroot}%{_libdir}/libgsequencer.so*
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/doc-base/
%find_lang %{name}

%check
xvfb-run --server-args="-screen 0 1920x1080x24" -a make check
desktop-file-validate %{buildroot}/%{_datadir}/applications/gsequencer.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%{_libdir}/libags.so.*
%{_libdir}/libags_thread.so.*
%{_libdir}/libags_server.so.*
%{_libdir}/libags_gui.so.*
%{_libdir}/libags_audio.so.*
%{_libdir}/libgsequencer.so.*
%{_libdir}/girepository-1.0
%{_bindir}/gsequencer
%{_bindir}/midi2xml
%{_mandir}/man1/gsequencer.1*
%{_mandir}/man1/midi2xml.1*
%{_datadir}/gsequencer/
%{_datadir}/xml/gsequencer/
%{_datadir}/icons/hicolor/*/apps/gsequencer.png
%{_datadir}/icons/hicolor/scalable/apps/gsequencer.svg
%{_datadir}/metainfo/
%{_datadir}/mime/packages/
%{_docdir}/gsequencer/
%{_datadir}/applications/gsequencer.desktop

%package devel
Summary:  Advanced Gtk+ Sequencer library development files
Requires: %{name}%{_isa} = %{version}-%{release}
%description devel
Advanced Gtk+ Sequencer library development files.

%files devel
%{_includedir}/ags/
%{_libdir}/libags.so
%{_libdir}/libags_thread.so
%{_libdir}/libags_server.so
%{_libdir}/libags_gui.so
%{_libdir}/libags_audio.so
%{_libdir}/libgsequencer.so
%{_datadir}/gir-1.0
%{_libdir}/pkgconfig/libags.pc
%{_libdir}/pkgconfig/libags_audio.pc
%{_libdir}/pkgconfig/libags_gui.pc
%{_libdir}/pkgconfig/libgsequencer.pc

%package -n gsequencer-devel-doc
Summary:  Advanced Gtk+ Sequencer library development documentation
BuildArch: noarch
%description -n gsequencer-devel-doc
Advanced Gtk+ Sequencer library development documentation.

%files -n gsequencer-devel-doc
%{_datadir}/gtk-doc/
%{_datadir}/doc/libags-audio-doc/

%changelog
%autochangelog
