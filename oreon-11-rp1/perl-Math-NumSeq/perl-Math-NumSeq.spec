%global source0_hash 7ea3e5cf4122c4cb87bedc371f67443ee3fce7d563e0bff0a65b4dffd61e8c61

# Enable optional evalutors like Math::Symbolic or Math::Expression::Evaluator
%bcond_without perl_Math_NumSeq_enables_maximum_interoperation
# Perform optional tests
%bcond_without perl_Math_NumSeq_enables_optional_test

Name:           perl-Math-NumSeq
Version:        75
Release:        12%{?dist}
Summary:        Number sequences
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/Math-NumSeq
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Math-NumSeq-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
# tools/make-oeis-catalogue.pl is executed
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Module::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant) >= 1.02
BuildRequires:  perl(constant::defer) >= 1
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Math::Factor::XS) >= 0.40
BuildRequires:  perl(Math::Libm)
BuildRequires:  perl(Math::Prime::XS) >= 0.23
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Safe) >= 2.30
BuildRequires:  perl(SDBM_File)
BuildRequires:  perl(Symbol)
# Tie::Hash::NamedCapture not needed if Safe >= 2.30 is available
# Optional run-time:
BuildRequires:  perl(Encode)
%if %{with perl_Math_NumSeq_enables_maximum_interoperation}
# Language::Expr 0.24 not yet packaged
# Language::Expr::Compiler::perl 0.24 not yet packaged
BuildRequires:  perl(Math::Expression::Evaluator)
BuildRequires:  perl(Math::Symbolic)
%endif
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
%if %{with perl_Math_NumSeq_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Data::Float)
# Devel::FindRef not available because it does not work since Perl 5.22.
BuildRequires:  perl(Devel::StackTrace)
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
# Language::Expr 0.24 not yet packaged
# Language::Expr::Compiler::perl 0.24 not yet packaged
Suggests:       perl(Math::Expression::Evaluator)
Suggests:       perl(Math::Symbolic)
%endif

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Math::Factor::XS\\) >= 0.39
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(MyTestHelpers\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(MyTestHelpers\\)

%description
This package contains a base class for number sequences and a collection of
its instances which implements various sequences like prime numbers or
multiples of a constant. Sequence objects can iterate through values and some
sequences have random access or a predicate test.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# Data::Dumper not used
Requires:       perl(File::Spec)
Requires:       perl(Math::Libm)
Requires:       perl(Scalar::Util)
%if %{with perl_Math_NumSeq_enables_optional_test}
# Optional tests:
Requires:       perl(Data::Float)
# Devel::FindRef not available because it does not work since Perl 5.22.
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license COPYING
%doc Changes examples
%{perl_vendorlib}/Math
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
