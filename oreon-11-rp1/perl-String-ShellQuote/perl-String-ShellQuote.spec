%global source0_hash e606365038ce20d646d255c805effdd32f86475f18d43ca75455b00e4d86dd35

Name:           perl-String-ShellQuote
Version:        1.04
Release:        47%{?dist}
Summary:        Perl module for quoting strings for passing through the shell
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later
URL:            https://metacpan.org/release/String-ShellQuote
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROSCH/String-ShellQuote-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# RS::Handy is never used
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
Requires:       perl(Carp)
Requires:       perl(Getopt::Long)

Provides:       perl(String::ShellQuote)
%description
This package contains a Perl module and a command line utility which
are useful for quoting strings which are going to pass through the
shell or a shell-like object.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n String-ShellQuote-%{version}

# Help generators to recognize Perl scripts
perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' test.t
chmod +x test.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}/t
cp -a test.t %{buildroot}%{_libexecdir}/%{name}/t
perl -i -pe 's{blib/script}{%{_bindir}}' %{buildroot}%{_libexecdir}/%{name}/t/test.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes README
%{_bindir}/shell-quote
%{perl_vendorlib}/String
%{_mandir}/man1/shell-quote*
%{_mandir}/man3/String::ShellQuote*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.04-47
- Prepare for Oreon 11 (RP1)
