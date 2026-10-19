%global source0_hash f296c5c662886635d4cd597e8ac0afcde7982be4486533c2b7f095b268be8668
%bcond dvi %{undefined flatpak}
%bcond djvu %{undefined rhel}
%bcond gspell %{undefined rhel}
%bcond nautilus 0
%global __provides_exclude_from ^%{_libdir}/evince/
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/evince/ -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
%global libarchive_version 3.6.0
%global poppler_version 22.05.0
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           evince
Version:        48.4
Release:        1%{?dist}
Summary:        Document viewer
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND X11 AND MIT AND Afmparse
URL:            https://wiki.gnome.org/Apps/Evince
Source0:        https://download.gnome.org/sources/%{name}/48/%{name}-%{version}.tar.xz
Patch:          evince-46.3.1-kpathsea-header-files.patch
%if %{with gspell}
%endif
%if %{with dvi}
%endif
%if %{with djvu}
%endif
%if %{with nautilus}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-previewer%{?_isa} = %{version}-%{release}
Requires: %{name}-thumbnailer%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-nautilus < 43~alpha-2
# oreon:deps
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  djvulibre-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gi-docgen
BuildRequires:  libappstream-glib-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(adwaita-icon-theme)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(synctex)
BuildRequires:  systemd-rpm-macros
BuildRequires:  texlive-lib-devel
BuildRequires:  yelp-tools
# /oreon:deps
%description
Evince is simple multi-page document viewer. It can display and print
Portable Document Format (PDF), PostScript (PS) and Encapsulated PostScript
(EPS) files. When supported by the document format, evince allows searching
for text, copying text to the clipboard, hypertext navigation,
table-of-contents bookmarks and editing of forms.

 Support for other document formats such as DVI and DJVU can be added by
installing additional backends.

%package libs
Summary: Libraries for the evince document viewer
%if %{with djvu}
Recommends: %{name}-djvu%{?_isa} = %{version}-%{release}
%endif
Requires:   libarchive%{?_isa} >= %{libarchive_version}
Requires:   poppler-glib%{?_isa} >= %{poppler_version}
%description libs
This package contains shared libraries needed for evince

%package devel
Summary: Support for developing backends for the evince document viewer
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Recommends: gi-docgen-fonts
%description devel
This package contains libraries and header files needed for evince
backend development.

%package dvi
Summary: Evince backend for dvi files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: texlive-collection-fontsrecommended
%description dvi
This package contains a backend to let evince display dvi files.

%if %{with djvu}
%package djvu
Summary: Evince backend for djvu files
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description djvu
This package contains a backend to let evince display djvu files.
%endif

%if %{with nautilus}
%package nautilus
Summary: Evince extension for nautilus
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: nautilus%{?_isa}
%description nautilus
This package contains the evince extension for the nautilus file manager.
It adds an additional tab called "Document" to the file properties dialog.
%endif

%package thumbnailer
Summary: Evince thumbnailer
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description thumbnailer
This package brings the Evince thumbnailer independently from Evince.

%package previewer
Summary: Evince previewer
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description previewer
This package brings the Evince previewer independently from Evince.
It provides the printing preview for the GTK printing dialog.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
        -Dcomics=enabled \
%if %{with dvi}
        -Ddvi=enabled \
%else
        -Ddvi=disabled \
%endif
%if %{with djvu}
        -Ddjvu=enabled \
%else
        -Ddjvu=disabled \
%endif
%if %{with gspell}
        -Dgspell=enabled \
%else
        -Dgspell=disabled \
%endif
        -Dxps=enabled \
%if 0%{?flatpak}
        -Dsystemduserunitdir=no \
%endif
        -Dnautilus=false \
        -Dps=enabled
%meson_build
%install
%meson_install
%find_lang evince --with-gnome
mkdir -p %{buildroot}%{_datadir}/applications
rm -f %{buildroot}%{_metainfodir}/evince-pdfdocument.metainfo.xml
rm -f %{buildroot}%{_metainfodir}/evince-psdocument.metainfo.xml
rm -f %{buildroot}%{_metainfodir}/evince-tiffdocument.metainfo.xml
rm -f %{buildroot}%{_metainfodir}/evince-comicsdocument.metainfo.xml
rm -f %{buildroot}%{_metainfodir}/evince-xpsdocument.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Evince.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Evince.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Evince-previewer.desktop
%files -f %{oreon_filedir}/main.list
%files -n evince-libs -f %{oreon_filedir}/evince-libs.list
%files -n evince-devel -f %{oreon_filedir}/evince-devel.list
%files -n evince-dvi -f %{oreon_filedir}/evince-dvi.list
%files -n evince-djvu -f %{oreon_filedir}/evince-djvu.list
%files -n evince-thumbnailer -f %{oreon_filedir}/evince-thumbnailer.list
%files -n evince-previewer -f %{oreon_filedir}/evince-previewer.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 48.1-2
- Prepare for Oreon 11 (RP1)
