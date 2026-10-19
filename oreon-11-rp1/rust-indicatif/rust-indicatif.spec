%global source0_hash 9433806cd6b4ec1aba79c021c7e4c58fb4c3b9977c085062e611ac929998fb0c
%bcond check 0
%global debug_package %{nil}
%global crate indicatif
Name:           rust-indicatif
Version:        0.18.6
Release:        1%{?dist}
Summary:        A progress bar and cli reporting library for Rust
License:        MIT
URL:            https://crates.io/crates/indicatif
Source0:        https://static.crates.io/crates/indicatif/indicatif-%{version}.crate
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
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+futures-devel
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+futures-devel

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%package     -n %{name}+improved_unicode-devel
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+improved_unicode-devel

This package contains library source intended for building other packages which
use the "improved_unicode" feature of the "%{crate}" crate.

%package     -n %{name}+in_memory-devel
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+in_memory-devel

This package contains library source intended for building other packages which
use the "in_memory" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-segmentation-devel
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+unicode-segmentation-devel

This package contains library source intended for building other packages which
use the "unicode-segmentation" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-width-devel
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+unicode-width-devel

This package contains library source intended for building other packages which
use the "unicode-width" feature of the "%{crate}" crate.

%package     -n %{name}+vt100-devel
Summary:        A progress bar and cli reporting library for Rust
BuildArch:      noarch
%description -n %{name}+vt100-devel

This package contains library source intended for building other packages which
use the "vt100" feature of the "%{crate}" crate.

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
%files -n rust-indicatif-devel -f %{oreon_filedir}/rust-indicatif-devel.list

%changelog

%autochangelog
