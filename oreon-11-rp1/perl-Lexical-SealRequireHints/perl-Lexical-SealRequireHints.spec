%global source0_hash c32bdc38e06f8d6c90765bbbe3168c358247da7dae85b80ba84a2da1763757dd
%bcond_without perl_Lexical_SealRequireHints_enables_optional_test
Name:           perl-Lexical-SealRequireHints
Version:        0.012
Release:        12%{?dist}
Summary:        Prevent leakage of lexical hints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lexical-SealRequireHints
Source0:        https://cpan.metacpan.org/modules/by-module/Lexical/Lexical-SealRequireHints-%{version}.tar.gz
%if %{with perl_Lexical_SealRequireHints_enables_optional_test}
%endif
Conflicts:      perl(B:Hooks::OP::Check) < 0.19
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(t::.*\\)
Provides:       perl(Lexical::SealRequireHints)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module works around two historical bugs in Perl's handling of the %%^H
(lexical hints) variable. One bug causes lexical state in one file to leak
into another that is required/used from it. This bug [perl #68590], was
present from Perl 5.6 up to Perl 5.10, fixed in Perl 5.11.0. The second bug
causes lexical state (normally a blank %%^H once the first bug is fixed) to
leak outwards from utf8.pm, if it is automatically loaded during Unicode
regular expression matching, into whatever source is compiling at the time
of the regexp match. This bug [perl #73174], was present from Perl 5.8.7
up to Perl 5.11.5, fixed in Perl 5.12.0.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Lexical-SealRequireHints-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} -c $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Lexical-SealRequireHints-tests -f %{oreon_filedir}/perl-Lexical-SealRequireHints-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.012-12
- Prepare for Oreon 11 (RP1)
