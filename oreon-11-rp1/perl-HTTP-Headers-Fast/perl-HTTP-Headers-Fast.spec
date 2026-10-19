%global source0_hash cc431db68496dd884db4bc0c0b7112c1f4a4f1dc68c4f5a3caa757a1e7481b48
Name:           perl-HTTP-Headers-Fast
Version:        0.22
Release:        1%{?dist}
Summary:        Faster implementation of HTTP::Headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Headers-Fast
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTTP-Headers-Fast-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(HTTP::Date)
Requires:       perl(MIME::Base64)
Requires:       perl(Storable)
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(URI)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
HTTP::Headers::Fast is a perl class for parsing/writing HTTP headers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Headers-Fast-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
