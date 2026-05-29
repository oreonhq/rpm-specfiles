%global source0_hash 44eec2da147ba0511090871b0ca82f69794376bc31e8c76d1040961ba57f59b8

# Perform tests that need the Internet
%bcond_with perl_LWP_Protocol_https_enables_internet_test

Name:           perl-LWP-Protocol-https
Version:        6.15
Release:        1%{?dist}
Summary:        Provide HTTPS support for LWP::UserAgent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-Protocol-https
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-Protocol-https-6.15.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(parent)
BuildRequires:  perl(IO::Socket::SSL) >= 1.970
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::http::SocketMethods)
BuildRequires:  perl(Mozilla::CA) >= 20180117
BuildRequires:  perl(Net::HTTPS) >= 6
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::UserAgent) >= 6.06
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs) >= 0.002010
%if %{with perl_LWP_Protocol_https_enables_internet_test}
BuildRequires:  perl(Test::RequiresInternet)
%endif
# Optional tests:
BuildRequires:  perl(IO::Socket::SSL) >= 1.953
BuildRequires:  perl(IO::Socket::SSL::Utils)
Requires:       perl(IO::Socket::SSL) >= 1.54
Requires:       perl(Mozilla::CA) >= 20180117
Requires:       perl(Net::HTTPS) >= 6

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Net::HTTPS\\)\\s*$

%description
The LWP::Protocol::https module provides support for using HTTPS schemed
URLs with LWP. This module is a plug-in to the LWP protocol handling, so
you don't use it directly. Once the module is installed LWP is able to
access sites using HTTP over SSL/TLS.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n LWP-Protocol-https-%{version}
%if !%{with perl_LWP_Protocol_https_enables_internet_test}
rm t/example.t
perl -i -ne 'print $_ unless m{^t/example.t}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/00*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.15-1
- Prepare for Oreon 11 (RP1)
