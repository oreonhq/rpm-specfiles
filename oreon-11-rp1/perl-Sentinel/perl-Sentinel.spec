%global source0_hash 3649795b34ffd3b539d6d3e01216d5aaac3413b17f9cc813df47229c595f68a4

Name:           perl-Sentinel
Version:        0.07
Release:        9%{?dist}
Summary:        Create lightweight SCALARs with get/set callbacks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Sentinel
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Sentinel-%{version}.tar.gz

# build requirements
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Syntax::Keyword::Dynamically)
BuildRequires:  perl(Test2::V0) >= 0.000148

Requires:       perl(XSLoader)

%{?perl_default_filter}

Provides:       perl(Sentinel)
%description
This module provides a single lvalue function, sentinel, which yields a
scalar that invoke callbacks to get or set its value. Primarily this is
useful to create lvalue object accessors or other functions, to invoke
actual code when a new value is set, rather than simply updating a
scalar variable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sentinel-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/Sentinel
%{perl_vendorarch}/Sentinel*
%{_mandir}/man3/Sentinel*

%changelog
%autochangelog
