%global source0_hash 486762e4cacddcc77b13989f979a029f84630b8175e7fef17989e157d4b6318a
%bcond_with perl_Unicode_LineBreak_enables_optional_test
Name:           perl-Unicode-LineBreak
Version:        2019.001
Release:        1%{?dist}
Summary:        UAX #14 Unicode Line Breaking Algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Unicode-LineBreak
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/Unicode-LineBreak-%{version}.tar.gz
%if %{with perl_Unicode_LineBreak_enables_optional_test}
%endif
Requires:       perl(Encode) >= 1.98
Requires:       perl(MIME::Charset) >= 1.006.2
Provides:       perl(Unicode::GCString)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libthai-devel
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(MIME::Charset)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  sombok-devel
# /oreon:deps
%description
Unicode::LineBreak performs Line Breaking Algorithm described in Unicode
Standards Annex #14 [UAX #14]. East_Asian_Width informative properties
defined by Annex #11 [UAX #11] will be concerned to determine breaking
positions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Unicode-LineBreak-%{version}
# Remove bundled library
rm -rf sombok
sed -i -e '/^sombok/d' MANIFEST

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man3
for mod in Text::LineFold Unicode::GCString Unicode::LineBreak; do
  mv $RPM_BUILD_ROOT%{_mandir}/man3/POD2::JA::$mod.3pm \
     $RPM_BUILD_ROOT%{_mandir}/ja/man3/$mod.3pm
done
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2019.001-26
- Prepare for Oreon 11 (RP1)
