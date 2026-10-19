%global source0_hash bb919243f34364b6bd2fc10ef797edbfa75f33c252e7998527479c6d6b47e1ec
%bcond check 0
%global debug_package %{nil}
%global crate rlp
Name:           rust-rlp
Version:        0.5.2
Release:        1%{?dist}
Summary:        Recursive-length prefix encoding, decoding, and compression
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rlp
Source0:        https://static.crates.io/crates/rlp/rlp-%{version}.crate
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
Summary:        Recursive-length prefix encoding, decoding, and compression
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Recursive-length prefix encoding, decoding, and compression
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+rlp-derive-devel
Summary:        Recursive-length prefix encoding, decoding, and compression
BuildArch:      noarch
%description -n %{name}+rlp-derive-devel

This package contains library source intended for building other packages which
use the "rlp-derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Recursive-length prefix encoding, decoding, and compression
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-rlp-devel -f %{oreon_filedir}/rust-rlp-devel.list

%changelog

%autochangelog
