%global source0_hash 65b978ebf3c3985e55ee32bb6da1e9faea494a85d3005c63baec7e969859f026

Name:           perl-CSS-DOM
Version:        0.17
Release:        25%{?dist}
Summary:        Document Object Model for Cascading Style Sheets

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CSS-DOM
Source0:        https://cpan.metacpan.org/authors/id/S/SP/SPROUT/CSS-DOM-%{version}.tar.gz
# Remove apostrophe as package separator - it is deprecated in 5.37.9 and
# will be removed by 5.40. CPAN RT#146661
Patch0:         CSS-DOM-0.17-Dont-use-deprecated-code.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(Carp) >= 1.01
BuildRequires:  perl(Clone) >= 0.09
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode) >= 2.10
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Dependencies not detected automatically:
Requires:       perl(Clone) >= 0.09
Requires:       perl(Encode) >= 2.10

%{?perl_default_filter}

%description
This set of modules provides the CSS-specific interfaces described in
the W3C DOM recommendation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CSS-DOM-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/CSS/
%{_mandir}/man3/CSS::DOM*.3*

%changelog
%autochangelog
