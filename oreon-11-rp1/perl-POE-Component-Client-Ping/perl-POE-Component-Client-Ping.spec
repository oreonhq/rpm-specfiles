%global source0_hash b33b2bf9c12aa97662f0883255fbea4f0ae4450199ac13e76f0129ab0a1912d4

Name:           perl-POE-Component-Client-Ping
Version:        1.177
Release:        15%{?dist}
Summary:        Non-blocking ICMP ping client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-Ping
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Component-Client-Ping-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE) >= 1.007
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes) >= 1.2
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(POE) >= 1.007

%{?perl_default_filter}

%description
POE::Component::Client::Ping is non-blocking ICMP ping client. It lets
several other sessions ping through it in parallel, and it lets them
continue doing other things while they wait for responses.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Client-Ping-%{version}
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README eg
%{perl_vendorlib}/POE
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
