%global source0_hash 8426964033a87fad7ab89a88b34aeefab59afcac377a4b476b6e32b3b2d3c511

Name:           perl-PPI-HTML
Version:        1.08
Release:        39%{?dist}
Summary:        Generate syntax-highlighted HTML for Perl using PPI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPI-HTML
Source0:        https://cpan.metacpan.org/modules/by-module/PPI/PPI-HTML-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
# Module Run-time:
BuildRequires:  perl(CSS::Tiny) >= 1.10
BuildRequires:  perl(Params::Util) => 0.05
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Script Run-time:
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(PPI) >= 0.990
# Tests:
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.47
# Dependencies
Requires:       perl(CSS::Tiny) >= 1.10
Requires:       perl(Params::Util) => 0.05
Requires:       perl(PPI) >= 0.990

# Filter under specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CSS::Tiny|Params::Util|PPI\\)$

%description
PPI::HTML converts Perl documents into syntax highlighted HTML pages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PPI-HTML-%{version}

# Remove bundled inc::Module::Install
rm -r inc/
sed -i '/^\/inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/ppi2html
%{perl_vendorlib}/PPI/
%{_mandir}/man3/PPI::HTML.3*

%changelog
%autochangelog
