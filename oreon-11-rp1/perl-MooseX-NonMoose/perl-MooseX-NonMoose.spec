%global source0_hash 6fc7893b47a7db812a3c1fe8bb90d9c235143c6937251e570e27bdbd0d844ece

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_MooseX_NonMoose_enables_extra_test
%else
%bcond_with perl_MooseX_NonMoose_enables_extra_test
%endif

Name:           perl-MooseX-NonMoose
Version:        0.27
Release:        4%{?dist}
Summary:        Easy subclassing of non-Moose classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-NonMoose
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-NonMoose-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role) >= 2.0000
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Try::Tiny)
# Test
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test2::Require::Module) >= 0.000121
# Optional tests
%if %{with perl_MooseX_NonMoose_enables_extra_test}
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(MooseX::GlobRef)
BuildRequires:  perl(MooseX::InsideOut) >= 0.100
%endif
# Dependencies
# (none)

Provides:       perl(MooseX::NonMoose)
Provides:       perl(MooseX::NonMoose)
%description
MooseX::NonMoose allows for easily subclassing non-Moose classes with
Moose, taking care of the annoying details connected with doing this, such
as setting up proper inheritance from Moose::Object and installing (and
inlining, at make_immutable time) a constructor that makes sure things like
BUILD methods are called. It tries to be as non-intrusive as possible -
when this module is used, inheriting from non-Moose classes and inheriting
from Moose classes should work identically, aside from the few caveats
mentioned below. One of the goals of this module is that including it in a
Moose::Exporter-based package used across an entire application should be
possible, without interfering with classes that only inherit from Moose
modules, or even classes that don't inherit from anything at all.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-NonMoose-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/MooseX/
%{_mandir}/man3/MooseX::NonMoose.3*
%{_mandir}/man3/MooseX::NonMoose::InsideOut.3*
%{_mandir}/man3/MooseX::NonMoose::Meta::Role::Class.3*
%{_mandir}/man3/MooseX::NonMoose::Meta::Role::Constructor.3*

%changelog
%autochangelog
