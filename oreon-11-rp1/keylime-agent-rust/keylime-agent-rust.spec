%global source0_hash 6cb94da09d5d23b458013147e45c1e5fd642ff5a8d31a8d3c3d5968b1ccf74a7
%bcond_without check
%global crate keylime_agent
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global bundled_rust_deps 1
%global __brp_mangle_shebangs_exclude_from ^/usr/src/debug/.*$
%else
%global bundled_rust_deps 0
%endif
Name:           keylime-agent-rust
Version:        0.2.9
Release:        1%{?dist}
Summary:        The Keylime agent
License: (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND Apache-2.0 WITH LLVM-exception AND ISC AND MIT AND (MIT OR Unlicense)
URL:            https://github.com/keylime/rust-keylime/
Source0:        https://github.com/keylime/rust-keylime/archive/refs/tags/v%{version}.tar.gz#/rust-keylime-%{version}.tar.gz
Patch0:       0001-rust-keylime-metadata.patch
Patch1:       0002-rust-keylime-do-not-require-usr-libexec.patch
ExclusiveArch:  %{rust_arches}
%if 0%{?bundled_rust_deps}
%else
%endif
Requires:       tpm2-tss
Requires:       util-linux-core
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
Requires:       keylime-base
%endif
Requires: keylime-agent-rust-common = %{version}-%{release}
Requires: keylime-agent-rust-ima-emulator%{?_isa} = %{version}-%{release}
Provides: keylime-agent = %{version}-%{release}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  git-core
BuildRequires:  openssl-devel
BuildRequires:  rustc
BuildRequires:  systemd
BuildRequires:  tpm2-tss-devel
# /oreon:deps
%description
The Keylime agent

#===============================================================================

%package common
Summary:   Common files for Keylime agent
License:   (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND Apache-2.0 WITH LLVM-exception AND ISC AND MIT AND (MIT OR Unlicense)
BuildArch: noarch
Obsoletes: keylime-agent-rust-pull < %{version}-%{release}
Obsoletes: keylime-agent-rust < %{version}-%{release}
%description common
Common files for the Keylime agent in both push and pull models

#===============================================================================

%package push
Summary:        The Keylime agent for push model deployment
License: (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND Apache-2.0 WITH LLVM-exception AND ISC AND MIT AND (MIT OR Unlicense)
Requires:       tpm2-tss
Requires:       util-linux-core
Requires: keylime-agent-rust-common = %{version}-%{release}
Requires: keylime-agent-rust-ima-emulator%{?_isa} = %{version}-%{release}
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
Requires:       keylime-base
%endif
Provides:       keylime-agent = %{version}-%{release}
%description push
The Keylime agent for push model deployment

#===============================================================================

%package ima-emulator
Summary:        The Keylime IMA emulator
License: (Apache-2.0 OR MIT) AND BSD-3-Clause AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND Apache-2.0 WITH LLVM-exception AND ISC AND MIT AND (MIT OR Unlicense)
Requires:       tpm2-tss
Requires:       keylime-agent-rust-common = %{version}-%{release}
%if 0%{?fedora} >= 36 || 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
Requires:       keylime-base
%endif
Provides:       keylime-ima-emulator = %{version}-%{release}
%description ima-emulator
The Keylime IMA emulator for testing with emulated TPM

#===============================================================================

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n rust-keylime-%{version} -N
%autopatch -M 99 -p1
%if 0%{?bundled_rust_deps}
cargo vendor --versioned-dirs
find vendor/ -name '*.a' -delete
%else
%oreon_vendor_cargo
%build

%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif
%install
mkdir -p %{buildroot}/%{_sharedstatedir}/keylime
mkdir -p --mode=0700 %{buildroot}/%{_rundir}/keylime
mkdir -p --mode=0700  %{buildroot}/%{_sysconfdir}/keylime
mkdir -p --mode=0700  %{buildroot}/%{_sysconfdir}/keylime/agent.conf.d
install -Dpm 400 keylime-agent.conf \
    %{buildroot}%{_sysconfdir}/keylime/agent.conf
install -Dpm 644 ./dist/systemd/system/keylime_agent.service \
    %{buildroot}%{_unitdir}/keylime_agent.service
install -Dpm 644 ./dist/systemd/system/var-lib-keylime-secure.mount \
    %{buildroot}%{_unitdir}/var-lib-keylime-secure.mount
install -Dpm 644 ./dist/systemd/system/keylime_push_model_agent.service \
    %{buildroot}%{_unitdir}/keylime_push_model_agent.service
cat > %{buildroot}/%{_sysconfdir}/keylime/agent.conf.d/001-run_as.conf << EOF
[agent]
run_as = "keylime:keylime"
EOF
install -Dpm 0755 \
    -t %{buildroot}%{_bindir} \
    ./target/release/keylime_agent
install -Dpm 0755 \
    -t %{buildroot}%{_bindir} \
    ./target/release/keylime_ima_emulator
install -Dpm 0755 \
    -t %{buildroot}%{_bindir} \
    ./target/release/keylime_push_model_agent
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%posttrans

chmod 500 %{_sysconfdir}/keylime/agent.conf.d
chmod 400 %{_sysconfdir}/keylime/agent.conf.d/*.conf
chmod 500 %{_sysconfdir}/keylime
chown -R keylime:keylime %{_sysconfdir}/keylime
%preun

%systemd_preun keylime_push_model_agent.service
%systemd_preun keylime_agent.service
%systemd_preun var-lib-keylime-secure.mount
%postun

%systemd_postun_with_restart keylime_push_model_agent.service
%systemd_postun_with_restart keylime_agent.service
%systemd_postun_with_restart var-lib-keylime-secure.mount
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n keylime-agent-rust-common -f %{oreon_filedir}/keylime-agent-rust-common.list
%files -n keylime-agent-rust-push -f %{oreon_filedir}/keylime-agent-rust-push.list
%files -n keylime-agent-rust-ima-emulator -f %{oreon_filedir}/keylime-agent-rust-ima-emulator.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.9-1
- Import
