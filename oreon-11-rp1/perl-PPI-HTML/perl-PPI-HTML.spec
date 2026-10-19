%global source0_hash 8426964033a87fad7ab89a88b34aeefab59afcac377a4b476b6e32b3b2d3c511
Name:           perl-PPI-HTML
Version:        1.08
Release:        1%{?dist}
Summary:        Generate syntax-highlighted HTML for Perl using PPI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPI-HTML
Source0:        https://cpan.metacpan.org/modules/by-module/PPI/PPI-HTML-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CSS::Tiny) >= 1.10
Requires:       perl(Params::Util) => 0.05
Requires:       perl(PPI) >= 0.990
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CSS::Tiny|Params::Util|PPI\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CSS::Tiny)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
