%global source0_hash 9dcfdf4ca357caa6557c04bf6e215c1ef4784d5711ab246c5400b49863a3f61b
%bcond_without perl_XS_Parse_Keyword_enables_optional_test
Name:           perl-XS-Parse-Keyword
Version:        0.51
Release:        1%{?dist}
Summary:        XS functions to assist in parsing keyword syntax
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XS-Parse-Keyword
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/XS-Parse-Keyword-%{version}.tar.gz
Source1:        macros.perl-XS-Parse-Keyword
%if %{with perl_XS_Parse_Keyword_enables_optional_test}
%endif
Provides:       perl(:XS_Parse_Keyword_ABI_1) = 1
Provides:       perl(:XS_Parse_Keyword_ABI_2) = 2
Provides:       perl(:XS_Parse_Infix_ABI_1) = 1
Provides:       perl(:XS_Parse_Infix_ABI_2) = 2
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(testcase\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(testcase\\)
Provides:       perl(XS::Parse::Keyword)
Provides:       perl(XS::Parse::Infix)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CChecker)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides some XS functions to assist in writing syntax modules
that provide new perl-visible syntax, primarily for authors of keyword plugins
using the PL_keyword_plugin hook mechanism.

%package Builder
Summary:        Build-time support for XS::Parse::Keyword
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-interpreter
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(File::Spec)
Requires:       perl(XS::Parse::Infix)
Requires:       perl(XS::Parse::Keyword)
Conflicts:      %{name}%{?_isa} < 0.06
%description Builder
This module provides a build-time helper to assist authors writing XS modules
that use XS::Parse::Keyword. It prepares a Module::Build-using distribution to
be able to make use of XS::Parse::Keyword.

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
%autosetup -p1 -n XS-Parse-Keyword-%{version}
%if !%{with perl_XS_Parse_Keyword_enables_optional_test}
rm t/99pod.t
perl -i -ne 'print $_ unless m{\A\Qt/99pod.t\E\b}' MANIFEST
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
%if %{with perl_XS_Parse_Keyword_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-XS-Parse-Keyword-Builder -f %{oreon_filedir}/perl-XS-Parse-Keyword-Builder.list
%files -n perl-XS-Parse-Keyword-tests -f %{oreon_filedir}/perl-XS-Parse-Keyword-tests.list

%changelog

%autochangelog
