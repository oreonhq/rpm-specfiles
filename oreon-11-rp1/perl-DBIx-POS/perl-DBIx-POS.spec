%global source0_hash 20587c4d86241f1db68a082b45d26a16cc7d99c668a37ac47735945f647b054f

Name:           perl-DBIx-POS
Version:        0.03
Release:        51%{?dist}
Summary:        Define a dictionary of SQL statements in a POD dialect (POS)
# There was some code that was taken from Class::Singleton, which was Artistic only at the time.
# That code has since been relicensed to GPL+ or Artistic.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-POS
Source0:        https://cpan.metacpan.org/authors/id/M/MD/MDORMAN/DBIx-POS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML)
# Tests
BuildRequires:  perl(Test::More)

%description
DBIx-POS subclasses Pod::Parser to define a POD dialect for writing a SQL
dictionary for an application, and uses code from Class::Singleton to make
the resulting structure easily accessible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-POS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
# we include the test as it's a bit more helpful than the man page, IMHO
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
