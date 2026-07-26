%global source0_hash eed3a2e05cf195fa0ec03890551cda665bc8551acde731c8e530fe3c976edfa5

# Perform optional tests
%bcond_without perl_Tree_enables_optional_test

Name:           perl-Tree
Version:        1.16
Release:        7%{?dist}
Summary:        Tree data structure
# lib/Tree/Binary2.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Tree/DeepClone.pm:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Tree/Fast.pm:     GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Tree.pm:          GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:              GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tree
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Tree-%{version}.tgz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# I deliberately striped dependency versions because upstream blindly copies
# versions from his machine, and that prevents from pushing this software into
# older distributions, CPAN RT#117858
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
%if %{with perl_Tree_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Memory::Cycle) >= 1.02
%endif

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Tests\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Tests\\)

%description
This implements a full-featured N-ary tree representation with configurable
error-handling and a simple events system that allows for transparent
persistence to a variety of data stores.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Tree_enables_optional_test}
Requires:       perl(Test::Memory::Cycle) >= 1.02
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tree-%{version}
perl -MConfig -pi -e 's/\A#!.*/$Config{startperl}/' scripts/print.tree.pl
# Help generators to recognize Perl scripts
for F in t/*.t t/Tree*/*.t; do
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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# README not useful
%doc Changes scripts
%{perl_vendorlib}/Tree
%{perl_vendorlib}/Tree.pm
%{_mandir}/man3/Tree.*
%{_mandir}/man3/Tree::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
