%global source0_hash a61ebc4c4e058565285d54a1134a4f9f5d951ef901194c79437f3ee4f2538e49
%bcond check 1
%global debug_package %{nil}
%global crate rusty_paseto
Name:           rust-rusty_paseto
Version:        0.8.0
Release:        1%{?dist}
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rusty_paseto
Source0:        https://static.crates.io/crates/rusty_paseto/rusty_paseto-%{version}.crate
Patch:          rusty_paseto-fix-metadata.diff
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
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aes-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+aes-devel

This package contains library source intended for building other packages which
use the "aes" feature of the "%{crate}" crate.

%package     -n %{name}+batteries_included-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+batteries_included-devel

This package contains library source intended for building other packages which
use the "batteries_included" feature of the "%{crate}" crate.

%package     -n %{name}+blake2-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+blake2-devel

This package contains library source intended for building other packages which
use the "blake2" feature of the "%{crate}" crate.

%package     -n %{name}+chacha20-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+chacha20-devel

This package contains library source intended for building other packages which
use the "chacha20" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+ctr-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+ctr-devel

This package contains library source intended for building other packages which
use the "ctr" feature of the "%{crate}" crate.

%package     -n %{name}+ed25519-dalek-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+ed25519-dalek-devel

This package contains library source intended for building other packages which
use the "ed25519-dalek" feature of the "%{crate}" crate.

%package     -n %{name}+erased-serde-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+erased-serde-devel

This package contains library source intended for building other packages which
use the "erased-serde" feature of the "%{crate}" crate.

%package     -n %{name}+generic-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+generic-devel

This package contains library source intended for building other packages which
use the "generic" feature of the "%{crate}" crate.

%package     -n %{name}+hmac-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+hmac-devel

This package contains library source intended for building other packages which
use the "hmac" feature of the "%{crate}" crate.

%package     -n %{name}+local-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+local-devel

This package contains library source intended for building other packages which
use the "local" feature of the "%{crate}" crate.

%package     -n %{name}+p384-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+p384-devel

This package contains library source intended for building other packages which
use the "p384" feature of the "%{crate}" crate.

%package     -n %{name}+public-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+public-devel

This package contains library source intended for building other packages which
use the "public" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+v1-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v1-devel

This package contains library source intended for building other packages which
use the "v1" feature of the "%{crate}" crate.

%package     -n %{name}+v1_local-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v1_local-devel

This package contains library source intended for building other packages which
use the "v1_local" feature of the "%{crate}" crate.

%package     -n %{name}+v1_public-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v1_public-devel

This package contains library source intended for building other packages which
use the "v1_public" feature of the "%{crate}" crate.

%package     -n %{name}+v2-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v2-devel

This package contains library source intended for building other packages which
use the "v2" feature of the "%{crate}" crate.

%package     -n %{name}+v2_public-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v2_public-devel

This package contains library source intended for building other packages which
use the "v2_public" feature of the "%{crate}" crate.

%package     -n %{name}+v3-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v3-devel

This package contains library source intended for building other packages which
use the "v3" feature of the "%{crate}" crate.

%package     -n %{name}+v3_local-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v3_local-devel

This package contains library source intended for building other packages which
use the "v3_local" feature of the "%{crate}" crate.

%package     -n %{name}+v3_public-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v3_public-devel

This package contains library source intended for building other packages which
use the "v3_public" feature of the "%{crate}" crate.

%package     -n %{name}+v4-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v4-devel

This package contains library source intended for building other packages which
use the "v4" feature of the "%{crate}" crate.

%package     -n %{name}+v4_local-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v4_local-devel

This package contains library source intended for building other packages which
use the "v4_local" feature of the "%{crate}" crate.

%package     -n %{name}+v4_public-devel
Summary:        Type-driven, ergonomic alternative to JWT for secure stateless PASETO tokens
BuildArch:      noarch
%description -n %{name}+v4_public-devel

This package contains library source intended for building other packages which
use the "v4_public" feature of the "%{crate}" crate.

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
%files -n rust-rusty_paseto-devel -f %{oreon_filedir}/rust-rusty_paseto-devel.list

%changelog

%autochangelog
