%global source0_hash 8c90db44bf09b11041761528edafb821669c87c154a757dd470608545a7dc75e

Name:           perl-Dist-Zilla
Version:        6.037
Release:        1%{?dist}
Summary:        Distribution builder; installer not included!
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Dist-Zilla-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(App::Cmd::Command::version)
BuildRequires:  perl(App::Cmd::Setup) >= 0.330
BuildRequires:  perl(App::Cmd::Tester) >= 0.306
BuildRequires:  perl(App::Cmd::Tester::CaptureExternal)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Config::MVP) >= 2.200011
BuildRequires:  perl(Config::MVP::Assembler)
BuildRequires:  perl(Config::MVP::Assembler::WithBundles) >= 2.200010
BuildRequires:  perl(Config::MVP::Reader) >= 2.101540
BuildRequires:  perl(Config::MVP::Reader::Findable::ByExtension)
BuildRequires:  perl(Config::MVP::Reader::Finder)
BuildRequires:  perl(Config::MVP::Reader::INI) >= 2.101461
BuildRequires:  perl(Config::MVP::Section) >= 2.200009
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Converter) >= 2.101550
BuildRequires:  perl(CPAN::Meta::Merge)
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.120630
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(CPAN::Meta::Validator) >= 2.101550
BuildRequires:  perl(CPAN::Uploader) >= 0.103004
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Section) >= 0.200002
BuildRequires:  perl(DateTime) >= 0.44
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(experimental)
BuildRequires:  perl(ExtUtils::Manifest) >= 1.66
BuildRequires:  perl(File::Copy::Recursive) >= 0.41
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Log::Dispatchouli) >= 1.102220
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.92
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::LazyRequire)
BuildRequires:  perl(MooseX::Role::Parameterized) >= 1.01
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Perl)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Class) >= 0.22
BuildRequires:  perl(Path::Tiny) >= 0.052
BuildRequires:  perl(Perl::PrereqScanner) >= 1.016
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Document) >= 1.222
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Software::License) >= 0.104001
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(String::Formatter) >= 0.100680
BuildRequires:  perl(String::RewritePrefix) >= 0.006
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::ForMethods)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Term::Encoding)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::UI)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Text::Glob) >= 0.08
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(YAML::Tiny)
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Software::License::None)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::File::ShareDir)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Archive::Tar)
#Requires:       perl(autobox) >= 2.53
Requires:       perl(Config::INI::Reader)
Requires:       perl(Config::MVP) >= 2.200011
Requires:       perl(Config::MVP::Assembler)
Requires:       perl(Config::MVP::Assembler::WithBundles) >= 2.200010
Requires:       perl(Config::MVP::Reader::Findable::ByExtension)
Requires:       perl(Config::MVP::Reader::Finder)
Requires:       perl(Config::MVP::Reader::INI) >= 2
Requires:       perl(CPAN::Meta::Converter) >= 2.101550
Requires:       perl(CPAN::Meta::Validator) >= 2.101550
Requires:       perl(CPAN::Uploader) >= 0.103004
Requires:       perl(DateTime)
Requires:       perl(ExtUtils::Manifest) >= 1.54
Requires:       perl(File::Path)
Requires:       perl(File::ShareDir::Install) >= 0.06
Requires:       perl(Hash::Merge::Simple)
Requires:       perl(Module::CoreList)
Requires:       perl(Path::Class) >= 0.22
Requires:       perl(Pod::Simple)
Requires:       perl(PPI::Document) >= 1.222
Requires:       perl(Software::LicenseUtils) >= 0.104001
Requires:       perl(Term::ANSIColor) >= 5.00
Requires:       perl(Term::Encoding)
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine)
Requires:       perl(Term::UI)

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((App::Cmd::Setup|CPAN::Meta::Requirements|Moose|Path::Class|String::RewritePrefix)\\)$
# Remove autogenerated nonsense
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}\\{

%description
Dist::Zilla builds distributions of code to be uploaded to the CPAN. In
this respect, it is like ExtUtils::MakeMaker, Module::Build, or
Module::Install. Unlike those tools, however, it is not also a system for
installing code that has been downloaded from the CPAN. Since it's only run
by authors, and is meant to be run on a repository checkout rather than on
published, released code, it can do much more than those tools, and is free
to make much more ludicrous demands in terms of prerequisites.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# install bash_completion script
install -D -m 0644 misc/dzil-bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/dzil

%check
make test

%files
%license LICENSE
%doc Changes README todo
%{perl_vendorlib}/*
%{_bindir}/dzil
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_sysconfdir}/bash_completion.d

%changelog
%autochangelog
