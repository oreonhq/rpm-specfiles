%global source0_hash c5fe697e6fdd7bd20438836076f8901094926ae40cf13f3f7255c1f3f085122c
%bcond check 1
%global crate hyperfine
Name:           rust-hyperfine
Version:        1.20.0
Release:        1%{?dist}
Summary:        Command-line benchmarking tool
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hyperfine
Source0:        https://static.crates.io/crates/hyperfine/hyperfine-%{version}.crate
Patch:          hyperfine-fix-metadata-auto.diff
Patch:          hyperfine-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Command-line benchmarking tool
License:        %{shrink:
    (MIT OR Apache-2.0) AND
    MIT AND
    MPL-2.0 AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
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
install -Dpm 0644 doc/hyperfine.1 -t %{buildroot}/%{_mandir}/man1
install -Dpm 0644 target/release/build/%{crate}-*/out/hyperfine.bash \
    -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 target/release/build/%{crate}-*/out/hyperfine.fish \
    -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 target/release/build/%{crate}-*/out/_hyperfine \
    -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n hyperfine -f %{oreon_filedir}/hyperfine.list

%changelog

%autochangelog
