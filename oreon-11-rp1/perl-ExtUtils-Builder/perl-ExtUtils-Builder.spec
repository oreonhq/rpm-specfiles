%global source0_hash e18185965cbfb6beda131cf9929eccc2f64148c5ba2ad1032096a39da9e178f7

Name:           perl-ExtUtils-Builder
Version:        0.019
Release:        1%{?dist}
Summary:        Abstract actions and plans for the ExtUtils-Builder framework

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-Builder
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/ExtUtils-Builder-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(blib)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::Config)
BuildRequires:  perl(ExtUtils::Config::MakeMaker)
BuildRequires:  perl(ExtUtils::Helpers) >= 0.027
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(parent)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
Requires:       perl(Sub::Util) >= 1.40
Requires:       perl(Data::Dumper)
Requires:       perl(Perl::OSType)

%{?perl_default_filter}

%description
Writing extensions for various build tools can be a daunting
task. This module tries to abstract steps of build processes into
reusable building blocks for creating platform and build system
agnostic executable descriptions of work.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-Builder-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%dir %{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/ExtUtils/Builder.pm
%{perl_vendorlib}/ExtUtils/Builder
%{_mandir}/man3/ExtUtils::Builder*

%changelog
%autochangelog
