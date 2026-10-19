%global source0_hash 23b97319f7b8343df12cc98938e5c3eb436064524c8d2b4e30a1d3a36eecdf81
%bcond check 0
%global debug_package %{nil}
%global crate winnow
Name:           rust-winnow
Version:        1.0.4
Release:        1%{?dist}
Summary:        Byte-oriented, zero-copy, parser combinators library
License:        MIT
URL:            https://crates.io/crates/winnow
Source0:        https://static.crates.io/crates/winnow/winnow-%{version}.crate
Patch:          winnow-fix-metadata.diff
Patch10:        0001-Port-from-is_terminal_polyfill-to-std-io-IsTerminal.patch
Patch11:        no-term-transcript.patch
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
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+ascii-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+ascii-devel

This package contains library source intended for building other packages which
use the "ascii" feature of the "%{crate}" crate.

%package     -n %{name}+binary-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+binary-devel

This package contains library source intended for building other packages which
use the "binary" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+parser-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+parser-devel

This package contains library source intended for building other packages which
use the "parser" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-doc-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+unstable-doc-devel

This package contains library source intended for building other packages which
use the "unstable-doc" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-recover-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+unstable-recover-devel

This package contains library source intended for building other packages which
use the "unstable-recover" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f debug
%install
%cargo_install -f debug
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f debug
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-winnow-devel -f %{oreon_filedir}/rust-winnow-devel.list

%changelog

%autochangelog
