%global source0_hash d15b6607fa632996eb8a17c9041cb6071cb75ac057abd45dece578723ea8c7c0
%bcond check 1
%global debug_package %{nil}
%global crate pipeline
Name:           rust-pipeline
Version:        0.5.0
Release:        1%{?dist}
Summary:        Macro collection to pipe |> your functions calls, like in F# or Elixir
License:        MIT
URL:            https://crates.io/crates/pipeline
Source0:        https://static.crates.io/crates/pipeline/pipeline-%{version}.crate
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
Summary:        Macro collection to pipe |> your functions calls, like in F# or Elixir
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-pipeline-devel -f %{oreon_filedir}/rust-pipeline-devel.list

%changelog

%autochangelog
