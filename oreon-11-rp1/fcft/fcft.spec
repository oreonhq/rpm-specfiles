%global source0_hash bb298772d625e7d917373d541456f34f1957a9e22b16f17f64158b2c3816563c
%global abi_ver 4
Name:           fcft
Version:        3.3.3
Release:        1%{?dist}
Summary:        Simple library for font loading and glyph rasterization
License:        MIT AND Unicode-3.0 AND Zlib
URL:            https://codeberg.org/dnkl/%{name}
Source0:        https://codeberg.org/dnkl/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-5BBD4992C116573F.asc
Provides:       bundled(nanosvg) = 0^20241219gea6a6ac
# oreon:deps
BuildRequires:  font(dejavuserif)
BuildRequires:  font(notoemoji)
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist)
BuildRequires:  tllist-static
# /oreon:deps
%description
fcft is a small font loading and glyph rasterization library built
on top of FontConfig, FreeType2 and pixman.
It can load and cache fonts from a fontconfig-formatted name string,
e.g. Monospace:size=12, optionally with user configured fallback fonts.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp 3rd-party/nanosvg/LICENSE.txt LICENSE.nanosvg
cp unicode/license.txt LICENSE.Unicode

%build

%meson \
    -Dtest-text-shaping=true
%meson_build
%install
%meson_install
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n fcft-devel -f %{oreon_filedir}/fcft-devel.list

%changelog

%autochangelog
