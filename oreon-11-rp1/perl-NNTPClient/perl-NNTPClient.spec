%global source0_hash 5c51a634ffccca95eb2d95855bcc937b057f9a14bd79ee4db6e65583bd576da3
Name:           perl-NNTPClient
Version:        0.37
Release:        1%{?dist}
Summary:        Perl 5 module to talk to NNTP (RFC977) server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/NNTPClient
Source0:        https://cpan.metacpan.org/authors/id/R/RV/RVA/NNTPClient-%{version}.tar.gz
Patch0:         NNTPClient-0.37-Skip-tests-with-unportable-commands.patch
Patch1:         NNTPClient-0.37-Perform-network-tests-only-if-EXTENDED_TESTING-1.patch
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/t
cp -a test.pl %{buildroot}%{_libexecdir}/%{name}/t/test.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-NNTPClient-tests -f %{oreon_filedir}/perl-NNTPClient-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.37-28
- Prepare for Oreon 11 (RP1)
