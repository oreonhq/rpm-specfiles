%global source0_hash 66e3d19bcc9130ca376277d93b60767ff121ace3be06f5f95f81dd68956407d1
%bcond check 0
%global debug_package %{nil}
%global crate ratatui-widgets
Name:           rust-ratatui-widgets
Version:        0.3.2
Release:        1%{?dist}
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
License:        MIT
URL:            https://crates.io/crates/ratatui-widgets
Source0:        https://static.crates.io/crates/ratatui-widgets/ratatui-widgets-%{version}.crate
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
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-widgets-devel
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+all-widgets-devel

This package contains library source intended for building other packages which
use the "all-widgets" feature of the "%{crate}" crate.

%package     -n %{name}+calendar-devel
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+calendar-devel

This package contains library source intended for building other packages which
use the "calendar" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-rendered-line-info-devel
Summary:        A collection of Ratatui widgets for building terminal user interfaces...
BuildArch:      noarch
%description -n %{name}+unstable-rendered-line-info-devel

This package contains library source intended for building other packages which
use the "unstable-rendered-line-info" feature of the "%{crate}" crate.

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
%files -n rust-ratatui-widgets-devel -f %{oreon_filedir}/rust-ratatui-widgets-devel.list

%changelog

%autochangelog
