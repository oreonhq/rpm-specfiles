%global source1_hash 083802bcf6be6c23bf8d9368c0129126fc6247864502099f1600258c26c60170
%global source0_hash 61886a377dabf98797145c31f6ba95e6837b6786e70c932324b7d6176d50f7fb
Summary:        Filter IPv4 and IPv6 addresses matching CIDR patterns
Name:           grepcidr
Version:        2.0
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.pc-tools.net/unix/grepcidr/
Source0:        https://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz
Source1:        https://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz.sha512
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The grepcidr utility can be used to filter a list of IP addresses against
one or more Classless Inter-Domain Routing (CIDR) specifications. As with
grep, there are options to invert matching and load patterns from a file.
It is capable of efficiently processing large numbers of IPs and networks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -e 's/install /$(INSTALL) /' -i Makefile

%build

%make_build CFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS"
%install
%make_install BINDIR="%{_bindir}" MANDIR="%{_mandir}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
