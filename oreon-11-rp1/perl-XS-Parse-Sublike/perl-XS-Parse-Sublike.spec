%global source0_hash a10f5e07273b105e5c0b4c6e7e2a6d2d2a68afe9ff4f989c11f38d4bf39cc86d
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_XS_Parse_Sublike_enables_optional_tests
%if %{with perl_XS_Parse_Sublike_enables_optional_tests} && !%{defined perl_bootstrap}
%global optional_tests 1
%else
%global optional_tests 0
%endif
Name:           perl-XS-Parse-Sublike
Version:        0.41
Release:        2%{?dist}
Summary:        XS functions to assist in parsing sub-like syntax
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XS-Parse-Sublike
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Sublike-%{version}.tar.gz
Source1:        macros.perl-XS-Parse-Sublike
Provides:       perl(:XS_Parse_Sublike_ABI) = 5
Provides:       perl(:XS_Parse_Sublike_ABI) = 6
Provides:       perl(:XS_Parse_Sublike_ABI) = 7
Provides:       perl(:XS_Parse_Sublike_ABI) = 8
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Future::AsyncAwait|Object::Pad)\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(testcase\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(testcase\\)
Provides:       perl(Sublike::Extended)
Provides:       perl(XS::Parse::Sublike)
Provides:       perl(XS::Parse::Sublike::Builder)
Provides:       perl(XS::Parse::Sublike)
Provides:       perl(XS::Parse::Sublike::Builder)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides some XS functions to assist in writing parsers for
sub-like syntax, primarily for authors of keyword plugins using the
PL_keyword_plugin hook mechanism.

%package Builder
Summary:        Build-time support for XS::Parse::Sublike
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(File::Spec)
Requires:       perl(XS::Parse::Sublike)
Conflicts:      %{name}%{?_isa} < 0.13
%description Builder
This module provides a build-time helper to assist authors writing XS modules
that use XS::Parse::Sublike. It prepares a Module::Build-using distribution to
be able to make use of XS::Parse::Sublike.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(XSLoader)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n XS-Parse-Sublike-%{version}
%if !%{optional_tests}
for F in t/80extended+async.t t/80extended+Object-Pad.t t/99pod.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
%endif
chmod +x t/*.t

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
./Build testlib
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
install -D -m 0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE1}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
find %{buildroot}%{_libexecdir}/%{name} -type f \
    \( -name '*.bs' -o -name '*.c' -o -name '*.o' \) -delete
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-XS-Parse-Sublike-Builder -f %{oreon_filedir}/perl-XS-Parse-Sublike-Builder.list
%files -n perl-XS-Parse-Sublike-tests -f %{oreon_filedir}/perl-XS-Parse-Sublike-tests.list

%changelog

%autochangelog
