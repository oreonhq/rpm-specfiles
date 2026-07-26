%global source0_hash e0f35567636353709a61d68e2e6a41d3f27e32b6bb40d9a140455a459cea5d24

Name:           perl-pip
Summary:        Perl Installation Program, for scripted and distribution installation
Version:        1.19
Release:        42%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/pip-%{version}.tar.gz 
URL:            https://metacpan.org/release/pip
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip) >= 1.29
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN) >= 1.76
BuildRequires:  perl(CPAN::Inject) >= 0.07
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::pushd) >= 0.32
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Temp) >= 0.14
BuildRequires:  perl(File::Which) >= 1.08
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(PAR::Dist) >= 0.25
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(strict)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(LWP::Online) >= 1.06
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Script) >= 1.02

Requires:       perl(Archive::Zip) >= 1.29
Requires:       perl(CPAN) >= 1.76
Requires:       perl(CPAN::Inject) >= 0.07
Requires:       perl(File::pushd) >= 0.32
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(File::Temp) >= 0.14
Requires:       perl(File::Which) >= 1.08
Requires:       perl(IO::Zlib)
Requires:       perl(LWP::Simple)
Requires:       perl(PAR::Dist) >= 0.25
Requires:       perl(Params::Util) >= 1.00

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Spec\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Which\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::pushd\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Params::Util\\)\s*$

%description
The pip ("Perl Installation Program") console application is used to
install Perl distributions in a wide variety of formats, both from CPAN and
from external third-party locations, while supporting module dependencies
that go across the boundary from third-party to CPAN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pip-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
mv $RPM_BUILD_ROOT%{_bindir}/pip $RPM_BUILD_ROOT%{_bindir}/perl-pip
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# too long response time
%{?!_with_network_tests: rm t/03_uri.t }
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/perl-pip

%changelog
%autochangelog
