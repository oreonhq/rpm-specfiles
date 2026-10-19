%global source0_hash 8734088f19d2b3bda1ee935161d466e29b0ce4c78e344a3df0bfd0e303e97a03
%bcond check 1
%global crate ingredients
Name:           rust-ingredients
Version:        0.3.0
Release:        1%{?dist}
Summary:        Check ingredients of published Rust crates
License:        MIT
URL:            https://crates.io/crates/ingredients
Source0:        https://static.crates.io/crates/ingredients/ingredients-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Check ingredients of published Rust crates
License:        %{shrink:
    MIT
    AND Apache-2.0
    AND Unicode-DFS-2016
    AND Unicode-3.0
    AND Zlib
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
}
Requires:       cargo
Requires:       git-core
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Check ingredients of published Rust crates
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Check ingredients of published Rust crates
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f cli
%{cargo_license_summary -f cli}
%{cargo_license -f cli} > LICENSE.dependencies
%install
%cargo_install -f cli
target/rpm/ingredients completions bash > ingredients.bash
target/rpm/ingredients completions fish > ingredients.fish
target/rpm/ingredients completions zsh > _ingredients
install -Dpm 0644 ingredients.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 ingredients.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _ingredients -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f cli
%endif
%files -f %{oreon_filedir}/main.list
%files -n ingredients -f %{oreon_filedir}/ingredients.list
%files -n rust-ingredients-devel -f %{oreon_filedir}/rust-ingredients-devel.list

%changelog

%autochangelog
