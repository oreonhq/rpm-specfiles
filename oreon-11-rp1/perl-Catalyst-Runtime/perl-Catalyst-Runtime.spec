%global source0_hash bb83758b7bda360d16e002e5ace69c6459e3d47227cdee6ac4b1b65a6685f110
Name:           perl-Catalyst-Runtime
Summary:        Catalyst Framework Runtime
Version:        5.90132
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Runtime-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Runtime
BuildArch:      noarch
Requires:       perl(B::Hooks::EndOfScope) >= 0.08
Requires:       perl(CGI::Simple::Cookie) >= 1.11
Requires:       perl(Class::C3::Adopt::NEXT) >= 0.07
Requires:       perl(Class::Load) >= 0.12
Requires:       perl(Class::MOP) >= 0.95
Requires:       perl(HTML::HeadParser)
Requires:       perl(HTTP::Body) >= 1.06
Requires:       perl(HTTP::Headers) >= 1.64
Requires:       perl(HTTP::Request) >= 5.814
Requires:       perl(HTTP::Response) >= 5.813
Requires:       perl(List::Util) >= 1.45
Requires:       perl(LWP::UserAgent)
Requires:       perl(Module::Pluggable::Object) >= 4.7
Requires:       perl(Moose) >= 1.03
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00903
Requires:       perl(MooseX::Getopt) >= 0.30
Requires:       perl(MooseX::MethodAttributes::Role::AttrContainer::Inheritable) >= 0.24
Requires:       perl(MooseX::Role::WithOverloading) >= 0.09
Requires:       perl(namespace::clean) >= 0.23
Requires:       perl(Path::Class) >= 0.09
Requires:       perl(Plack::Middleware::MethodOverride) >= 0.12
Requires:       perl(Plack::Middleware::ReverseProxy) >= 0.04
Requires:       perl(Plack::Request) >= 0.9991
Requires:       perl(Plack::Test::ExternalServer)
Requires:       perl(Socket) >= 1.96
Requires:       perl(String::RewritePrefix) >= 0.004
Requires:       perl(Text::SimpleTable) >= 0.03
Requires:       perl(Tree::Simple) >= 1.15
Requires:       perl(URI) >= 1.35
Provides:       perl-Catalyst-Plugin-Unicode-Encoding = 99.0
Obsoletes:      perl-Catalyst-Plugin-Unicode-Encoding <= 1.9
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CGI::Simple::Cookie\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::C3::Adopt::NEXT\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::Load\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::MOP\\)$
%global __requires_exclude %__requires_exclude|^perl\\(HTTP::Body\\)$
%global __requires_exclude %__requires_exclude|^perl\\(HTTP::Headers\\)$
%global __requires_exclude %__requires_exclude|^perl\\(HTTP::Request\\)$
%global __requires_exclude %__requires_exclude|^perl\\(List::Util\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Module::Pluggable::Object\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Moose\\)$
%global __requires_exclude %__requires_exclude|^perl\\(MooseX::Getopt\\)$
%global __requires_exclude %__requires_exclude|^perl\\(MooseX::MethodAttributes::Role::AttrContainer::Inheritable\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Path::Class\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Plack::Middleware::MethodOverride\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Plack::Middleware::ReverseProxy\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Plack::Request\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Socket\\)$
%global __requires_exclude %__requires_exclude|^perl\\(String::RewritePrefix\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Text::SimpleTable\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Tree::Simple\\)$
%global __requires_exclude %__requires_exclude|^perl\\(URI\\)$
%global __requires_exclude %__requires_exclude|^perl\\(namespace::autoclean\\)$
%global __requires_exclude %__requires_exclude|^perl\\(namespace::clean\\)$
# oreon:deps
BuildRequires:  /usr/bin/perldoc
BuildRequires:  groff
BuildRequires:  make
BuildRequires:  perl(CGI::Simple::Cookie)
BuildRequires:  perl(CGI::Struct)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::C3::Adopt::NEXT)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Class::MOP::Object)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(Devel::InnerPackage)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(HTTP::Body::OctetStream)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Daemonize)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::MethodAttributes)
BuildRequires:  perl(MooseX::MethodAttributes::Role)
BuildRequires:  perl(MooseX::MethodAttributes::Role::AttrContainer::Inheritable)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Plack::App::File)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Handler::Starman)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Middleware::Conditional)
BuildRequires:  perl(Plack::Middleware::ContentLength)
BuildRequires:  perl(Plack::Middleware::FixMissingBodyInRedirect)
BuildRequires:  perl(Plack::Middleware::HTTPExceptions)
BuildRequires:  perl(Plack::Middleware::Head)
BuildRequires:  perl(Plack::Middleware::IIS6ScriptNameFix)
BuildRequires:  perl(Plack::Middleware::IIS7KeepAliveFix)
BuildRequires:  perl(Plack::Middleware::LighttpdScriptNameFix)
BuildRequires:  perl(Plack::Middleware::MethodOverride)
BuildRequires:  perl(Plack::Middleware::RemoveRedundantBody)
BuildRequires:  perl(Plack::Middleware::ReverseProxy)
BuildRequires:  perl(Plack::Middleware::Static)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Request::Upload)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Test::ExternalServer)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Stream::Buffered)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::SimpleTable)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Tree::Simple)
BuildRequires:  perl(Tree::Simple::Visitor::FindByPath)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(URI::http)
BuildRequires:  perl(URI::https)
BuildRequires:  perl(attributes)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is the primary class for the Catalyst-Runtime distribution.  It provides
the core of any runtime Catalyst instance.
 
%package        scripts
Summary:        Scripts for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Catalyst::Devel) >= 1.0
%description    scripts

The %{name}-scripts package contains scripts distributed with
%{name} but generally used for developing Catalyst applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Runtime-%{version}

# something like this seems to beg for explicitness
perldoc perlgpl      > COPYING.gpl
perldoc perlartistic > COPYING.artistic

find .  -type f -exec chmod -c -x {} +
find t/ -type f -exec /usr/bin/perl -pi -e 's|^#!perl|#!/usr/bin/perl|' {} +

%build

PERL5_CPANPLUS_IS_RUNNING=1 /usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export TEST_LIGHTTPD=1
export TEST_HTTP=0
export TEST_POD=1
export TEST_STRESS=1
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
make clean
%files -f %{oreon_filedir}/main.list
%files -n perl-Catalyst-Runtime-scripts -f %{oreon_filedir}/perl-Catalyst-Runtime-scripts.list

%changelog

%autochangelog
