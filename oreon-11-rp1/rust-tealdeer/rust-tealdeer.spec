%global source0_hash 3bdb5cacd200e73ef6548e7dd38932d3da843fb9d8f445b78b937362206e26c7
%bcond check 1
%global crate tealdeer
Name:           rust-tealdeer
Version:        1.7.3
Release:        1%{?dist}
Summary:        Fetch and show tldr help pages for many CLI commands
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tealdeer
Source0:        https://static.crates.io/crates/tealdeer/tealdeer-%{version}.crate
Patch:          tealdeer-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Fetch and show tldr help pages for many CLI commands
License:        %{shrink:
    Apache-2.0 AND
    MIT AND
    Unicode-3.0 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Apache-2.0 OR BSL-1.0) AND
    (MIT OR Zlib OR Apache-2.0) AND
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
%install
%cargo_install
install -Dpm0644 completion/bash_tealdeer %{buildroot}/%{bash_completions_dir}/tldr.bash
install -Dpm0644 completion/fish_tealdeer %{buildroot}/%{fish_completions_dir}/tldr.fish
install -Dpm0644 completion/zsh_tealdeer %{buildroot}/%{zsh_completions_dir}/_tldr
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -- --bins
%endif
%files -f %{oreon_filedir}/main.list
%files -n tealdeer -f %{oreon_filedir}/tealdeer.list

%changelog

%autochangelog
