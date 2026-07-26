%global source0_hash 646cc78db159de64f20c9afc4876fd2b18a78d12156c1aa1793aac8f5d989f4c

Name:       perl-HTML-LinkList 
Version:    0.1701
Release:    32%{?dist}
# lib/HTML/LinkList.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl 

Summary:    Create a 'smart' list of HTML links
Source:     https://cpan.metacpan.org/authors/id/R/RU/RUBYKAT/HTML-LinkList-%{version}.tar.gz 
Url:        https://metacpan.org/release/HTML-LinkList

BuildArch:     noarch
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Pod::Coverage::TrustPod)
BuildRequires: perl(Test::CPAN::Meta)
BuildRequires: perl(Test::HasVersion)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
BuildRequires: perl(Test::Portability::Files)
BuildRequires: perl(blib)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)

%{?perl_default_filter}

%description
This module contains a number of functions for taking sets of URLs and
labels and creating suitably formatted HTML. These links are "smart"
because, if given the url of the current page, if any of the links in
the list equal it, that item in the list will be formatted as a special
label, not as a link; this is a Good Thing, since the user would be
confused by clicking on a link back to the current page. While many
website systems have plugins for "smart" navbars, they are specialized
for that system only, and can't be reused elsewhere, forcing people to
reinvent the wheel. I hereby present one wheel, free to be reused by
anybody; just the simple functions, a backend, which can be plugged into
whatever system you want.The default format for the HTML is to make an
unordered list, but there are many options, enabling one to have a
flatter layout with any separators you desire, or a more complicated
list with differing formats for different levels.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-LinkList-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 ./Build test

%files
%doc Changes OldChanges README README.mkdn
%license LICENSE
%{perl_vendorlib}/HTML*
%{_mandir}/man3/HTML*

%changelog
%autochangelog
