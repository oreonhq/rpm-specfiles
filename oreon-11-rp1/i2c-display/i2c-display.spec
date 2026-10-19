%global source0_hash da7579628f7c488377933902c215e2caceea17499f307291142a268f4c9f5f5d
%bcond check 1
%global goipath         github.com/ausil/i2c-display
Version:                0.5.3
%gometa -L -f
Name:           i2c-display
Release:        1%{?dist}
Summary:        I2C OLED display controller for single board computers
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       systemd
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
A Go application for Single Board Computers (Raspberry Pi 3/4, Rock 3C) that
controls I2C OLED displays (SSD1306, SH1106, etc.) showing system stats and
network information with rotating pages.

Features:
- System monitoring (disk, RAM, CPU temperature)
- Network interface information
- Automatic page rotation
- Systemd integration
- JSON configuration

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

%build

%global gomodulesmode GO111MODULE=on
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
hardlink -cfv %{buildroot}/%{_licensedir}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -d %{buildroot}%{_sysconfdir}/i2c-display
install -m 0644 configs/config.example.json %{buildroot}%{_sysconfdir}/i2c-display/config.json
install -d %{buildroot}%{_docdir}/i2c-display/configs/platforms
install -m 0644 configs/*.json %{buildroot}%{_docdir}/i2c-display/configs/
install -m 0644 configs/platforms/*.json %{buildroot}%{_docdir}/i2c-display/configs/platforms/
install -m 0644 configs/platforms/README.md %{buildroot}%{_docdir}/i2c-display/configs/platforms/
install -d %{buildroot}%{_unitdir}
install -m 0644 systemd/i2c-display.service %{buildroot}%{_unitdir}/i2c-display.service
install -d %{buildroot}%{_mandir}/man1
install -m 0644 man/i2c-displayd.1 %{buildroot}%{_mandir}/man1/i2c-displayd.1
%oreon_autofiles main

%post

%systemd_post i2c-display.service
%preun

%systemd_preun i2c-display.service
%postun

%systemd_postun_with_restart i2c-display.service
%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
