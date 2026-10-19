%global source0_hash 68343f3a4bf4afeae32c7f4bee549823034c6f754d7b718d8c2459aa1a15406e
%bcond check 1
%global debug_package %{nil}
%global crate postmark
Name:           rust-postmark
Version:        0.11.3
Release:        1%{?dist}
Summary:        Postmark rust client
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/postmark
Source0:        https://static.crates.io/crates/postmark/postmark-%{version}.crate
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
Summary:        Postmark rust client
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Postmark rust client
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-devel
Summary:        Postmark rust client
BuildArch:      noarch
%description -n %{name}+reqwest-devel

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-native-tls-devel
Summary:        Postmark rust client
BuildArch:      noarch
%description -n %{name}+reqwest-native-tls-devel

This package contains library source intended for building other packages which
use the "reqwest-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-rustls-tls-devel
Summary:        Postmark rust client
BuildArch:      noarch
%description -n %{name}+reqwest-rustls-tls-devel

This package contains library source intended for building other packages which
use the "reqwest-rustls-tls" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f reqwest
%install
%cargo_install -f reqwest
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f reqwest
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-postmark-devel -f %{oreon_filedir}/rust-postmark-devel.list

%changelog

%autochangelog
