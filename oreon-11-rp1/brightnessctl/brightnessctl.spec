%global source0_hash a68869e23f56ac4f2e28f1783002810ddbf10f95e1af9b48b2912fb169f46994
Name:		brightnessctl
Version:	0.5.1
Release:        16%{?dist}
Summary:        Read and control device brightness
License:	MIT
URL:		https://github.com/Hummer12007/brightnessctl
Source0:        https://github.com/Hummer12007/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:		brightnessctl-0.5.1-Support-displaying-brightness-as-a-percentage.patch
Requires: systemd >= 243
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libsystemd)
# /oreon:deps
%description
This program allows you read and control device brightness. Devices,
by default, include back-light and LEDs (searched for in corresponding
classes).

It can also preserve current brightness before applying the operation,
allowing for use cases like disabling back-light on lid close.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export ENABLE_SYSTEMD=1
%set_build_flags
%make_build
%install
%make_install INSTALL_UDEV_RULES=0 ENABLE_SYSTEMD=1 PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
