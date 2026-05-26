Name:           perl-Devel-Leak
Version:        0.03
Release:        61%{?dist}
Summary:        Utility for looking for perl objects that are not reclaimed
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Leak
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NI-S/Devel-Leak-0.03.tar.gz
# oreon url source checksums begin
%global source0_sha256 6f42c34f11e2b4e3ea2e0e6b9416a88a685add447910caf4d91dd2c178177252
%global source0_file Devel-Leak-0.03.tar.gz
# oreon url source checksums end

# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test)
# Deps:
# (none)

%{?perl_default_filter}

%description
This module provides a basic way to discover if a piece of perl code
is allocating perl data and not releasing them again.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Devel-Leak-0.03.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6f42c34f11e2b4e3ea2e0e6b9416a88a685add447910caf4d91dd2c178177252" || { echo "oreon: Source0 SHA256 mismatch for Devel-Leak-0.03.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Devel-Leak-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc README
%{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/Devel/
%{_mandir}/man3/Devel::Leak.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.03-61
- Prepare for Oreon 11 (RP1)
