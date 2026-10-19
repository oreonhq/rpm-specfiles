%global source0_hash b1f6b0be347efb355968abca961643f8e11144a9f301e81df5432795d9d63751
%bcond_without perl_Syntax_Keyword_Defer_enables_optional_test
%if %{with perl_Syntax_Keyword_Defer_enables_optional_test} && !%{defined perl_bootstrap}
%define optional_tests 1
%else
%define optional_tests 0
%endif
Name:           perl-Syntax-Keyword-Defer
Version:        0.11
Release:        1%{?dist}
Summary:        Add defer block syntax to Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Keyword-Defer
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Defer-%{version}.tar.gz
%if %{optional_tests}
%endif
Requires:       perl(XS::Parse::Keyword) >= 0.13
%if %{defined perl_XS_Parse_Keyword_ABI}
Requires:       %{perl_XS_Parse_Keyword_ABI}
%endif
Provides:       perl(Syntax::Keyword::Defer)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Syntax::Keyword::Try)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XS::Parse::Keyword)
BuildRequires:  perl(XS::Parse::Keyword::Builder)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides a syntax plugin that implements a block which
executes when the containing scope has finished. The "defer" blocks are
primarily intended for cases such as resource finalization tasks that may be
conditionally required.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(feature)
%if %{optional_tests}
Requires:       perl(Future)
Requires:       perl(Future::AsyncAwait) >= 0.50
Requires:       perl(Syntax::Keyword::Try) >= 0.18
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Syntax-Keyword-Defer-%{version}
%if !%{optional_tests}
for F in t/80await+defer.t t/80defer+SKT.t t/99pod.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E\b}' MANIFEST
done
%endif
chmod +x t/*.t

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{optional_tests}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Syntax-Keyword-Defer-tests -f %{oreon_filedir}/perl-Syntax-Keyword-Defer-tests.list

%changelog

%autochangelog
