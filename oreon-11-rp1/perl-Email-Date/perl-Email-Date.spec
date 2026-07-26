%global source0_hash 437c572b1aa9d1c77da26595bb03e003a3b2756c2fcc87d65177b10fc07d52c9

Name:           perl-Email-Date
Version:        1.104
Release:        33%{?dist}
Summary:        Find and format date headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Date
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-Date-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Module
BuildRequires:  perl(Date::Parse) >= 2.27
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Email::Date::Format) >= 1.000
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Piece) >= 1.08
# Dependencies
Requires:       perl(Email::Abstract)

%description
RFC 2822 defines the "Date:" header. It declares the header a required
part of an email message. The syntax for date headers is clearly laid
out. Stil, even a perfectly planned world has storms. The truth is, many
programs get it wrong. Very wrong. Or, they don't include a "Date:"
header at all. This often forces you to look elsewhere for the date, and
hoping to find something.

For this reason, the tedious process of looking for a valid date has
been encapsulated in this software. Further, the process of creating RFC
compliant date strings is also found in this software.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Date-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::Date.3*

%changelog
%autochangelog
