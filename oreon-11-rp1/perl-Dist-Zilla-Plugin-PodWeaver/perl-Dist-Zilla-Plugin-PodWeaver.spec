%global source0_hash 666d52d545d48d2a67f1537adc74cf38c764a1f9951d0b623623f62060cb623e
Name:           perl-Dist-Zilla-Plugin-PodWeaver
Version:        4.010
Release:        9%{?dist}
Summary:        Weave your POD together from configuration and Dist::Zilla
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-PodWeaver
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Dist-Zilla-Plugin-PodWeaver-%{version}.tar.gz
Patch0:         Dist-Zilla-Plugin-PodWeaver-4.010-List-tested-files-explicitely.patch
BuildArch:      noarch
Requires:       perl(Dist::Zilla) >= 6
Requires:       perl(Dist::Zilla::Role::FileFinderUser)
Requires:       perl(Dist::Zilla::Role::FileMunger)
Requires:       perl(Pod::Elemental::PerlMunger) >= 0.1
Requires:       perl(Pod::Weaver) >= 4
Requires:       perl(Pod::Weaver::Config::Assembler)
Requires:       perl(PPI)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Pod::Weaver\\) >= 3
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Dist::Zilla)
BuildRequires:  perl(Dist::Zilla::Role::FileFinderUser)
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Pod::Elemental::PerlMunger)
BuildRequires:  perl(Pod::Weaver)
BuildRequires:  perl(Pod::Weaver::Config::Assembler)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
PodWeaver is the bridge between Dist::Zilla and Pod::Weaver. It rips
apart your kinda-POD and reconstructs it as a boring old real POD.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Dist-Zilla-Plugin-PodWeaver-%{version}
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
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Dist-Zilla-Plugin-PodWeaver-tests -f %{oreon_filedir}/perl-Dist-Zilla-Plugin-PodWeaver-tests.list

%changelog

%autochangelog
