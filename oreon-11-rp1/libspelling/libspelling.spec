# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 56e3f01a3a18b575beea4c34349f99cdaba316e1f7c271b1231f7bcf5d9af73b
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           libspelling
Version:        0.4.10
Release:        %autorelease
Summary:        Spellcheck library for GTK 4
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libspelling
Source:         https://download.gnome.org/sources/libspelling/0.4/libspelling-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# for vapigen
BuildRequires:  vala
BuildRequires:  gi-docgen


%description
A spellcheck library for GTK 4.  This library is heavily based upon GNOME Text
Editor and GNOME Builder's spellcheck implementation.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%oreon_verify_sources
%autosetup -n libspelling-%{version}


%build
%meson -Ddocs=false
%meson_build


%install
%meson_install
%find_lang libspelling


%check
%meson_test


%files -f libspelling.lang
%license COPYING
%doc NEWS
%{_libdir}/libspelling-1.so.2*
%{_libdir}/girepository-1.0/Spelling-1.typelib


%files devel
%{_includedir}/libspelling-1
%{_libdir}/libspelling-1.so
%{_libdir}/pkgconfig/libspelling-1.pc
%{_datadir}/gir-1.0/Spelling-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libspelling-1.deps
%{_datadir}/vala/vapi/libspelling-1.vapi


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.10-1
- Prepare for Oreon 11 (RP1)
