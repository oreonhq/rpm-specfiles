%global source0_hash e9dbcd6c7a3d03bcf5ac1b168c11e785723cd81d554fc833a65695d1b9d11f8b

Name:           perl-B-Hooks-OP-PPAddr
Version:        0.06
Release:        28%{?dist}
Summary:        Hook into opcode execution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Hooks-OP-PPAddr
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-OP-PPAddr-%{version}.tar.gz

BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::Depends) >= 0.302
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module provides a c api for XS modules to hook into the execution of
perl opcodes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n B-Hooks-OP-PPAddr-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENCE
%doc CONTRIBUTING Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/B*
%{_mandir}/man3/*

%changelog
%autochangelog
