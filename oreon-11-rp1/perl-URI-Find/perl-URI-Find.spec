%global source0_hash e213a425a51b5f55324211f37909d78749d0bacdea259ba51a9855d0d19663d6

Name:           perl-URI-Find
Summary:        Find URIs in plain text
Version:        20160806
Release:        27%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/URI-Find-%{version}.tar.gz
URL:            https://metacpan.org/release/URI-Find
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build) >= 0.30
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(URI) >= 1.60
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 0.95
Requires:       perl(URI) >= 1.60
Obsoletes:      %{name}-tests < 20140709-5

%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(URI\\)$

Provides:       perl(URI::Find)
Provides:       perl(URI::Find)
%description
This module does one thing: Finds URIs and URLs in plain text. It finds
them quickly and it finds them *all* (or what URI::URL considers a URI to
be.) It only finds URIs which include a scheme (http:// or the like), for
something a bit less strict have a look at URI::Find::Schemeless.

For a command-line interface, see Darren Chamberlain's 'urifind' script.
It's available from his CPAN directory:

    http://www.cpan.org/authors/id/D/DA/DARREN/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n URI-Find-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README TODO
%{perl_vendorlib}/*
%{_bindir}/urifind
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
