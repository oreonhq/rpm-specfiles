%global source1_hash 1ac9f6d29b1f8b41703153ec735a20b268bc3c4f9c67f5e4478b4604af88d3c0
%global source0_hash 1417e5c1b61e86bb9527db1f5bee1995a0eea82475db3cbc880e04bf706083e4
Name:           aeskeyfind
Version:        1.0
Release:        24%{?dist}
License:        LicenseRef-Callaway-BSD
Summary:        Locate 128-bit and 256-bit AES keys in a captured memory image
URL:            https://citp.princeton.edu/our-work/memory/
Source0:        http://citpsite.s3-website-us-east-1.amazonaws.com/memory-content/src/%{name}-%{version}.tar.gz
Source1:        http://citpsite.s3-website-us-east-1.amazonaws.com/oldsite-htdocs/memory-content/src/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-12E404FFD3C931F934052D06B8841A919D0FACE4.gpg
Source3:        aeskeyfind.1
Patch1:         aeskeyfind-10_add-GCC-hardening.patch
Patch2:         aeskeyfind-20_sbox-size.patch
Patch3: 	aeskeyfind-30_big-files-support.patch
Patch4: 	aeskeyfind-40_fix-undefined-left-shift.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
