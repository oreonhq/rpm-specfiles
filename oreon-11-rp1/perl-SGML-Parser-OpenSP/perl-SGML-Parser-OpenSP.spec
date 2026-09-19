%global source0_hash a7eb7ef74a9853d45296813cff608349e6a00c0fa8fe9c8f6ac3be58d636b3fe

Name:           perl-SGML-Parser-OpenSP
Version:        0.994
Release:        55%{?dist}
Summary:        Perl interface to the OpenSP SGML and XML parser

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SGML-Parser-OpenSP
Source0:        https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/SGML-Parser-OpenSP-%{version}.tar.gz
# Don't use deprecated uvuni_to_utf8_flags (CPAN RT#148488)
Patch0:         SGML-Parser-OpenSP-0.994-Stop-using-deprecated-uvuni_to_utf8_flags.patch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  opensp-devel
Requires:       perl(Class::Accessor)

%{?perl_default_filter}

%description
SGML::Parser::OpenSP provides a native Perl interface, written in C++
and XS, to the OpenSP SGML and XML parser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SGML-Parser-OpenSP-%{version}
%patch -P0 -p1
# POD Coverage is interesting for upstream, not us.
perl -pi -e 's|t/99podcov.t||' MANIFEST ; rm t/99podcov.t
find . -type f -print0 | xargs -0 chmod -c -x
perl -pi -e 's|\r||g' Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/SGML/
%{perl_vendorarch}/SGML/
%{_mandir}/man3/SGML::Parser::OpenSP*.3*

%changelog
%autochangelog
