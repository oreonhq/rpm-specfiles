Name:           perl-IO-HTML
Version:        1.004
Release:        16%{?dist}
Summary:        Open an HTML file with automatic character set detection
# examples/detect-encoding.pl: Public Domain
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/IO-HTML
Source0:        https://cpan.metacpan.org/authors/id/C/CJ/CJM/IO-HTML-%{version}.tar.gz
# Do not use /usr/bin/env in a shebang
Patch0:         IO-HTML-1.004-Normalize-a-shebang.patch
# oreon url source checksums begin
%global source0_sha256 c87b2df59463bbf2c39596773dfb5c03bde0f7e1051af339f963f58c1cbd8bf5
%global source0_file IO-HTML-1.004.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2.10
BuildRequires:  perl(Exporter) >= 5.57
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88

%description
IO::HTML provides an easy way to open a file containing HTML while
automatically determining its encoding. It uses the HTML5 encoding sniffing
algorithm specified in section 8.2.2.1 of the draft standard.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/IO-HTML-1.004.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c87b2df59463bbf2c39596773dfb5c03bde0f7e1051af339f963f58c1cbd8bf5" || { echo "oreon: Source0 SHA256 mismatch for IO-HTML-1.004.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n IO-HTML-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
cp META.json %{buildroot}%{_libexecdir}/%{name}/
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.004-16
- Prepare for Oreon 11 (RP1)
