%global source0_hash 738281c777e4b0c9c0e26a78f910e88885bbc1c6ec93fefca65a77b6c4dccb1c

Name:           perl-MDV-Packdrakeng
Version:        1.13
Release:        41%{?dist}
Summary:        Simple Archive Extractor/Builder
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/MDV-Packdrakeng
Source0:        https://cpan.metacpan.org/authors/id/N/NA/NANARDON/MDV-Packdrakeng-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(POSIX)
# Tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Test::More)

%description
MDV::Packdrakeng is a simple indexed archive builder and extractor using
standard compression methods.

%{?perl_default_filter}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MDV-Packdrakeng-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/MDV*
%{_mandir}/man3/MDV::Packdrakeng*

%changelog
%autochangelog
