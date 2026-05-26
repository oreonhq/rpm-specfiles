Name:           perl-Canary-Stability
Version:        2013
Release:        22%{?dist}
Summary:        Canary to check perl compatibility for Schmorp's modules
# See COPYING file.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Canary-Stability
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Canary-Stability-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 a5c91c62cf95fcb868f60eab5c832908f6905221013fea2bce3ff57046d7b6ea
%global source0_file Canary-Stability-2013.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
Requires:       perl(ExtUtils::MakeMaker)

%description
This module is used by Schmorp's modules during configuration stage to test
the installed perl for compatibility with his modules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Canary-Stability-2013.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a5c91c62cf95fcb868f60eab5c832908f6905221013fea2bce3ff57046d7b6ea" || { echo "oreon: Source0 SHA256 mismatch for Canary-Stability-2013.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Canary-Stability-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTOMATED_TESTING PERL_CANARY_STABILITY_COLOUR \
    PERL_CANARY_STABILITY_DISABLE PERL_CANARY_STABILITY_NOPROMPT
make test

%files
%license COPYING
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2013-22
- Prepare for Oreon 11 (RP1)
