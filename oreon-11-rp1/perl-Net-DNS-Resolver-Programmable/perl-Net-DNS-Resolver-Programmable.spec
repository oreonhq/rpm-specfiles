# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8080a2ab776629585911af1179bdb7c4dc2bebfd4b5efd77b11d1dac62454bf8
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           perl-Net-DNS-Resolver-Programmable
Version:        0.009
Release:        24%{?dist}
Summary:        Programmable DNS resolver class for offline emulation of DNS
# License contradicts itself, saying "same as perl" (which would be (GPL-1.0-or-later OR Artistic-1.0-Perl))
# but then going on to clarify that as "either the GNU General Public License (version 2 or later) or the Artistic License"
# Clarification requested at https://rt.cpan.org/Ticket/Display.html?id=147412
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-DNS-Resolver-Programmable
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Net-DNS-Resolver-Programmable-0.009.tar.gz

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl%{?fedora:-interpreter}
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Net::DNS) >= 0.69
BuildRequires:  perl(Net::DNS::Packet)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More)
# Dependencies
# (none)

%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant class
that allows a virtual DNS to be emulated instead of querying the real DNS.
A set of static DNS records may be supplied, or arbitrary code may be
specified as a means for retrieving DNS records, or even generating them
on the fly.

%prep
%oreon_verify_sources
%setup -q -n Net-DNS-Resolver-Programmable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc CHANGES README TODO
%{perl_vendorlib}/Net/
%{_mandir}/man3/Net::DNS::Resolver::Programmable.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.009-24
- Prepare for Oreon 11 (RP1)
