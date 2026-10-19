%global source0_hash 7969a9ba84b0ff843813e7249eed1678d9b6607ce5a3b8f0a47af3fcf7978e6e
%bcond check 0
%global debug_package %{nil}
%global crate bson
Name:           rust-bson
Version:        2.15.0
Release:        1%{?dist}
Summary:        Encoding and decoding support for BSON in Rust
License:        MIT
URL:            https://crates.io/crates/bson
Source0:        https://static.crates.io/crates/bson/bson-%{version}.crate
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
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-0_4-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+chrono-0_4-devel

This package contains library source intended for building other packages which
use the "chrono-0_4" feature of the "%{crate}" crate.

%package     -n %{name}+hashable-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+hashable-devel

This package contains library source intended for building other packages which
use the "hashable" feature of the "%{crate}" crate.

%package     -n %{name}+serde_path_to_error-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+serde_path_to_error-devel

This package contains library source intended for building other packages which
use the "serde_path_to_error" feature of the "%{crate}" crate.

%package     -n %{name}+serde_with-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+serde_with-devel

This package contains library source intended for building other packages which
use the "serde_with" feature of the "%{crate}" crate.

%package     -n %{name}+serde_with-3-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+serde_with-3-devel

This package contains library source intended for building other packages which
use the "serde_with-3" feature of the "%{crate}" crate.

%package     -n %{name}+time-0_3-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+time-0_3-devel

This package contains library source intended for building other packages which
use the "time-0_3" feature of the "%{crate}" crate.

%package     -n %{name}+uncapped_max_size-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+uncapped_max_size-devel

This package contains library source intended for building other packages which
use the "uncapped_max_size" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-0_8-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+uuid-0_8-devel

This package contains library source intended for building other packages which
use the "uuid-0_8" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-1-devel
Summary:        Encoding and decoding support for BSON in Rust
BuildArch:      noarch
%description -n %{name}+uuid-1-devel

This package contains library source intended for building other packages which
use the "uuid-1" feature of the "%{crate}" crate.

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
%files -n rust-bson-devel -f %{oreon_filedir}/rust-bson-devel.list

%changelog

%autochangelog
