%global source0_hash 522d40aba5540236ae5adeb80e15eb488bac9bfc35f3d5e96436d22cfccb9666
%bcond_without perl_Syntax_Operator_In_enables_optional_test
Name:           perl-Syntax-Operator-In
Version:        0.10
Release:        5%{?dist}
Summary:        Infix element-of-list meta-operator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Operator-In
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Operator-In-%{version}.tar.gz
%define xs_parse_infix_minver 0.44
%global meta_min_ver 0.003.002
%if %{with perl_Syntax_Operator_In_enables_optional_test}
%endif
Requires:       perl(meta) >= %{meta_min_ver}
Requires:       perl(XS::Parse::Infix) >= %{xs_parse_infix_minver}
%if %{defined perl_XS_Parse_Infix_ABI}
Requires:       %{perl_XS_Parse_Infix_ABI}
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(meta\\) >= 0\\.003$
Provides:       perl(Syntax::Operator::In)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Syntax::Operator::Equ)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XS::Parse::Infix)
BuildRequires:  perl(XS::Parse::Infix::Builder)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(meta)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides an infix meta-operator that implements an
element-of-list test on either strings or numbers.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Syntax_Operator_In_enables_optional_test}
Requires:       perl(Syntax::Operator::Equ)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Syntax-Operator-In-%{version}
%if !%{with perl_Syntax_Operator_In_enables_optional_test}
for T in t/80in+equ.t t/99pod.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
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
%if %{with perl_Syntax_Operator_In_enables_optional_test}
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
%files -n perl-Syntax-Operator-In-tests -f %{oreon_filedir}/perl-Syntax-Operator-In-tests.list

%changelog

%autochangelog
