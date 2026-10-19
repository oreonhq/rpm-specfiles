%global source0_hash 8da15d0e4d5077b6c5d203765b2885bf728e509e32de9264605c0862137e397e
Name:           perl-Math-PlanePath
Version:        129
Release:        16%{?dist}
Summary:        Mathematical paths through the 2-D plane
License:        GPL-3.0-or-later
URL:            http://user42.tuxfamily.org/math-planepath/index.html
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-PlanePath-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(constant::defer) >= 5
Requires:       perl(File::Spec)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Requires:       perl(Math::BigRat)
Requires:       perl(Math::Factor::XS)
Requires:       perl(Math::NumSeq::Modulo)
Requires:       perl(Module::Load)
Requires:       perl(Scalar::Util)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::PlanePath::CellularRule::Line\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::PlanePath::CellularRule::OddSolid\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::PlanePath::CellularRule::OneTwo\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::PlanePath::CellularRule::Two\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(constant\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(constant::defer\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Float)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::BigRat)
BuildRequires:  perl(Math::Factor::XS)
BuildRequires:  perl(Math::Libm)
BuildRequires:  perl(Math::NumSeq)
BuildRequires:  perl(Math::NumSeq::Base::IterateIth)
BuildRequires:  perl(Math::NumSeq::Modulo)
BuildRequires:  perl(Math::NumSeq::OEIS::Catalogue::Plugin)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Number::Fraction)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(constant)
BuildRequires:  perl(constant::defer)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This spot of Perl code calculates various mathematical paths through a 2-D X,Y
plane. There's no drawing in Math-PlanePath, just coordinate calculations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-PlanePath-%{version}
find examples -type f -exec chmod 0644 -c {} +

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
