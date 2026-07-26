%global source0_hash b3e871bada8fe7cc82bcb43355ae41d014932349821238caabc81576cc61f46f

Name:           perl-Shell-Guess
Version:        0.10
Release:        5%{?dist}
Summary:        Make an educated guess about the shell in use
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Shell-Guess
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Shell-Guess-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(Unix::Process)
# Win32::Getppid not used on Linux
# Win32::Process::List not used on Linux
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.98
# Optional tests
BuildRequires:  bash
BuildRequires:  tcsh
Requires:       perl(Unix::Process)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(FakeLogin\\)

%description
The Shell::Guess Perl module makes a reasonably aggressive attempt to
determine the shell being employed by the user, either the shell that executed
the Perl script directly, or the users' login shell.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       bash
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.98
Requires:       tcsh

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Shell-Guess-%{version}
# Remove always skipped tests
for T in t/shell_guess__os_{dos,vms,win32}.t; do
    rm -- "$T"
    perl -i -ne 'print $_ unless m{\A\Q'"$T"'\E}' MANIFEST
done
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
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL5OPT
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL5OPT
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Shell
%{perl_vendorlib}/Shell/Guess.pm
%{_mandir}/man3/Shell::Guess.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
