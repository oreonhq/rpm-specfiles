%global source0_hash 5720a649267a240a4f7ba5a6445193481070049c1d08ba38b00d20fc551c3a67

Name:       pass-otp
Version:    1.2.0
Release:    19%{?dist}
Summary:    A pass extension for managing one-time-password (OTP) tokens
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
BuildArch:  noarch
URL:        https://github.com/tadfisher/pass-otp
Source:     https://github.com/tadfisher/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2136582
Patch0:     %{name}-1.2.0-fix_hotp_counter.patch
BuildRequires: make
BuildRequires: expect
BuildRequires: git
BuildRequires: pass >= 1.7.0
BuildRequires: oathtool
Requires:   pass >= 1.7.0
Requires:   oathtool
Requires:   qrencode
Suggests:   zbar

%description
pass-otp extends the pass utility with the otp command for adding OTP secrets,
generating OTP codes, and displaying secret key URIs using the standard
otpauth:// scheme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build

%install
%make_install

%check
%make_build test

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_usr}/lib/password-store/extensions/otp.bash
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/bash_completion.d/pass-otp

%changelog
%autochangelog
