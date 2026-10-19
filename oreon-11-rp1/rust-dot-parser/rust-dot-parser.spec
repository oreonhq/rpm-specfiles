%global source0_hash 6b3eabf2d7face13d70d37537133fbc536e68d766257a01c4cba3fb60e214b9c
%bcond check 0
%global debug_package %{nil}
%global crate dot-parser
Name:           rust-dot-parser
Version:        0.6.1
Release:        1%{?dist}
Summary:        This library provides a parser for the DOT/Graphviz graph description...
License:        GPL-2.0-or-later
URL:            https://crates.io/crates/dot-parser
Source0:        https://static.crates.io/crates/dot-parser/dot-parser-%{version}.crate
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
Summary:        This library provides a parser for the DOT/Graphviz graph description...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        This library provides a parser for the DOT/Graphviz graph description...
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+proc-macro2-devel
Summary:        This library provides a parser for the DOT/Graphviz graph description...
BuildArch:      noarch
%description -n %{name}+proc-macro2-devel

This package contains library source intended for building other packages which
use the "proc-macro2" feature of the "%{crate}" crate.

%package     -n %{name}+quote-devel
Summary:        This library provides a parser for the DOT/Graphviz graph description...
BuildArch:      noarch
%description -n %{name}+quote-devel

This package contains library source intended for building other packages which
use the "quote" feature of the "%{crate}" crate.

%package     -n %{name}+to_tokens-devel
Summary:        This library provides a parser for the DOT/Graphviz graph description...
BuildArch:      noarch
%description -n %{name}+to_tokens-devel

This package contains library source intended for building other packages which
use the "to_tokens" feature of the "%{crate}" crate.

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
%files -n rust-dot-parser-devel -f %{oreon_filedir}/rust-dot-parser-devel.list

%changelog

%autochangelog
