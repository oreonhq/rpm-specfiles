# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 2992125eab7d2b1c5a2b15a26ad7955f7d989eba6c831abdcaf2000e86a91337
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           perl-podlators
Epoch:          1
Version:        6.0.2
Release:        521%{?dist}
Summary:        Format POD source into various output formats
# pod/perlpodstyle.pod:     FSFAP
# other files:              GPL-1.0-or-later OR Artistic-1.0-Perl
## Not in the binary package
# t/data/basic.cap:         FSFAP
# t/data/basic.clr:         FSFAP
# t/data/basic.man:         FSFAP
# t/data/basic.ovr:         FSFAP
# t/data/basic.pod:         FSFAP
# t/data/basic.txt:         FSFAP
# t/data/man/*:             FSFAP
# t/data/snippets/man/uppercase-license:    MIT
# t/data/snippets/README:   FSFAP
# t/docs/pod.t:             MIT
# t/docs/pod-spelling.t:    MIT
# t/docs/spdx-license.t:    MIT
# t/docs/synopsis.t:        MIT
# t/docs/urls.t:            MIT
# t/lib/Test/RRA.pm:        MIT
# t/lib/Test/RRA/Config.pm:         MIT
# t/lib/Test/RRA/ModuleVersion.pm:  MIT
# t/style/minimum-version.t:        MIT
# t/style/module-version.t:         MIT
# t/style/strict.t:         MIT
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND FSFAP
URL:            https://metacpan.org/release/podlators
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRA/podlators-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
# Cwd run by PL script in scripts directory
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Basename run by PL script in scripts directory
BuildRequires:  perl(File::Basename)
# File::Spec version declared in lib/Pod/Man.pm comment
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(parent)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(Pod::Simple) >= 3.26
# Pod::Usage not used at tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::Cap)
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests:
# JSON::PP not used
# Perl::Critic::Utils not used
# Perl6::Slurp not used
BuildRequires:  perl(PerlIO::encoding)
# Test::CPAN::Changes not used
# Test::MinimumVersion not used
# Test::Pod not used
# Test::Spelling not used
# Test::Strict not used
# Test::Synopsis not used
Requires:       perl(File::Basename)
# File::Spec version declared in lib/Pod/Man.pm comment
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(PerlIO)
Requires:       perl(Pod::Simple) >= 3.26
Conflicts:      perl < 4:5.16.1-234

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Pod::Simple\\)$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::Podlators\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::RRA.*\\)

%description
This package contains Pod::Man and Pod::Text modules which convert POD input
to *roff source output, suitable for man pages, or plain text.  It also
includes several sub-classes of Pod::Text for formatted output to terminals
with various capabilities.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(PerlIO)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_verify_sources
%setup -q -n podlators-v%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
for F in `find %{buildroot}%{_libexecdir}/%{name} -name *.t -o -name *.pm`; do
    perl -i -pe "s{'t', 'tmp'}{'/tmp'}" $F
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING AUTOMATED_TESTING RELEASE_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
unset AUTHOR_TESTING AUTOMATED_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes README THANKS TODO
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.2-521
- Prepare for Oreon 11 (RP1)
