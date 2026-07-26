%global source0_hash f15a9df92c282419f7010964aca1ada844ddfae7afc735cd2ba1bb20883e955c

Name:           perl-HTML-Entities-Interpolate
Version:        1.10
Release:        28%{?dist}
Summary:        Call HTML::Entities::encode_entities via a hash within a string
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Entities-Interpolate
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/HTML-Entities-Interpolate-%{version}.tgz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Function)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This is a pure perl module which calls HTML::Entities::encode_entities 
via a hash within a string.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Entities-Interpolate-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/HTML*
%{_mandir}/man3/HTML*

%changelog
%autochangelog
