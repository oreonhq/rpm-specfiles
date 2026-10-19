%global source0_hash 41df66389afab8644bcbc33b11391f3e0e778664e422a63cd63c813529653734
Name:           perl-CGI-Application-FastCGI
Version:        0.02
Release:        1%{?dist}
Summary:        For using CGI::Application under FastCGI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Application-FastCGI
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NAOYA/CGI-Application-FastCGI-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CGI::Application)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
%description
Inherit this module instead of CGI::Application if you want to run your cgi
programs based on CGI::Application under FastCGI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Application-FastCGI-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
