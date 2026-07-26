%global source0_hash 542da542fa36bb3fdd7b8776e230d3ccc02aa6744ce9b77b4eef4ccae7c04adf

Name:           perl-PerlIO-Layers
Version:        0.012
Release:        21%{?dist}
Summary:        Querying your file handle capabilities
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlIO-Layers
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/PerlIO-Layers-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(List::Util)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More) >= 0.82

%{?perl_default_filter}

%description
Perl file handles are implemented as a stack of layers, with the bottom-most
usually doing the actual IO and the higher ones doing buffering,
encoding/decoding or transformations. PerlIO::Layers allows you to query the
file handle properties concerning these layers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PerlIO-Layers-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PerlIO*
%{_mandir}/man3/*

%changelog
%autochangelog
