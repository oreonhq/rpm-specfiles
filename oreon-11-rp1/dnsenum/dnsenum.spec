%global source0_hash 1eea22c047736cee66d9cdd97181a68362bcfcede83d517891df7567936d55c1

Name:       dnsenum 
Version:    1.3.2
Release:    5%{?dist}
Summary:    A tool to enumerate DNS info about domains 

License:    GPL-2.0-or-later
URL:        https://github.com/SparrowOchon/dnsenum2
Source0:    https://github.com/SparrowOchon/dnsenum2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make
BuildRequires:  perl-generators

Requires:   perl-WWW-Mechanize
Requires:   perl-Readonly

%description
The purpose of this tool is to gather as much information as possible about a 
domain. The program currently gathers A, NS, MX records, performs axfr queries,
gets extra names and subdomains via google scraping, bruteforces subdomains from
file, calculate C class domain network ranges, perform reverse lookups on
netranges, writes ip-blocks to domain_ips.txt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dnsenum2-%{version} -p 1
pod2man dnsenum.pl > dnsenum.1

%build
# nothing to build

%install
%make_install INSTALL_DEPS=-1

%files
%doc README.md
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
