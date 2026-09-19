%global source0_hash ad6610a9d0f2cd8914dc6ef40c39421bcdb19a7334390c5cefa743edf0bedc5a

Name:           perl-WebService-Dropbox
Version:        2.10
Release:        2%{?dist}
Summary:        Perl interface to Dropbox API
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Dropbox
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASKADNA/WebService-Dropbox-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# for running Build.PL
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(utf8)

# Furl is optional, not yet available in Fedora
#BuildRequires:  perl(Furl) >= 3.11
BuildRequires:  perl(IO::Socket::SSL) >= 2.048
BuildRequires:  perl(HTTP::Message) >= 6.11
BuildRequires:  perl(JSON) >= 2.94
# optional
#BuildRequires:  perl(JSON::XS) >= 3.03
BuildRequires:  perl(LWP::Protocol::https) >= 6.07
BuildRequires:  perl(LWP::UserAgent) >= 6.26
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Net::OAuth) >= 0.28
BuildRequires:  perl(Software::License)
BuildRequires:  perl(URI) >= 1.71
# for tests
BuildRequires:  perl(Test::More) >= 1.302085
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::CPAN::Meta)
# not yet available in Fedora
#BuildRequires:  perl(Test::MinimumVersion::Fast) >= 0.04
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Spellunker) >= 0.2.7

# optional package, not yet available in Fedora
#Requires:       perl(Furl) >= 3.11
Requires:       perl(IO::Socket::SSL) >= 2.048
Requires:       perl(HTTP::Message) >= 6.11
Requires:       perl(JSON) >= 2.94
# optional
#Requires:       perl(JSON::XS) >= 3.03
Requires:       perl(LWP::Protocol::https) >= 6.07
Requires:       perl(LWP::UserAgent) >= 6.26
Requires:       perl(Net::OAuth) >= 0.28
Requires:       perl(Software::License)
Requires:       perl(URI) >= 1.71
Requires:       perl(HTTP::Request)
Obsoletes:      perl-Net-Dropbox-API <= 1.9

%description
This package provides a Perl interface to Dropbox API with following features:
- Support Dropbox v1 REST API
- Support Furl (Fast!!!)
- Streaming IO (Low Memory)
- Default URI Escape (The specified path is UTF-8 decoded string)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WebService-Dropbox-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md example HOW_TO_DEVELOPMENT.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
