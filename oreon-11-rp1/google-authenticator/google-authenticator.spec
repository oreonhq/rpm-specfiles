%global source0_hash d9b59ab064675d927166f83ade9424078287366b3efd1cf39ba91938867621fe
Name:           google-authenticator
Version:        1.11
Release:        1%{?dist}
Summary:        One-time pass-code support using open standards
License:        Apache-2.0
URL:            https://github.com/google/%{name}-libpam/
Source0:        https://github.com/google/%{name}-libpam/archive/%{version}.zip
Requires:       qrencode-libs
# oreon:deps
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pam-devel
# /oreon:deps
%description
The Google Authenticator package contains a plug-able authentication
module (PAM) which allows login using one-time pass-codes conforming to
the open standards developed by the Initiative for Open Authentication
(OATH) (which is unrelated to OAuth).

Pass-code generators are available (separately) for several mobile
platforms.

These implementations support the HMAC-Based One-time Password (HOTP)
algorithm specified in RFC 4226 and the Time-based One-time Password
(TOTP) algorithm currently in draft.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-libpam-%{version}

%build

./bootstrap.sh
%configure
make %{?_smp_mflags}
%check

make check
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
