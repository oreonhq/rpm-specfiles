%global source0_hash none
Name:           opentype-sanitizer
Version:        9.3.0
Release:        1%{?dist}
Summary:        Parses and serializes OpenType/WOFF/WOFF2 font files
License:        BSD-3-Clause
URL:            https://github.com/khaledhosny/ots
Source0:        ots-%{version}-filtered.tar.xz
Source1:        get-source.py
Source2:        ots-%{version}-excluded-font-checksums.txt
ExcludeArch:    %{ix86}
%global common_description %{expand:
The OpenType Sanitizer (OTS) parses and serializes OpenType files (OTF, TTF)
and WOFF and WOFF2 font files, validating them and sanitizing them as it goes.
The C library is integrated into Chromium and Firefox, and also simple command
line tools to check files offline in a Terminal.
The CSS font-face property is great for web typography. Having to use images in
order to get the correct typeface is a great sadness; one should be able to use
vectors.
However, on many platforms the system-level TrueType font renderers have never
been part of the attack surface before, and putting them on the front line is a
scary proposition... Especially on platforms like Windows, where it’s a
closed-source blob running with high privilege.}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description %{common_description}

%prep

%autosetup -n ots-%{version} -p1
# Remove bundled dependencies
rm -rf third_party
# Disable tests that use fonts that were filtered out for license issues.
sed -r -i "/$(tr '\n' '|' < '%{SOURCE2}' | sed -r 's@\|+$@@')/d" \
    tests/meson.build

%conf
# gtest 1.17.0 requires at least C++17
%meson -Dcpp_std=c++17

%build

%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
