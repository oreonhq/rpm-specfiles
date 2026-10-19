%global source0_hash 4921d211b0cea63c2ca06dfc0c948a7203a3d48ad80a06f43b46104354f2c1c3
%bcond_without perl_autodie_enables_optional_test
Name:           perl-autodie
Version:        2.37
Release:        1%{?dist}
Summary:        Replace functions with ones that succeed or die
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/autodie
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/autodie-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
%if %{with perl_autodie_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Requires:       perl(B)
Requires:       perl(Fcntl)
Requires:       perl(POSIX)
%if !%{defined perl_bootstrap}
Requires:  perl(IPC::System::Simple) >= 0.12
%endif
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(lib\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(autodie::test.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(autodie_.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Caller_helper\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Hints_.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(lethal\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(my::.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(pujHa::ghach\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Some::Module\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(lib)
%if %{with perl_autodie_enables_optional_test} && !%{defined perl_bootstrap}
Requires:       perl(BSD::Resource)
Requires:       perl(Import::Into) >= 1.002004
%endif
Provides:       perl(autodie)
Provides:       perl(Fatal)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%description
The "autodie" and "Fatal" pragma provides a convenient way to replace
functions that normally return false on failure with equivalents that throw an
exception on failure.

However "Fatal" has been obsoleted by the new autodie pragma. Please use
autodie in preference to "Fatal".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n autodie-%{version}
find -type f -exec chmod -x {} +

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
unset AUTHOR_TESTING AUTOMATED_TESTING PERL_CORE RELEASE_TESTING
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING AUTOMATED_TESTING PERL_CORE RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-autodie-tests -f %{oreon_filedir}/perl-autodie-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.37-522
- Prepare for Oreon 11 (RP1)
