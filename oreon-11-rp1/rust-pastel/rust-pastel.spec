%global source0_hash 60c08ad0192cd8ba04db7617ab5535089f5cef907b7d09214fb449d68d569b65
%bcond check 1
%global crate pastel
Name:           rust-pastel
Version:        0.12.0
Release:        1%{?dist}
Summary:        Command-line tool to generate, analyze, convert and manipulate colors
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pastel
Source0:        https://static.crates.io/crates/pastel/pastel-%{version}.crate
Patch:          pastel-fix-metadata.diff
Patch10:        0001-Downstream-only-bypass-output_vt100-no-op-on-non-Win.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Command-line tool to generate, analyze, convert and manipulate colors
License:        %{shrink:
    (MIT OR Apache-2.0) AND
    MIT AND
    Unicode-DFS-2016 AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
    }
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Command-line tool to generate, analyze, convert and manipulate colors
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

export SHELL_COMPLETIONS_DIR='_completions'
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
pushd _completions
install -Dpm 0644 pastel.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 pastel.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _pastel -t %{buildroot}/%{zsh_completions_dir}
install -Dpm 0644 *.1 -t %{buildroot}%{_mandir}/man1
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n pastel -f %{oreon_filedir}/pastel.list
%files -n rust-pastel-devel -f %{oreon_filedir}/rust-pastel-devel.list

%changelog

%autochangelog
