Name:           perl-PerlIO-utf8_strict
Version:        0.010
Release:        12%{?dist}
Summary:        Fast and correct UTF-8 I/O
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlIO-utf8_strict
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/PerlIO-utf8_strict-0.010.tar.gz
# oreon url source checksums begin
%global source0_sha256 bcd2848b72df290b5e984fae8b1a6ca96f6d072003cf222389a8c9e8e1c570cd
%global source0_file PerlIO-utf8_strict-0.010.tar.gz
# oreon url source checksums end

# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Dependencies

%{?perl_default_filter}

%description
This module provides a fast and correct UTF-8 PerlIO layer. Unlike perl's
default :utf8 layer it checks the input for correctness.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/PerlIO-utf8_strict-0.010.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bcd2848b72df290b5e984fae8b1a6ca96f6d072003cf222389a8c9e8e1c570cd" || { echo "oreon: Source0 SHA256 mismatch for PerlIO-utf8_strict-0.010.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n PerlIO-utf8_strict-%{version}

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
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/PerlIO/
%{perl_vendorarch}/PerlIO/
%{_mandir}/man3/PerlIO::utf8_strict.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.010-12
- Prepare for Oreon 11 (RP1)
