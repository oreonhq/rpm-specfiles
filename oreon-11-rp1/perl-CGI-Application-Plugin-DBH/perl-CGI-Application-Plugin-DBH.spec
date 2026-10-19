%global source0_hash 77f3c9c4b555e412fcaa53f133f4aa60e5a4101ed8188d42f186be5cb899467e
Name:           perl-CGI-Application-Plugin-DBH
Version:        4.04
Release:        1%{?dist}
Summary:        Easy DBI access from CGI::Application
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-DBH
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/CGI-Application-Plugin-DBH-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(DBD::Mock)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
