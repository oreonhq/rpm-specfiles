%global source0_hash df82f6b264f98d11eeb80d85bbb10c7935fcd69c7abae1d610ce49b9a0437faf
Name:		openslide
Version:	4.0.1
Release:        1%{?dist}
Summary:        C library for reading virtual slides
License:	LGPL-2.1-only
URL:		https://openslide.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libjpeg-turbo-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdicom)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.

%package	devel
Summary:	Development files for %{name}
License:	LGPL-2.1-only AND MIT
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	bundled(js-jquery) = 3.6.0
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package   	tools
Summary:	Command line tools for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	tools
The %{name}-tools package contains command line tools for working
with virtual slides.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Ddoc=disabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n openslide-devel -f %{oreon_filedir}/openslide-devel.list
%files -n openslide-tools -f %{oreon_filedir}/openslide-tools.list

%changelog

%autochangelog
