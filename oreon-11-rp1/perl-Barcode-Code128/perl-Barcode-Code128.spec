%global source0_hash f8c90811d916e13bdbce348924db45f39dc7688580505a897d2196a8781b6f06

name:           perl-Barcode-Code128
Version:        2.21
Release:        30%{?dist}
Summary:        Generate CODE 128 bar codes
# README:       LicenseRef-Fedora-Public-Domain
License:        LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Barcode-Code128
Source0:        https://cpan.metacpan.org/authors/id/W/WR/WRW/Barcode-Code128-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(GD) >= 2.18
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(GD) >= 2.18

%description
Barcode::Code128 generates bar codes using the CODE 128 symbology. It can
generate images in PNG or GIF format using the GD package, or it can
generate a text string representing the barcode that you can render using
some other technology if desired.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Barcode-Code128-%{version}
# Extract a license text
perl -pe '$license=1 if /\ATERMS:/; $license=0 if /\A$/; undef $_ unless $license;' \
    <README >LICENSE
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
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Barcode
%{perl_vendorlib}/Barcode/Code128.pm
%{_mandir}/man3/Barcode::Code128.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
