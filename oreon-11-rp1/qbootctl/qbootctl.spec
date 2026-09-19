%global source0_hash e66b361f86fac413f6a96974b4045a1fbc385f9eb6cee7fa8a26e0ca77c74a51

Name:           qbootctl
Version:        0.2.2
Release:        %autorelease
Summary:        CLI tool for manipulating A/B slots on Android devices
URL:            https://github.com/linux-msm/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service

# exceptions:
# crc32.c, crc32.h: GPL-2.0
# gpt-utils.c: BSD-3-Clause
# gpt-utils.h, ufs-bsg.*: BSD-3-Clause
# qbootctl.service: LGPL-2.1-or-later
License:        GPL-3.0-only AND BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros

%description
%{summary}.
It is a port of the original Android boot control HAL developed by
Qualcomm, modified to build on Linux and provide a friendly CLI
interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%ifarch aarch64
export LDFLAGS="$LDFLAGS -Wl,-z,force-bti"
%endif
%meson
%meson_build

%install
%meson_install
install -Dm644 %{SOURCE1} -t %{buildroot}%{_unitdir}

%post
%systemd_post                %{name}.service
%preun
%systemd_preun               %{name}.service
%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
%autochangelog
