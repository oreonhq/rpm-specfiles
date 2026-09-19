%global source0_hash 103aab245304f08e9e87ac7bc884ddb44a630de6bac077dc921f716d71154922

Name:           perl-WebService-Linode
Version:        0.29
Release:        19%{?dist}
Summary:        Perl Interface to the Linode.com API
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Linode
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKEGRB/WebService-Linode-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(JSON) >= 2.00
BuildRequires:  perl(List::Util)
# Default URL has https schema
# LWP::Protocol::https not used at tests
BuildRequires:  perl(LWP::UserAgent)
# Tests:
# Test::Kwalitee 1.21 not used
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(JSON) >= 2.00
# Default URL has https schema
Requires:       perl(LWP::Protocol::https)

# Not to process documentation
%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(JSON\\)$

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

%check
unset AUTHOR_TESTING
unset RELEASE_TESTING
./Build test

%files
%doc Changes README examples/
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
