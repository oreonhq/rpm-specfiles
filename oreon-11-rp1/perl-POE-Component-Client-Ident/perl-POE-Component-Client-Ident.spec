%global source0_hash 2a5b1ce0b15fde4ca2167931d8c455330486044a32df3d91e582bc23b1a0fcb4

# Run optional tests
%{bcond_without perl_POE_Component_Client_Ident_enables_optional_test}

Name:           perl-POE-Component-Client-Ident
Version:        1.16
Release:        38%{?dist}
Summary:        A component that provides non-blocking Ident lookups to your sessions
# FSF address issue, CPAN RT #85675
# lib/POE/Component/Client/Ident.pm:        GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/POE/Component/Client/Ident/Agent.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/POE/Filter/Ident.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                  GPL-1.0-or-later OR Artistic-1.0-Perl
## Not used, unbundled
# inc/Module/Install:       GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Client-Ident
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Component-Client-Ident-%{version}.tar.gz
BuildArch:      noarch
# build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoLicense)
BuildRequires:  perl(Module::Install::GithubMeta)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
# runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Driver::SysRW)
BuildRequires:  perl(POE::Filter::Line)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Session)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Socket)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# testsuite
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::POE::Server::TCP)
%if %{with perl_POE_Component_Client_Ident_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
Requires:       perl(POE::Driver::SysRW)
Requires:       perl(POE::Filter::Line)
Requires:       perl(POE::Filter::Stream)
Requires:       perl(POE::Wheel::ReadWrite)
Requires:       perl(POE::Wheel::SocketFactory)
Requires:       perl(POE::Session)

%description
This package ships with three ident modules:

POE::Component::Client::Ident is a POE component that provides
non-blocking Ident lookup services to other components
and sessions. The Ident protocol is described in RFC 1413
<http://www.faqs.org/rfcs/rfc1413.html>.

POE::Component::Client::Ident::Agent is a POE component that provides
a single "one shot" lookup of a user name on the remote side of a TCP
connection to other components and sessions, using the ident (auth/tap)
protocol.

POE::Filter::Ident takes lines of raw Ident input and turns
them into weird little data structures, suitable for feeding to
POE::Component::Client::Ident::Agent.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(POE::Filter::Line)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Client-Ident-%{version}
# Remove bundled modules
rm -r ./inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Remove unused tests
%if !%{with perl_POE_Component_Client_Ident_enables_optional_test}
for T in t/99_pod*.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done 

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_POE_Component_Client_Ident_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/99_pod*.t 
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component
%dir %{perl_vendorlib}/POE/Component/Client
%{perl_vendorlib}/POE/Component/Client/Ident
%{perl_vendorlib}/POE/Component/Client/Ident.pm
%dir %{perl_vendorlib}/POE/Filter
%{perl_vendorlib}/POE/Filter/Ident.pm
%{_mandir}/man3/POE::Component::Client::Ident::*
%{_mandir}/man3/POE::Component::Client::Ident.3*
%{_mandir}/man3/POE::Filter::Ident.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
