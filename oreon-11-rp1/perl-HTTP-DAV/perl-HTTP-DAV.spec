%global source0_hash aaf315027c26904b86c628d322fe2d65d5a777d45efb696a9ad0a43c60b79828
Name:           perl-HTTP-DAV
Version:        0.50
Release:        1%{?dist}
Summary:        WebDAV client library for Perl5
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-DAV
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COSIMO/HTTP-DAV-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(HTTP::Headers)
Requires:       perl(LWP) >= 5.48
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(LWP\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(LWP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(XML::DOM)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTTP::DAV is a Perl API for interacting with and modifying content on
web servers using the WebDAV protocol. Now you can LOCK, DELETE and PUT
files and much more on a DAV-enabled web server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-DAV-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

PERLDAV_TEST=default make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
