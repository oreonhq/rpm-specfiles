%global source0_hash 8aaa6edf90255a3d0b4d0047d6270e1124bf1e1acd2414804e87310b6b39be40
%{bcond_without perl_PDL_enables_optional_test}
Name:           perl-PDL
%global cpan_version 2.100
Version:        2.100.0
Release:        4%{?dist}
Summary:        The Perl Data Language
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Url:            http://pdl.perl.org/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/PDL-%{cpan_version}.tar.gz
Patch1:         PDL-2.72.0-Fix-numbering-of-line-in-test.patch
%if %{with perl_PDL_enables_optional_test}
%endif
Requires:       perl(ExtUtils::Liblist)
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(ExtUtils::MM)
Requires:       perl(ExtUtils::Typemaps)
Requires:       perl(Fcntl)
Requires:       perl(File::Map) >= 0.57
Requires:       perl(File::Spec) >= 0.6
Requires:       perl(Filter::Simple) >= 0.88
Requires:       perl(Graph)
Requires:       perl(Inline) >= 0.43
Requires:       perl(Text::Balanced) >= 2.05
Provides:       perl(PDL::AutoLoader) = %{version}
Provides:       perl(PDL::Config) = %{version}
Provides:       perl(PDL::DiskCache) = %{version}
Provides:       perl(PDL::NiceSlice::FilterSimple) = %{version}
Provides:       perl(PDL::PP::CType) = %{version}
Provides:       perl(PDL::PP::Dims) = %{version}
Provides:       perl(PDL::PP::PDLCode) = %{version}
Provides:       perl(PDL::PP::PdlParObj) = %{version}
Provides:       perl(PDL::PP::SymTab) = %{version}
Provides:       perl(PDL::PP::XS) = %{version}
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PDL::Graphics::Simple\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Inline\\)$
%global __provides_exclude %{__provides_exclude}|^perl\\(Win32.*\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\((Data::Dumper|File::Spec|Filter::Simple|Inline|Module::Compile|OpenGL|Text::Balanced)\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(My::Test::Primitive\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  netpbm-progs
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::MakeMaker::Config)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(ExtUtils::Typemaps)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Map)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Filter::Simple)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Graph)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Complex)
BuildRequires:  perl(Module::Compile)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(Pod::Select)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SelfLoader)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sharutils
# /oreon:deps
%description
PDL ("Perl Data Language") gives standard Perl the ability to
compactly store and speedily manipulate the large N-dimensional data
arrays which are the bread and butter of scientific computing.  PDL
turns perl into a free, array-oriented, numerical language similar to
such commercial packages as IDL and MatLab.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Devel::CheckLib)
%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PDL-%{cpan_version}
%patch -P1 -p1

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

CFLAGS="%{optflags} -Wno-unused"
CFLAGS="$CFLAGS" perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$CFLAGS"
make OPTIMIZE="$CFLAGS" %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
perl -Mblib utils/scantree.pl %{buildroot}%{perl_vendorarch}
perl -pi -e "s|%{buildroot}/|/|g" %{buildroot}%{perl_vendorarch}/PDL/pdldoc.db
find %{buildroot}%{perl_vendorarch} -type f -name "*.pm" | xargs chmod -x
find %{buildroot} -type f -name '*.bs' -empty -delete
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/t
cp -a t/* %{buildroot}/%{_libexecdir}/%{name}/t/
for F in compression.t fft.t image2d.t; do
    perl -i -pe 's{lib/PDL}{%{perl_vendorarch}/PDL}' %{buildroot}%{_libexecdir}/%{name}/t/$F
done
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
set -e
unset DISPLAY
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset DISPLAY
export PERL5LIB=`pwd`/blib/lib
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PDL-tests -f %{oreon_filedir}/perl-PDL-tests.list

%changelog

%autochangelog
