%global         clutter_version 1.23.7
%global         gtk3_version 3.21.0

%global         api_ver 1.0

Name:           clutter-gtk
Version:        1.8.4
Release:        24%{?dist}
Summary:        A basic GTK clutter widget

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.clutter-project.org
Source0:        http://download.gnome.org/sources/clutter-gtk/1.8/clutter-gtk-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 521493ec038973c77edcb8bc5eac23eed41645117894aaee7300b2487cb42b06
%global source0_file clutter-gtk-1.8.4.tar.xz
# oreon url source checksums end

BuildRequires:  clutter-devel >= %{clutter_version}
BuildRequires:  gtk3-devel >= %{gtk3_version}
BuildRequires:  gobject-introspection-devel
BuildRequires: make

Requires:       clutter%{?_isa} >= %{clutter_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}

%description
clutter-gtk is a library which allows the embedding of a Clutter
canvas (or "stage") into a GTK+ application, as well as embedding
GTK+ widgets inside the stage.

%package devel
Summary:        Clutter-gtk development environment
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
clutter-gtk.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/clutter-gtk-1.8.4.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "521493ec038973c77edcb8bc5eac23eed41645117894aaee7300b2487cb42b06" || { echo "oreon: Source0 SHA256 mismatch for clutter-gtk-1.8.4.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q


%build

%configure
make %{?_smp_mflags} V=1


%install
%make_install

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%find_lang cluttergtk-1.0

%check
make check %{?_smp_mflags} V=1


%ldconfig_scriptlets

%files -f cluttergtk-1.0.lang
%license COPYING
%doc NEWS
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/GtkClutter-%{api_ver}.typelib

%files devel
%{_includedir}/clutter-gtk-%{api_ver}/
%{_libdir}/pkgconfig/clutter-gtk-%{api_ver}.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/GtkClutter-%{api_ver}.gir
%{_datadir}/gtk-doc/html/clutter-gtk-1.0

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.4-24
- Prepare for Oreon 11 (RP1)
