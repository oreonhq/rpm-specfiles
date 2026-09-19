%global source0_hash d2fbc8c84404a4b45bfd04601e2ff52bc519e3e68714df97b81720e15788f7e0

Name:           perl-Dancer
Version:        1.3522
Release:        1%{?dist}
Summary:        Lightweight yet powerful web application framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dancer
Source0:        http://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Dancer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(HTTP::Body) >= 1.07
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Server::Simple::PSGI) >= 0.11
BuildRequires:  perl(HTTP::Tiny) >= 0.014
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP)
BuildRequires:  perl(MIME::Types) >= 2.17
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny) >= 0.09
BuildRequires:  perl(URI) >= 1.59
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time for tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::CookieJar) >= 0.008
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(mro)
BuildRequires:  perl(Plack::Handler::FCGI)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(URI::Escape)
# Optional tests:
BuildRequires:  perl(HTTP::Parser::XS)
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(Dancer::Session::Cookie) >= 0.14
%endif
Requires:       perl(HTTP::Body) >= 1.07
Requires:       perl(HTTP::Server::Simple::PSGI) >= 0.11
Requires:       perl(HTTP::Tiny) >= 0.014
Requires:       perl(MIME::Types) >= 2.17
Requires:       perl(Try::Tiny) >= 0.09
Requires:       perl(URI) >= 1.59
Requires:       perl(YAML)

%{?perl_default_filter}

# Do not export under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(HTTP::Body\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(HTTP::Server::Simple::PSGI\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(HTTP::Tiny\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(MIME::Types\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(Try::Tiny\\)\\s*$
%global __requires_exclude %{?__requires_exclude}|perl\\(URI\\)\\s*$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(t::lib.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(EasyMocker\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(FromDataApp\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(LinkBlocker\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(TestApp.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(TestPlugin.*\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(TestUtils\\)

%description
Dancer is a web application framework designed to be as effortless as
possible for the developer, taking care of the boring bits as easily as
possible, yet staying out of your way and letting you get on with writing
your code.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Dancer::Session::Cookie)
Requires:       perl(HTTP::Parser::XS)
Requires:       perl(JSON)
Requires:       perl(Template)
Requires:       perl(Test::Output)
Requires:       perl(Test::TCP)
Requires:       perl(XML::Simple)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dancer-%{version}
# Temporary remove the test based on GH issue
# https://github.com/PerlDancer/Dancer/issues/1239
rm t/14_serializer/04_request_xml.t
perl -i -ne 'print $_ unless m{^t/14_serializer/04_request_xml.t}' MANIFEST

# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/author*
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/00_base/08_pod_coverage_dancer.t
ln -s %{_bindir}/dancer %{buildroot}%{_libexecdir}/%{name}/bin
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The solution is to
# copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc AUTHORS Changes examples SECURITY.md
%{_bindir}/dancer
%dir %{perl_vendorlib}/Dancer
%{perl_vendorlib}/Dancer.pm
%{perl_vendorlib}/Dancer/*
%dir %{perl_vendorlib}/HTTP
%dir %{perl_vendorlib}/HTTP/Tiny
%{perl_vendorlib}/HTTP/Tiny/NoProxy.pm
%{_mandir}/man1/dancer.1*
%{_mandir}/man3/Dancer.3*
%{_mandir}/man3/Dancer::*
%{_mandir}/man3/HTTP::Tiny::NoProxy*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
