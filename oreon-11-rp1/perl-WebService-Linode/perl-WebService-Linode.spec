%global source0_hash 103aab245304f08e9e87ac7bc884ddb44a630de6bac077dc921f716d71154922
Name:           perl-WebService-Linode
Version:        0.29
Release:        1%{?dist}
Summary:        Perl Interface to the Linode.com API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Linode
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKEGRB/WebService-Linode-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(JSON) >= 2.00
Requires:       perl(LWP::Protocol::https)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(JSON\\)$
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements the Linode.com API methods. Linode methods have had
dots replaced with underscores to generate the perl method name. All keys 
and parameters have been lower cased but returned data remains otherwise 
the same. For additional information see <http://www.linode.com/api/>.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn WebService-Linode-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
unset RELEASE_TESTING
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
