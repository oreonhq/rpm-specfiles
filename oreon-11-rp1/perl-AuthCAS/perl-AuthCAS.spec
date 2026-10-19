%global source0_hash 2222eb876642939238e73d17f5421116173bf3fcbc4d3a8f9cc5520b0f2a2f57
Name:           perl-AuthCAS
Version:        1.7
Release:        1%{?dist}
Summary:        Client library for CAS 2.0 authentication server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AuthCAS
Source0:        https://cpan.metacpan.org/authors/id/O/OS/OSALAUN/AuthCAS-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
AuthCAS aims at providing a Perl API to Yale's Central Authentication
System (CAS). Only a basic Perl library is provided with CAS whereas
AuthCAS is a full object-oriented library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AuthCAS-%{version}
iconv -f iso8859-1 -t utf-8 README > README.utf8 && \
touch -r README README.utf8 && \
mv -f README.utf8 README

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
