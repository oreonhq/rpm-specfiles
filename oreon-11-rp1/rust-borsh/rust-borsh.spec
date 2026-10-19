%global source0_hash a88b7ea17d208c4193f2c1e6de3c35fe71f98c96982d5ced308bdcc749ff6e1f
%bcond check 0
%global debug_package %{nil}
%global crate borsh
Name:           rust-borsh
Version:        1.8.0
Release:        1%{?dist}
Summary:        Binary Object Representation Serializer for Hashing
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/borsh
Source0:        https://static.crates.io/crates/borsh/borsh-%{version}.crate
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
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ascii-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+ascii-devel

This package contains library source intended for building other packages which
use the "ascii" feature of the "%{crate}" crate.

%package     -n %{name}+borsh-derive-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+borsh-derive-devel

This package contains library source intended for building other packages which
use the "borsh-derive" feature of the "%{crate}" crate.

%package     -n %{name}+bson-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+bson-devel

This package contains library source intended for building other packages which
use the "bson" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+de_strict_order-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+de_strict_order-devel

This package contains library source intended for building other packages which
use the "de_strict_order" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+rc-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+rc-devel

This package contains library source intended for building other packages which
use the "rc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable__schema-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+unstable__schema-devel

This package contains library source intended for building other packages which
use the "unstable__schema" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

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
%files -n rust-borsh-devel -f %{oreon_filedir}/rust-borsh-devel.list

%changelog

%autochangelog
