%global source0_hash f139d2b3114c549e91847daaab8b75cb699e57daf5bbf0dbd13293f33fe5e22a

Name:           perl-Web-Machine
Version:        0.17
Release:        14%{?dist}
Summary:        Perl port of Webmachine
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Web-Machine
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Web-Machine-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTTP::Headers::ActionPack) >= 0.07
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(IO::Handle::Util)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Plack::Component)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
# test requirements
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(GD::Simple)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::HTTP)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%description
Web::Machine provides a RESTful web framework modeled as a state machine.
You define one or more resource classes. Each resource represents a single
RESTful URI end point, such as a user, an email, etc. The resource class
can also be the target for POST requests to create a new user, email, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Web-Machine-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes CONTRIBUTING.md README.md
%license LICENSE
%{perl_vendorlib}/Web*
%{_mandir}/man3/Web*

%changelog
%autochangelog
