%global source0_hash 2127b754afb3b191fb71e536c2c160a0e6975dad48b3d469c0e3f3290c0ee31c
%bcond check 1
%global goipath         github.com/Yubico/yubihsm-connector
Version:                3.0.7
%global tag             3.0.7
%gometa -L -f
%global common_description %{expand:
Backend to talk to YubiHSM 2}
Name:           yubihsm-connector
Release:        1%{?dist}
Summary:        YubiHSM Connector
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0 AND Zlib
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        %{gosource}.sig
Source4:        gpgkey-9588EA0F.gpg
%{?systemd_requires}
Recommends:     yubihsm-shell
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --quiet --keyring %{SOURCE4} %{SOURCE3} %{SOURCE0}
%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

# Create a sysusers.d config file
cat >yubihsm-connector.sysusers.conf <<EOF
u yubihsm-connector - 'YubiHSM connector account' - -
EOF

%build

go generate
%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/yubihsm-connector %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644  deb/yubihsm-connector.yaml %{buildroot}%{_sysconfdir}/yubihsm-connector.yaml
install -Dpm 0644  deb/yubihsm-connector.service %{buildroot}%{_unitdir}/yubihsm-connector.service
install -Dpm 0644  deb/70-yubihsm-connector.rules %{buildroot}%{_udevrulesdir}/70-yubihsm-connector.rules
install -m0644 -D yubihsm-connector.sysusers.conf %{buildroot}%{_sysusersdir}/yubihsm-connector.conf
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%post

%systemd_post yubihsm-connector.service
%preun

%systemd_preun yubihsm-connector.service
%postun

%systemd_postun_with_restart yubihsm-connector.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
