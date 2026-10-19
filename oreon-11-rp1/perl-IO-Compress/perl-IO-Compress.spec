%global source0_hash 76e54ae93e96ee6ff68ed78760fdcc8621d133ff375fec43f10e19d5a1516857
%bcond_without long_tests
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_IO_Compress_enables_optional_test
%else
%bcond_with perl_IO_Compress_enables_optional_test
%endif
%{?perl_default_filter}
Name:           perl-IO-Compress
Version:        2.224
Release:        1%{?dist}
Summary:        Read and write compressed data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Compress
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/IO-Compress-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
%if %{with perl_IO_Compress_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       perl(File::Glob)
Obsoletes:      perl-Compress-Zlib < %{version}-%{release}
Provides:       perl-Compress-Zlib = %{version}-%{release}
Obsoletes:      perl-IO-Compress-Base < %{version}-%{release}
Provides:       perl-IO-Compress-Base = %{version}-%{release}
Obsoletes:      perl-IO-Compress-Bzip2 < %{version}-%{release}
Provides:       perl-IO-Compress-Bzip2 = %{version}-%{release}
Obsoletes:      perl-IO-Compress-Zlib < %{version}-%{release}
Provides:       perl-IO-Compress-Zlib = %{version}-%{release}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(CompTestUtils\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(.*\.pl)\s*$
%if %{defined perl_bootstrap}
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Builder)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Simple)\s*$
%endif
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(IO::Compress::Base)
Provides:       perl(IO::Compress::Base::Common)
Provides:       perl(IO::Compress::Bzip2)
Provides:       perl(IO::Compress::Deflate)
Provides:       perl(IO::Compress::Gzip)
Provides:       perl(IO::Compress::Xz)
Provides:       perl(IO::Compress::Zip)
Provides:       perl(Compress::Zlib)
Provides:       perl(IO::Uncompress::AnyUncompress)
Provides:       perl(IO::Uncompress::Base)
Provides:       perl(IO::Uncompress::Bunzip2)
Provides:       perl(IO::Uncompress::Gunzip)
Provides:       perl(IO::Uncompress::Inflate)
Provides:       perl(IO::Uncompress::RawInflate)
Provides:       perl(IO::Uncompress::Unzip)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Bzip2)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This distribution provides a Perl interface to allow reading and writing of
compressed data created with the zlib and bzip2 libraries.

IO-Compress supports reading and writing of bzip2, RFC 1950, RFC 1951,
RFC 1952 (i.e. gzip) and zip files/buffers.

The following modules used to be distributed separately, but are now
included with the IO-Compress distribution:
* Compress-Zlib
* IO-Compress-Zlib
* IO-Compress-Bzip2
* IO-Compress-Base

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Compress-%{version}

# Remove spurious exec permissions
chmod -c -x lib/IO/Uncompress/{Adapter/Identity,RawInflate}.pm
find examples -type f -exec chmod -c -x {} \;

%if ! %{defined perl_bootstrap}
# Remove bundled Test::* modules
rm -rf t/Test
perl -i -ne 'print $_ unless m{^t/Test/}' MANIFEST
%endif

# Fix shellbangs in examples
perl -MConfig -pi -e 's|^#!/usr/local/bin/perl\b|$Config{startperl}|' examples/io/anycat \
        examples/io/bzip2/* examples/io/gzip/* examples/compress-zlib/*

# Help file to recognise the Perl scripts and normalize shebangs
for F in `find t -name *.t` `find t -name *.pl`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install} INSTALLDIRS=perl
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a examples t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/999pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/999meta-*.t
perl -i -pe "s{\"./bin/\"}{\"%{_bindir}\"}" %{buildroot}%{_libexecdir}/%{name}/t/011-streamzip.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
unset PERL_CORE
export TEST_SKIP_VERSION_CHECK=1
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} -c %{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
export TEST_SKIP_VERSION_CHECK=1
make test COMPRESS_ZLIB_RUN_%{?with_long_tests:ALL}%{!?with_long_tests:MOST}=1
%files -f %{oreon_filedir}/main.list
%files -n perl-IO-Compress-tests -f %{oreon_filedir}/perl-IO-Compress-tests.list

%changelog

%autochangelog
