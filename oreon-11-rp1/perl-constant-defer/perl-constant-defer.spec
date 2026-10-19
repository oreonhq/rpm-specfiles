%global source0_hash 7b21263198ca22686efff3ae987a240be423dd2160afdeb29fe716d032986ffa
%bcond_without perl_constant_defer_enables_optional_test
Name:           perl-constant-defer
Version:        6
Release:        1%{?dist}
Summary:        Constant subs with deferred value calculation
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/constant-defer
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/constant-defer-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_constant_defer_enables_optional_test}
%endif
Requires:       perl(Carp)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(MyTestHelpers\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(MyTestHelpers\\)
Provides:       perl(constant::defer)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
constant::defer creates a subroutine which on the first call runs given
code to calculate its value, and on the second and subsequent calls just
returns that value, like a constant. The value code is discarded once run,
allowing it to be garbage collected.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Scalar::Util)
%if %{with perl_constant_defer_enables_optional_test}
Requires:       perl(Data::Dumper)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n constant-defer-%{version}
chmod -x examples/*

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
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
%files -n perl-constant-defer-tests -f %{oreon_filedir}/perl-constant-defer-tests.list

%changelog

%autochangelog
