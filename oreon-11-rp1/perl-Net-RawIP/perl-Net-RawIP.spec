%global source0_hash 6d104b2f0e453eff7a1b479c528798670b15729ed6ecf41430405ff6d7e1ee58

# Execute tests that requires working network
%bcond_with perl_Net_RawIP_enables_network_test
# Execute optional test
%bcond_without perl_Net_RawIP_enables_optional_test

Name:           perl-Net-RawIP
Version:        0.25
Release:        55%{?dist}
Summary:        Perl extension for manipulating raw IP packets using libpcap
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-RawIP
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-RawIP-%{version}.tar.gz
Patch0:         Net-RawIP-0.23-format.patch
# Adapt to changes in glibc-2.20, CPAN RT#124134
Patch1:         Net-RawIP-0.25-Use-_DEFAULT_SOURCE-instead-of-_BSD_SOURCE.patch
# Fix missing function prototypes, CPAN RT#124134
Patch2:         Net-RawIP-0.25-Decalare-used-function.patch
# Fix compiler warnings, CPAN RT#124134
Patch3:         Net-RawIP-0.25-Silent-compiler-warnings.patch
BuildRequires: make
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if %{without perl_Net_RawIP_enables_network_test}
BuildRequires:  sed
%endif
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
# Prefer XSLoader over DynaLoader
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
%if %{with perl_Net_RawIP_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Proc::ProcessTable)
%endif
# Prefer XSLoader over DynaLoader
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
This package provides a Perl class  which can be used for creating,
manipulating and sending raw IP packets with optional features for
manipulating Ethernet headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-RawIP-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
chmod a-x examples/*
%if %{without perl_Net_RawIP_enables_network_test}
rm t/iflist.t
sed -i -e '/^t\/iflist\.t/d' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_MODE
make test

%files
%doc Changes examples README README.Devel TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
%autochangelog
