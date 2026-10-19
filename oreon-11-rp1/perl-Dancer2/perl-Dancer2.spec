%global source0_hash f0b98f8887cb8178124a06dd6f26ab85c71dcbeb0a18034669220abb47b87ed8
Name:           perl-Dancer2
Version:        2.0.1
Release:        1%{?dist}
Summary:        Lightweight yet powerful web application framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dancer2
Source0:        https://cpan.metacpan.org/authors/id/C/CR/CROMEDOME/Dancer2-%{version}.tar.gz
Patch0:         no-phone-home.patch
BuildArch:      noarch
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Exporter::Tiny)
Requires:       perl(File::Copy)
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(HTTP::Server::PSGI)
Requires:       perl(Moo) >= 1.003000
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(CGI::Deurl::XS)
BuildRequires:  perl(CLI::Osprey)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Censor)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Share)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Entity::Parser)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Headers::Fast)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Server::PSGI)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Math::Random::ISAAC::XS)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::MIME)
BuildRequires:  perl(Plack::Middleware::FixMissingBodyInRedirect)
BuildRequires:  perl(Plack::Middleware::Head)
BuildRequires:  perl(Plack::Middleware::RemoveRedundantBody)
BuildRequires:  perl(Plack::Middleware::Static)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Pod::Simple::Search)
BuildRequires:  perl(Pod::Simple::SimpleTree)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Tiny)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Registry)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URL::Encode::XS)
BuildRequires:  perl(YAML)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{make_build} test
%package -n dancer2
Summary:       Dancer2 command line interface
%description -n dancer2
Dancer2 is the new generation lightweight web-framework for Perl. This tool
provides nice, easily-extendable CLI interface for it.

%files -f %{oreon_filedir}/main.list
%files -n dancer2 -f %{oreon_filedir}/dancer2.list

%changelog

%autochangelog
