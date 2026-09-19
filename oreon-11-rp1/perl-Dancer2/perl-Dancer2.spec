%global source0_hash f0b98f8887cb8178124a06dd6f26ab85c71dcbeb0a18034669220abb47b87ed8

Name:           perl-Dancer2
Version:        2.0.1
Release:        3%{?dist}
Summary:        Lightweight yet powerful web application framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Dancer2
Source0:        https://cpan.metacpan.org/authors/id/C/CR/CROMEDOME/Dancer2-%{version}.tar.gz
# https://anonscm.debian.org/cgit/pkg-perl/packages/libdancer2-perl.git/plain/debian/patches/no-phone-home.patch?id=cfa2426c2feb48bfb8b433a53449374273612f73
Patch0:         no-phone-home.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CLI::Osprey)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Censor) >= 0.04
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Share)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Entity::Parser)
BuildRequires:  perl(HTTP::Headers::Fast) >= 0.21
BuildRequires:  perl(HTTP::Server::PSGI)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.16
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
# Plack::Builder version from Plack >= 1.0035 in Makefile.PL
BuildRequires:  perl(Plack::Builder) >= 1.0035
BuildRequires:  perl(Plack::Middleware::FixMissingBodyInRedirect)
BuildRequires:  perl(Plack::Middleware::Head)
BuildRequires:  perl(Plack::Middleware::RemoveRedundantBody)
BuildRequires:  perl(Plack::Middleware::Static)
BuildRequires:  perl(Plack::MIME)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Pod::Simple::Search)
BuildRequires:  perl(Pod::Simple::SimpleTree)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Tiny) >= 1.16
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Registry)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(YAML) >= 0.86
# Optional run-time:
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(CGI::Deurl::XS)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Math::Random::ISAAC::XS)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(URL::Encode::XS)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Test)
# Test::CPAN::Meta not used
BuildRequires:  perl(Test::Fatal)
# Test::NoTabs not used
# Test::Pod 1.41 not used
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional tests:
BuildRequires:  perl(Test::Memory::Cycle) >= 1.04
BuildRequires:  perl(Test::MockTime)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Exporter::Tiny)
Requires:       perl(File::Copy)
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(HTTP::Server::PSGI)
Requires:       perl(Moo) >= 1.003000
# Plack::Builder version from Plack >= 1.0035 in Makefile.PL
Requires:       perl(Plack::Builder) >= 1.0035
Requires:       perl(Pod::Simple::Search)
Requires:       perl(Pod::Simple::SimpleTree)
Requires:       perl(Template::Tiny)
Requires:       perl(Test::EOL)
Requires:       perl(Test::More) >= 0.92
Requires:       perl(Types::Standard)
Requires:       perl(YAML) >= 0.86

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Exporter\\)$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moo\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Plack::Builder\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Test::More\\)$
%global __requires_exclude %__requires_exclude|^perl\\(YAML\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Dancer2::Plugin::Auth::Tiny\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Dancer2::Plugin::CryptPassphrase\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Dancer2::Plugin::DBIx::Class\\)$

%description
Dancer2 is the new generation of Dancer, the lightweight web-framework for
Perl. It is a complete rewrite based on Moo and is meant to be easy and fun.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dancer2-%{version}
%patch 0 -p1
/usr/bin/sed -i -e '1s,#!.*perl,#!/usr/bin/perl,' script/dancer2 share/skel/default/bin/+app.psgi share/skel/tutorial/bin/+app.psgi
/usr/bin/chmod +x share/skel/default/bin/+app.psgi share/skel/tutorial/bin/+app.psgi
/usr/bin/rm share/.gitignore

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc AUTHORS Changes CONTRIBUTING.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%package -n dancer2
Summary:       Dancer2 command line interface

%description -n dancer2
Dancer2 is the new generation lightweight web-framework for Perl. This tool
provides nice, easily-extendable CLI interface for it.

%files -n dancer2
%license LICENSE
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
