%global source0_hash 5595ddf7876d17fb470dd3bbb2a89ed6d8f2a1f57d9450b49fba207761582a5d

Name:           perl-Symbol-Get
Version:        0.12
Release:        %autorelease
Summary:        Read Perl’s symbol table programmatically

License:        MIT
URL:            https://metacpan.org/dist/Symbol-Get
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FELIPE/Symbol-Get-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  /usr/bin/chmod
BuildRequires:  make
BuildRequires:  perl(Call::Context)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.44
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

%{?perl_default_filter}

%description
Occasionally I have need to reference a variable programmatically. This
module facilitates that by providing an easy, syntactic-sugar-y,
read-only interface to the symbol table.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Symbol-Get-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes
%doc README.md
%dir %{perl_vendorlib}/Symbol
%{perl_vendorlib}/Symbol/Get.pm
%{_mandir}/man3/Symbol::Get.3pm*

%changelog
%autochangelog
