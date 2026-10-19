%global source0_hash 6076f0c0036d592f6e3f36e60338e7fabf14eb282103169b8e1422e1594550a5
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_Syntax_Keyword_Dynamically_enables_Devel_MAT
%bcond_without perl_Syntax_Keyword_Dynamically_enables_optional_test
Name:           perl-Syntax-Keyword-Dynamically
Version:        0.14
Release:        1%{?dist}
Summary:        Dynamically change the value of a variable
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Keyword-Dynamically
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Dynamically-%{version}.tar.gz
%if %{with perl_Syntax_Keyword_Dynamically_enables_Devel_MAT}
%endif
%define Future_AsyncAwait_minver 0.60
%if %{with perl_Syntax_Keyword_Dynamically_enables_optional_test} && !%{defined perl_bootstrap}
%define Object_Pad_minver 0.800
%endif
Requires:       perl(Future::AsyncAwait) >= %{Future_AsyncAwait_minver}
%if %{defined perl_Future_AsyncAwait_ABI}
Requires:       %{perl_Future_AsyncAwait_ABI}
%endif
Requires:       perl(XS::Parse::Keyword) >= 0.13
%if %{defined perl_XS_Parse_Keyword_ABI}
Requires:       %{perl_XS_Parse_Keyword_ABI}
%endif
Provides:       perl(Syntax::Keyword::Dynamically)
Provides:       perl(Syntax::Keyword::Dynamically)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait)
BuildRequires:  perl(Future::AsyncAwait::ExtensionBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Object::Pad)
BuildRequires:  perl(Sentinel)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XS::Parse::Keyword)
BuildRequires:  perl(XS::Parse::Keyword::Builder)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides a syntax plugin that implements a single keyword,
dynamically, which alters the behavior of a scalar assignment operation.
Syntactically and semantically it is similar to the built-in Perl keyword
local, but is implemented somewhat differently to give two key advantages over
regular local: You can dynamically assign to left-value functions and
accessors, and you can dynamically assign to regular lexical variables.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Syntax_Keyword_Dynamically_enables_optional_test} && !%{defined perl_bootstrap}
Requires:       perl(Future)
Requires:       perl(Future::AsyncAwait) >= 0.31
Requires:       perl(Object::Pad) >= %{Object_Pad_minver}
Requires:       perl(Sentinel)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Syntax-Keyword-Dynamically-%{version}
%if !%{with perl_Syntax_Keyword_Dynamically_enables_optional_test} || %{defined perl_bootstrap}
for F in t/80await+dynamically.t t/80dynamically+Object-Pad.t \
    t/80dynamically+Sentinel.t t/81async-method+dynamically.t t/99pod.t
do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
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
%if %{with perl_Syntax_Keyword_Dynamically_enables_optional_test} && !%{defined perl_bootstrap}
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
%files -n perl-Syntax-Keyword-Dynamically-tests -f %{oreon_filedir}/perl-Syntax-Keyword-Dynamically-tests.list

%changelog

%autochangelog
