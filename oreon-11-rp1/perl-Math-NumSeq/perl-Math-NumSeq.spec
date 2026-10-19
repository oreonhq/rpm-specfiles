%global source0_hash 7ea3e5cf4122c4cb87bedc371f67443ee3fce7d563e0bff0a65b4dffd61e8c61
%bcond_without perl_Math_NumSeq_enables_maximum_interoperation
%bcond_without perl_Math_NumSeq_enables_optional_test
Name:           perl-Math-NumSeq
Version:        75
Release:        1%{?dist}
Summary:        Number sequences
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/Math-NumSeq
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-NumSeq-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Math_NumSeq_enables_maximum_interoperation}
%endif
%if %{with perl_Math_NumSeq_enables_optional_test}
%endif
Recommends:     perl(Encode)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Temp)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::Trig)
Requires:       perl(Module::Load)
Requires:       perl(Safe) >= 2.30
Requires:       perl(SDBM_File)
%if %{with perl_Math_NumSeq_enables_maximum_interoperation}
Suggests:       perl(Math::Expression::Evaluator)
Suggests:       perl(Math::Symbolic)
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Math::Factor::XS\\) >= 0.39
%global __requires_exclude %{__requires_exclude}|^perl\\(MyTestHelpers\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(MyTestHelpers\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Float)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Expression::Evaluator)
BuildRequires:  perl(Math::Factor::XS)
BuildRequires:  perl(Math::Libm)
BuildRequires:  perl(Math::Prime::XS)
BuildRequires:  perl(Math::Symbolic)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(SDBM_File)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
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
This package contains a base class for number sequences and a collection of
its instances which implements various sequences like prime numbers or
multiples of a constant. Sequence objects can iterate through values and some
sequences have random access or a predicate test.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(File::Spec)
Requires:       perl(Math::Libm)
Requires:       perl(Scalar::Util)
%if %{with perl_Math_NumSeq_enables_optional_test}
Requires:       perl(Data::Float)
Requires:       perl(Devel::StackTrace)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Math-NumSeq-%{version}
chmod +x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Math-NumSeq-tests -f %{oreon_filedir}/perl-Math-NumSeq-tests.list

%changelog

%autochangelog
