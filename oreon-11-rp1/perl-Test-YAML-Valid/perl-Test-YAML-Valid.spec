%global source0_hash bac927352c68b13dcf169fd5d5c8f8bd4598ed88edb1a78b0e43e823d08e80de

Name:           perl-Test-YAML-Valid
Version:        0.04
Release:        46%{?dist}
Summary:        Lets you test the validity of YAML files in unit tests
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-YAML-Valid
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-YAML-Valid-%{version}.tar.gz
Patch0:         Test-YAML-Valid-0.04-Fix-building-on-Perl-without-.-in-INC.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Dependencies of bundled Module::Install
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(vars)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML) >= 0.60
# Test Suite
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(YAML::XS)
# Dependencies
# Default backend; can also optionally use YAML::Syck, YAML::Tiny, or YAML::XS
Requires:       perl(YAML) >= 0.60

%description
Lets you test the validity of YAML files inside your
(Test::Builder-based) unit tests.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-YAML-Valid-%{version}

# Fix building on Perl without "." in @INC (CPAN RT#120438)
%patch -P 0 -p1

%build
perl Makefile.PL --skipdeps INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::YAML::Valid.3*

%changelog
%autochangelog
