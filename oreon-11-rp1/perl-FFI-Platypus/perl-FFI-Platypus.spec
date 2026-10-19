%global source0_hash f5dd3320e91b01f30bd6932fd3bfe4f374bc41e1908179985171fc64f95f0cf4
%bcond_without perl_FFI_Platypus_enables_cpp
%bcond_without perl_FFI_Platypus_enables_fortran
%bcond_without perl_FFI_Platypus_enables_optional_test
Name:           perl-FFI-Platypus
Version:        2.11
Release:        2%{?dist}
Summary:        Write Perl bindings to non-Perl libraries with FFI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://pl.atypus.org/
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/FFI-Platypus-%{version}.tar.gz
%if %{with perl_FFI_Platypus_enables_cpp}
%endif
%if %{with perl_FFI_Platypus_enables_optional_test}
%endif
Requires:       gcc
%if %{with perl_FFI_Platypus_enables_cpp}
Recommends:     gcc-c++
%endif
%if %{with perl_FFI_Platypus_enables_fortran}
Recommends:     gcc-gfortran
%endif
Requires:       perl(bytes)
Requires:       perl(FFI::CheckLib) >= 0.05
Requires:       perl(IPC::Cmd)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^libplfill.so\\(\\)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test2::API|Test2::V0)\\)$
%global __provides_exclude %{__provides_exclude}|^perl\\((FFI::Build::Plugin::Foo(1|2)|Test::Cleanup|Test::FauxAttach|Test::Platypus)\\)
%global __requires_exclude %{__requires_exclude}|^perl\\((Test::Cleanup|Test::FauxAttach|Test::Platypus)\\)
%global __provides_exclude %{__provides_exclude}|^libtest\\.so\\(\\)
%global __provides_exclude %{__provides_exclude}|^perl\\(FFI::Platypus\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Acme::Alien::DontPanic)
BuildRequires:  perl(Alien::Base::Wrapper)
BuildRequires:  perl(Alien::FFI)
BuildRequires:  perl(B)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FFI::CheckLib)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(autodie)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Platypus is a Perl library for creating interfaces to machine code libraries
written in languages like C, C++, Fortran, Rust, Pascal. Essentially anything
that gets compiled into machine code. This implementation uses libffi to
accomplish this task. libffi is battle tested by a number of other scripting
and virtual machine languages, such as Python and Ruby to serve a similar
role. There are a number of reasons why you might want to write an extension
with Platypus instead of XS.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Test2::API) >= 1.302015
Requires:       perl(Test2::V0) >= 0.000121
%if %{with perl_FFI_Platypus_enables_optional_test}
Requires:       perl(Acme::Alien::DontPanic) >= 1.03
Requires:       perl(Devel::Hide) >= 0.0010
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n FFI-Platypus-%{version}
# Remove bundled modules,
# forks is not packaged
for F in \
    inc/Alien/Base inc/Alien/FFI \
    t/forks.t \
%if !%{with perl_FFI_Platypus_enables_optional_test}
    t/type_longdouble__hide.t \
%endif
; do
    rm -r "$F"
    perl -i -n -e 'print unless m{^\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build

unset FFI_PLATYPUS_DEBUG_FAKE32 FFI_PLATYPUS_NO_ALLOCA \
    FFI_PLATYPUS_NO_EXTRA_TYPES FFI_PLATYPUS_PROBE_OVERRIDE V
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%{make_build} ffi-test
chmod 0755 t/ffi/_build
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe 's{blib/lib}{%{perl_vendorarch}}' \
    %{buildroot}%{_libexecdir}/%{name}/t/ffi_probe.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset FFI_PLATYPUS_DLERROR FFI_PLATYPUS_MEMORY_STRDUP_IMPL PERL5LIB V
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset FFI_PLATYPUS_DLERROR FFI_PLATYPUS_MEMORY_STRDUP_IMPL PERL5LIB V
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-FFI-Platypus-tests -f %{oreon_filedir}/perl-FFI-Platypus-tests.list

%changelog

%autochangelog
