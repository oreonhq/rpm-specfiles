# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Sub_Install_enables_optional_test
%else
%bcond_with perl_Sub_Install_enables_optional_test
%endif

Name:           perl-Sub-Install
Version:        0.929
Release:        9%{?dist}
Summary:        Install subroutines into packages easily
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Install
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Install-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 80b1e281d8cd3b2b31dac711f5c8a1657a87cd80bbe69af3924bcbeb4e5db077
%global source0_file Sub-Install-0.929.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# ================= Module Build ============================
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# ================= Run-time ================================
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
# ================= Test Suite ==============================
BuildRequires:  perl(Test::More) >= 0.88
%if %{with perl_Sub_Install_enables_optional_test} && !%{defined perl_bootstrap}
# ================= Optional Tests ==========================
# Test::Output -> Sub::Exporter -> Sub::Install
BuildRequires:  perl(Test::Output)
%endif
# ================= Run-time ================================
Requires:       perl(B)

%description
This module makes it easy to install subroutines into packages without the
unsightly mess of no strict or typeglobs lying about where just anyone
can see them.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Sub-Install-0.929.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "80b1e281d8cd3b2b31dac711f5c8a1657a87cd80bbe69af3924bcbeb4e5db077" || { echo "oreon: Source0 SHA256 mismatch for Sub-Install-0.929.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Sub-Install-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Sub/
%{_mandir}/man3/Sub::Install.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.929-9
- Prepare for Oreon 11 (RP1)
