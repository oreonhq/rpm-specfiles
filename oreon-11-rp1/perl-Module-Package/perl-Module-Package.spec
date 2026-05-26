Name:           perl-Module-Package
Version:        0.30
Release:        39%{?dist}
Summary:        Postmodern Perl Module Packaging
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Package
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Module-Package-%{version}.tar.gz
# Fix building on Perl without "." in @INC, CPAN RT#121748
Patch0:         Module-Package-0.30-Fix-building-on-Perl-without-.-in-INC.patch
# oreon url source checksums begin
%global source0_sha256 7c3c89e779baa83afaf0dc9599c20f90b3e613ea3ece0328931257ab7cc24a99
%global source0_file Module-Package-0.30.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::All) >= 0.41
BuildRequires:  perl(Module::Install) >= 1.01
BuildRequires:  perl(Module::Install::AuthorRequires) >= 0.02
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(Module::Install::ManifestSkip) >= 0.19
BuildRequires:  perl(Moo) >= 0.009008
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(Data::Dumper)
Requires:       perl(File::Path)

%description
This module is a drop-in replacement for Module::Install. It does everything
Module::Install does, but just a bit better.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Module-Package-0.30.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7c3c89e779baa83afaf0dc9599c20f90b3e613ea3ece0328931257ab7cc24a99" || { echo "oreon: Source0 SHA256 mismatch for Module-Package-0.30.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Module-Package-%{version}
%patch -P0 -p1
# XXX: Do not unbundle ./inc/ because of bootstrap

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.30-39
- Prepare for Oreon 11 (RP1)
