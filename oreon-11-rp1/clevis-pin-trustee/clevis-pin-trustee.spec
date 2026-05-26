# SPDX-FileCopyrightText: Sergio Arroutbi <sarroutb@redhat.com>
#
# SPDX-License-Identifier: MIT
Name:           clevis-pin-trustee
Version:        0.1.0
Release:        %autorelease
Summary:        Clevis PIN for Trustee attestation

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
License:        BSD-3-Clause AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Zlib OR Apache-2.0) AND Unicode-3.0 AND (Unlicense OR MIT)
URL:            https://github.com/latchset/clevis-pin-trustee
Source0:        https://github.com/latchset/%{name}/archive/refs/tags/v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 5f229eed038f5259174b908614dff86a011c8dd837a29ed64495e6c4ef5b4dcc
%global source0_file v0.1.0.tar.gz
# oreon url source checksums end

BuildRequires:  cargo-rpm-macros

# Runtime dependencies
Requires:       clevis
Requires:       jose

%description
clevis-pin-trustee is a Clevis PIN that implements encryption and decryption
operations using remote attestation via a Trustee server. It enables automated
unlocking of LUKS-encrypted volumes in confidential computing environments by
fetching encryption keys from Trustee servers after successful attestation.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v0.1.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5f229eed038f5259174b908614dff86a011c8dd837a29ed64495e6c4ef5b4dcc" || { echo "oreon: Source0 SHA256 mismatch for v0.1.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
# Build using cargo macros
%cargo_build

# Generate license information for statically-linked dependencies
%cargo_license_summary
# Generate license file for bundled dependencies
%{cargo_license} > LICENSE.dependencies

%install
# Install main binary
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# Install Clevis wrapper scripts
install -D -m 0755 clevis-encrypt-trustee %{buildroot}%{_bindir}/clevis-encrypt-trustee
install -D -m 0755 clevis-decrypt-trustee %{buildroot}%{_bindir}/clevis-decrypt-trustee

%check
# Run tests using cargo macro
%cargo_test

%files
%license LICENSES/MIT.txt
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_bindir}/clevis-encrypt-trustee
%{_bindir}/clevis-decrypt-trustee

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.0-1
- Prepare for Oreon 11 (RP1)
