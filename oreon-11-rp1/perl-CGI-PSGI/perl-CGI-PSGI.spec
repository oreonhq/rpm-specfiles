%global source0_hash c50dcb10bf8486a9843baed032ad89d879ff2f41c993342dead62f947a598d91

Name:           perl-CGI-PSGI
Version:        0.15
Release:        42%{?dist}
Summary:        Enable your CGI.pm aware applications to adapt PSGI protocol
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-PSGI
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/CGI-PSGI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Repository)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(CGI)
BuildRequires:  perl(strict)
# Tests
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(CGI::Util)
BuildRequires:  perl(Config)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This module is for web application framework developers who currently uses
CGI to handle query parameters. You can switch to use CGI::PSGI instead of
CGI, to make your framework compatible to PSGI with a slight modification
of your framework adapter. The framework should already be collecting the
body content to print at one place, and not printing any content directly
to STDOUT.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-PSGI-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
