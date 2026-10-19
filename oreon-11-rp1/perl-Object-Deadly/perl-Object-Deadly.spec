%global source0_hash 5ef24cc7901ad3cf2020d608a60fa6a6c889b312664df03f37fe5fdfb381bef7
Name:           perl-Object-Deadly
Version:        0.09
Release:        1%{?dist}
Summary:        Perl module providing an object that dies whenever examined
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Object-Deadly
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJORE/Object-Deadly-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Devel::StackTrace)
Provides:       perl(Object::Deadly)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Object::Deadly is meant to be used in testing. All possible
overloading and method calls die. You can pass this object into
methods which are not supposed to accidentally trigger any potentially
overloading.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Object-Deadly-%{version}
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
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/01*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/02*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/03*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/04*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Object-Deadly-tests -f %{oreon_filedir}/perl-Object-Deadly-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.09-51
- Prepare for Oreon 11 (RP1)
