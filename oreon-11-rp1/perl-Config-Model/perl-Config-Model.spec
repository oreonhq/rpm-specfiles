%global source0_hash 2172cccde5750f93e2949916203380386cb8cb03d8c6ad90c0e8fc7ba39f6297

# The test fuse_ui.t doesn't work in mock, they can be run on local machine
%bcond_with test_fuse

Name:           perl-Config-Model
Version:        2.155
Release:        4%{?dist}
Summary:        Framework to create configuration validation tools and editors
License:        LGPL-2.1-or-later

URL:            https://metacpan.org/release/Config-Model
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Assert::More)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Model::Tester) >= 4.002
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Fuse)
BuildRequires:  perl(Hash::Merge) >= 0.12
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Log4perl) >= 1.11
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(MouseX::NativeTraits)
BuildRequires:  perl(MouseX::StrictConstructor)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Parse::RecDescent) >= v1.90.0
BuildRequires:  perl(Path::Tiny) >= 0.070
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::Simple) >= 3.23
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::ReadLine::Gnu)
# Term::ReadLine::Perl - not used
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::Log::Log4perl)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Synopsis::Expectation)
BuildRequires:  perl(Test::Warn) >= 0.11
BuildRequires:  perl(Text::Levenshtein::Damerau)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XXX)
BuildRequires:  perl(YAML::Tiny)
%if %{with test_fuse}
BuildRequires:  fuse
BuildRequires:  kmod
%endif
Requires:       perl(MouseX::NativeTraits)
Requires:       perl(Text::Levenshtein::Damerau)

# RPM 4.8 filters
# Fedora is not a Debian system
%filter_from_requires /perl(AptPkg::Config)/d; /perl(AptPkg::System)/d; /perl(AptPkg::Version)/d
%{?perl_default_filter}
# RPM 4.9 filters
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(AptPkg::.*\\)
%global __requires_exclude %__requires_exclude|perl\\(Log::Log4perl\\)\s*$

%description
Using Config::Model, a typical configuration validation tool will be made
of 3 parts :
1. The user interface
2. The validation engine which is in charge of validating all the 
configuration information provided by the user.
3. The storage facility that store the configuration information

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Model-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TEST_AUTHOR
%if %{with test_fuse}
modprobe fuse
%endif
./Build test

%files
%license LICENSE
%doc Changes MODELS README.md TODO CONTRIBUTING.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
