%global source0_hash f77b8032dc584527975f34aa5a897d0ef5a785573fda778771a614ff9da501d9
%bcond check 0
%global crate ripgrep
Name:           rust-ripgrep
Version:        14.1.1
Release:        1%{?dist}
Summary:        Line-oriented search tool
License:        Unlicense OR MIT
URL:            https://crates.io/crates/ripgrep
Source0:        https://static.crates.io/crates/ripgrep/ripgrep-%{version}.crate
Patch:          ripgrep-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Line-oriented search tool
License:        BSD-3-Clause AND MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
%install
%cargo_install -a
target/release/rg --generate man > rg.1
install -Dpm 0644 rg.1 -t %{buildroot}/%{_mandir}/man1/
target/release/rg --generate complete-bash > rg.bash
target/release/rg --generate complete-fish > rg.fish
target/release/rg --generate complete-zsh > _rg
install -Dpm 0644 rg.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 rg.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _rg -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n ripgrep -f %{oreon_filedir}/ripgrep.list

%changelog

%autochangelog
