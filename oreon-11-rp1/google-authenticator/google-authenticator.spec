%global source0_hash d9b59ab064675d927166f83ade9424078287366b3efd1cf39ba91938867621fe

Name:           google-authenticator
Version:        1.11
Release:        4%{?dist}
Summary:        One-time pass-code support using open standards

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/google/%{name}-libpam/
Source0:        https://github.com/google/%{name}-libpam/archive/%{version}.zip
Requires:       qrencode-libs
BuildRequires:  pam-devel
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make

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

%files
/%{_usr}/%{_lib}/security/*
%{_bindir}/%{name}
%doc CONTRIBUTING.md
%doc %attr(0644,root,root) %{_mandir}/man1/%{name}*
%doc %attr(0644,root,root) %{_mandir}/man8/pam_google_authenticator*
%docdir %{_docdir}/%{name}
%license LICENSE
%{_docdir}/%{name}/*

%changelog
%autochangelog
