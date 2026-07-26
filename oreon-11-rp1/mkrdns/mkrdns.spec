%global source0_hash 2f57ee90420beb26f43a17512da92bc354a1338803c6661e2726ac7a9c571e6a

%global commit 9dee4a3ff1438ce3099811833e80f614dfa78932
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:          mkrdns
Version:       3.3
Release:       18.20220829git%{shortcommit}%{?dist}
Summary:       Automatic reverse DNS zone generator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://github.com/oasys/%{name}
Source0:       https://github.com/oasys/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:     noarch
BuildRequires: perl-podlators
Requires:      perl-Getopt-Long

%description
mkrdns automates the tedious procedure of editing both forward and reverse 
zones when making changes to your zones with likely no changes to your current 
configuration file.

mkrdns does this by reading through all of the primary/secondary (master/slave) 
zones in your configuration file (either named.boot or named.conf). It will 
then automatically generate the reverse zone entries (IN PTR) for the networks 
for which you are the primary/master. It is now possible to simply edit the 
forward map, run mkrdns, and reload the zone. Clean, simple, and best of all, 
automatic.

mkrdns also acts as a limited lint-like program, issuing warnings and errors if 
there are problems with your configuration or zone files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
# Nothing to build

%install
install -Dp -m 0755 mkrdns %{buildroot}%{_bindir}/mkrdns
mkdir -p %{buildroot}%{_mandir}/man1
pod2man mkrdns %{buildroot}%{_mandir}/man1/mkrdns.1

%files
%doc README.md
%license LICENSE
%{_bindir}/mkrdns
%{_mandir}/man1/mkrdns.1.gz

%changelog
%autochangelog
