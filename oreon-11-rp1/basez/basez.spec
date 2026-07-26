%global source0_hash 2a9f821488791c2763ef0120c75c43dc83dd16567b7c416f30331889fd598937

Name:           basez
Version:        1.6.2
Release:        10%{?dist}
Summary:        Base 16/32/64 encode/decode data to standard output

License:        GPL-3.0-or-later AND CC-BY-3.0-US AND BSD-2-Clause AND FSFAP
# BaseZ package: GPL-3.0-or-later
# Documentation: GPL-3.0-or-later OR CC-BY-3.0-US
# Core files: BSD-2-Clause
# ChangeLog: FSFAP
URL:            http://www.quarkline.net/%{name}/
Source0:        %{url}/download/%{name}-%{version}.tar.gz
Source1:        %{url}/download/README
Source2:        %{url}/download/%{name}-%{version}.tar.gz.sig
Source3:        %{url}/download/GPG-KEY

# sent this patch to upstream.  patch built for 1.6.2.
Patch0:         add_disable_hex_opt.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make

%description
BaseZ encodes/decodes base16, base32, base32hex, base64 or base64url data
stream per RFC 4648; MIME base64 Content-Transfer-Encoding per RFC 2045;
or PEM Printable Encoding per RFC 1421.

This binary package provides a list of commands: basez hex unhex base16
base32plain base32hex base64plain base64url base64mime base64pem

base32/64 are OMITTED from this package since coreutils provides them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE2}' --data='%{SOURCE0}'
%autosetup

%build
%configure \
  --disable-base32-command \
  --disable-base64-command \
  --disable-unhex-command \
  --disable-hex-command
# disabling base32/64 which are provided by coreutils
# disabling hex/unhex -> basez symlinks to prevent conflicts
%make_build

%check
make test

%install
%make_install
install -p %{SOURCE1} -t %{buildroot}%{_datadir}/doc/%{name}/
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE

%files
%license LICENSE
%doc README ChangeLog
%{_bindir}/*
%{_datadir}/bash-completion/completions/*
%{_mandir}/man1/*

%changelog
%autochangelog
