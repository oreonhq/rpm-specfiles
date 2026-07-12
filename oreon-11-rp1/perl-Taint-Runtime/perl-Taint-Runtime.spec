%global source0_hash 6ece97234a19a6f627481b44ec28a71374a95e6fc94d417d2dccb397a00aa706

Name:           perl-Taint-Runtime
Version:        0.03
Release:        58%{?dist}
Summary:        Runtime enable taint checking
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Taint-Runtime
Source0:        https://cpan.metacpan.org/modules/by-module/Taint/Taint-Runtime-%{version}.tar.gz



# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)
# Dependencies:
Requires:       perl(Carp)

%{?perl_default_filter}

Provides:       perl(Taint::Runtime)
%description
This module enables run-time taint checking, for cases where the -T
switch on the command line is not appropriate or viable. There are
a somewhat limited number of legitimate use cases where you should 
use this module instead of the -T switch. Unless you have a specific and
good reason for not using the -T option, you should use the -T option.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Taint-Runtime-%{version}
chmod -c +x is_taint_bench.pl

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/Taint/
%{perl_vendorarch}/Taint/
%{_mandir}/man3/Taint::Runtime.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.03-58
- Prepare for Oreon 11 (RP1)
