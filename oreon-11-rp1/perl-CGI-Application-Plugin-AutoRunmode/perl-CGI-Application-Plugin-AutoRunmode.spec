%global source0_hash 0185fa5ed3bc367bc85543f625ba8ec78d98eb4a77bc6f6bddb6801e5663f5dd

Name:           perl-CGI-Application-Plugin-AutoRunmode
Version:        0.18
Release:        42%{?dist}
Summary:        CGI::App plugin to automatically register runmodes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-AutoRunmode
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THILO/CGI-Application-Plugin-AutoRunmode-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(CGI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This plugin for CGI::Application provides easy ways to setup run modes. You
can just write the method that implement a run mode, you do not have to
explicitly register it with CGI::App anymore.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-AutoRunmode-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
