%global source0_hash ccb07ad337a03aec81a1bea0a89cd2954691ff5bb367df9a32b9d9130f175110

Name:           perl-WebService-Validator-HTML-W3C
Version:        0.28
Release:        39%{?dist}
Summary:        Access the W3Cs online HTML validator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Validator-HTML-W3C
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STRUAN/WebService-Validator-HTML-W3C-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Recommends:     perl(XML::XPath)

%{?perl_default_filter}

%description
WebService::Validator::HTML::W3C provides access to the W3C's online Markup
validator. As well as reporting on whether a page is valid it also provides
access to a detailed list of the errors and where in the validated document
they occur.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WebService-Validator-HTML-W3C-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
