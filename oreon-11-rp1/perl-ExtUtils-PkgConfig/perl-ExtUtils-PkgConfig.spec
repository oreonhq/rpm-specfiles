Name:           perl-ExtUtils-PkgConfig
Version:        1.16
Release:        28%{?dist}
Summary:        Simplistic interface to pkg-config
License:        LGPL-2.0-or-later
URL:            https://metacpan.org/release/ExtUtils-PkgConfig
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/ExtUtils-PkgConfig-1.16.tar.gz
# oreon url source checksums begin
%global source0_sha256 bbeaced995d7d8d10cfc51a3a5a66da41ceb2bc04fedcab50e10e6300e801c6e
%global source0_file ExtUtils-PkgConfig-1.16.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  pkgconfig
# Test Suite
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Dependencies
Requires:       pkgconfig

%description
The pkg-config program retrieves information about installed libraries,
usually for the purposes of compiling against and linking to them.

ExtUtils::PkgConfig is a very simplistic interface to this utility,
intended for use in the Makefile.PL of perl extensions that bind
libraries that pkg-config knows. It is really just boilerplate code
that you would've written yourself.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ExtUtils-PkgConfig-1.16.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bbeaced995d7d8d10cfc51a3a5a66da41ceb2bc04fedcab50e10e6300e801c6e" || { echo "oreon: Source0 SHA256 mismatch for ExtUtils-PkgConfig-1.16.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n ExtUtils-PkgConfig-%{version}

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
%doc Changes README
%{perl_vendorlib}/ExtUtils/
%{_mandir}/man3/ExtUtils::PkgConfig.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-28
- Prepare for Oreon 11 (RP1)
