%global source0_hash 937d53d5e401f9f7007949e150d7c09c6230fb255c95116b89b5c3237c501acd
Name:           R-sodium
Version:        %R_rpm_version 1.4.0
Release:        1%{?dist}
Summary:        A Modern and Easy-to-Use Crypto Library
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=sodium&version=%{version}#/sodium_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  pkgconfig(libsodium)
# /oreon:deps
%description
Bindings to 'libsodium': a modern, easy-to-use software library for encryption,
decryption, signatures, password hashing and more. Sodium uses curve25519, a
state-of-the-art Diffie-Hellman function by Daniel Bernstein, which has become
very popular after it was discovered that the NSA had backdoored Dual EC DRBG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
