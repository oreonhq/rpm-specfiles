%global source0_hash 14a8d5088a38d5849bd3d507a5c32fef957ec93cae6a45ef05ed6da1d61f07ba

Name:           logitech-27mhz-keyboard-encryption-setup
Version:        0.1
Release:        13%{?dist}
Summary:        Logitech 27MHz keyboard encryption setup tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/jwrdegoede/logitech-27mhz-keyboard-encryption-setup
Source0:        https://gitlab.freedesktop.org/jwrdegoede/logitech-27mhz-keyboard-encryption-setup/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  make gcc libusb1-devel

%description
A tool for enabling encryption on the 27 MHz wireless connection
used by some (somewhat older) Logitech keyboards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%build
%make_build PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_bindir}/lg-27MHz-keyboard-encryption-setup

%changelog
%autochangelog
