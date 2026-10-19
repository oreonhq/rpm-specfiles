%global source0_hash 55cd8f68ffc0899cc5d265b4f4573c88c435a2620fd85993d25f5f81bfa169d7
%global cpan_version 1.03
Name:           perl-XML-Catalog
Version:        %(echo '%{cpan_version}' | tr -d 'v')
Release:        1%{?dist}
Summary:        Resolve public identifiers and remap system identifiers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Catalog
Source0:        https://cpan.metacpan.org/authors/id/J/JF/JFEARN/XML-Catalog-1.03.tar.gz
Patch:          XML-Catalog-1.03-Adapt-to-changes-in-XML-Parser-2.48.patch
BuildArch:      noarch
Provides:       perl(XML::Catalog)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements draft 0.4 of John Cowan's XML Catalog (formerly
known as XCatalog) see
(<https://www.oasis-open.org/committees/entity/specs/cs-entity-xml-catalogs-1.0.html>)
Catalogs may be written in either SOCAT or XML syntax. XML::Catalog will
assume SOCAT syntax if the catalog is not in well-formed XML syntax.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n XML-Catalog-%{cpan_version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

for i in Changes README; do
    perl -pi -e 's/\r//' $i
done
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-Catalog-tests -f %{oreon_filedir}/perl-XML-Catalog-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.03-35
- Import
