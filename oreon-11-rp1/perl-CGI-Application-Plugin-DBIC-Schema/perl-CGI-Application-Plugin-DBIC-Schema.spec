%global source0_hash ac601ce4d19d1fad547e2b50909bea1a5cf8533537f48b8e6a57b55a1e0c93f5

Name:           perl-CGI-Application-Plugin-DBIC-Schema
Version:        0.3
Release:        46%{?dist}
Summary:        Easy DBIx::Class access from CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-DBIC-Schema
Source0:        https://cpan.metacpan.org/authors/id/V/VA/VANAMBURG/CGI-Application-Plugin-DBIC-Schema-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Pod)
Requires:       perl(CGI::Application)
Requires:       perl(DBIx::Class)

%{?perl_default_filter}

%description
CGI::Application::Plugin::DBIC::Schema adds easy access to a
DBIx::Class::Schema to your Titanium or CGI::Application modules. Lazy
loading is used to prevent a database connection from being made if the
schema method is not called during the request. In other words, the
database connection is not created until it is actually needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-DBIC-Schema-%{version}

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
