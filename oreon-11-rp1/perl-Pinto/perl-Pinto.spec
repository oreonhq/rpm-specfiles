%global source0_hash f8c4546491a091e55f58a32163bc38b66e550a99a67bf8bc9bf7f8ad3b3b6220
Name:           perl-Pinto
Epoch:          1
Version:        0.14
Release:        1%{?dist}
Summary:        Curate a repository of Perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pinto
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Pinto-%{version}.tar.gz
Source1:        pintod.service
Source2:        pintod.conf
BuildArch:      noarch
Requires:       perl(App::cpanminus) >= 1.6920
Requires:       perl(App::Cmd) >= 0.323
Requires:       perl(Archive::Extract) >= 0.68
Requires:       perl(Authen::Simple::Passwd)
Requires:       perl(DBD::SQLite) >= 1.33
Requires:       perl(DBIx::Class) >= 0.08200
Requires:       perl(DBIx::Class::Core)
Requires:       perl(DBIx::Class::Schema)
Requires:       perl(Dist::Metadata) >= 0.924
Requires:       perl(Encode)
Requires:       perl(File::Spec)
Requires:       perl(IO::Prompt)
Requires:       perl(JSON::PP) >= 2.27103
Requires:       perl(Module::CoreList) >= 5.20160720
Requires:       perl(Module::Metadata) >= 1.000031
Requires:       perl(MooseX::ClassAttribute) >= 0.27
Requires:       perl(Plack) >= 1.0028
Requires:       perl(Starman) >= 0.3014
Requires:       perl(Throwable::Error) >= 0.200005
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Archive::Extract\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Dist::Metadata\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Module::CoreList\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(MooseX::ClassAttribute\\)\s*$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Apache::Htpasswd)
BuildRequires:  perl(App::Cmd)
BuildRequires:  perl(App::Cmd::Command::help)
BuildRequires:  perl(App::Cmd::Setup)
BuildRequires:  perl(App::cpanminus)
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Authen::Simple::Passwd)
BuildRequires:  perl(CPAN::Checksums)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Cwd::Guard)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::ResultSet)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(DateTime::TimeZone::Local::Unix)
BuildRequires:  perl(DateTime::TimeZone::OffsetOnly)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Dist::Metadata)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::NFSLock)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Body)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Server::PSGI)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Interactive)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Prompt)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Faker::Dist)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Aliases)
BuildRequires:  perl(MooseX::ClassAttribute)
BuildRequires:  perl(MooseX::Configuration)
BuildRequires:  perl(MooseX::MarkAsMethods)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Class::Dir)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Plack)
BuildRequires:  perl(Plack::MIME)
BuildRequires:  perl(Plack::Middleware::Auth::Basic)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Proc::Fork)
BuildRequires:  perl(Proc::Terminator)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Router::Simple)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Format)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Throwable::Error)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(UUID::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  systemd
# /oreon:deps
%description
Pinto is an application for creating and managing a custom CPAN-like
repository of Perl modules. The purpose of such a repository is to provide
a stable, curated stack of dependencies from which you can reliably build,
test, and deploy your application using the standard Perl tool chain. Pinto
supports various operations for gathering and managing distribution
dependencies within the repository, so that you can control precisely which
dependencies go into your application.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pinto-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/pintod.service
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/pintod
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%post

%systemd_post pintod.service
%preun

%systemd_preun pintod.service
%postun

%systemd_postun_with_restart pintod.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
