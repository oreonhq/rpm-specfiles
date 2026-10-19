%global source0_hash d43917174bbbc9aba5abb92402384ba7b09f4249339eac372d1ada2720e7aa4b
%global __provides_exclude_from ^%{_libdir}/%{name}/.*$
Name:		xreader
Version:	4.6.8
Release:        1%{?dist}
Summary:        Simple document viewer
License:	GPL-2.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:	shared-mime-info%{?_isa}
Requires:	gsettings-desktop-schemas%{?_isa}
Requires:	xapps%{?_isa}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Recommends:	yelp%{?_isa}
Recommends: %{name}-thumbnailer%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  mathjax
BuildRequires:  meson
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(kpathsea)
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xapp)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-packaging
BuildRequires:  t1lib-devel
BuildRequires:  texlive
BuildRequires:  yelp-tools
# /oreon:deps
%description
X-Apps Document Reader is a document viewer capable of displaying
multiple and single page document formats like PDF and PostScript.

%package libs
Summary:    xreader document viewer libraries
Requires:	%{name}-data = %{version}-%{release}
%description libs
This package contains the shared library files for %{name}.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the development files for %{name}.

%package doc
Summary:	Documentation files for %{name}
BuildArch:	noarch
%description doc
This package contains the documentation files for %{name}.

%package data
Summary: Support files for the %{name} document viewer
BuildArch: noarch
%description data
This package contains icons and other support files used by the
%{name} application and libraries.

%package thumbnailer
Summary: System thumbnailer using %{name} libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description thumbnailer
This package adds configuration to use %{name} as a thumbnailer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson	\
 -Ddeprecated_warnings=false \
 -Ddjvu=true \
 -Ddvi=true \
 -Depub=false \
 -Dt1lib=true \
 -Dpixbuf=true \
 -Dcomics=true \
 -Dintrospection=true \
 -Dhelp_files=true
%meson_build
%install
%meson_install
%{__sed} -i -e '/.*<project_group>.*/d' \
	%{buildroot}%{_metainfodir}/%{name}.appdata.xml
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{_bindir}/desktop-file-validate    \
	%{buildroot}%{_datadir}/applications/%{name}.desktop
%{_bindir}/appstream-util validate-relax --nonet    \
	%{buildroot}%{_metainfodir}/%{name}.appdata.xml
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n xreader-libs -f %{oreon_filedir}/xreader-libs.list
%files -n xreader-devel -f %{oreon_filedir}/xreader-devel.list
%files -n xreader-doc -f %{oreon_filedir}/xreader-doc.list
%files -n xreader-data -f %{oreon_filedir}/xreader-data.list
%files -n xreader-thumbnailer -f %{oreon_filedir}/xreader-thumbnailer.list

%changelog

%autochangelog
