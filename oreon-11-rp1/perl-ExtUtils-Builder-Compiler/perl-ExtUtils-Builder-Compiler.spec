%global source0_hash 79890f72ebe447ed8bf9b4ae9216a0f5fae460f424845f2467e2d2e4edb85b07

Name:           perl-ExtUtils-Builder-Compiler
Version:        0.035
Release:        1%{?dist}
Summary:        Interface around different compilers

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/ExtUtils-Builder-Compiler
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/ExtUtils-Builder-Compiler-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Builder) >= 0.018
BuildRequires:  perl(ExtUtils::Builder::Action::Command)
BuildRequires:  perl(ExtUtils::Builder::Node)
BuildRequires:  perl(ExtUtils::Builder::Planner) >= 0.007
BuildRequires:  perl(ExtUtils::Builder::Planner::Extension)
BuildRequires:  perl(ExtUtils::Builder::Util)
BuildRequires:  perl(ExtUtils::Config) >= 0.007
BuildRequires:  perl(ExtUtils::Helpers) >= 0.027
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(parent)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(sort)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(warnings)
Requires:       perl(ExtUtils::Builder) >= 0.016
Requires:       perl(ExtUtils::Builder::Planner) >= 0.007
Requires:       perl(DynaLoader)

%{?perl_default_filter}

%description
This is an interface wrapping around different compilers. It's usually not
used directly but by a portability layer like
ExtUtils::Builder::Autodetect::C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ExtUtils-Builder-Compiler-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes prereqs.yml README
%license LICENSE
%dir %{perl_vendorlib}/ExtUtils
%{perl_vendorlib}/ExtUtils/Builder
%{_mandir}/man3/ExtUtils::Builder*

%changelog
%autochangelog
