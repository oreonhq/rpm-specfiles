%global source0_hash 3049536486459e38e1d791c07ce022326a91a302beaf01dcdb0e7b703a5da6cc

Name:           perl-String-Print
Version:        1.02
Release:        2%{?dist}
Summary:        Alternative for Perl printf
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-Print
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/String-Print-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Parse) >= 2.30
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(locale)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(constant)
# DateTime 1.00 not used
BuildRequires:  perl(Test::More) >= 0.86
Requires:       perl(Date::Parse) >= 2.30

# Remove under-specifed dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Date::Parse|Test::More)\\)$

%description
This module inserts values into (translated) strings. It provides printf
and sprintf alternatives via both an object oriented and a functional
interface. It supports translation, user-defined non-string value
serialization, user-defined modifiers, and correct Unicode string padding.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.86

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-Print-%{version}
# Correct shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset MARKOV_DEVEL
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset MARKOV_DEVEL
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc ChangeLog README.md
%dir %{perl_vendorlib}/String
%{perl_vendorlib}/String/Print.{pm,pod}
%{_mandir}/man3/String::Print.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
