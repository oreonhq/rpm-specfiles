%global source0_hash f786a369cd0ba9f4a721c29e5fb9d18de8756645449b4151ad70c80001e4a22b
%bcond check 1
%global debug_package %{nil}
%global crate jql-runner
Name:           rust-jql-runner
Version:        8.0.9
Release:        1%{?dist}
Summary:        Runner for jql - the JSON Query Language tool
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jql-runner
Source0:        https://static.crates.io/crates/jql-runner/jql-runner-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Runner for jql - the JSON Query Language tool
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli-set Cargo.toml del 'dev-dependencies.criterion'
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
%files -n rust-jql-runner-devel -f %{oreon_filedir}/rust-jql-runner-devel.list

%changelog

%autochangelog
