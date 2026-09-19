%global source0_hash 9368ceb63580f0f3a877a9295268cbdab538e399e67c0cb5e7d175cac0042c5c

Name:           perl-Test-POE-Server-TCP
Version:        1.20
Release:        30%{?dist}
Summary:        POE Component providing TCP server services for test cases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-POE-Server-TCP
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Test-POE-Server-TCP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter >= 1:5.6.0
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE) >= 1.004
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(blib)
# Missed by the automatic perl dependancy generator.
Requires:       perl(POE) >= 1.004
Requires:       perl(POE::Filter::Line)
Requires:       perl(POE::Wheel::ReadWrite)
Requires:       perl(POE::Wheel::SocketFactory)

%description
Test::POE::Server::TCP is a POE component that provides a TCP server
framework for inclusion in client component test cases, instead of having
to roll your own.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-POE-Server-TCP-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/author*
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
%doc Changes examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
