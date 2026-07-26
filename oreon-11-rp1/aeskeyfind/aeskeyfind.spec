%global source0_hash 1417e5c1b61e86bb9527db1f5bee1995a0eea82475db3cbc880e04bf706083e4

Name:           aeskeyfind
Version:        1.0
Release:        24%{?dist}
# 3-clause BSD license
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Summary:        Locate 128-bit and 256-bit AES keys in a captured memory image

# Original URL: https://citp.princeton.edu/research/memory/
# https://citp.princeton.edu/our-work/memory/
# https://citp.princeton.edu/our-work/memory/code
URL:            https://citp.princeton.edu/our-work/memory/
# New mirror on github
# Mirror        https://github.com/DonnchaC/coldboot-attacks
# Fork          https://github.com/makomk/aeskeyfind

#               https://citp.princeton.edu/memory-content/src/aeskeyfind-1.0.tar.gz
#               https://web.archive.org/web/20160501132651/https://citp.princeton.edu/memory-content/src/aeskeyfind-1.0.tar.gz
#               http://citpsite.s3-website-us-east-1.amazonaws.com/oldsite-htdocs/memory-content/src/%%{name}-%%{version}.tar.gz
Source0:        http://citpsite.s3-website-us-east-1.amazonaws.com/memory-content/src/%{name}-%{version}.tar.gz

#               https://web.archive.org/web/20160501132651/https://citp.princeton.edu/memory-content/src/aeskeyfind-1.0.tar.gz.asc
#               http://citpsite.s3-website-us-east-1.amazonaws.com/oldsite-htdocs/memory-content/src/%%{name}-%%{version}.tar.gz.asc
Source1:        http://citpsite.s3-website-us-east-1.amazonaws.com/oldsite-htdocs/memory-content/src/%{name}-%{version}.tar.gz.asc

# The authenticator public key obtained from release 1.0
# gpg2 -vv aeskeyfind-1.0.tar.gz.asc
# Signed by Jacob Appelbaum <jacob () appelbaum net>
# gpg2 --search-key B8841A919D0FACE4
# gpg2 --search-key 12E404FFD3C931F934052D06B8841A919D0FACE4
# gpg2 --list-public-keys 12E404FFD3C931F934052D06B8841A919D0FACE4
# gpg2 --export --export-options export-minimal 12E404FFD3C931F934052D06B8841A919D0FACE4 > gpgkey-12E404FFD3C931F934052D06B8841A919D0FACE4.gpg
Source2:        gpgkey-12E404FFD3C931F934052D06B8841A919D0FACE4.gpg

# Manual page from Debian
Source3:        aeskeyfind.1

# Original Debian patch to allow build hardening by usage of CFLAGS and LDFLAGS
# Author: Joao Eriberto Mota Filho <eriberto@debian.org>
Patch1:         aeskeyfind-10_add-GCC-hardening.patch

# Original Debian patch to fix the size of the sbox
# Author: Samuel Henrique <samueloph@debian.org>
Patch2:         aeskeyfind-20_sbox-size.patch

# Original Debian patch to support for files bigger than 4GB
# Author: Harry Sintonen <debianbugs@kyber.fi>
Patch3: 	aeskeyfind-30_big-files-support.patch

# Original Debian patch to fix silent regression caused by UC
# Author: Adrian Bunk <bunk@debian.org>
Patch4: 	aeskeyfind-40_fix-undefined-left-shift.patch

Buildrequires:  gcc
Buildrequires:  make
BuildRequires:  gnupg2

%description
This program illustrates automatic techniques for locating 128-bit and
256-bit AES keys in a captured memory image.

The program uses various algorithms and also performs a simple entropy
test to filter out blocks that are not keys. It counts the number of
repeated bytes and skips blocks that have too many repeats.

This method works even if several bits of the key schedule have been
corrupted due to memory decay.

This package is useful to several activities, as forensics investigations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#check signature
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}

%build
%set_build_flags
%make_build %{?_smp_mflags}

%install
install -Dp -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -p -m644 %{SOURCE3} %{buildroot}%{_mandir}/man1

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
