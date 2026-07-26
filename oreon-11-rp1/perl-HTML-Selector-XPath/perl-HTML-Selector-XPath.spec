%global source0_hash 432717f03ed2cf3d641130cfd3d4a153f09ad4f856da007813792fe0b2e58d0f

Name:           perl-HTML-Selector-XPath
Version:        0.28
Release:        7%{?dist}
Summary:        CSS Selector to XPath compiler
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Selector-XPath
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/HTML-Selector-XPath-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter >= 1:5.8.1
BuildRequires:  perl-generators

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::More)

BuildRequires:  perl(inc::Module::Install)

# for improved tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(HTML::TreeBuilder::XPath)
BuildRequires:  perl(Test::Pod) >= 1.00

%description
HTML::Selector::XPath is a utility function to compile CSS2 selector to the
equivalent XPath expression.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Selector-XPath-%{version}
rm -r inc
sed -i -e '/^inc\/.*$/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
