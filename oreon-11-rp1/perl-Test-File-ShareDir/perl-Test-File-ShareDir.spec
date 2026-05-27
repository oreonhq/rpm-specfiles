%global source0_hash b33647cbb4b2f2fcfbde4f8bb4383d0ac95c2f89c4c5770eb691f1643a337aad

Name:           perl-Test-File-ShareDir
Version:        1.001002
Release:        26%{?dist}
Summary:        Create a Fake ShareDir for your modules for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-File-ShareDir
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Test-File-ShareDir-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) > 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scope::Guard)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(File::Copy::Recursive)
Requires:       perl(Scope::Guard)

%{?perl_default_filter}

%description
Create a fake ShareDir for your modules for testing.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Test-File-ShareDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=true
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.001002-26
- Prepare for Oreon 11 (RP1)
