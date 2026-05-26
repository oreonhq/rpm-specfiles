%global base_version 3.68

# Perform optional tests
%bcond_without perl_Devel_PPPort_enables_optional_test

Name:           perl-Devel-PPPort
Version:        3.73
Release:        522%{?dist}
Summary:        Perl Pollution Portability header generator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-PPPort
Source0:        https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Devel-PPPort-%{base_version}.tar.gz
# Upgrade to 3.71 based on perl-5.37.11
Patch0:         Devel-PPPort-3.68-Upgrade-to-3.71.patch
Patch1:         Devel-PPPort-3.68-Add-shebang-to-tests.patch
# Upgrade to 3.72 based on perl-5.40.0-RC1
Patch2:         Devel-PPPort-3.71-Upgrade-to-3.72.patch
# Upgrade to 3.73 based on perl-5.42.0
Patch3:         Devel-PPPort-3.72-Upgrade-to-3.73.patch
# oreon url source checksums begin
%global source0_sha256 5290d5bb84cde9e9e61113a20c67b5d47267eb8e65a119a8a248cc96aac0badb
%global source0_file Devel-PPPort-3.68.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.3
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time:
# warnings in PPPort.pm not used
# Tests:
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(less)
BuildRequires:  perl(lib)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
%if %{with perl_Devel_PPPort_enables_optional_test} && !%{defined %perl_bootstrap}
# Optional tests:
# File::Spec not helpful
BuildRequires:  perl(Test::Pod) >= 0.95
%endif

# Filter modules bundled for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.::parts/.*\\)

%description
Perl's API has changed over time, gaining new features, new functions,
increasing its flexibility, and reducing the impact on the C name space
environment (reduced pollution). The header file written by this module,
typically ppport.h, attempts to bring some of the newer Perl API features
to older versions of Perl, so that you can worry less about keeping track
of old releases, but users can still reap the benefit.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(File::Spec)
Requires:       perl(less)
Requires:       perl(utf8)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%{?perl_default_filter}

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Devel-PPPort-3.68.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5290d5bb84cde9e9e61113a20c67b5d47267eb8e65a119a8a248cc96aac0badb" || { echo "oreon: Source0 SHA256 mismatch for Devel-PPPort-3.68.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n Devel-PPPort-%{base_version}

# Help generators to recognize Perl scripts
for F in t/*.pl parts/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t parts %{buildroot}%{_libexecdir}/%{name}
chmod +x %{buildroot}%{_libexecdir}/%{name}/t/*.t
perl -i -pe 's{(ppptmp)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/ppphtest.t
rm %{buildroot}%{_libexecdir}/%{name}/t/podtest.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL_CORE SKIP_SLOW_TESTS
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make regen_tests
make test

%files
# README.md is useless
%doc Changes HACKERS README soak TODO
%{perl_vendorarch}/auto/Devel*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/Devel::PPPort*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.73-522
- Prepare for Oreon 11 (RP1)
