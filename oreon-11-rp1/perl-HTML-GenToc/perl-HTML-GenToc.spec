%global source0_hash 961f7e4127bc84de6fc6087f73af105083446a434b199b37bcf479269594a0c3
Name:           perl-HTML-GenToc
Version:        3.20
Release:        42%{?dist}
Summary:        Generate a Table of Contents for HTML documents
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/HTML-GenToc
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RUBYKAT/HTML-GenToc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Getopt::ArgvFile)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::LinkList)
BuildRequires:  perl(HTML::SimpleParse)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl-generators
# /oreon:deps
%description
HTML::GenToc generates anchors and a table of contents for HTML documents.
Depending on the arguments, it will insert the information it generates, or
output to a string, a separate file or STDOUT.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-GenToc-%{version}

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
