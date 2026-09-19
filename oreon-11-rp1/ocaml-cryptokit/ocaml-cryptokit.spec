%global source0_hash b933c32b4e03e7236add969c2f583df241aeff8eabd2cabb1f345a78250fcea6

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-cryptokit
Version:        1.20.1
Release:        8%{?dist}
Summary:        OCaml library of cryptographic and hash functions

%global upver %(tr -d . <<< %{version})

# LGPL-2.0-or-later WITH OCaml-LGPL-linking-exception: the project as a whole
# LGPL-2.1-or-later: src/blowfish.{c,h}
License:        LGPL-2.0-or-later WITH OCaml-LGPL-linking-exception AND LGPL-2.1-or-later
URL:            https://github.com/xavierleroy/cryptokit/
VCS:            git:%{url}.git
Source0:        %{url}/archive/release%{upver}/cryptokit-%{version}.tar.gz
# Use zlib-ng directly instead of via the zlib compatibility API
Patch:          %{name}-zlib-ng.patch

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-dune >= 2.5
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-zarith-devel >= 1.4
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(zlib-ng)

%description
The Cryptokit library for Objective Caml provides a variety of
cryptographic primitives that can be used to implement cryptographic
protocols in security-sensitive applications. The primitives provided
include:

* Symmetric-key cryptography: AES, Chacha20, DES, Triple-DES, Blowfish,
  ARCfour, in ECB, CBC, CFB, OFB and counter modes.
* Authenticated encryption: AES-GCM, Chacha20-Poly1305.
* Public-key cryptography: RSA encryption and signature; Diffie-Hellman
  key agreement.
* Hash functions and MACs: SHA-3, SHA-2, BLAKE2, BLAKE3, RIPEMD-160;
  MACs based on AES and DES; SipHash.  (SHA-1 and MD5, despite being
  broken, are also provided for historical value.)
* Random number generation.
* Encodings and compression: base 64, hexadecimal, Zlib compression. 

Additional ciphers and hashes can easily be used in conjunction with
the library. In particular, basic mechanisms such as chaining modes,
output buffering, and padding are provided by generic classes that can
easily be composed with user-provided ciphers. More generally, the
library promotes a "Lego"-like style of constructing and composing
transformations over character streams.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-zarith-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cryptokit-release%{upver} -p1

%build
# On x86 and x86_64, the configure script finds support for the -maes flag in
# the compiler, and uses it to compile src/aesni.{c,h}.  This is okay because
# use of the compiled code is conditional.  The function aesni_check_available()
# is called first, which checks the CPUID to verify that the instructions exist
# on the CPU.  Therefore, older CPUs can still run the compiled code.
%dune_build

%check
# This opens /dev/random but never reads from it.
%dune_check

%install
%dune_install

%files -f .ofiles
%license LICENSE

%files devel -f .ofiles-devel
%doc README.md Changes

%changelog
%autochangelog
