%global source0_hash 463ac6a969c0f7a9c546034eda963a63d11d344744113fafdd057d86b5222b89

Name:           perl-CGI-Application
Version:        4.61
Release:        24%{?dist}
Summary:        Framework for building reusable web-applications
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARTO/CGI-Application-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::PSGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
Requires:       perl(CGI)
Requires:       perl(HTML::Template)

%{?perl_default_filter}

%description
CGI::Application is an Object-Oriented Perl module which implements an
Abstract Class. It is not intended that this package be instantiated
directly. Instead, it is intended that your Application Module will be
implemented as a Sub-Class of CGI::Application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc ARTISTIC Changes GPL README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
