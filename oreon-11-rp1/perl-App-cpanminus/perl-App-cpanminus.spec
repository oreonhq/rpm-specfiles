%global source0_hash b9ffb88e62a06aa91bd7d5a28ef6bdbb942608aea90e3969aa29b33640035214
Name:           perl-App-cpanminus
Version:        1.7049
Release:        1%{?dist}
Summary:        Get, unpack, build and install CPAN modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-cpanminus
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/App-cpanminus-%{version}.tar.gz
Source1:        fatunpack
Patch0:         App-cpanminus-1.7044-SHA1-SHA256-in-checksum-chat.patch
BuildArch:      noarch
%if 0%(perl -e 'print $] < 5.026' 2>/dev/null)
Requires:       perl-core
%else
Requires:       perl
%endif
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta)
Requires:       perl(CPAN::Meta::Check) >= 0.018
Requires:       perl(CPAN::Meta::YAML)
Requires:       perl(Digest::SHA)
Requires:       perl(ExtUtils::Install) >= 1.46
Requires:       perl(ExtUtils::MakeMaker) >= 6.58
Requires:       perl(ExtUtils::Manifest)
Requires:       perl(File::pushd)
Requires:       perl(HTTP::Tiny)
Requires:       perl(local::lib)
Requires:       perl(Module::Build) >= 0.38
Requires:       perl(Module::CoreList)
Requires:       perl(Module::CPANfile)
Requires:       perl(Module::Metadata)
Requires:       perl(Parse::PMFile)
Requires:       perl(Safe)
Requires:       perl(YAML)
Provides:       cpanminus = %{version}-%{release}
Obsoletes:      cpanminus <= 1.2002
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(App::cpanminus\\)$
%global __provides_exclude %{__provides_exclude}|^perl\\(ModuleBuildSkipMan\\)
# oreon:deps
BuildRequires:  /usr/bin/podselect
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Why? It's dependency free, requires zero configuration, and stands alone 
but it's maintainable and extensible with plug-ins and friendly to shell 
scripting. When running, it requires only 10 MB of RAM.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n App-cpanminus-%{version}
# Unbundle fat-packed modules
podselect lib/App/cpanminus.pm > lib/App/cpanminus.pod

for F in bin/cpanm lib/App/cpanminus/fatscript.pm; do
    # CVE-2024-45321 - patch to use https instead of http
    perl -pi -E 's{http://(cpan\.cpantesters\.org|www\.cpan\.org|backpan\.perl\.org|cpan\.metacpan\.org|fastapi\.metacpan\.org|cpanmetadb\.plackperl\.org)}{https://$1}g' "$F"
    %{SOURCE1} --libdir lib --filter '^App/cpanminus' "$F" > "${F}.stripped"
    perl -c -Ilib "${F}.stripped"
    mv "${F}.stripped" "$F"
done

%patch -P0 -p1

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-App-cpanminus-tests -f %{oreon_filedir}/perl-App-cpanminus-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7049-1
- Prepare for Oreon 11 (RP1)
