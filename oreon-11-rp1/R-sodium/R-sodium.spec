%global source0_hash 937d53d5e401f9f7007949e150d7c09c6230fb255c95116b89b5c3237c501acd

Name:           R-sodium
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        A Modern and Easy-to-Use Crypto Library

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libsodium)

%description
Bindings to 'libsodium': a modern, easy-to-use software library for encryption,
decryption, signatures, password hashing and more. Sodium uses curve25519, a
state-of-the-art Diffie-Hellman function by Daniel Bernstein, which has become
very popular after it was discovered that the NSA had backdoored Dual EC DRBG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
