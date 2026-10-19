%global source0_hash aaf48467765deea6e48054bc7d43e46e4d40cbcda16552c629d37be098289309
Name:		perl-Algorithm-C3
Version:	0.11
Release:        1%{?dist}
Summary:        Module for merging hierarchies using the C3 algorithm
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Algorithm-C3
Source0:        https://cpan.metacpan.org/modules/by-module/Algorithm/Algorithm-C3-%{version}.tar.gz
BuildArch:	noarch
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test::More)\\)$
Provides:       perl(Algorithm::C3)
Provides:       perl(Algorithm::C3)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements the C3 algorithm.  Most of the uses I have for C3
revolve around class building and metamodels but it could also be used for
things like dependency resolution as well since it tends to do such a nice
job of preserving local precedence orderings.

%package tests
Summary:	Tests for %{name}
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	perl-Test-Harness
Requires:	perl(Test::More) >= 0.47
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Algorithm-C3-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -r -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Algorithm-C3-tests -f %{oreon_filedir}/perl-Algorithm-C3-tests.list

%changelog

%autochangelog
