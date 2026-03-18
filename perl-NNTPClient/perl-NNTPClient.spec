Name:           perl-NNTPClient
Version:        0.37
Release:        28%{?dist}
Summary:        Perl 5 module to talk to NNTP (RFC977) server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/NNTPClient
Source0:        https://cpan.metacpan.org/authors/id/R/RV/RVA/NNTPClient-%{version}.tar.gz
# Skip unportable tests whose command is not supported by a server,
# CPAN RT#118794
Patch0:         NNTPClient-0.37-Skip-tests-with-unportable-commands.patch
# Skip network tests by default, CPAN RT#118799, inn segfaults (bug #1395717)
Patch1:         NNTPClient-0.37-Perform-network-tests-only-if-EXTENDED_TESTING-1.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.2.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Do not scan documentation for dependencies
%{?perl_default_filter}

%description
This module implements a client interface to NNTP, enabling a Perl 5
application to talk to NNTP servers. It uses the Object Oriented
Programming interface.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n NNTPClient-%{version}
%patch -P0 -p1
%patch -P1 -p1
perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "test.pl"
chmod +x "test.pl"

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/t
cp -a test.pl %{buildroot}%{_libexecdir}/%{name}/t/test.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc demos README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.37-28
- Prepare for Oreon 11 (RP1)
