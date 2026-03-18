# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Compress_Raw_Zlib_enables_optional_test
%else
%bcond_with perl_Compress_Raw_Zlib_enables_optional_test
%endif


Name:           perl-Compress-Raw-Zlib
Version:        2.222
Release:        1%{?dist}
Summary:        Low-level interface to the zlib compression library
# Zlib.xs:  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Zlib
# Others:   GPL-1.0-or-later OR Artistic-1.0-Perl
## Not used to produce binary packages
# zlib-src: Zlib
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Zlib
URL:            https://metacpan.org/release/Compress-Raw-Zlib
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Zlib-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(vars)
BuildRequires:  zlib-devel >= 1.3
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
BuildRequires:  perl(List::Util)
BuildRequires:  perl(threads::shared)
# Dual-lived module needs rebuilding early in the boot process
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::More)
%endif
%if %{with perl_Compress_Raw_Zlib_enables_optional_test}
# Optional Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
# Dual-lived module needs rebuilding early in the boot process
%if !%{defined perl_bootstrap}
# Release tests are deleted
BuildRequires:  perl(Test::NoWarnings)
%endif
%endif
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


%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib
compression library, which is used by IO::Compress::Zlib.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Compress_Raw_Zlib_enables_optional_test}
# Optional Tests
Requires:       perl(File::Temp)
Requires:       perl(overload)
# Dual-lived module needs rebuilding early in the boot process
%if !%{defined perl_bootstrap}
Requires:       perl(Test::NoWarnings)
%endif
%endif

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Compress-Raw-Zlib-%{version}

# Remove bundled zlib
rm -rf zlib-src
perl -i -ne 'print $_ unless m{^zlib-src/}' MANIFEST

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

%build
OLD_ZLIB=False
BUILD_ZLIB=False 
ZLIB_LIB=%{_libdir}
ZLIB_INCLUDE=%{_includedir}
export BUILD_ZLIB OLD_ZLIB ZLIB_LIB ZLIB_INCLUDE
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove release tests
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/meta-*.t
perl -i -pe "s{DIR => '.'}{DIR => '/tmp'}" %{buildroot}%{_libexecdir}/%{name}/t/compress/CompTestUtils.pm
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_CORE
COMPRESS_ZLIB_RUN_MOST=1
export COMPRESS_ZLIB_RUN_MOST
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test COMPRESS_ZLIB_RUN_MOST=1

%files
%doc Changes README SECURITY.md
%{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/Compress/
%{_mandir}/man3/Compress::Raw::Zlib.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.222-1
- Prepare for Oreon 11 (RP1)
