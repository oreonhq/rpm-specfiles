%global source0_hash ed6f0525fe921382cc219d5a71abeedcedb4f2b63a43d78c0f65f80ac9b11ffd
%bcond_with perl_Dumbbench_enables_SOOT
Name:           perl-Dumbbench
Version:        0.505
Release:        1%{?dist}
Summary:        More reliable bench-marking with the least amount of thinking
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dumbbench
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Dumbbench-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Dumbbench_enables_SOOT}
%endif
Requires:       bash
%if %{with perl_Dumbbench_enables_SOOT}
Requires:       perl(Capture::Tiny)
%endif
Requires:       perl(Class::XSAccessor) >= 1.05
Requires:       perl(Number::WithError) >= 1.00
Requires:       perl(Statistics::CaseResampling) >= 0.06
Requires:       sudo
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Class::XSAccessor|Number::WithError|Statistics::CaseResampling|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Number::WithError)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Statistics::CaseResampling)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Dumbbench is a fancier benchmark module for Perl. It times the runs of code,
does some statistical analysis to discard outliers, and prints the results.

%if %{with perl_Dumbbench_enables_SOOT}
%package BoxPlot
Summary:        Dumbbench visualization using ROOT
ExclusiveArch: %{ix86} x86_64 noarch
%if %{with perl_Dumbbench_enables_SOOT}
Requires:       perl(SOOT)
%endif
%description BoxPlot
Dumbbench::BoxPlot module provides a way how to plot a Dumbbench timing using
ROOT toolkit.
%endif

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 1
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Dumbbench-%{version}
# Normalize shebangs
for F in examples/*.pl; do
    perl -MConfig -i -pe 's/\A#!.*perl/$Config{startperl}/' "$F";
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Dumbbench-tests -f %{oreon_filedir}/perl-Dumbbench-tests.list

%changelog

%autochangelog
