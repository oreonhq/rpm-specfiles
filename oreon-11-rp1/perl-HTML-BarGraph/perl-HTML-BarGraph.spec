%global source0_hash eab638488417fe571c3b2e865378002c627b0bb224bd4bd184419a55c6c751c3
Name:           perl-HTML-BarGraph
Version:        0.5
Release:        1%{?dist}
Summary:        Generate multiset bar graphs using plain HTML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-BarGraph
Source0:        https://cpan.metacpan.org/authors/id/P/PO/PODGURSV/HTML-BarGraph-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-generators
# /oreon:deps
%description
HTML::BarGraph is a module that creates graphics for one or more data-sets,
using plain HTML and, optionally, one-pixel images, which are stretched
using the width and height attributes of the HTML img tag.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-BarGraph-%{version}
chmod -x BarGraph.pm

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp sample.html $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -r pixels $RPM_BUILD_ROOT/%{_datadir}/%{name}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
