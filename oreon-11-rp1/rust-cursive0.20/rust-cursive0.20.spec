%global source1_hash 34732cfadbccc51ae3660f332b609c491005993d21735c9b949a0b6821b34c1d
%global source0_hash 5438eb16bdd8af51b31e74764fef5d0a9260227a5ec82ba75c9d11ce46595839
%bcond check 1
%global debug_package %{nil}
%global crate cursive
Name:           rust-cursive0.20
Version:        0.20.0
Release:        1%{?dist}
Summary:        TUI (Text User Interface) library focused on ease-of-use
License:        MIT
URL:            https://crates.io/crates/cursive
Source0:        https://static.crates.io/crates/cursive/cursive-%{version}.crate
Source1:        https://github.com/gyscos/cursive/raw/main/LICENSE
Patch:          cursive-fix-metadata.diff
Patch10:        cursive-0.20-no-atty.patch
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
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+crossterm-devel

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%package     -n %{name}+crossterm-backend-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+crossterm-backend-devel

This package contains library source intended for building other packages which
use the "crossterm-backend" feature of the "%{crate}" crate.

%package     -n %{name}+doc-cfg-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+doc-cfg-devel

This package contains library source intended for building other packages which
use the "doc-cfg" feature of the "%{crate}" crate.

%package     -n %{name}+maplit-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+maplit-devel

This package contains library source intended for building other packages which
use the "maplit" feature of the "%{crate}" crate.

%package     -n %{name}+term_size-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+term_size-devel

This package contains library source intended for building other packages which
use the "term_size" feature of the "%{crate}" crate.

%package     -n %{name}+termion-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+termion-devel

This package contains library source intended for building other packages which
use the "termion" feature of the "%{crate}" crate.

%package     -n %{name}+termion-backend-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+termion-backend-devel

This package contains library source intended for building other packages which
use the "termion-backend" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_scroll-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+unstable_scroll-devel

This package contains library source intended for building other packages which
use the "unstable_scroll" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-cursive0.20-devel -f %{oreon_filedir}/rust-cursive0.20-devel.list

%changelog

%autochangelog
