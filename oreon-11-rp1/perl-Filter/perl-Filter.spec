%global source0_hash cb70da7ae5e19138a0b22fb3b6387c3ae697a3cd3f3f6ecde425152e9124d1e6

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Filter_enables_optional_test
%else
%bcond_with perl_Filter_enables_optional_test
%endif

Name:           perl-Filter
Epoch:          2
Version:        1.65
Release:        2%{?dist}
Summary:        Perl source filters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Filter
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Filter-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(perl5db.pl)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_Filter_enables_optional_test}
# Optional tests
BuildRequires:  m4
BuildRequires:  perl(POSIX)
%if !%{defined perl_bootstrap}
# Class::XSAccessor not used
# List::MoreUtils not used
# Perl::MinimumVersion 1.20 not used
# Test::CPAN::Meta 0.12 not used
# Test::Kwalitee not used
# Test::MinimumVersion 0.008 not used
BuildRequires:  perl(Test::Pod) >= 1.00
# Test::Pod::Coverage 1.04 not used
# Text::CSV_XS not used
%endif
BuildRequires:  perl(vars)
%endif
Requires:       perl(Carp)
# For Filer::sh
Suggests:       bash
# For Filter::cpp
Suggests:       gcc
# For Filter::m4
Suggests:       m4

%{?perl_default_filter}

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(rt_101033\\)

%description
Source filters alter the program text of a module before Perl sees it, much as
a C preprocessor alters the source text of a C program before the compiler
sees it.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(perl5db.pl)
# Optional tests
%if %{with perl_Filter_enables_optional_test}
Requires:       m4
Requires:       perl(POSIX)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/decrypt
cp -a decrypt/encrypt %{buildroot}%{_libexecdir}/%{name}/decrypt/
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/z_*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
unset FULLPERL PERL_CORE
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING FULLPERL IS_MAINTAINER PERL_CORE RELEASE_TESTING TRAVIS
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc examples Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Filter*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.65-2
- Prepare for Oreon 11 (RP1)
