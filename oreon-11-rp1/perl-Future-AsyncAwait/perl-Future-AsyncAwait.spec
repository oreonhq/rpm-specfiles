%global source0_hash 16caa557a3e7a95e0e6ff5fe39672aa8580047c75fa7748eb8b1cb183a7beb70
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_Future_AsyncAwait_enables_Devel_MAT
%bcond_without perl_Future_AsyncAwait_enables_optional_test
%bcond_without perl_Future_AsyncAwait_enables_role
%if %{with perl_Future_AsyncAwait_enables_optional_test} && !%{defined perl_bootstrap}
%global optional_tests 1
%else
%global optional_tests 0
%endif
Name:           perl-Future-AsyncAwait
Version:        0.71
Release:        1%{?dist}
Summary:        Deferred subroutine syntax for futures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Future-AsyncAwait
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-AsyncAwait-%{version}.tar.gz
Source1:        macros.perl-Future-AsyncAwait
%if %{with perl_Future_AsyncAwait_enables_Devel_MAT}
%endif
%define xs_parse_keyword_min_ver 0.13
%define xs_parse_sublike_min_ver 0.31
%define future_min_ver 0.50
%if %{with perl_Future_AsyncAwait_enables_role}
%endif
%if %{with perl_Future_AsyncAwait_enables_role}
%endif
Requires:       perl(Future) >= %{future_min_ver}
%if %{with perl_Future_AsyncAwait_enables_role}
Recommends:     perl(Role::Tiny)
%endif
Requires:       perl(XS::Parse::Keyword) >= %{xs_parse_keyword_min_ver}
%if %{defined perl_XS_Parse_Keyword_ABI}
Requires:       %{perl_XS_Parse_Keyword_ABI}
%endif
Requires:       perl(XS::Parse::Sublike) >= %{xs_parse_sublike_min_ver}
%if %{defined perl_XS_Parse_Sublike_ABI}
Requires:       %{perl_XS_Parse_Sublike_ABI}
%endif
Provides:       perl(:Future_AsyncAwait_ABI) = 1
Provides:       perl(:Future_AsyncAwait_ABI) = 2
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Future|Object::Pad|Sublike::Extended|Syntax::Keyword::Dynamically|Syntax::Keyword::Try)\\)$
Provides:       perl(Future::AsyncAwait)
Provides:       perl(Future::AsyncAwait::ExtensionBuilder)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Future)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Future::Deferred)
BuildRequires:  perl(XS::Parse::Keyword)
BuildRequires:  perl(XS::Parse::Keyword::Builder)
BuildRequires:  perl(XS::Parse::Sublike)
BuildRequires:  perl(XS::Parse::Sublike::Builder)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(attributes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides syntax for deferring and resuming subroutines while
waiting for Futures to complete. This syntax aims to make code that performs
asynchronous operations using futures look neater and more expressive than
simply using then chaining and other techniques on the futures themselves.

%package ExtensionBuilder
Summary:        Build script for Future::AsyncAwait extensions
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(File::Spec)
Requires:       perl(Future::AsyncAwait)
Requires:       rpm
%description ExtensionBuilder
These Perl modules support building XS extensions for Future::AsyncAwait
module.

%package Test
Summary:        Conformance tests for Future::AsyncAwait::Awaitable role
BuildArch:      noarch
%description Test
This Perl module provides a single test function, which runs a suite of
subtests to check that a given class provides a usable implementation of the
Future::AsyncAwait::Awaitable role. It runs tests that simulate various ways
in which Future::AsyncAwait will try to use an instance of this class, to
check that the implementation is valid.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(experimental)
Requires:       perl(Future) >= %{future_min_ver}
%if %{with perl_Future_AsyncAwait_enables_role}
Requires:       perl(Role::Tiny)
Requires:       perl(Role::Tiny::With)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Future-AsyncAwait-%{version}
for F in \
%if !%{optional_tests} || !%{with perl_Future_AsyncAwait_enables_Devel_MAT}
    t/82devel-mat-dumper-helper.t \
%endif
%if !%{optional_tests}
    t/80await+defer.t t/80await+dynamically.t t/80await+matchcase.t \
    t/80await+SKT.t t/80async-method.t t/80extended+async.t \
    t/81async-method+dynamically.t t/81memory-growth.t t/99pod.t \
%endif
%if !%{with perl_Future_AsyncAwait_enables_role}
    t/51awaitable-role.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
chmod +x t/*.t

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
install -D -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}
install -m 0755 -d %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{perl_vendorarch}/Test %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Future-AsyncAwait-ExtensionBuilder -f %{oreon_filedir}/perl-Future-AsyncAwait-ExtensionBuilder.list
%files -n perl-Future-AsyncAwait-Test -f %{oreon_filedir}/perl-Future-AsyncAwait-Test.list
%files -n perl-Future-AsyncAwait-tests -f %{oreon_filedir}/perl-Future-AsyncAwait-tests.list

%changelog

%autochangelog
