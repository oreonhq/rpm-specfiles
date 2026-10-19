%global source0_hash f139d2b3114c549e91847daaab8b75cb699e57daf5bbf0dbd13293f33fe5e22a
Name:           perl-Web-Machine
Version:        0.17
Release:        14%{?dist}
Summary:        Perl port of Webmachine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Web-Machine
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Web-Machine-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(GD::Simple)
BuildRequires:  perl(HTTP::Headers::ActionPack)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(IO::Handle::Util)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Net::HTTP)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Plack::Component)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
