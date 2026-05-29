%global source0_hash 48143505b176665896ac4276167c2cabe94ddb59c59d81610444f1bd36843138

# Perform optional tests
%bcond_without perl_Tie_RefHash_enables_optional_test

Name:           perl-Tie-RefHash
Version:        1.41
Release:        521%{?dist}
Summary:        Use references as hash keys
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-RefHash
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Tie-RefHash-1.41.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util) >= 1.01
BuildRequires:  perl(Tie::Hash)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
%if %{with perl_Tie_RefHash_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(threads)
%endif
Requires:       perl(Scalar::Util) >= 1.01
Conflicts:      perl-interpreter < 4:5.30.1-451

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Scalar::Util\\)$

%description
This module provides the ability to use references as hash keys if you first
"tie" the hash variable to this module. Normally, only the keys of the tied
hash itself are preserved as references; to use references as keys in
hashes-of-hashes, use Tie::RefHash::Nestable, included as part of
Tie::RefHash.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(threads)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Tie-RefHash-%{version}
%if !%{with perl_Tie_RefHash_enables_optional_test}
rm t/refhash.t
perl -i -ne 'print $_ unless m{^t/refhash\.t}' MANIFEST
%endif

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%dir %{perl_vendorlib}/Tie
%{perl_vendorlib}/Tie/RefHash.pm
%{_mandir}/man3/Tie::RefHash.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.41-521
- Prepare for Oreon 11 (RP1)
