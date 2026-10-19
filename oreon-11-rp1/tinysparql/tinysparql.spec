%global source0_hash 40e3e3ae9811ae07a94ac7dfe8259f218679ebb1c9bc98d7ab345b2405926b57
%global systemd_units tinysparql-xdg-portal-3.service
%global tarball_version %(echo %{version} | tr '~' '.')
%global tracker_obsoletes_version 3.8
%if 0%{?rhel} || (0%{?oreon} >= 11)
%bcond libstemmer 0
%else
%bcond libstemmer 1
%endif
Name:           tinysparql
Version:        3.12.0
Release:        1%{?dist}
Summary:        Desktop-neutral metadata database and search tool
License:        GPL-2.0-or-later
URL:            https://gnome.pages.gitlab.gnome.org/tinysparql/
Source0:        https://download.gnome.org/sources/%{name}/3.12/%{name}-%{version}.tar.xz
%if %{with libstemmer}
%endif
Obsoletes:      tracker < %{tracker_obsoletes_version}
Provides:       tracker = %{version}-%{release}
Provides:       tracker%{?_isa} = %{version}-%{release}
Requires: libtinysparql%{?_isa} = %{version}-%{release}
Recommends: localsearch%{?_isa}
# oreon:deps
BuildRequires:  /usr/bin/dbus-run-session
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  libstemmer-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3-gobject
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
# /oreon:deps
%description
Tinysparql is a powerful desktop-neutral first class object database,
tag/metadata database and search tool.

It consists of a common object database that allows entities to have an
almost infinite number of properties, metadata (both embedded/harvested as
well as user definable), a comprehensive database of keywords/tags and
links to other entities.

It provides additional features for file based objects including context
linking and audit trails for a file object.

Metadata indexers are provided by the localsearch package.

%package -n     libtinysparql
Summary:        Libtinysparql library
License:        LGPL-2.1-or-later
Requires:       libsoup3%{?_isa}
Recommends:     %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      libtracker-sparql < %{tracker_obsoletes_version}
Provides:       libtracker-sparql = %{version}-%{release}
Provides:       libtracker-sparql%{?_isa} = %{version}-%{release}
%description -n libtinysparql
This package contains the libtinysparql library.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-2.1-or-later
Requires:       libtinysparql%{?_isa} = %{version}-%{release}
Obsoletes:      tracker-devel < %{tracker_obsoletes_version}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
License:        LicenceRef-Fedora-Public-Domain AND LGPL-2.1-or-later AND GPL-2.0-or-later
%description doc
This package contains the documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
  -Dunicode_support=icu \
  -Dsystemd_user_services_dir=%{_userunitdir} \
%if %{without libstemmer}
  -Dstemmer=disabled \
%endif
  %{nil}
%meson_build
%install
%meson_install
%find_lang tinysparql3
%oreon_autofiles libtinysparql usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_user_post tinysparql-xdg-portal-3.service
%preun

%systemd_user_preun tinysparql-xdg-portal-3.service
%postun

%systemd_user_postun_with_restart tinysparql-xdg-portal-3.service
%files -f %{oreon_filedir}/main.list
%files -n libtinysparql -f %{oreon_filedir}/libtinysparql.list
%files -n tinysparql-devel -f %{oreon_filedir}/tinysparql-devel.list
%files -n tinysparql-doc -f %{oreon_filedir}/tinysparql-doc.list

%changelog

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.1-3
- Rebuild

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.1-2
- Disable libstemmer on %%{?oreon} (no stemmer package in tree yet)

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.1-1
- Prep for or11
