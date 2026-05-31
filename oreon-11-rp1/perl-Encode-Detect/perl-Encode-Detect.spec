%global source0_hash 834d893aa7db6ce3f158afbd0e432d6ed15a276e0940db0a74be13fd9c4bbbf1

Name: perl-Encode-Detect
Version: 1.01
Release: 52%{?dist}
Summary: Encode::Encoding subclass that detects the encoding of data

License: MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.0-or-later
URL: https://metacpan.org/release/Encode-Detect
Source0:        https://cpan.metacpan.org/authors/id/J/JG/JGMYERS/Encode-Detect-%{version}.tar.gz

BuildRequires: coreutils
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
# Run-time
BuildRequires: perl(base)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Encode)
BuildRequires: perl(Encode::Encoding)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Tests
BuildRequires: perl(Test::More)

%description
This Perl module is an Encode::Encoding subclass that uses
Encode::Detect::Detector to determine the charset of the input data and then
decodes it using the encoder of the detected charset.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Encode-Detect-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="${RPM_OPT_FLAGS}"
./Build

%check
./Build test

%install
./Build install destdir="${RPM_BUILD_ROOT}" create_packlist=0
find "${RPM_BUILD_ROOT}" -type f -name "*.bs" -empty -delete
%{_fixperms} "${RPM_BUILD_ROOT}"/*

%files
%doc Changes LICENSE
%{perl_vendorarch}/auto/Encode
%{perl_vendorarch}/Encode
%{_mandir}/man3/Encode::Detect.3*
%{_mandir}/man3/Encode::Detect::Detector.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.01-52
- Prepare for Oreon 11 (RP1)
