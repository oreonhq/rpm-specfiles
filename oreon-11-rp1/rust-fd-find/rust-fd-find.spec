%global source0_hash f35becce49c551724fd26d9824ec01d6578868cecbcc4e3d060658f9f8ad1e4d
%bcond check 1
%global crate fd-find
Name:           rust-fd-find
Version:        10.5.0
Release:        1%{?dist}
Summary:        Fd is a simple, fast and user-friendly alternative to find
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fd-find
Source0:        https://static.crates.io/crates/fd-find/fd-find-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Fd is a simple, fast and user-friendly alternative to find
License:        %{shrink:
    MIT AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
./target/release/fd --gen-completions bash > fd.bash
./target/release/fd --gen-completions fish > fd.fish
./target/release/fd --gen-completions zsh > fd.zsh
%install
%cargo_install
install -Dpm 644 doc/fd.1 -t %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 fd.bash %{buildroot}/%{bash_completions_dir}/fd.bash
install -Dpm 0644 fd.fish %{buildroot}/%{fish_completions_dir}/fd.fish
install -Dpm 0644 fd.zsh %{buildroot}/%{zsh_completions_dir}/_fd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n fd-find -f %{oreon_filedir}/fd-find.list

%changelog

%autochangelog
