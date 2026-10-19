%global source0_hash 7b5ef0006ac9ab233c38522f5ae99cae3625151de8f706cacee1cba4b8e2832a
%bcond check 0
%global debug_package %{nil}
%global crate encoding_rs
Name:           rust-encoding_rs
Version:        0.8.41
Release:        1%{?dist}
Summary:        A Gecko-oriented implementation of the Encoding Standard
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause
URL:            https://crates.io/crates/encoding_rs
Source0:        https://static.crates.io/crates/encoding_rs/encoding_rs-%{version}.crate
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
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+any_all_workaround-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+any_all_workaround-devel

This package contains library source intended for building other packages which
use the "any_all_workaround" feature of the "%{crate}" crate.

%package     -n %{name}+fast-big5-hanzi-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+fast-big5-hanzi-encode-devel

This package contains library source intended for building other packages which
use the "fast-big5-hanzi-encode" feature of the "%{crate}" crate.

%package     -n %{name}+fast-gb-hanzi-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+fast-gb-hanzi-encode-devel

This package contains library source intended for building other packages which
use the "fast-gb-hanzi-encode" feature of the "%{crate}" crate.

%package     -n %{name}+fast-hangul-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+fast-hangul-encode-devel

This package contains library source intended for building other packages which
use the "fast-hangul-encode" feature of the "%{crate}" crate.

%package     -n %{name}+fast-hanja-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+fast-hanja-encode-devel

This package contains library source intended for building other packages which
use the "fast-hanja-encode" feature of the "%{crate}" crate.

%package     -n %{name}+fast-kanji-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+fast-kanji-encode-devel

This package contains library source intended for building other packages which
use the "fast-kanji-encode" feature of the "%{crate}" crate.

%package     -n %{name}+fast-legacy-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+fast-legacy-encode-devel

This package contains library source intended for building other packages which
use the "fast-legacy-encode" feature of the "%{crate}" crate.

%package     -n %{name}+less-slow-big5-hanzi-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+less-slow-big5-hanzi-encode-devel

This package contains library source intended for building other packages which
use the "less-slow-big5-hanzi-encode" feature of the "%{crate}" crate.

%package     -n %{name}+less-slow-gb-hanzi-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+less-slow-gb-hanzi-encode-devel

This package contains library source intended for building other packages which
use the "less-slow-gb-hanzi-encode" feature of the "%{crate}" crate.

%package     -n %{name}+less-slow-kanji-encode-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+less-slow-kanji-encode-devel

This package contains library source intended for building other packages which
use the "less-slow-kanji-encode" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+simd-accel-devel
Summary:        A Gecko-oriented implementation of the Encoding Standard
BuildArch:      noarch
%description -n %{name}+simd-accel-devel

This package contains library source intended for building other packages which
use the "simd-accel" feature of the "%{crate}" crate.

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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-encoding_rs-devel -f %{oreon_filedir}/rust-encoding_rs-devel.list

%changelog

%autochangelog
