%global source0_hash 57c013ac065f4d011b871385b366ceadec590d08e183219bf7189c148fcb513d

Name:           perl-Pod-PseudoPod
Version:        0.19
Release:        19%{?dist}
Summary:        Framework for extending the POD tags for book manuscripts
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-PseudoPod
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Pod-PseudoPod-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Simple) >= 3.02
BuildRequires:  perl(Test::More)
Requires:       perl(Pod::Simple) >= 3.02

%description
PseudoPod is an extended set of Pod tags used for book manuscripts.
Standard Pod doesn't have all the markup options you need to mark up files
for publishing production. PseudoPod adds a few extra tags for footnotes,
tables, sidebars, etc. For further information see Pod::PseudoPod::Tutorial.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-PseudoPod-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
%{__rm} -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

# Added to remove the waring messages from rpmlint
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes LICENSE README Todo
%{perl_vendorlib}/Pod/PseudoPod.pm
%{perl_vendorlib}/Pod/PseudoPod
%{_mandir}/man3/*
%{_bindir}/ppod2docbook
%{_bindir}/ppod2txt
%{_bindir}/ppodchecker
%{_bindir}/ppod2html

%changelog
%autochangelog
