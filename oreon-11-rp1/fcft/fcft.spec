%global source0_hash bb298772d625e7d917373d541456f34f1957a9e22b16f17f64158b2c3816563c

%global abi_ver 4

Name:           fcft
Version:        3.3.3
Release:        2%{?dist}
Summary:        Simple library for font loading and glyph rasterization

# main source:  MIT
# unicode/*:    Unicode-3.0
# nanosvg:      Zlib
License:        MIT AND Unicode-3.0 AND Zlib
URL:            https://codeberg.org/dnkl/%{name}
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
# Daniel Eklöf (Git signing) <daniel@ekloef.se>
Source2:        gpgkey-5BBD4992C116573F.asc

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.58.0

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist)
# require *-static for header-only library
BuildRequires:  tllist-static
# test dependencies: 'Serif' and 'emoji' fonts
BuildRequires:  font(dejavuserif)
BuildRequires:  font(notoemoji)

Provides:       bundled(nanosvg) = 0^20241219gea6a6ac

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
# license will be installed to the correct location with rpm macros
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

%check
%meson_test

%files
%license LICENSE
%license LICENSE.nanosvg
%license LICENSE.Unicode
%{_libdir}/lib%{name}.so.%{abi_ver}{,.*}
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/CHANGELOG.md
%{_docdir}/%{name}/README.md

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}*.3*

%changelog
%autochangelog
