%global source0_hash eafd7c7655dfa8261df3446b931a283d30306877b83ac4671c49cff74ea7f00b

Name:           perl-HTML-Mason-PSGIHandler
Version:        0.53
Release:        38%{?dist}
Summary:        PSGI handler for HTML::Mason
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Mason-PSGIHandler
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RUZ/HTML-Mason-PSGIHandler-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  %{__make}
BuildRequires:  %{__perl}
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(CGI::PSGI)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Mason)
BuildRequires:  perl(HTML::Mason::CGIHandler)
BuildRequires:  perl(HTML::Mason::Exceptions)
BuildRequires:  perl(HTML::Mason::Request::CGI)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
HTML::Mason::PSGIHandler is a PSGI handler for HTML::Mason. It's based on
HTML::Mason::CGIHandler and allows you to process Mason templates on any
web servers that support PSGI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Mason-PSGIHandler-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
