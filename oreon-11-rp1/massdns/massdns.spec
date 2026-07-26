%global source0_hash 9ca6e684d2febf707f165ce74b7a38455302f5851309fb82b5951c28cb07d0d7

Name:           massdns
Version:        0.3
Release:        15%{?dist}
Summary:        High-performance DNS stub resolver for bulk lookups and reconnaissance

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/blechschmidt/massdns
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  ldns-devel

%description
MassDNS is a simple high-performance DNS stub resolver targetting those who
seek to resolve a massive amount of domain names in the order of millions or
even billions. Without special configuration, MassDNS is capable of resolving
over 350,000 names per second using publicly available resolvers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install PREFIX=%{buildroot}/usr/

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
