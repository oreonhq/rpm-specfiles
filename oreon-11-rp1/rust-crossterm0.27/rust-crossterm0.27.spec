%global source0_hash f476fe445d41c9e991fd07515a6f463074b782242ccf4a5b7b1d1012e70824df
%bcond check 0
%global debug_package %{nil}
%global crate crossterm
Name:           rust-crossterm0.27
Version:        0.27.0
Release:        1%{?dist}
Summary:        Crossplatform terminal library for manipulating terminals
License:        MIT
URL:            https://crates.io/crates/crossterm
Source0:        https://static.crates.io/crates/crossterm/crossterm-%{version}.crate
Patch:          crossterm-fix-metadata-auto.diff
Patch:          crossterm-fix-metadata.diff
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
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bracketed-paste-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+bracketed-paste-devel

This package contains library source intended for building other packages which
use the "bracketed-paste" feature of the "%{crate}" crate.

%package     -n %{name}+event-stream-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+event-stream-devel

This package contains library source intended for building other packages which
use the "event-stream" feature of the "%{crate}" crate.

%package     -n %{name}+events-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+events-devel

This package contains library source intended for building other packages which
use the "events" feature of the "%{crate}" crate.

%package     -n %{name}+filedescriptor-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+filedescriptor-devel

This package contains library source intended for building other packages which
use the "filedescriptor" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+use-dev-tty-devel
Summary:        Crossplatform terminal library for manipulating terminals
BuildArch:      noarch
%description -n %{name}+use-dev-tty-devel

This package contains library source intended for building other packages which
use the "use-dev-tty" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip style::types::colored::tests::test_parse_ansi_bg --skip style::types::colored::tests::test_parse_ansi_fg
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-crossterm0.27-devel -f %{oreon_filedir}/rust-crossterm0.27-devel.list

%changelog

%autochangelog
