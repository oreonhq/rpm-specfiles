%global source12_hash a54dc8488f8193bf30c3820cf6f261f911f9d328d699e1a1b8042641554cec70
%global source11_hash a4bbe688531db7853383649e17b67d7ded1d3a2492f5c3f44f715a6a3919b9ac
%global source10_hash 257cafd9c63c0c29f77b357eb4143f574149ac45e26596c3db9997451a64fbb0
%global source0_hash 01c0457472c38ea5bd1c3b5ada5e368271cb550be7a4ca4a0b4634e9913f6cc2
%bcond check 1
%global debug_package %{nil}
%global crate ab_glyph
Name:           rust-ab_glyph
Version:        0.2.32
Release:        1%{?dist}
Summary:        API for loading, scaling, positioning and rasterizing OpenType font glyphs
License:        Apache-2.0
URL:            https://crates.io/crates/ab_glyph
Source0:        https://static.crates.io/crates/ab_glyph/ab_glyph-%{version}.crate
Source10:       https://github.com/alexheretic/ab-glyph/raw/refs/tags/ab-glyph-%{version}/dev/fonts/Cantarell-VF.otf
Source11:       https://github.com/alexheretic/ab-glyph/raw/refs/tags/ab-glyph-%{version}/dev/fonts/Exo2-Light.otf
Source12:       https://github.com/alexheretic/ab-glyph/raw/refs/tags/ab-glyph-%{version}/dev/fonts/OpenSans-Italic.ttf
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        API for loading, scaling, positioning and rasterizing OpenType font glyphs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gvar-alloc-devel
Summary:        API for loading, scaling, positioning and rasterizing OpenType font glyphs
BuildArch:      noarch
%description -n %{name}+gvar-alloc-devel

This package contains library source intended for building other packages which
use the "gvar-alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        API for loading, scaling, positioning and rasterizing OpenType font glyphs
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+variable-fonts-devel
Summary:        API for loading, scaling, positioning and rasterizing OpenType font glyphs
BuildArch:      noarch
%description -n %{name}+variable-fonts-devel

This package contains library source intended for building other packages which
use the "variable-fonts" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

install -D -t src/../../dev/fonts/ -m 0644 -p \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ab_glyph-devel -f %{oreon_filedir}/rust-ab_glyph-devel.list

%changelog

%autochangelog
