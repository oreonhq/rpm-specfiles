%global source0_hash 87187e49d301c510e6964098cdb612126bf030d2a875fd799eadcad3eae56dab

Name:           klavaro
Version:        3.14
Release:        10%{?dist}
Summary:        Typing tutor

License:        GPL-3.0-or-later
URL:            http://klavaro.sourceforge.net/en/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3-docutils
BuildRequires:  libcurl-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  gtkdatabox-devel

Requires:       hicolor-icon-theme
Recommends:     espeak

%description
Klavaro  is a touch typing tutor that is very flexible and supports
customizable keyboard layouts. Users can edit and save new or unknown
keyboard layouts, as the basic course provided by the program was
designed to not depend on specific layouts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-rpath --enable-static=no
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|$(DATADIRNAME)|share|' data/Makefile.in

%make_build

%install
%make_install

# Adding folder for scores saving
mkdir -p %{buildroot}%{_localstatedir}/games/%{name}
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%attr(0755, root, games) %{_localstatedir}/games/%{name}
%{_mandir}/man*/*.*
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
