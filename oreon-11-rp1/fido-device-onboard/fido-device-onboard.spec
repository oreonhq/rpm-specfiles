%global source0_hash none

%global dracutlibdir %{_prefix}/lib/dracut
%bcond_without check
%global combined_license Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND (CC0-1.0 OR Apache-2.0) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND ISC AND MIT AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR MIT OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT)

Name:           fido-device-onboard
Version:        0.5.5
Release:        8%{?dist}
Summary:        A rust implementation of the FIDO Device Onboard Specification
License:        BSD-3-Clause

URL:            https://github.com/fdo-rs/fido-device-onboard-rs
Source0:        https://github.com/fdo-rs/fido-device-onboard-rs/archive/refs/tags/v%{version}.tar.gz#/fido-device-onboard-rs-%{version}.tar.gz
Patch1:        0001-use-released-aws-nitro-enclaves-cose-version.patch

# Patches >=1000 are only applied when using system Rust dependencies:
# - Update nix dependency from 0.26 to 0.31
#   https://github.com/fdo-rs/fido-device-onboard-rs/pull/803
Patch1000:        fido-device-onboard-fix-metadata.diff
Patch1001:        https://github.com/fdo-rs/fido-device-onboard-rs/pull/739.patch#/fido-libcryptsetup-rs-0.11.patch

# Because nobody cares
ExcludeArch: %{ix86}

%if 0%{?rhel} || (0%{?oreon} >= 11)
BuildRequires:  rust-toolset
%else
BuildRequires:  rust-packaging
%endif
BuildRequires:  clang-devel
BuildRequires:  cryptsetup-devel
BuildRequires:  device-mapper-devel
BuildRequires:  golang
BuildRequires:  openssl-devel >= 3.0.1-12
BuildRequires:  systemd-rpm-macros
BuildRequires:  tpm2-tss-devel
BuildRequires:  sqlite-devel
BuildRequires:  libpq-devel

%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if 0%{?rhel} || (0%{?oreon} >= 11)
%autosetup -n %{name}-rs-%{version} -N
%autopatch -p1 -M999
rm -f Cargo.lock
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%cargo_prep -v vendor
%else
%cargo_prep -V 1
%endif
%endif

%if 0%{?fedora} && !(0%{?oreon} >= 11)
%autosetup -p1 -n %{name}-rs-%{version}
%cargo_prep
%generate_buildrequires
%cargo_generate_buildrequires -a
%endif

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
# db sql files
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_manufacturing_server_postgres  migrations/migrations_manufacturing_server_postgres/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_manufacturing_server_sqlite  migrations/migrations_manufacturing_server_sqlite/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_owner_onboarding_server_postgres  migrations/migrations_owner_onboarding_server_postgres/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_owner_onboarding_server_sqlite  migrations/migrations_owner_onboarding_server_sqlite/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_rendezvous_server_postgres  migrations/migrations_rendezvous_server_postgres/2023-10-03-152801_create_db/*
install -D -m 0644 -t %{buildroot}%{_docdir}/fdo/migrations/migrations_rendezvous_server_sqlite  migrations/migrations_rendezvous_server_sqlite/2023-10-03-152801_create_db/*
# duplicates as needed by AIO command so link them
mkdir -p %{buildroot}%{_bindir}
ln -sr %{buildroot}%{_bindir}/fdo-owner-tool  %{buildroot}%{_libexecdir}/fdo/fdo-owner-tool
ln -sr %{buildroot}%{_bindir}/fdo-admin-tool %{buildroot}%{_libexecdir}/fdo/fdo-admin-tool
# Create directories needed by the various services so we own them
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
# Dracut manufacturing service
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/52fdo dracut/52fdo/module-setup.sh
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/52fdo dracut/52fdo/manufacturing-client-generator
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/52fdo dracut/52fdo/manufacturing-client-service
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/52fdo dracut/52fdo/manufacturing-client.service

%package -n fdo-init
Summary: dracut module for device initialization
License: %combined_license
Requires: openssl-libs >= 3.0.1-12
Requires: dracut
%description -n fdo-init
%{summary}

%files -n fdo-init
%license LICENSE LICENSE.dependencies
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%license cargo-vendor.txt
%endif
%{dracutlibdir}/modules.d/52fdo/
%{_libexecdir}/fdo/fdo-manufacturing-client

%package -n fdo-owner-onboarding-server
Summary: FDO Owner Onboarding Server implementation
License: %combined_license
Requires: openssl-libs >= 3.0.1-12
%description -n fdo-owner-onboarding-server
%{summary}

%files -n fdo-owner-onboarding-server
%license LICENSE LICENSE.dependencies
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%license cargo-vendor.txt
%endif
%dir %{_sysconfdir}/fdo
%dir %{_sysconfdir}/fdo/keys
%dir %{_sysconfdir}/fdo/owner-onboarding-server.conf.d
%dir %{_sysconfdir}/fdo/serviceinfo-api-server.conf.d
%dir %{_sysconfdir}/fdo/stores
%dir %{_sysconfdir}/fdo/stores/owner_onboarding_sessions
%dir %{_sysconfdir}/fdo/stores/owner_vouchers
%dir %{_sysconfdir}/fdo/stores/serviceinfo_api_devices
%{_libexecdir}/fdo/fdo-owner-onboarding-server
%{_libexecdir}/fdo/fdo-serviceinfo-api-server
%dir %{_localstatedir}/lib/fdo
%dir %{_docdir}/fdo
%{_docdir}/fdo/device_specific_serviceinfo.yml
%{_docdir}/fdo/serviceinfo-api-server.yml
%{_docdir}/fdo/owner-onboarding-server.yml
%{_docdir}/fdo/migrations/migrations_owner_onboarding_server_postgres/*
%{_docdir}/fdo/migrations/migrations_owner_onboarding_server_sqlite/*
%{_unitdir}/fdo-serviceinfo-api-server.service
%{_unitdir}/fdo-owner-onboarding-server.service

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

%files -n fdo-rendezvous-server
%license LICENSE LICENSE.dependencies
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%license cargo-vendor.txt
%endif
%dir %{_sysconfdir}/fdo
%dir %{_sysconfdir}/fdo/keys
%dir %{_sysconfdir}/fdo/rendezvous-server.conf.d
%dir %{_sysconfdir}/fdo/stores
%dir %{_sysconfdir}/fdo/stores/rendezvous_registered
%dir %{_sysconfdir}/fdo/stores/rendezvous_sessions
%{_libexecdir}/fdo/fdo-rendezvous-server
%dir %{_localstatedir}/lib/fdo
%dir %{_docdir}/fdo
%{_docdir}/fdo/rendezvous-*.yml
%{_docdir}/fdo/migrations/migrations_rendezvous_server_postgres/*
%{_docdir}/fdo/migrations/migrations_rendezvous_server_sqlite/*
%{_unitdir}/fdo-rendezvous-server.service

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

%files -n fdo-manufacturing-server
%license LICENSE LICENSE.dependencies
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%license cargo-vendor.txt
%endif
%dir %{_sysconfdir}/fdo
%dir %{_sysconfdir}/fdo/keys
%dir %{_sysconfdir}/fdo/manufacturing-server.conf.d
%dir %{_sysconfdir}/fdo/stores
%dir %{_sysconfdir}/fdo/stores/manufacturer_keys
%dir %{_sysconfdir}/fdo/stores/manufacturing_sessions
%dir %{_sysconfdir}/fdo/stores/owner_vouchers
%{_libexecdir}/fdo/fdo-manufacturing-server
%dir %{_localstatedir}/lib/fdo
%dir %{_docdir}/fdo
%{_docdir}/fdo/manufacturing-server.yml
%{_docdir}/fdo/migrations/migrations_manufacturing_server_postgres/*
%{_docdir}/fdo/migrations/migrations_manufacturing_server_sqlite/*
%{_unitdir}/fdo-manufacturing-server.service

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

%files -n fdo-client
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%license cargo-vendor.txt
%endif
%license LICENSE LICENSE.dependencies
%{_libexecdir}/fdo/fdo-client-linuxapp
%{_unitdir}/fdo-client-linuxapp.service

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

%files -n fdo-owner-cli
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%license cargo-vendor.txt
%endif
%license LICENSE LICENSE.dependencies
%{_bindir}/fdo-owner-tool
%{_libexecdir}/fdo/fdo-owner-tool

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

%files -n fdo-admin-cli
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%license cargo-vendor.txt
%endif
%license LICENSE LICENSE.dependencies
%dir %{_sysconfdir}/fdo
%dir %{_sysconfdir}/fdo/keys
%{_bindir}/fdo-admin-tool
%{_libexecdir}/fdo/fdo-admin-tool
%{_unitdir}/fdo-aio.service

%post -n fdo-admin-cli
%systemd_post fdo-aio.service

%preun -n fdo-admin-cli
%systemd_preun fdo-aio.service

%postun -n fdo-admin-cli
%systemd_postun_with_restart fdo-aio.service

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.5-8
- Import
