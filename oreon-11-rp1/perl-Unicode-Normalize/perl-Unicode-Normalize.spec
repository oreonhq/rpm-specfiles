%global base_version 1.26
Name:           perl-Unicode-Normalize
Version:        1.32
Release:        521%{?dist}
Summary:        Unicode Normalization Forms
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Unicode-Normalize
Source0:        https://cpan.metacpan.org/authors/id/K/KH/KHW/Unicode-Normalize-%{base_version}.tar.gz
# Unbundled from perl 5.37.11
Patch0:         Unicode-Normalize-1.26-Upgrade-to-1.32.patch
# oreon url source checksums begin
%global source0_sha256 bade6f74e89b95a4b2226a0965ac1218e0e4eeaa0edb4b30ee7aac9d5dae773f
%global source0_file Unicode-Normalize-1.26.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# unicore/CombiningClass.pl and unicore/Decomposition.pl from perl-libs
BuildRequires:  perl-libs
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
Conflicts:      perl < 4:5.22.0-347

%description
This package provides Perl functions that can convert strings into various
Unicode normalization forms as defined in Unicode Standard Annex #15.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Unicode-Normalize-1.26.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bade6f74e89b95a4b2226a0965ac1218e0e4eeaa0edb4b30ee7aac9d5dae773f" || { echo "oreon: Source0 SHA256 mismatch for Unicode-Normalize-1.26.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Unicode-Normalize-%{base_version}
%patch -P0 -p1

# Generate ppport.h which is used since 1.32
perl -MDevel::PPPort \
    -e 'Devel::PPPort::WriteFile() or die "Could not generate ppport.h: $!"'

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
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
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Unicode
%{_mandir}/man3/Unicode::Normalize*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.32-521
- Prepare for Oreon 11 (RP1)
