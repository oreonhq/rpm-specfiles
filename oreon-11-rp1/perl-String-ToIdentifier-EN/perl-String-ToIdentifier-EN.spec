%global source0_hash 3afb84232930b9ac5b1ada383c8dd5907ae4e23aec5abb016f70f9e8053cdc8a

Name:           perl-String-ToIdentifier-EN
Version:        0.12
Release:        24%{?dist}
Summary:        Convert Strings to English Program Identifiers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-ToIdentifier-EN
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/String-ToIdentifier-EN-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Lingua::EN::Inflect::Phrase)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Unicode::UCD)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

%description
This module provides a utility method, "to_identifier" for converting an
arbitrary string into a readable representation using the ASCII subset of
\w for use as an identifier in a computer program. The intent is to make
unique identifier names from which the content of the original string can
be easily inferred by a human just by reading the identifier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-ToIdentifier-EN-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
