%global source0_hash f0e2ffff12594331712405bafe35111075093d35c13553f1b738fdf5799e5721

Name:           perl-CGI-Application-Plugin-JSON
Version:        1.02
Release:        44%{?dist}
Summary:        Easy manipulation of JSON headers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-Plugin-JSON
Source0:        https://cpan.metacpan.org/authors/id/W/WO/WONKO/CGI-Application-Plugin-JSON-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Application) >= 4
BuildRequires:  perl(JSON) >= 2.02
BuildRequires:  perl(JSON::Any) >= 1.14
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(CGI::Application)

%{?perl_default_filter}

%description
When communicating with client-side JavaScript, it is common to send data
in X-JSON HTTP headers or through the document body as content-type
application/json. This CGI::Application plugin adds a couple of convenience
methods to make that just a little bit easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-Plugin-JSON-%{version}

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
