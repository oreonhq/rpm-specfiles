%global source0_hash 39ff9a7df25b319b0e0e74fe4161de17720a32bf73dea8096647e13efcd89f9d
Name:		libskk
Version:	1.0.4
Release:        19%{?dist}
Summary:        Library to deal with Japanese kana-to-kanji conversion method
License:	GPL-3.0-or-later
URL:		http://github.com/ueno/libskk
Source0:        https://github.com/ueno/libskk/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:		libskk-1.0.5-int-conversion.patch
Patch:		libskk-1.0.5-json-escape.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  json-glib-devel
BuildRequires:  libfep-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  vala
# /oreon:deps
%description
The libskk project aims to provide GObject-based interface of Japanese
input methods.  Currently it supports SKK (Simple Kana Kanji) with
various typing rules including romaji-to-kana, AZIK, ACT, TUT-Code,
T-Code, and NICOLA.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:	Tools for %{name}
BuildRequires:	libfep-devel
BuildRequires: make
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	tools
The %{name}-tools package contains tools for developing applications
that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
find -name '*.vala' -exec touch {} \;

%build

autoreconf -fi
%configure --disable-static --enable-fep
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libskk-devel -f %{oreon_filedir}/libskk-devel.list
%files -n libskk-tools -f %{oreon_filedir}/libskk-tools.list

%changelog

%autochangelog
