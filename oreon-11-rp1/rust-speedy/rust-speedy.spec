%global source0_hash da1992073f0e55aab599f4483c460598219b4f9ff0affa124b33580ab511e25a
%bcond check 0
%global debug_package %{nil}
%global crate speedy
Name:           rust-speedy
Version:        0.8.7
Release:        1%{?dist}
Summary:        A fast binary serialization framework
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/speedy
Source0:        https://static.crates.io/crates/speedy/speedy-%{version}.crate
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
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+external_doc-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+external_doc-devel

This package contains library source intended for building other packages which
use the "external_doc" feature of the "%{crate}" crate.

%package     -n %{name}+glam-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+glam-devel

This package contains library source intended for building other packages which
use the "glam" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap_v1-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+indexmap_v1-devel

This package contains library source intended for building other packages which
use the "indexmap_v1" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap_v2-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+indexmap_v2-devel

This package contains library source intended for building other packages which
use the "indexmap_v2" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+speedy-derive-devel
Summary:        A fast binary serialization framework
BuildArch:      noarch
%description -n %{name}+speedy-derive-devel

This package contains library source intended for building other packages which
use the "speedy-derive" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        A fast binary serialization framework
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
%files -n rust-speedy-devel -f %{oreon_filedir}/rust-speedy-devel.list

%changelog

%autochangelog
