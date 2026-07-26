%global source0_hash 64305ce8028e799b27a11537f3c2aae4fa7512ccd0484ea0c1d4f47c73d28c4b

# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Date-Holidays-DE

Summary:        Perl module to determine German holidays
Name:           perl-Date-Holidays-DE
Version:        2.07
Release:        3%{?dist}
License:        MIT
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/F/FR/FROGGS/%{pkgname}-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(warnings)
BuildArch:      noarch

%description
A perl module that creates a list of German holidays in a given year.
It knows about special holiday regulations for all of Germany's federal
states and also about "semi-holidays" and religious "silent days" that
will be treated as holidays on request. Holidays that occur on weekends
can be excluded from the generated list. The generated list can also be
freely formatted using regular strftime() format definitions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

# Don't add dependencies for %%doc
chmod -x example/*.pl

%check
make test

%files
%doc Changes README example
%{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Date/Holidays/

%changelog
%autochangelog
