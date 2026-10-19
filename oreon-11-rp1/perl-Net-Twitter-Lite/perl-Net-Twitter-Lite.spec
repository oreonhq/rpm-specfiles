%global source0_hash b2eabe1f2a3f2c64decd60f27bc3b46ee652560b024c4c568115616c8d4a468e
Name:           perl-Net-Twitter-Lite
Version:        0.12008
Release:        1%{?dist}
Summary:        Perl interface to the Twitter API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Twitter-Lite
Source0:        https://cpan.metacpan.org/authors/id/M/MM/MMIMS/Net-Twitter-Lite-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(JSON) >= 2.02
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent) >= 5.82
Requires:       perl(Net::Netrc)
Requires:       perl(Net::OAuth) >= 0.25
Requires:       perl(Scalar::Util)
Requires:       perl(Storable)
Requires:       perl(URI) >= 1.40
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(JSON\\)$
%global __requires_exclude %__requires_exclude|^perl\\(LWP::UserAgent\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Net::OAuth\\)$
%global __requires_exclude %__requires_exclude|^perl\\(URI\\)$
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::DoubleEncodedUTF8)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::HTTP)
BuildRequires:  perl(Net::Netrc)
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(blib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a perl interface to the Twitter API v1.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Twitter-Lite-%{version}

%build

%{__perl} Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
