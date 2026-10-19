%global source0_hash 19f8f2857558c1ae03de11401ac78179a703158dded267ed391ba90f392bda2a
Name:           perl-WWW-Search
Version:        2.519
Release:        1%{?dist}
Summary:        Virtual base class for WWW searches
License:        LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/WWW-Search
Source0:        https://cpan.metacpan.org/authors/id/M/MT/MTHURN/WWW-Search-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(LWP::Debug)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Bit::Vector)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Capture::Stderr)
BuildRequires:  perl(LWP::MemberMixin)
BuildRequires:  perl(LWP::RobotUA)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::File)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This class is the parent for all access methods supported by the WWW::Search
library. This library implements a Perl API to web-based search engines. See
README for a list of search engines currently supported, and for a lot of
interesting high-level information about this distribution. Search results can
be limited, and there is a pause between each request to avoid overloading
either the client or the server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Search-%{version}
# Remove bundled modules
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
