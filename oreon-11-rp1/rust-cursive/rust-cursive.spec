%global source0_hash 386d5a36020bb856e9a34ecb8a4e6c9bd6b0262d1857bae4db7bc7e2fdaa532e
%bcond check 1
%global debug_package %{nil}
%global crate cursive
Name:           rust-cursive
Version:        0.21.1
Release:        1%{?dist}
Summary:        TUI (Text User Interface) library focused on ease-of-use
License:        MIT
URL:            https://crates.io/crates/cursive
Source0:        https://static.crates.io/crates/cursive/cursive-%{version}.crate
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

%package     -n %{name}+builder-devel
Summary:        TUI (Text User Interface) library focused on ease-of-use
BuildArch:      noarch
%description -n %{name}+builder-devel

This package contains library source intended for building other packages which
use the "builder" feature of the "%{crate}" crate.

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
%files -n rust-cursive-devel -f %{oreon_filedir}/rust-cursive-devel.list

%changelog

%autochangelog
