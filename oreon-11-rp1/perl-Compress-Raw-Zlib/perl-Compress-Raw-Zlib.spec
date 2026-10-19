%global source0_hash c17d0fb139eba9b8ad6a1dc42942c812dae7dae96ed1337b3ca950542810d8fc
%bcond_with perl_Compress_Raw_Zlib_enables_optional_test
Name:           perl-Compress-Raw-Zlib
Version:        2.224
Release:        1%{?dist}
Summary:        Low-level interface to the zlib compression library
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Zlib
URL:            https://metacpan.org/release/Compress-Raw-Zlib
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Zlib-%{version}.tar.gz
%if !%{defined perl_bootstrap}
%endif
%if %{with perl_Compress_Raw_Zlib_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       perl(XSLoader)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(CompTestUtils\\)
%if %{defined perl_bootstrap}
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Builder)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Simple)\s*$
%endif
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(Compress::Raw::Zlib)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib
compression library, which is used by IO::Compress::Zlib.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Compress_Raw_Zlib_enables_optional_test}
Requires:       perl(File::Temp)
Requires:       perl(overload)
%if !%{defined perl_bootstrap}
Requires:       perl(Test::NoWarnings)
%endif
%endif
%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/meta-*.t
perl -i -pe "s{DIR => '.'}{DIR => '/tmp'}" %{buildroot}%{_libexecdir}/%{name}/t/compress/CompTestUtils.pm
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset PERL_CORE
COMPRESS_ZLIB_RUN_MOST=1
export COMPRESS_ZLIB_RUN_MOST
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test COMPRESS_ZLIB_RUN_MOST=1
%files -f %{oreon_filedir}/main.list
%files -n perl-Compress-Raw-Zlib-tests -f %{oreon_filedir}/perl-Compress-Raw-Zlib-tests.list

%changelog

%autochangelog
