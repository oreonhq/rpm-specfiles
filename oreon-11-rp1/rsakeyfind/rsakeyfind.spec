%global source1_hash 5e9071da164d42736999cf2bdf89c75c2a14c35979366c947afaf22c2e3347a5
%global source0_hash d897317636fc95548ea8c56d7d5585418abcb06bc68810dafd6944ea91965607
Name:           rsakeyfind
Version:        1.0
Release:        10%{?dist}
License:        BSD
Summary:        Locate BER-encoded RSA private and public keys in memory images
URL:            https://citp.princeton.edu/our-work/memory/
Source0:        https://citpsite.s3.amazonaws.com/memory-content/src/%{name}-%{version}.tar.gz
Source1:        https://citpsite.s3.amazonaws.com/memory-content/src/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-12E404FFD3C931F934052D06B8841A919D0FACE4.gpg
Source3:        rsakeyfind.1
Patch1:         rsakeyfind-10_add-GCC-hardening.patch
Patch2:         rsakeyfind-20_includes.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
The rsakeyfind tool locates BER-encoded RSA private and public keys in 
captured memory images. It can either try to locate keys based on a provided
hex-dump of a modulus of a known public key, or based on fixed pattern in
BER-encoded RSA version field.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#check signature
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}

%build

%set_build_flags
%make_build
%install
install -Dp -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -p -m644 %{SOURCE3} %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
