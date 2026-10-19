%global source0_hash c0bf912d9e66f057a759d92e386a280ea886b352ab757d6ac4d653c7ed2c43c2
%bcond check 0
%global debug_package %{nil}
%global crate ratatui-termina
Name:           rust-ratatui-termina
Version:        0.1.0
Release:        1%{?dist}
Summary:        Termina backend for the Ratatui Terminal UI library.
License:        MIT
URL:            https://crates.io/crates/ratatui-termina
Source0:        https://static.crates.io/crates/ratatui-termina/ratatui-termina-%{version}.crate
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
Summary:        Termina backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Termina backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+scrolling-regions-devel
Summary:        Termina backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+scrolling-regions-devel

This package contains library source intended for building other packages which
use the "scrolling-regions" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Termina backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+underline-color-devel
Summary:        Termina backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+underline-color-devel

This package contains library source intended for building other packages which
use the "underline-color" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Termina backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-backend-writer-devel
Summary:        Termina backend for the Ratatui Terminal UI library.
BuildArch:      noarch
%description -n %{name}+unstable-backend-writer-devel

This package contains library source intended for building other packages which
use the "unstable-backend-writer" feature of the "%{crate}" crate.

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
%files -n rust-ratatui-termina-devel -f %{oreon_filedir}/rust-ratatui-termina-devel.list

%changelog

%autochangelog
