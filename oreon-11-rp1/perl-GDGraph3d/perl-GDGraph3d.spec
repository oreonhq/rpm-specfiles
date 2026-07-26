%global source0_hash d1784461b86f00f564d29c4926e409a0a2ed087e6154f7a14341d53c3bb55259

Name:           perl-GDGraph3d
Version:        0.63
Release:        58%{?dist}
Summary:        3D graph generation package for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/GD-Graph3d
Source0:        https://cpan.metacpan.org/authors/id/W/WA/WADG/GD-Graph3d-%{version}.tar.gz

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  %{__make}
BuildRequires:  %{__perl}
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(GD)
BuildRequires:  perl(GD::Graph)
BuildRequires:  perl(strict)
# Test Suite
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
# Runtime
Provides:       perl-GD-Graph3d = %{version}-%{release}

%description
This is the GD::Graph3d extensions module. It provides 3D graphs for
the GD::Graph module by Martien Verbruggen, which in turn generates
graph using Lincoln Stein's GD.pm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GD-Graph3d-%{version}
perl -pi -e 's/\r//g' Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/GD/
%{_mandir}/man3/GD::Graph3d.3*

%changelog
%autochangelog
