%global source0_hash faa869bc426573641536a09f53502e540d5e3e3ad6a7aa1ac625d3f6976b42e1

Name:           perl-SQL-Tokenizer
Version:        0.24
Release:        32%{?dist}
Summary:        Simple SQL tokenizer
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/SQL-Tokenizer
Source0:        https://cpan.metacpan.org/authors/id/I/IZ/IZUT/SQL-Tokenizer-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
SQL::Tokenizer is a simple tokenizer for SQL queries. It does not claim to
be a parser or query verifier. It just creates sane tokens from a valid
SQL query.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-Tokenizer-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

# SQL-Tokenizer does not honor ExtUtils::MakeMaker's NO_PACKLIST
# Until this changes, we do things the old-fashioned way
# https://rt.cpan.org/Ticket/Display.html?id=107930
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/SQL*
%{_mandir}/man3/SQL*

%changelog
%autochangelog
