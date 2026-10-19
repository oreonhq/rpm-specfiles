%global source0_hash fb18801bf6473231199bb9e81f56ce945c4b93c68b05ed17049a8885b9e211f7
Name:           perl-CGI-Ajax
Version:        0.707
Release:        1%{?dist}
Summary:        Perl-specific system for writing Asynchronous web applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl 
URL:            https://metacpan.org/release/CGI-Ajax
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPEDERSE/CGI-Ajax-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CGI), perl(Class::Accessor)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl-generators
# /oreon:deps
%description
CGI::Ajax is an object-oriented module that provides a unique mechanism for
using perl code asynchronously from javascript- enhanced HTML pages.
CGI::Ajax unburdens the user from having to write extensive javascript,
except for associating an exported method with a document-defined event
(such as onClick, onKeyUp, etc). CGI::Ajax also mixes well with HTML
containing more complex javascript.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Ajax-%{version}

find scripts/ -type f -exec chmod -c -x {} + 

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
