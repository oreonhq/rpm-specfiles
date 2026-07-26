%global source0_hash 53d06f580062891baa5bcff6428ee4b5b1253458715cb2afaa932324b7a8e38a

Name:           perl-Config-Model-Tester
Version:        4.008
Release:        1%{?dist}
Summary:        Test framework for Config::Model
License:        LGPL-2.1-only
URL:            https://metacpan.org/release/Config-Model-Tester
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-Tester-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.1
# Bootstrap to prevent circular dependency on perl-Config-Model
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Config::Model)
BuildRequires:  perl(Config::Model::BackendMgr)
BuildRequires:  perl(Config::Model::Lister)
BuildRequires:  perl(Config::Model::Value)
%endif
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(locale)
BuildRequires:  perl(Log::Log4perl) >= 1.11
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::Log::Log4perl)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(ExtUtils::testlib)
Requires:       perl(Test::Log::Log4perl)

%description
This class provides a way to test configuration models with tests files.
This class was designed to tests several models and several tests cases
per model.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Model-Tester-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/Config*
%{_mandir}/man3/Config::Model::Tester*

%changelog
%autochangelog
