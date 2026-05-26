Name:           perl-Text-VCardFast
Version:        0.11
Release:        32%{?dist}
Summary:        Perl extension for very fast parsing of VCards
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-VCardFast
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Text-VCardFast-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 05ba5c43f88dd4e08137db872d16a01f6be5efd1fb470b3f2069da88410fea46
%global source0_file Text-VCardFast-0.11.tar.gz
# oreon url source checksums end
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.14.2
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Test::More)

%description
Text::VCardFast is designed to parse VCards very quickly compared to pure-Perl
solutions. It has a Perl and an XS version of the same API, accessible
as vcard2hash_pp and vcard2hash_c, with the XS version being preferred.

%package tests
BuildArch:      noarch
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Text-VCardFast-0.11.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "05ba5c43f88dd4e08137db872d16a01f6be5efd1fb470b3f2069da88410fea46" || { echo "oreon: Source0 SHA256 mismatch for Text-VCardFast-0.11.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Text-VCardFast-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/Cases.t writes to CWD/cases/
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11-32
- Prepare for Oreon 11 (RP1)
