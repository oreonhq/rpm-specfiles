Name:           perl-Sub-Uplevel
Summary:        Apparently run a function in a higher stack frame
Epoch:          1
Version:        0.2800
Release:        26%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Uplevel
Source0:        https://cpan.metacpan.org/modules/by-module/Sub/Sub-Uplevel-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
# Optional:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Explicit Run-time:
Requires:       perl(Carp)

# Remove bogus perl(DB) provide
%global __provides_exclude ^perl\\(DB\\)$

%description
Like Tcl's uplevel() function, but not quite so dangerous. The idea is
just to fool caller(). All the really naughty bits of Tcl's uplevel()
are avoided.

%prep
%setup -q -n Sub-Uplevel-%{version}

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
%doc Changes CONTRIBUTING.mkdn README examples/
%{perl_vendorlib}/Sub/
%{_mandir}/man3/Sub::Uplevel.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2800-26
- Prepare for Oreon 11 (RP1)
