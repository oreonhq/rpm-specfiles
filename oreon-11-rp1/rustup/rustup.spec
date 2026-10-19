%global source0_hash de73d1a62f4d5409a2f6bdb1c523d8dc08aa6d9d63588db62493c19ca8f8bf55
%bcond check 0
%global cargo_install_lib 0
Name:           rustup
Version:        1.29.0
Release:        1%{?dist}
Summary:        Manage multiple rust installations with ease
SourceLicense:  MIT OR Apache-2.0
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT AND Unicode-3.0 AND Unicode-DFS-2016 AND Zlib AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
URL:            https://github.com/rust-lang/rustup
Source0:        https://github.com/rust-lang/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          0001-Drop-Windows-specific-dependencies.patch
Patch:          0002-Drop-feature-for-statically-linking-against-vendored.patch
Patch:          0003-Remove-unused-tracing-support.patch
Patch:          0004-Remove-unused-git-based-versioning.patch
Patch:          0005-Revert-back-to-rustls-ring-instead-of-aws_lc_rs.patch
Patch:          0006-Disable-tests-suite-static_roots.patch
Patch:          0001-Unpin-tracing-subcriber.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n rustup-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f no-self-update
%{cargo_license_summary -f no-self-update}
%{cargo_license -f no-self-update} > LICENSE.dependencies
%install
%cargo_install -f no-self-update
cp -pav target/rpm/rustup-init target/rpm/rustup
target/rpm/rustup completions bash > rustup.bash
target/rpm/rustup completions fish > rustup.fish
target/rpm/rustup completions zsh > _rustup
install -Dpm 0644 rustup.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 rustup.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _rustup -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main
%if %{with check}
%check

%cargo_test -f test -- -- --skip suite::cli_exact::check_updates --skip suite::cli_ui::rustup_ui_doc_text_tests --skip suite::known_triples::gen_known_triples
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
