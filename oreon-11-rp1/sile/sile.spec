%global source1_hash 8177f97513213526df2cf6184d8ff986c675afb514d4e68a404010521b880643
%global source0_hash 7f89bedecedabb5168250ad9dd80c09ed289c8e88c3d0d756d2d1d92ee065e04
Name:      sile
Version:   0.14.17
Release:        1%{?dist}
Summary:        The SILE Typesetter
License:   MIT
URL:       https://sile-typesetter.org/
Source0:        https://github.com/sile-typesetter/sile/releases/download/v%{version}/sile-%{version}.tar.xz
Source1:   https://raw.githubusercontent.com/sile-typesetter/libtexpdf/736a5e7530c13582ea704a061a358d0caa774916/LICENSE#/LICENSE-libtexpdf
Requires: lua-cassowary
Requires: lua-cldr
Requires: lua-cliargs
Requires: lua-cosmo
Requires: lua-expat
Requires: lua-filesystem
Requires: lua-fluent
Requires: lua-linenoise
Requires: lua-loadkit
Requires: lua-lpeg
Requires: lua-luarepl
Requires: lua-penlight
Requires: lua-sec
Requires: lua-socket
Requires: lua-luautf8
Requires: lua-vstruct
Requires: lua-zlib
Requires: libtexpdf%{?_isa} = %{version}-%{release}
Recommends: font(gentiumplus)
Suggests:   font(libertinusmath)
Suggests:   font(libertinussans)
Suggests:   font(libertinusserif)
Suggests:   font(hack)
Provides: bundled(lua-lunamark)
# oreon:deps
BuildRequires:  /usr/bin/pdfinfo
BuildRequires:  automake
BuildRequires:  font(gentiumplus)
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  harfbuzz-devel
BuildRequires:  jq
BuildRequires:  libtool
BuildRequires:  lua
BuildRequires:  lua-cassowary
BuildRequires:  lua-cldr
BuildRequires:  lua-cliargs
BuildRequires:  lua-cosmo
BuildRequires:  lua-devel
BuildRequires:  lua-expat
BuildRequires:  lua-filesystem
BuildRequires:  lua-fluent
BuildRequires:  lua-linenoise
BuildRequires:  lua-loadkit
BuildRequires:  lua-lpeg
BuildRequires:  lua-luarepl
BuildRequires:  lua-luautf8
BuildRequires:  lua-penlight
BuildRequires:  lua-rpm-macros
BuildRequires:  lua-sec
BuildRequires:  lua-socket
BuildRequires:  lua-srpm-macros
BuildRequires:  lua-vstruct
BuildRequires:  lua-zlib
BuildRequires:  make
# /oreon:deps
%description
SILE is a typesetting system; its job is to produce beautiful printed documents.
Conceptually, SILE is similar to TeX—from which it borrows some concepts and
even syntax and algorithms—but the similarities end there.
Rather than being a derivative of the TeX family SILE is a new typesetting and
layout engine written from the ground up using modern technologies and borrowing
some ideas from graphical systems such as InDesign.

%package -n libtexpdf
Summary: A PDF library extracted from TeX's dvipdfmx
License: GPL-2.0-only
%description -n libtexpdf
%{summary}.

%package -n libtexpdf-devel
Summary:  Development files for libtexpdf
License:  GPL-2.0-only
Requires: libtexpdf%{?_isa} = %{version}-%{release}
%description -n libtexpdf-devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
cp %{SOURCE1} LICENSE-libtexpdf

%build

%configure --disable-static --with-system-luarocks
%make_build all
%install
%make_install
%oreon_autofiles libtexpdf usr/*/lib*.so.*
%oreon_autofiles libtexpdf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export SILE_PATH=$(pwd)
echo -n '\document{foo}' | ./sile - -o foo.pdf
%files -f %{oreon_filedir}/main.list
%files -n libtexpdf -f %{oreon_filedir}/libtexpdf.list
%files -n libtexpdf-devel -f %{oreon_filedir}/libtexpdf-devel.list

%changelog

%autochangelog
