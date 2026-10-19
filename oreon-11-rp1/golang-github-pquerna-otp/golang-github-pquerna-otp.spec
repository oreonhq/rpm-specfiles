%global source0_hash 2a7ea5baad4a15095bba2be39dddafd4b38c7b392476db3a761e78bb929a97e6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pquerna/otp
Version:                1.5.0
%gometa
%global common_description %{expand:
One Time Passwords (OTPs) are an mechanism to improve security over passwords
alone. When a Time-based OTP (TOTP) is stored on a user's phone, and combined
with something the user knows (Password), you have an easy on-ramp to
Multi-factor authentication without adding a dependency on a SMS provider. This
Password and TOTP combination is used by many popular websites including Google,
Github, Facebook, Salesforce and many others.
The otp library enables you to easily add TOTPs to your own application,
increasing your user's security against mass-password breaches and malware.}
%global golicenses      LICENSE NOTICE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        TOTP library for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/otp-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/boombuler/barcode)
BuildRequires:  golang(github.com/boombuler/barcode/qr)
BuildRequires:  golang(github.com/gokyle/twofactor)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
