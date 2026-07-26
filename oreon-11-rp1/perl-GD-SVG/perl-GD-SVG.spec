%global source0_hash aee397906a94cf6a478defff9f4939dbf8293a62ee382360c77e3e209170012b

Name:           perl-GD-SVG
Version:        0.33
Release:        45%{?dist}
Summary:        GD::SVG enables SVG output from scripts written using GD

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GD-SVG
Source0:        https://cpan.metacpan.org/authors/id/T/TW/TWH/GD-SVG-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(GD::Polygon)
BuildRequires:  perl(SVG)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test::More)

%description
GD::SVG seamlessly enables the scalable vector graphics (SVG) output
from scripts written using GD.  It accomplishes this by translating GD
functions into SVG functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GD-SVG-%{version}

# avoid extra dependencies
chmod 644 examples/generate_test_image.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags} 

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README Changes examples
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
