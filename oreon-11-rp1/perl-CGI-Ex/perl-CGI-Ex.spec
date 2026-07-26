%global source0_hash 2fbb4db15e713fcbfc164bb399dac033bd2abdd03a8f9370af6892ebbf7f777b

Name:           perl-CGI-Ex
Version:        2.55
Release:        7%{?dist}
Summary:        CGI utility suite - makes powerful application writing fun and easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Ex
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/CGI-Ex-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Config::IniHash)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Taint::Runtime)
BuildRequires:  perl(Template::Alloy) >= 1.016
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)

%{?perl_default_filter}

%description
CGI::Ex provides a suite of utilities to make writing CGI scripts more
enjoyable. Although they can all be used separately, the main functionality
of each of the modules is best represented in the CGI::Ex::App module.
CGI::Ex::App takes CGI application building to the next step. CGI::Ex::App
is not quite a framework (which normally includes pre-built HTML) instead
CGI::Ex::App is an extended application flow that dramatically reduces CGI
build time in most cases. It does so using as little magic as possible. See
CGI::Ex::App.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Ex-%{version}

# make rpmlint happy :)
find samples/ -type f -exec chmod -c -x {} \;
rm -f samples/app/app1/INSTALL
/usr/bin/perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/1_validate_14_untaint.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README samples/ t/
%license LICENSE
%{perl_vendorlib}/CGI*
%{_mandir}/man3/CGI*

%changelog
%autochangelog
