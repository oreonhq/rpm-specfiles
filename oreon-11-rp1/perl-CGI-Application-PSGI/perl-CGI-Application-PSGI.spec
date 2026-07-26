%global source0_hash 8870e2f7e9cee2fe19c1402cb26a2b8d82d3c75339dba2992868f2d0bac7d601

Name:           perl-CGI-Application-PSGI
Version:        1.00
Release:        46%{?dist}
Summary:        PSGI Adapter for CGI::Application
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Application-PSGI
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/CGI-Application-PSGI-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter >= 1:5.8.1
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(CGI::PSGI)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Include)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Install::TestBase)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(warnings)
BuildRequires:  sed

%{?perl_default_filter}

%description
CGI::Application::PSGI is a runner to run CGI::Application application as a
PSGI application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-PSGI-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete
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
