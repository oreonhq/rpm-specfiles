%global source0_hash 709cc7440fe79a0794209c82e48fe5044358f1e37d11bb9a4a27ebe64fb6eae2
%bcond check 1
%ifarch %{ix86}
%global rustflags_debuginfo 1
%endif
%global crate sequoia-chameleon-gnupg
Name:           rust-sequoia-chameleon-gnupg
Version:        0.13.1
Release:        1%{?dist}
Summary:        Sequoia's reimplementation of the GnuPG interface
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://crates.io/crates/sequoia-chameleon-gnupg
Source0:        https://static.crates.io/crates/sequoia-chameleon-gnupg/sequoia-chameleon-gnupg-%{version}.crate
Source1:        gpgconf-sq.sh
Source2:        activate.sh
Patch:          sequoia-chameleon-gnupg-fix-metadata.diff
Patch2:         0001-fix-integration-tests-for-release-mode-and-use-prebu.patch
Patch3:         0001-Upgrade-pty-process.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/gpg
BuildRequires:  /usr/bin/gpgconf
BuildRequires:  /usr/bin/gpgv
BuildRequires:  /usr/bin/sq
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Sequoia's reimplementation of the GnuPG interface
License:        %{shrink:
    GPL-3.0-or-later AND
    Apache-2.0 AND
    BSD-3-Clause AND
    BSL-1.0 AND
    LGPL-2.0-or-later AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    bzip2-1.0.6 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
Provides:       bundled(libgpg-error)
Requires:       /usr/bin/gpg-agent
Requires:       /usr/bin/gpgconf
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
install -Dpm0644 %{SOURCE2} -T %{buildroot}/%{_datadir}/%{crate}/activate
install -Dpm0755 %{SOURCE1} -T %{buildroot}/%{_datadir}/%{crate}/shims/gpgconf
ln -s /usr/bin/gpg-sq %{buildroot}/%{_datadir}/%{crate}/shims/gpg
ln -s /usr/bin/gpg-sq %{buildroot}/%{_datadir}/%{crate}/shims/gpg2
ln -s /usr/bin/gpgv-sq %{buildroot}/%{_datadir}/%{crate}/shims/gpgv
ln -s /usr/bin/gpgv-sq %{buildroot}/%{_datadir}/%{crate}/shims/gpgv2
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav target/release/build/%{crate}-*/out/man-pages/*.1 \
    %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 \
    target/release/build/%{crate}-*/out/shell-completions/gpg-sq.bash \
    %{buildroot}/%{bash_completions_dir}/gpg-sq.bash
install -Dpm 0644 \
    target/release/build/%{crate}-*/out/shell-completions/gpgv-sq.bash \
    %{buildroot}/%{bash_completions_dir}/gpgv-sq.bash
install -Dpm 0644 \
    target/release/build/%{crate}-*/out/shell-completions/gpg-sq.fish \
    %{buildroot}/%{fish_completions_dir}/gpg-sq.fish
install -Dpm 0644 \
    target/release/build/%{crate}-*/out/shell-completions/gpgv-sq.fish \
    %{buildroot}/%{fish_completions_dir}/gpgv-sq.fish
install -Dpm 0644 \
    target/release/build/%{crate}-*/out/shell-completions/_gpg-sq \
    %{buildroot}/%{zsh_completions_dir}/_gpg-sq
install -Dpm 0644 \
    target/release/build/%{crate}-*/out/shell-completions/_gpgv-sq \
    %{buildroot}/%{zsh_completions_dir}/_gpgv-sq
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export RUST_TEST_THREADS=8
%{cargo_test -- -- %{shrink:
    --skip gpg::decrypt::general_purpose_
    --skip gpg::decrypt::restricted_agent
    --skip gpg::sign::general_purpose_
    --skip gpg::sign::restricted_agent
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n sequoia-chameleon-gnupg -f %{oreon_filedir}/sequoia-chameleon-gnupg.list

%changelog

%autochangelog
