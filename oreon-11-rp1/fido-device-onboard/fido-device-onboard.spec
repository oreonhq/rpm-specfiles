%global source0_hash b48a43f7aa212978ae243a8d378186342d17e51458c152c2c5d68f8e67d54204
%global source1_hash none
%global dracutlibdir %{_prefix}/lib/dracut
%bcond_without check
%global combined_license Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND ISC AND MIT AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR MIT OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT)
Name:           fido-device-onboard
Version:        0.5.6
Release:        1%{?dist}
Summary:        A rust implementation of the FIDO Device Onboard Specification
License:        BSD-3-Clause
URL:            https://github.com/fdo-rs/fido-device-onboard-rs
Source0:        https://github.com/fdo-rs/fido-device-onboard-rs/archive/refs/tags/v%{version}.tar.gz#/fido-device-onboard-rs-%{version}.tar.gz
Patch1:        0001-use-released-aws-nitro-enclaves-cose-version.patch
ExcludeArch: %{ix86}
%if 0%{?rhel} || (0%{?oreon} >= 11)
%else
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang-devel
BuildRequires:  cryptsetup-devel
BuildRequires:  device-mapper-devel
BuildRequires:  golang
BuildRequires:  libpq-devel
BuildRequires:  openssl-devel
BuildRequires:  rustc
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tpm2-tss-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%if 0%{?rhel} || (0%{?oreon} >= 11)
%autosetup -n %{name}-rs-%{version} -N
%autopatch -p1
rm -f Cargo.lock
cargo vendor
find vendor/ -name '*.a' -delete
%endif
%if 0%{?fedora} && !(0%{?oreon} >= 11)
%autosetup -p1 -n %{name}-rs-%{version}
%oreon_vendor_cargo
%build

%cargo_build \
-F openssl-kdf/deny_custom
%{?cargo_license_summary}
%{?cargo_license} > LICENSE.dependencies
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%cargo_vendor_manifest
%endif
%install
install -D -m 0755 -t %{buildroot}%{_libexecdir}/fdo target/release/fdo-client-linuxapp
install -D -m 0755 -t %{buildroot}%{_libexecdir}/fdo target/release/fdo-manufacturing-client
install -D -m 0755 -t %{buildroot}%{_libexecdir}/fdo target/release/fdo-manufacturing-server
install -D -m 0755 -t %{buildroot}%{_libexecdir}/fdo target/release/fdo-owner-onboarding-server
install -D -m 0755 -t %{buildroot}%{_libexecdir}/fdo target/release/fdo-rendezvous-server
install -D -m 0755 -t %{buildroot}%{_libexecdir}/fdo target/release/fdo-serviceinfo-api-server
install -D -m 0755 -t %{buildroot}%{_bindir} target/release/fdo-owner-tool
install -D -m 0755 -t %{buildroot}%{_bindir} target/release/fdo-admin-tool
install -D -m 0644 -t %{buildroot}%{_unitdir} examples/systemd/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo examples/config/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_manufacturing_server_postgres  migrations/migrations_manufacturing_server_postgres/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_manufacturing_server_sqlite  migrations/migrations_manufacturing_server_sqlite/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_owner_onboarding_server_postgres  migrations/migrations_owner_onboarding_server_postgres/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_owner_onboarding_server_sqlite  migrations/migrations_owner_onboarding_server_sqlite/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_rendezvous_server_postgres  migrations/migrations_rendezvous_server_postgres/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_rendezvous_server_sqlite  migrations/migrations_rendezvous_server_sqlite/2023-10-03-152801_create_db/*
mkdir -p %{buildroot}%{_bindir}
ln -sr %{buildroot}%{_bindir}/fdo-owner-tool  %{buildroot}%{_libexecdir}/fdo/fdo-owner-tool
ln -sr %{buildroot}%{_bindir}/fdo-admin-tool %{buildroot}%{_libexecdir}/fdo/fdo-admin-tool
mkdir -p %{buildroot}%{_sysconfdir}/fdo
mkdir -p %{buildroot}%{_sysconfdir}/fdo/keys
mkdir -p %{buildroot}%{_sysconfdir}/fdo/stores
mkdir -p %{buildroot}%{_sysconfdir}/fdo/stores/manufacturer_keys
mkdir -p %{buildroot}%{_sysconfdir}/fdo/stores/manufacturing_sessions
mkdir -p %{buildroot}%{_sysconfdir}/fdo/stores/owner_onboarding_sessions
mkdir -p %{buildroot}%{_sysconfdir}/fdo/stores/owner_vouchers
mkdir -p %{buildroot}%{_sysconfdir}/fdo/stores/rendezvous_registered
mkdir -p %{buildroot}%{_sysconfdir}/fdo/stores/rendezvous_sessions
mkdir -p %{buildroot}%{_sysconfdir}/fdo/stores/serviceinfo_api_devices
mkdir -p %{buildroot}%{_sysconfdir}/fdo/manufacturing-server.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/fdo/owner-onboarding-server.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/fdo/rendezvous-server.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/fdo/serviceinfo-api-server.conf.d
mkdir -p %{buildroot}%{_localstatedir}/lib/fdo
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/52fdo dracut/52fdo/module-setup.sh
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/52fdo dracut/52fdo/manufacturing-client-generator
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/52fdo dracut/52fdo/manufacturing-client-service
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/52fdo dracut/52fdo/manufacturing-client.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package -n fdo-init
Summary: dracut module for device initialization
License: %combined_license
Requires: openssl-libs >= 3.0.1-12
Requires: dracut
%description -n fdo-init
%{summary}

%package -n fdo-owner-onboarding-server
Summary: FDO Owner Onboarding Server implementation
License: %combined_license
Requires: openssl-libs >= 3.0.1-12
%description -n fdo-owner-onboarding-server
%{summary}

%post -n fdo-owner-onboarding-server

%systemd_post fdo-owner-onboarding-server.service
%systemd_post fdo-serviceinfo-api-server.service
%preun -n fdo-owner-onboarding-server

%systemd_preun fdo-owner-onboarding-server.service
%systemd_post fdo-serviceinfo-api-server.service
%postun -n fdo-owner-onboarding-server

%systemd_postun_with_restart fdo-owner-onboarding-server.service
%systemd_postun_with_restart fdo-serviceinfo-api-server.service
%package -n fdo-rendezvous-server
Summary: FDO Rendezvous Server implementation
License: %combined_license
%description -n fdo-rendezvous-server
%{summary}

%post -n fdo-rendezvous-server

%systemd_post fdo-rendezvous-server.service
%preun -n fdo-rendezvous-server

%systemd_preun fdo-rendezvous-server.service
%postun -n fdo-rendezvous-server

%systemd_postun_with_restart fdo-rendezvous-server.service
%package -n fdo-manufacturing-server
Summary: FDO Manufacturing Server implementation
License: %combined_license
Requires: openssl-libs >= 3.0.1-12
%description -n fdo-manufacturing-server
%{summary}

%post -n fdo-manufacturing-server

%systemd_post fdo-manufacturing-server.service
%preun -n fdo-manufacturing-server

%systemd_preun fdo-manufacturing-server.service
%postun -n fdo-manufacturing-server

%systemd_postun_with_restart fdo-manufacturing-server.service
%package -n fdo-client
Summary: FDO Client implementation
License: %combined_license
Requires: openssl-libs >= 3.0.1-12
Requires: clevis
Requires: clevis-luks
Requires: clevis-pin-tpm2
Requires: cryptsetup
%description -n fdo-client
%{summary}

%post -n fdo-client

%systemd_post fdo-client-linuxapp.service
%preun -n fdo-client

%systemd_preun fdo-client-linuxapp.service
%postun -n fdo-client

%systemd_postun_with_restart fdo-client-linuxapp.service
%package -n fdo-owner-cli
Summary: FDO Owner tools implementation
License: %combined_license
%description -n fdo-owner-cli
%{summary}

%package -n fdo-admin-cli
Summary: FDO admin tools implementation
License: %combined_license
Requires: fdo-manufacturing-server = %{version}-%{release}
Requires: fdo-rendezvous-server = %{version}-%{release}
Requires: fdo-owner-onboarding-server = %{version}-%{release}
Requires: fdo-owner-cli = %{version}-%{release}
Requires: fdo-client = %{version}-%{release}
Requires: fdo-init = %{version}-%{release}
%description -n fdo-admin-cli
%{summary}

%post -n fdo-admin-cli

%systemd_post fdo-aio.service
%preun -n fdo-admin-cli

%systemd_preun fdo-aio.service
%postun -n fdo-admin-cli

%systemd_postun_with_restart fdo-aio.service
%files -f %{oreon_filedir}/main.list
%files -n fdo-init -f %{oreon_filedir}/fdo-init.list
%files -n fdo-owner-onboarding-server -f %{oreon_filedir}/fdo-owner-onboarding-server.list
%files -n fdo-rendezvous-server -f %{oreon_filedir}/fdo-rendezvous-server.list
%files -n fdo-manufacturing-server -f %{oreon_filedir}/fdo-manufacturing-server.list
%files -n fdo-client -f %{oreon_filedir}/fdo-client.list
%files -n fdo-owner-cli -f %{oreon_filedir}/fdo-owner-cli.list
%files -n fdo-admin-cli -f %{oreon_filedir}/fdo-admin-cli.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.5-8
- Import
%endif
