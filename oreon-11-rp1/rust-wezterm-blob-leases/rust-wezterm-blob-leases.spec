%global source0_hash 692daff6d93d94e29e4114544ef6d5c942a7ed998b37abdc19b17136ea428eb7
%bcond check 0
%global debug_package %{nil}
%global crate wezterm-blob-leases
Name:           rust-wezterm-blob-leases
Version:        0.1.1
Release:        1%{?dist}
Summary:        Manage image blob caching/leasing for wezterm
License:        MIT
URL:            https://crates.io/crates/wezterm-blob-leases
Source0:        https://static.crates.io/crates/wezterm-blob-leases/wezterm-blob-leases-%{version}.crate
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
Summary:        Manage image blob caching/leasing for wezterm
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Manage image blob caching/leasing for wezterm
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+simple_tempdir-devel
Summary:        Manage image blob caching/leasing for wezterm
BuildArch:      noarch
%description -n %{name}+simple_tempdir-devel

This package contains library source intended for building other packages which
use the "simple_tempdir" feature of the "%{crate}" crate.

%package     -n %{name}+tempfile-devel
Summary:        Manage image blob caching/leasing for wezterm
BuildArch:      noarch
%description -n %{name}+tempfile-devel

This package contains library source intended for building other packages which
use the "tempfile" feature of the "%{crate}" crate.

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
%files -n rust-wezterm-blob-leases-devel -f %{oreon_filedir}/rust-wezterm-blob-leases-devel.list

%changelog

%autochangelog
