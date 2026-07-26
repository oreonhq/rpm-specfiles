%global source0_hash bf20a1d76aad83fc3aabedc6ddc7f96b655dc94bec3fa276a50af6046ebb554c

Name:           xorsearch
Version:        1.11.4
Release:        9%{?dist}
Summary:        Search for a given string in an XOR, ROL, ROT or SHIFT encoded binary file

# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            http://blog.didierstevens.com/programs/xorsearch/

%global pkgver %(echo %{version} | sed 's/\\./_/g')
# Source0:      http://didierstevens.com/files/software/XORSearch_V%%{pkgver}.zip
Source0:        https://github.com/DidierStevens/FalsePositives/raw/master/XORSearch_V%{pkgver}.zip
Patch0:         %{name}-cosmetics.patch

BuildRequires:  gcc

%description
XORSearch is a program to search for a given string in an XOR, ROL, ROT or SHIFT
encoded binary file. An XOR encoded binary file is a file where some (or all)
bytes have been XORed with a constant value (the key). A ROL (or ROR) encoded
file has its bytes rotated by a certain number of bits (the key). A ROT encoded
file has its alphabetic characters (A-Z and a-z) rotated by a certain number
of positions. A SHIFT encoded file has its bytes shifted left by a certain
number of bits (the key): all bits of the first byte shift left, the MSB
of the second byte becomes the LSB of the first byte, all bits of the second
byte shift left, … XOR and ROL/ROR encoding is used by malware programmers
to obfuscate strings like URLs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -v -c -n %{name}-%{version}
#remove binaries
rm -rf OSX Linux XORSearch.exe

%build
# gcc %{optflags} -Wno-trigraphs XORSearch.c -o %{name}
gcc %{optflags} -Wno-trigraphs -D __APPLE__=1 XORSearch.c -o %{name}

%install
#Targetting EPEL as well
rm -rf "%{buildroot}"
install -m 755 -D %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%{_bindir}/%{name}

%changelog
%autochangelog
