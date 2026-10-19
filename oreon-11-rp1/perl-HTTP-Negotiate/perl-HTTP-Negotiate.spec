%global source0_hash 1c729c1ea63100e878405cda7d66f9adfd3ed4f1d6cacaca0ee9152df728e016
Name:           perl-HTTP-Negotiate
Version:        6.01
Release:        1%{?dist}
Summary:        Choose a variant to serve
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Negotiate
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/HTTP-Negotiate-%{version}.tar.gz
Patch0:         0001-Fix-warning-in-test.patch
BuildArch:      noarch
Requires:       perl(HTTP::Headers) >= 6
Conflicts:      perl-libwww-perl < 6
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(HTTP::Headers\\)$
Provides:       perl(HTTP::Negotiate)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a complete implementation of the HTTP content
negotiation algorithm specified in draft-ietf-http-v11-spec-00.ps chapter
12. Content negotiation allows for the selection of a preferred content
representation based upon attributes of the negotiable variants and the
value of the various Accept* header fields in the request.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n HTTP-Negotiate-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-HTTP-Negotiate-tests -f %{oreon_filedir}/perl-HTTP-Negotiate-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.01-42
- Prepare for Oreon 11 (RP1)
