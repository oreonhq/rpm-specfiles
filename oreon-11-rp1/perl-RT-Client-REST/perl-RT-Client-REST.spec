%global source0_hash 28f20158a0f7b1f34b74ce36de5bdd56299eb940140472c8497c95358226fdb3

Name:       perl-RT-Client-REST 
Version:    0.72
Release:    8%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Talk to RT using REST protocol 
Url:        https://metacpan.org/release/RT-Client-REST
Source:     https://cpan.metacpan.org/authors/id/D/DJ/DJZORT/RT-Client-REST-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::DateParse)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(parent)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Server::Simple) >= 0.44
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(HTTP::Server::Simple\\)$

%description
RT::Client::REST is a set of object-oriented Perl modules designed to make
communicating with RT using REST protocol easy. Most of the features have been
implemented and tested with rt 3.6.0 and later.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(blib)
Requires:       perl(HTTP::Server::Simple) >= 0.44

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RT-Client-REST-%{version}
# Delete author and release tests
rm t/{author,release}-* t/60-with-rt.t
perl -i -ne 'print $_ unless m{^t/(?:author|release)-.*}' MANIFEST
perl -i -ne 'print $_ unless m{^t/60-with-rt\.t}' MANIFEST
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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING RELEASE_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc CHANGES CONTRIBUTORS examples README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
