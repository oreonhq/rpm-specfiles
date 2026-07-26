%global source0_hash 02769df0ec74deace9b4f07e5a596c110830872dff162af1452b633c1332fda9

Name:           perl-Search-Elasticsearch
Version:        8.12
Release:        5%{?dist}
Summary:        Official client for Elasticsearch
License:        Apache-2.0

URL:            https://metacpan.org/release/Search-Elasticsearch
Source0:        https://cpan.metacpan.org/authors/id/E/EZ/EZIMUEL/Search-Elasticsearch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Any::URI::Escape)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hijk)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::Callback)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape::XS)
BuildRequires:  perl(warnings)
Requires:       perl(IO::Socket::SSL)
Requires:       perl(IO::Uncompress::Inflate)
Requires:       perl(JSON::XS)
Requires:       perl(MIME::Base64)
Requires:       perl(URI::Escape::XS)

%{?perl_default_filter}

%description
Search::Elasticsearch is the official Perl client for Elasticsearch,
supported by elasticsearch.com. Elasticsearch itself is a flexible and
powerful open source, distributed real-time search and analytics engine for
the cloud. You can read more about it on elasticsearch.org.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Search-Elasticsearch-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Search*
%{_mandir}/man3/Search*

%changelog
%autochangelog
