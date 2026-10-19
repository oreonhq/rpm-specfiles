%global source0_hash f51f0a8ba140d8722851416206677f2f3e87c207abc8c1193e691e2eeb2eb0ea
Name:           perl-Test-Inter
Version:        1.13
Release:        1%{?dist}
Summary:        Framework for more readable interactive test scripts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Inter
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/Test-Inter-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(lib)
Provides:       perl(Test::Inter)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is another framework for writing test scripts. It is loosely inspired
by Test::More, and has most of it's functionality, but it is not a drop-in
replacement.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Inter-%{version}
chmod -x examples/*
# Help generators to recognize Perl scripts
for F in t/*.t; do
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
rm -f %{buildroot}%{_libexecdir}/%{name}/t/_*
mkdir %{buildroot}%{_libexecdir}/%{name}/lib
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset RELEASE_TESTING TI_END TI_MODE TI_NOCLEAN TI_QUIET TI_START TI_TESTNUM \
    TI_WIDTH
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Inter-tests -f %{oreon_filedir}/perl-Test-Inter-tests.list

%changelog

%autochangelog
