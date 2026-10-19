%global source0_hash 21a74fafb35a62d3308295c16cb1e0596543207df67d974b3c2516e9bddca308
%bcond_without perl_PerlX_Maybe_enables_xs
Name:           perl-PerlX-Maybe
Version:        1.202
Release:        11%{?dist}
Summary:        Return a pair only if they are both defined
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlX-Maybe
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/PerlX-Maybe-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_PerlX_Maybe_enables_xs}
%endif
Requires:       perl(Exporter)
Requires:       perl(Exporter::Tiny)
%if %{with perl_PerlX_Maybe_enables_xs}
Recommends:     perl(PerlX::Maybe::XS) >= 0.003
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(PerlX::Maybe::XS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides a syntax sugar for passing a pair of variables only
if both of them match some criteria (to be defined usually).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_PerlX_Maybe_enables_xs}
Requires:       perl(PerlX::Maybe::XS) >= 0.003
%endif
Requires:       perl(Test::More) >= 0.61
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PerlX-Maybe-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
cd %{_libexecdir}/%{name}
%if %{with perl_PerlX_Maybe_enables_xs}
unset PERLX_MAYBE_IMPLEMENTATION
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
export PERLX_MAYBE_IMPLEMENTATION=PP
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%if %{with perl_PerlX_Maybe_enables_xs}
unset PERLX_MAYBE_IMPLEMENTATION
make test
%endif
PERLX_MAYBE_IMPLEMENTATION=PP make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PerlX-Maybe-tests -f %{oreon_filedir}/perl-PerlX-Maybe-tests.list

%changelog

%autochangelog
