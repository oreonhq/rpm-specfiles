%global source0_hash 1eabe1e44f112578c19cb1e0dfbc2746c9ed6fde70745da57680708667db77d7

Name:           perl-Catalyst-View-HTML-Template
Version:        0.03
Release:        43%{?dist}
Summary:        HTML::Template View Class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Catalyst-View-HTML-Template
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRAMBERG/Catalyst-View-HTML-Template-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst) >= 5.7
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%if 0%{?fedora} < 15
Requires:       perl(Catalyst::View)
%endif

%{?perl_default_filter}

%description
This is the HTML::Template view class. Your subclass should inherit from
this class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-View-HTML-Template-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=yep ./Build test

%files
%doc Changes README
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
%autochangelog
