%global source0_hash acd4bbb55cc8e3aea76052cdeb94301eb8753b18820dc39795d3aedccaaa8a9d

Name:           perl-Types-DateTime
Version:        0.002
Release:        23%{?dist}
Summary:        Type constraints and coercions for datetime objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Types-DateTime/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Types-DateTime-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Locale)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 2.06
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Modern)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Type::Tiny) >= 0.041
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(warnings)

%description
Types::DateTime is a type constraint library suitable for use with
Moo/Moose attributes, Kavorka sub signatures, and so forth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Types-DateTime-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes COPYRIGHT CREDITS README
%license LICENSE
%{perl_vendorlib}/Types/
%{_mandir}/man3/Types::DateTime.3pm*

%changelog
%autochangelog
