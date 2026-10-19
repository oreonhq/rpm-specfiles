%global source0_hash 4bf45440ce7a899f2eca4d20343d31fc620fa2a3fe53bb929de244305330e930
%if 0%{?flatpak}
%global domain_ontology org.gnome.Music
%else
%global domain_ontology org.freedesktop
%endif
%global with_enca 1
%global with_ffmpeg 1
%global with_libcue 1
%global with_totem_pl_parser 1
%global tinysparql_version 3.8
%global systemd_units localsearch-3.service localsearch-control-3.service localsearch-writeback-3.service
%global __provides_exclude_from ^%{_libdir}/localsearch-3.0/
%global __requires_exclude ^(libtracker-extract\.so|libextract-.*\.so|libwriteback-.*\.so)
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           localsearch
Version:        3.12.0
Release:        1%{?dist}
Summary:        Localsearch and metadata extractors
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gnome.pages.gitlab.gnome.org/localsearch/
Source0:        https://download.gnome.org/sources/%{name}/3.%{with_enca}2/%{name}-%{version}.tar.xz
%if 0%{?with_enca}
%endif
%if 0%{?with_ffmpeg}
%endif
%if 0%{?with_libcue}
%endif
%if 0%{?with_totem_pl_parser}
%endif
%if !0%{?flatpak}
%endif
Obsoletes:      tracker-miners < 3.8
Provides:       tracker-miners = %{version}-%{release}
Provides:       tracker-miners%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gexiv2-0.16)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libosinfo-1.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(tinysparql-3.0)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  python3-dbusmock
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Tinysparql is a powerful desktop-neutral first class object database,
tag/metadata database and search tool.

This package contains various miners and metadata extractors for tinysparql.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
%if 0%{?flatpak}
  -Dwriteback=false \
  -Dsystemd_user_services=false \
  -Diso=disabled \
  -Dbattery_detection=none \
  -Ddomain_prefix=%{domain_ontology} \
%endif
%if ! 0%{?with_libcue}
  -Dcue=disabled \
%endif
%if ! 0%{?with_ffmpeg}
  -Dlibav=disabled \
%endif
%if ! 0%{?flatpak}
  -Dsystemd_user_services_dir=%{_userunitdir} \
%endif
%if ! 0%{?with_totem_pl_parser}
  -Dplaylist=disabled \
%endif
  %{nil}
%meson_build
%install
%meson_install
%find_lang localsearch3
%oreon_autofiles main

%post

%systemd_user_post %{systemd_units}
%preun

%systemd_user_preun %{systemd_units}
%postun

%systemd_user_postun_with_restart %{systemd_units}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
