%global source0_hash e759c4bae0b17b202a7c0f8281ff016f819b502780d3e77b46fe8767e7498e43

Name:           gpredict
Version:        2.2.1
Release:        24%{?dist}
Summary:        Real-time satellite tracking and orbit prediction program
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://gpredict.oz9aec.net/
Source0:        https://github.com/csete/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source1:        gpredict.desktop
Source2:        gpredict.appdata.xml
Patch0:         build_fix.patch

BuildRequires: gtk3-devel
BuildRequires: glib2-devel
BuildRequires: curl-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: goocanvas2-devel
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: make
Requires:      hamlib
Requires:      hicolor-icon-theme

%description
Gpredict is a real time satellite tracking and orbit prediction
program written using the Gtk+ widgets. Gpredict is targeted mainly
towards ham radio operators but others interested in satellite
tracking may find it useful as well. Gpredict uses the SGP4/SDP4
algorithms, which are compatible with the NORAD Keplerian elements.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%{configure} --prefix=%{_prefix}
%make_build

%install
%make_install

%find_lang %{name}
desktop-file-install --dir %{buildroot}/%{_datadir}/applications/ %{SOURCE1}
install -D -p -m644 pixmaps/logos/gpredict_icon_color.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -D -p -m644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/appdata/*%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/gpredict/icons/*
%{_datadir}/pixmaps/gpredict/maps/*
%{_datadir}/pixmaps/gpredict/logos/*
%{_datadir}/pixmaps/gpredict-icon.png
%{_mandir}/man1/gpredict*

%changelog
%autochangelog
