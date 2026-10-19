%global source0_hash ad6610a9d0f2cd8914dc6ef40c39421bcdb19a7334390c5cefa743edf0bedc5a
Name:           perl-WebService-Dropbox
Version:        2.10
Release:        2%{?dist}
Summary:        Perl interface to Dropbox API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Dropbox
Source0:        https://cpan.metacpan.org/authors/id/A/AS/ASKADNA/WebService-Dropbox-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(IO::Socket::SSL) >= 2.048
Requires:       perl(HTTP::Message) >= 6.11
Requires:       perl(JSON) >= 2.94
Requires:       perl(LWP::Protocol::https) >= 6.07
Requires:       perl(LWP::UserAgent) >= 6.26
Requires:       perl(Net::OAuth) >= 0.28
Requires:       perl(Software::License)
Requires:       perl(URI) >= 1.71
Requires:       perl(HTTP::Request)
Obsoletes:      perl-Net-Dropbox-API <= 1.9
# oreon:deps
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Message)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Spellunker)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
