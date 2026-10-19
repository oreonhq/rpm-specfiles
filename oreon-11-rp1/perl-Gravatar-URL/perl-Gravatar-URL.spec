%global source0_hash 23cabdaefbdc9c3de3f0552bb45005ce0add18bc4723a743ebf32cddc169b6d7
Name:           perl-Gravatar-URL
Version:        1.07
Release:        27%{?dist}
Summary:        Make URLs for Gravatars from an email address
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gravatar-URL
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/Gravatar-URL-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Net::DNS) >= 1.01
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Test::MockRandom)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A Gravatar is a Globally Recognized Avatar for a given email address. This
allows you to have a global picture associated with your email address. You
can look up the Gravatar for any email address by constructing a URL to get
the image from gravatar.com. This module does that.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gravatar-URL-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
