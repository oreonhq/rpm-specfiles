%global source0_hash ae285578f8565f9154c63e4234704b57b6835f77a2f82ffe724899d453262bb1

Name:           perl-HTML-Scrubber
Version:        0.19
Release:        19%{?dist}
Summary:        Library for scrubbing/sanitizing html
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Scrubber
Source0:        https://cpan.metacpan.org/authors/id/P/PO/PODMASTER/HTML-Scrubber-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Test::More) perl(Test::EOL) perl(Test::Memory::Cycle) perl(Test::NoTabs)
BuildRequires:	perl(Carp) perl(File::Spec) perl(File::Temp) perl(HTML::Entities) perl(utf8)
BuildRequires:  perl(IO::Handle) perl(IPC::Open3) perl(Test::CPAN::Meta)
BuildRequires:	perl(Module::Build) perl(Scalar::Util) perl(Test) perl(Test::Pod::Coverage)
BuildRequires:	perl(ExtUtils::MakeMaker) perl(Pod::Coverage::TrustPod) 
# Not in Fedora yet: perl(Test::PAUSE::Permissions)
# ... but the tests pass without it, so on we go.
BuildRequires:  perl(Test::CPAN::Meta) perl(Test::Differences) perl(Test::Kwalitee) perl(Test::Pod)
BuildRequires:	perl(HTML::Parser) >= 3.47
BuildRequires:	perl(List::Util) >= 1.33
BuildRequires:	perl(strict), perl(warnings)

%description
If you wanna "scrub" or "sanitize" html input in a reliable an flexible
fashion, then this module is for you.
I wasn't satisfied with HTML::Sanitizer because it is based on
HTML::TreeBuilder, so I thought I'd write something similar that works
directly with HTML::Parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Scrubber-%{version}
%{__perl} -pi -e 's/\r\n/\n/' Changes LICENSE README Scrubber.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/HTML/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
