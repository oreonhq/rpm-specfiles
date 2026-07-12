%global source0_hash 522d40aba5540236ae5adeb80e15eb488bac9bfc35f3d5e96436d22cfccb9666

# Perform optional tests
%bcond_without perl_Syntax_Operator_In_enables_optional_test

Name:           perl-Syntax-Operator-In
Version:        0.10
Release:        5%{?dist}
Summary:        Infix element-of-list meta-operator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Operator-In
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Operator-In-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%define xs_parse_infix_minver 0.44
BuildRequires:  perl(XS::Parse::Infix::Builder) >= %{xs_parse_infix_minver}
# Run-time:
BuildRequires:  perl(Carp)
%global meta_min_ver 0.003.002
BuildRequires:  perl(meta) >= %{meta_min_ver}
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(XS::Parse::Infix) >= %{xs_parse_infix_minver}
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(utf8)
%if %{with perl_Syntax_Operator_In_enables_optional_test}
# Optional tests:
# Perl with PL_infix_plugin support is required (since 5.37.7)
BuildRequires:  perl(Syntax::Operator::Equ)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
Requires:       perl(meta) >= %{meta_min_ver}
Requires:       perl(XS::Parse::Infix) >= %{xs_parse_infix_minver}
%if %{defined perl_XS_Parse_Infix_ABI}
# XS::Parse::Infix ABI checked in XSParseInfix.h included from
# perl-XS-Parse-Keyword-Builder.
Requires:       %{perl_XS_Parse_Infix_ABI}
%endif

# Remove underspecied dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(meta\\) >= 0\\.003$

Provides:       perl(Syntax::Operator::In)
%description
This Perl module provides an infix meta-operator that implements an
element-of-list test on either strings or numbers.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Syntax_Operator_In_enables_optional_test}
# Optional tests:
# Perl with PL_infix_plugin support is required (since 5.37.7)
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Syntax_Operator_In_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/Syntax
%dir %{perl_vendorarch}/auto/Syntax/Operator
%{perl_vendorarch}/auto/Syntax/Operator/In
%dir %{perl_vendorarch}/Syntax
%{perl_vendorarch}/Syntax/Operator
%{_mandir}/man3/Syntax::Operator::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
