%global source0_hash 7a14cad0fa1d1fb02de486a95ea7fd8dd28567b82f65b4ca34bffa7da81823e4
%bcond check 1
%global debug_package %{nil}
%global crate anstyle-hyperlink
Name:           rust-anstyle-hyperlink
Version:        1.0.2
Release:        1%{?dist}
Summary:        ANSI escape code hyperlinks (OSC 8)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anstyle-hyperlink
Source0:        https://static.crates.io/crates/anstyle-hyperlink/anstyle-hyperlink-%{version}.crate
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
Summary:        ANSI escape code hyperlinks (OSC 8)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+file-devel
Summary:        ANSI escape code hyperlinks (OSC 8)
BuildArch:      noarch
%description -n %{name}+file-devel

This package contains library source intended for building other packages which
use the "file" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        ANSI escape code hyperlinks (OSC 8)
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
%files -n rust-anstyle-hyperlink-devel -f %{oreon_filedir}/rust-anstyle-hyperlink-devel.list

%changelog

%autochangelog
