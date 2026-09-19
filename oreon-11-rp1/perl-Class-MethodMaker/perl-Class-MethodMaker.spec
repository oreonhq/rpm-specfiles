%global source0_hash 70bd3a6595cc40e54a9521eae3247e7d69166e6783ea5faebd59b84537e1b588

Name:           perl-Class-MethodMaker
Version:        2.25
Release:        5%{?dist}
Summary:        Perl module for creating generic object-oriented methods
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-MethodMaker
Source0:        https://www.cpan.org/modules/by-module/Class/Class-MethodMaker-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin) >= 1.42
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
# Module Runtime
BuildRequires:  perl(AutoLoader) >= 5.57
BuildRequires:  perl(B::Deparse) >= 0.59
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fatal) >= 1.02
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Test Suite
BuildRequires:  perl(Cwd) >= 2.01
BuildRequires:  perl(Env)
BuildRequires:  perl(Fcntl) >= 1.03
BuildRequires:  perl(File::Compare) >= 1.1002
BuildRequires:  perl(File::Path) >= 1.04.01
BuildRequires:  perl(File::Spec) >= 0.6
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File) >= 1.08
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(POSIX) >= 1.03
BuildRequires:  perl(Test) >= 1.13
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(Tie::StdArray)
BuildRequires:  perl(Tie::StdHash)
BuildRequires:  perl(Tie::StdScalar)
BuildRequires:  perl(vars)
# Dependencies
Requires:       perl(B::Deparse) >= 0.59
Requires:       perl(Data::Dumper)

%{?perl_default_filter}

%description
Class::MethodMaker solves the problem of having to continually write accessor
methods for your objects that perform standard tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-MethodMaker-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README TODO
%{perl_vendorarch}/Class/
%{perl_vendorarch}/auto/Class/
%{_mandir}/man3/Class::MethodMaker.3*
%{_mandir}/man3/Class::MethodMaker::Constants.3*
%{_mandir}/man3/Class::MethodMaker::Engine.3*
%{_mandir}/man3/Class::MethodMaker::OptExt.3*
%{_mandir}/man3/Class::MethodMaker::V1Compat.3*
%{_mandir}/man3/Class::MethodMaker::array.3*
%{_mandir}/man3/Class::MethodMaker::hash.3*
%{_mandir}/man3/Class::MethodMaker::scalar.3*

%changelog
%autochangelog
