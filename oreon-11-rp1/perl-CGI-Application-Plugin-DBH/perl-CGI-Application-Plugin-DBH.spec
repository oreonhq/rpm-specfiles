%global source0_hash 77f3c9c4b555e412fcaa53f133f4aa60e5a4101ed8188d42f186be5cb899467e

Name:           perl-CGI-Application-Plugin-DBH
Version:        4.04
Release:        34%{?dist}
Summary:        Easy DBI access from CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-Plugin-DBH
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/CGI-Application-Plugin-DBH-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(DBD::Mock) >= 0.11
BuildRequires:  perl(DBI)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::MockObject) >= 1.20120301
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(CGI)

%{?perl_default_filter}

%description
CGI::Application::Plugin::DBH adds easy access to a DBI database handle to
your CGI::Application modules. Lazy loading is used to prevent a database
connection from being made if the dbh method is not called during the
request. In other words, the database connection is not created until it is
actually needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-DBH-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

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
