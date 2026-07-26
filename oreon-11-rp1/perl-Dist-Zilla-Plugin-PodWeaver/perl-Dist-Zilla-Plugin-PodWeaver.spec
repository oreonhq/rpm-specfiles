%global source0_hash 666d52d545d48d2a67f1537adc74cf38c764a1f9951d0b623623f62060cb623e

Name:           perl-Dist-Zilla-Plugin-PodWeaver
Version:        4.010
Release:        9%{?dist}
Summary:        Weave your POD together from configuration and Dist::Zilla
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-PodWeaver
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Dist-Zilla-Plugin-PodWeaver-%{version}.tar.gz
# Make the packaged tests useful, not suitable for upstream.
Patch0:         Dist-Zilla-Plugin-PodWeaver-4.010-List-tested-files-explicitely.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.20.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# A Dist::Zilla plug-in, version from META
BuildRequires:  perl(Dist::Zilla) >= 6
BuildRequires:  perl(Dist::Zilla::Role::FileFinderUser)
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Pod::Elemental::PerlMunger) >= 0.1
BuildRequires:  perl(Pod::Weaver) >= 4
BuildRequires:  perl(Pod::Weaver::Config::Assembler)
BuildRequires:  perl(PPI)
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# A Dist::Zilla plug-in, version from META
Requires:       perl(Dist::Zilla) >= 6
Requires:       perl(Dist::Zilla::Role::FileFinderUser)
Requires:       perl(Dist::Zilla::Role::FileMunger)
Requires:       perl(Pod::Elemental::PerlMunger) >= 0.1
Requires:       perl(Pod::Weaver) >= 4
Requires:       perl(Pod::Weaver::Config::Assembler)
Requires:       perl(PPI)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Pod::Weaver\\) >= 3
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::More\\)$

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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
