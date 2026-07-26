%global source0_hash 5b8b8a584acc6486d21e77feae71503d3cb60ca19c372d03edf6462e9fc5c520

# Run optional test
%bcond_without perl_POE_Component_Server_SimpleHTTP_enables_optional_test

Name:           perl-POE-Component-Server-SimpleHTTP
Version:        2.30
Release:        8%{?dist}
Summary:        Serve HTTP requests in POE
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-SimpleHTTP
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/POE-Component-Server-SimpleHTTP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Moose) >= 0.9
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::POE) >= 0.205
BuildRequires:  perl(POE) >= 1.0000
BuildRequires:  perl(POE::Component::SSLify) >= 0.04
BuildRequires:  perl(POE::Filter::HTTPD)
BuildRequires:  perl(POE::Filter::Stream)
BuildRequires:  perl(POE::Wheel::ReadWrite)
BuildRequires:  perl(POE::Wheel::SocketFactory)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Hostname)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POE::Filter::HTTP::Parser) >= 1.06
BuildRequires:  perl(POE::Kernel)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Test::POE::Client::TCP) >= 1.24
%if %{with perl_POE_Component_Server_SimpleHTTP_enables_optional_test}
# Optional tests only
BuildRequires:  perl(POE::Component::Client::HTTP) >= 0.82
%endif
Requires:       perl(HTTP::Request)
Requires:       perl(Moose) >= 0.9
Requires:       perl(Moose::Object)
Requires:       perl(MooseX::POE) >= 0.205
Requires:       perl(POE) >= 1.0000
Recommends:     perl(POE::Component::SSLify) >= 0.04
Requires:       perl(Storable)
Requires:       perl(Sys::Hostname)

%{?perl_default_filter}
# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Moose|MooseX::POE|POE|POE::Filter::HTTP::Parser|Test::More|Test::POE::Client::TCP)\\)$

%description
This module makes serving up HTTP requests a breeze in POE.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(POE) >= 1.0000
%if %{with perl_POE_Component_Server_SimpleHTTP_enables_optional_test}
Requires:       perl(POE::Component::Client::HTTP) >= 0.82
%endif
Requires:       perl(POE::Filter::HTTP::Parser) >= 1.06
Requires:       perl(POE::Filter::Stream)
Requires:       perl(Test::More) >= 0.47
Requires:       perl(Test::POE::Client::TCP) >= 1.24

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n POE-Component-Server-SimpleHTTP-%{version}
perl -i -pe 's/\r$//g' examples/*
# Remove unused tests
for F in \
    t/author-pod-coverage.t t/author-pod-syntax.t \
%if !%{with perl_POE_Component_Server_SimpleHTTP_enables_optional_test}
    t/06_stream.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
yes | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc README Changes Changes.old examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
