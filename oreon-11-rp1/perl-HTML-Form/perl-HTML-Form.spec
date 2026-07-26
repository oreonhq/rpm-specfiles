%global source0_hash ae5ad0f6fe70b1a382789d5e83a9b669cc541ee9d459e1bfa89b43ae0c014cdd

Name:           perl-HTML-Form
Version:        6.13
Release:        3%{?dist}
Summary:        Class that represents an HTML form element
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTML-Form
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTML-Form-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Request::Common) >= 6.03
BuildRequires:  perl(HTTP::Response) >= 7.01
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(HTML::TokeParser)
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Request::Common) >= 6.03

%{?perl_default_filter}

%description
Objects of the HTML::Form class represents a single HTML <form> ... </form>
instance. A form consists of a sequence of inputs that usually have names,
and which can take on various values. The state of a form can be tweaked
and it can then be asked to provide HTTP::Request objects that can be
passed to the request() method of LWP::UserAgent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Form-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
