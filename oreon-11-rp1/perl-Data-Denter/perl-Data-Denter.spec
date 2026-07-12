%global source0_hash 3ab4ff9bd49497bfc711dccf8c990aab10470a7bba65a9877632b14d8f5fdb55

Name:           perl-Data-Denter
Version:        0.15
Release:        47%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        An alternative to Data::Dumper and Storable
Source:         https://cpan.metacpan.org/authors/id/I/IN/INGY/Data-Denter-%{version}.tar.gz
Url:            https://metacpan.org/release/Data-Denter
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(Test)

Provides:       perl(Data::Denter)
Provides:       perl(Data::Denter)
%description
The main problem with Data::Dumper (one of my all-time favorite modules)
is that you have to use 'eval()' to deserialize the data you've dumped.
This is great if you can trust the data you're evaling, but horrible if
you can't. A good alternative is Storable.pm. It can safely thaw your
frozen data.  But if you want to read/edit the frozen data, you're out of
luck, because Storable uses a binary format. Even Data::Dumper's output
can be a little cumbersome for larger data objects. Enter Data::Denter.

Data::Denter is yet another Perl data serializer/deserializer. It formats
nested data structures in an indented fashion. It is optimized for human
readability/editability, safe deserialization, and (eventually) speed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Denter-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
