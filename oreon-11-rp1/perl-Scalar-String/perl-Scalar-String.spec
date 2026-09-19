%global source0_hash f54a17c9b78713b02cc43adfadf60b49467e7634d31317e8b9e9e97c26d68b52

Name:           perl-Scalar-String
Version:        0.003
Release:        29%{?dist}
Summary:        String aspects of scalars
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Scalar-String
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Scalar-String-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(if)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
Requires:       perl(Carp)
Requires:       perl(XSLoader)

%description
This module is about the string part of plain Perl scalars. A scalar has a
string value, which is notionally a sequence of Unicode codepoints, but
may be internally encoded in either ISO-8859-1 or UTF-8. In places, and
more so in older versions of Perl, the internal encoding shows through. To
fully understand Perl strings it is necessary to understand these
implementation details.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Scalar-String-%{version}

%build
%{__perl} Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Scalar*
%{_mandir}/man3/*

%changelog
%autochangelog
