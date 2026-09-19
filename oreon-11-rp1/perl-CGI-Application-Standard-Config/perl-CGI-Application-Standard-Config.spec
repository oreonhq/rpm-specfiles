%global source0_hash 5c92c16051c2fad326469b5f0d3bf2a2b27ff0714604b506deab30f13c287159

Name:           perl-CGI-Application-Standard-Config
Version:        1.01
Release:        46%{?dist}
Summary:        Defines a standard configuration API for CGI::Application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Standard-Config
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/CGI-Application-Standard-Config-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
This module defines a minimum standard interface that configuration
plugins for CGI::Application should meet. Having such a standard allows
other plugin authors to rely on basic configuration functionality without
coding exceptions for several configuration modules, or giving up on such
integration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Standard-Config-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
