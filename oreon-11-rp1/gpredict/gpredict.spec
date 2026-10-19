%global source0_hash 186907660a96a95e70df2212d9d783710bcf53079b1508eb55a13dbed60573bc
Name:           gpredict
Version:        2.5.2
Release:        1%{?dist}
Summary:        Real-time satellite tracking and orbit prediction program
License:        GPL-2.0-or-later
URL:            http://gpredict.oz9aec.net/
Source0:        https://github.com/csete/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source1:        gpredict.desktop
Source2:        gpredict.appdata.xml
Patch0:         build_fix.patch
Requires:      hamlib
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  goocanvas2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
