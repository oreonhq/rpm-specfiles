%global source0_hash 0fc94eb378dcba8c889e91f41dab3a8d6eebc7324a59a0704cc39aa66551987e

Name:          thinkfan
Version:       2.0.0
Release:       3%{?dist}
Summary:       A simple fan control program

License:       GPL-3.0-or-later
URL:           https://github.com/vmatare/thinkfan
Source0:       https://github.com/vmatare/thinkfan/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       thinkfan.modprobe
Source2:       thinkfan.sysconfig

# Fix systemd service install directory
Patch0:        thinkfan_systemd.patch
# Adapt for sbin-bin merge
Patch1:        thinkfan-sbin-bin.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: lm_sensors-devel
BuildRequires: systemd-units
BuildRequires: libatasmart-devel
BuildRequires: yaml-cpp-devel
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A simple fan control program. Works with any Linux hwmon driver, especially
with thinkpad_acpi. It is designed to eat as little CPU power as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DUSE_ATASMART:BOOL=ON
%cmake_build

%install
%cmake_install

# Install configuration file
install -Dpm 0644 examples/thinkfan.yaml %{buildroot}%{_sysconfdir}/thinkfan.conf

# Install modprobe configuration file
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d/thinkfan.conf

# Install sysconfig
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/thinkfan

# Installed through %%license
rm -f %{buildroot}/%{_pkgdocdir}/COPYING

%post
%systemd_post thinkfan.service

%preun
%systemd_preun thinkfan.service

%postun
%systemd_postun_with_restart thinkfan.service

%files
%license COPYING
%doc README.md
%doc %{_pkgdocdir}/thinkfan.yaml
%{_bindir}/thinkfan
%{_unitdir}/thinkfan.service
%{_unitdir}/thinkfan-wakeup.service
%{_unitdir}/thinkfan-sleep.service
%config(noreplace) %{_sysconfdir}/sysconfig/thinkfan
%config(noreplace) %{_sysconfdir}/thinkfan.conf
%config(noreplace) %{_sysconfdir}/modprobe.d/thinkfan.conf
%{_mandir}/man1/thinkfan.1.*
%{_mandir}/man5/thinkfan.conf.5.*
%{_mandir}/man5/thinkfan.conf.legacy.5.*

%changelog
%autochangelog
