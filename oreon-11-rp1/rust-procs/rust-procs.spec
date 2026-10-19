%global source0_hash f6a2677982576e9810579c303d631e4a9a9ae00bf7d80e5a5578feecb4b35be8
%bcond check 1
%global crate procs
Name:           rust-procs
Version:        0.14.10
Release:        1%{?dist}
Summary:        Modern replacement for ps
License:        MIT
URL:            https://crates.io/crates/procs
Source0:        https://static.crates.io/crates/procs/procs-%{version}.crate
Patch:          procs-fix-metadata-auto.diff
Patch:          procs-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Modern replacement for ps
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    MPL-2.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
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
target/rpm/procs --gen-completion-out bash > procs.bash
target/rpm/procs --gen-completion-out fish > procs.fish
target/rpm/procs --gen-completion-out zsh > _procs
install -Dpm 0644 procs.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 procs.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _procs -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n procs -f %{oreon_filedir}/procs.list

%changelog

%autochangelog
