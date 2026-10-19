%global source0_hash a217bbb075dcaefb292efa78897fc0678245ca67f265d12c351e42268fcb0305
%bcond check 0
%global debug_package %{nil}
%global crate i18n-embed
Name:           rust-i18n-embed
Version:        0.16.0
Release:        1%{?dist}
Summary:        Conveniently embed localization assets
License:        MIT
URL:            https://crates.io/crates/i18n-embed
Source0:        https://static.crates.io/crates/i18n-embed/i18n-embed-%{version}.crate
Patch:          i18n-embed-fix-metadata.diff
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
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arc-swap-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+arc-swap-devel

This package contains library source intended for building other packages which
use the "arc-swap" feature of the "%{crate}" crate.

%package     -n %{name}+autoreload-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+autoreload-devel

This package contains library source intended for building other packages which
use the "autoreload" feature of the "%{crate}" crate.

%package     -n %{name}+desktop-requester-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+desktop-requester-devel

This package contains library source intended for building other packages which
use the "desktop-requester" feature of the "%{crate}" crate.

%package     -n %{name}+filesystem-assets-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+filesystem-assets-devel

This package contains library source intended for building other packages which
use the "filesystem-assets" feature of the "%{crate}" crate.

%package     -n %{name}+fluent-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+fluent-devel

This package contains library source intended for building other packages which
use the "fluent" feature of the "%{crate}" crate.

%package     -n %{name}+fluent-syntax-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+fluent-syntax-devel

This package contains library source intended for building other packages which
use the "fluent-syntax" feature of the "%{crate}" crate.

%package     -n %{name}+fluent-system-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+fluent-system-devel

This package contains library source intended for building other packages which
use the "fluent-system" feature of the "%{crate}" crate.

%package     -n %{name}+i18n-embed-impl-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+i18n-embed-impl-devel

This package contains library source intended for building other packages which
use the "i18n-embed-impl" feature of the "%{crate}" crate.

%package     -n %{name}+notify-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+notify-devel

This package contains library source intended for building other packages which
use the "notify" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+rust-embed-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+rust-embed-devel

This package contains library source intended for building other packages which
use the "rust-embed" feature of the "%{crate}" crate.

%package     -n %{name}+sys-locale-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+sys-locale-devel

This package contains library source intended for building other packages which
use the "sys-locale" feature of the "%{crate}" crate.

%package     -n %{name}+walkdir-devel
Summary:        Conveniently embed localization assets
BuildArch:      noarch
%description -n %{name}+walkdir-devel

This package contains library source intended for building other packages which
use the "walkdir" feature of the "%{crate}" crate.

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
%files -n rust-i18n-embed-devel -f %{oreon_filedir}/rust-i18n-embed-devel.list

%changelog

%autochangelog
