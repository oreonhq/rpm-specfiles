%global source0_hash ec97aed8f0165d0f55503384181d632f3af5c857f8707f94572627b4159fdb71

Name:           perl-CGI-Application-Plugin-DBIProfile
Version:        0.07
Release:        45%{?dist}
Summary:        DBI profiling plugin
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-DBIProfile
Source0:        https://cpan.metacpan.org/authors/id/U/UN/UNRTST/CGI-Application-Plugin-DBIProfile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(Data::JavaScript)
BuildRequires:  perl(DBI)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)

%{?perl_default_filter}

%description
CGI::Application::Plugin::DBIProfile provides popup (using CAP::DevPopup if
available) holding DBI Profile information (see DBI::Profile,
DBI::ProfileDumper). It will output both graphed output and a
DBI::ProfileDumper report.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-DBIProfile-%{version}

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
