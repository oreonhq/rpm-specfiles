%global source0_hash aa80f52473b8ca3368e8f83496fac1b2a25d27723506b94c4ea6c861fce961f8

# Run optional test
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Compress_Raw_Bzip2_enables_optional_test
%else
%bcond_with perl_Compress_Raw_Bzip2_enables_optional_test
%endif

Name:           perl-Compress-Raw-Bzip2
Summary:        Low-level interface to bzip2 compression library
Version:        2.217
Release:        1%{?dist}
# Other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
## unbundled
# bzip2-src:    BSD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Compress-Raw-Bzip2
Source0:        https://cpan.metacpan.org/modules/by-module/Compress/Compress-Raw-Bzip2-%{version}.tar.gz



# Module Build
BuildRequires:  bzip2-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
# Module Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Test Suite
BuildRequires:  perl(File::Path)
BuildRequires:  perl(threads::shared)
# Dual-lived module needs rebuilding early in the boot process
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::More)
%endif
%if %{with perl_Compress_Raw_Bzip2_enables_optional_test}
# Optional Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
%if !%{defined perl_bootstrap}
# Release tests are deleted
BuildRequires:  perl(Test::NoWarnings)
%endif
BuildRequires:  perl(Scalar::Util)
%endif
BuildRequires:  perl(vars)
# Runtime
Requires:       perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

# Filter modules bundled for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(CompTestUtils\\)
%if %{defined perl_bootstrap}
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Builder)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Simple)\s*$
%endif
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

Provides:       perl(Compress::Raw::Bzip2)
%description
This module provides a Perl interface to the bzip2 compression library.
It is used by IO::Compress::Bzip2.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Compress_Raw_Bzip2_enables_optional_test}
# Optional Tests
Requires:       perl(File::Temp)
Requires:       perl(overload)
# Dual-lived module needs rebuilding early in the boot process
%if !%{defined perl_bootstrap}
Requires:       perl(Test::NoWarnings)
%endif
Requires:       perl(Scalar::Util)
%endif

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Compress-Raw-Bzip2-%{version}
# Remove bundled bzip2 sources
rm -r bzip2-src
perl -i -ne 'print unless /^bzip2-src\//' MANIFEST

%if ! %{defined perl_bootstrap}
# Remove bundled Test::* modules
rm -rf t/Test
perl -i -ne 'print $_ unless m{^t/Test/}' MANIFEST
%endif

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

# Remove release tests
rm t/99pod.t t/meta-*.t
perl -i -ne 'print $_ unless m{^t/99pod\.t}' MANIFEST
perl -i -ne 'print $_ unless m{^t/meta-.*\.t}' MANIFEST

%build
BUILD_BZIP2=0
BZIP2_LIB=%{_libdir}
export BUILD_BZIP2 BZIP2_LIB
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe "s{DIR => '.'}{DIR => '/tmp'}" %{buildroot}%{_libexecdir}/%{name}/t/compress/CompTestUtils.pm
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_CORE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%{_fixperms} -c %{buildroot}

%check
unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/Compress/
%{_mandir}/man3/Compress::Raw::Bzip2.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.217-1
- Import
