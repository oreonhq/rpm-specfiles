%global source0_hash 97942355391214a070565cadbfcf92c14f705f8d3aa12ff124d40fd53fac8e37
%bcond_without  perl_Syntax_Operator_Divides_enables_optional_test
%if %{with perl_Syntax_Operator_Divides_enables_optional_test} && !%{defined perl_bootstrap}
%global optional_tests 1
%else
%global optional_tests 0
%endif
Name:           perl-Syntax-Operator-Divides
Version:        0.08
Release:        1%{?dist}
Summary:        Infix operator for division test
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Operator-Divides
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Operator-Divides-%{version}.tar.gz
%global xs_parse_infix_minver 0.43
%global meta_min_ver 0.003.002
Requires:       perl(meta) >= %{meta_min_ver}
Requires:       perl(XS::Parse::Infix) >= %{xs_parse_infix_minver}
%if %{defined perl_XS_Parse_Infix_ABI}
Requires:       %{perl_XS_Parse_Infix_ABI}
%endif
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(meta\\) >= 0.003$
Provides:       perl(Syntax::Operator::Divides)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(XS::Parse::Infix::Builder)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(meta)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides an infix operator that implements an integer divides
test which returns true if the lefthand operand is a whole multiple of the
righthand.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Syntax-Operator-Divides-%{version}
%if !%{optional_tests}
for T in t/80match-divides.t t/99pod.t; do
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Syntax-Operator-Divides-tests -f %{oreon_filedir}/perl-Syntax-Operator-Divides-tests.list

%changelog

%autochangelog
