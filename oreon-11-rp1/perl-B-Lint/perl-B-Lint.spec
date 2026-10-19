%global source0_hash dc49408964fd8b7963859c92e013f0b9f92f74be5a7c2a78e3996279827c10b3
Name:           perl-B-Lint
Version:        1.20
Release:        1%{?dist}
Summary:        Perl lint
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Lint
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/B-Lint-%{version}.tar.gz
Patch0:         B-Lint-1.20-Skip-a-bare-sub-test.patch
BuildArch:      noarch
%if 0%(perl -e 'print $] > 5.017')
%endif
Requires:       perl(constant)
%if 0%(perl -e 'print $] > 5.017')
Requires:       perl(deprecate)
%endif
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(B::Lint::Plugin::Test\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(O)
BuildRequires:  perl(constant)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
The B::Lint module is equivalent to an extended version of the -w option of
perl. It is named after the program lint which carries out a similar process
for C programs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n B-Lint-%{version}
%patch -P0 -p1
# Install into architecture-agnostic path, CPAN RT#83049
sed -i '/PM *=>/,/}/d' Makefile.PL
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-B-Lint-tests -f %{oreon_filedir}/perl-B-Lint-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20-34
- Prepare for Oreon 11 (RP1)
