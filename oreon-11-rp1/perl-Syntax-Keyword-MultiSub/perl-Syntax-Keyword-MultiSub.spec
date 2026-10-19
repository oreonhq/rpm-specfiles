%global source0_hash 5d6bda083de66a69285431da5649fab1d9e7ded841afbe3773310a5c39667602
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without perl_Syntax_Keyword_MultiSub_enables_optional_test
Name:           perl-Syntax-Keyword-MultiSub
Version:        0.05
Release:        1%{?dist}
Summary:        Multiple dispatch on subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Keyword-MultiSub
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-MultiSub-%{version}.tar.gz
Patch0:         Syntax-Keyword-MultiSub-0.02-Fix-formatting-an-IV-variable.patch
%define xs_parse_sublike_min_ver 0.15
%if %{with perl_Syntax_Keyword_MultiSub_enables_optional_test}
%endif
Requires:       perl(XS::Parse::Sublike) >= %{xs_parse_sublike_min_ver}
%if %{defined perl_XS_Parse_Sublike_ABI}
Requires:       %{perl_XS_Parse_Sublike_ABI}
%endif
Provides:       perl(Syntax::Keyword::MultiSub)
Provides:       perl(Syntax::Keyword::MultiSub)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::AsyncAwait)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XS::Parse::Sublike)
BuildRequires:  perl(XS::Parse::Sublike::Builder)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a new keyword, multi, to put before subroutine
declarations, which permits multiple distinct function bodies to be
provided, which take different parameters. A call to a multi sub will
invoke whichever function body best fits the arguments passed.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Syntax_Keyword_MultiSub_enables_optional_test}
Requires:       perl(feature)
Requires:       perl(Future)
Requires:       perl(Future::AsyncAwait) >= 0.55
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Syntax-Keyword-MultiSub-%{version}
%if !%{with perl_Syntax_Keyword_MultiSub_enables_optional_test}
rm t/80async-multi-sub.t
perl -i -ne 'print $_ unless m{^t/80async-multi-sub\.t}' MANIFEST
%endif
chmod +x t/*.t
# Normalize an encoding
iconv -f ISO-8859-1 -t UTF-8 <README >README.new
touch -r README README.new
mv README.new README

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_Syntax_Keyword_MultiSub_enables_optional_test}
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
%files -n perl-Syntax-Keyword-MultiSub-tests -f %{oreon_filedir}/perl-Syntax-Keyword-MultiSub-tests.list

%changelog

%autochangelog
