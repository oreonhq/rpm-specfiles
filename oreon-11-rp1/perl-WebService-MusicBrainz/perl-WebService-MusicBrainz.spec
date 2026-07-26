%global source0_hash eafc57f0fc3f0b3e2da3f5ad5b0fcc1554a7fbf87d72a05956d97455a2aebdbf

%global debug_package %{nil}

Name:           perl-WebService-MusicBrainz
Version:        1.0.10
Release:        %autorelease
Summary:        Perl interface to search the musicbrainz.org database
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-MusicBrainz
Source0:        https://cpan.metacpan.org/authors/id/B/BF/BFAIST/WebService-MusicBrainz-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Depends), perl(ExtUtils::PkgConfig)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-Mojolicious
Requires:       pkgconf-pkg-config
Requires:       perl-IO-Socket-SSL

%{?perl_default_filter}

%description
This module will search the MusicBrainz database through their web service and
return objects with the found data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WebService-MusicBrainz-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?_with_testsuite:make test}

%files
%doc Changes README.md
%{_mandir}/man3/WebService::MusicBrainz*.3pm*
%perl_vendorlib/WebService

%changelog
%autochangelog
