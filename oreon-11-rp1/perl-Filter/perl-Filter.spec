%global source0_hash cb70da7ae5e19138a0b22fb3b6387c3ae697a3cd3f3f6ecde425152e9124d1e6
%bcond_with perl_Filter_enables_optional_test
Name:           perl-Filter
Epoch:          2
Version:        1.65
Release:        1%{?dist}
Summary:        Perl source filters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Filter
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Filter-%{version}.tar.gz
%if %{with perl_Filter_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       perl(Carp)
Suggests:       bash
Suggests:       gcc
Suggests:       m4
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(rt_101033\\)
Provides:       perl(Filter::Util::Call)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(lib)
BuildRequires:  perl(perl5db.pl)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Source filters alter the program text of a module before Perl sees it, much as
a C preprocessor alters the source text of a C program before the compiler
sees it.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(perl5db.pl)
%if %{with perl_Filter_enables_optional_test}
Requires:       m4
Requires:       perl(POSIX)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Filter-%{version}
# Clean examples
find examples -type f -exec chmod -x -- {} +

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl decrypt/encrypt; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/decrypt
cp -a decrypt/encrypt %{buildroot}%{_libexecdir}/%{name}/decrypt/
rm %{buildroot}%{_libexecdir}/%{name}/t/z_*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
unset FULLPERL PERL_CORE
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING FULLPERL IS_MAINTAINER PERL_CORE RELEASE_TESTING TRAVIS
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Filter-tests -f %{oreon_filedir}/perl-Filter-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.65-2
- Prepare for Oreon 11 (RP1)
