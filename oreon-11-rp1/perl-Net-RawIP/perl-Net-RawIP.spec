%global source0_hash 6d104b2f0e453eff7a1b479c528798670b15729ed6ecf41430405ff6d7e1ee58
%bcond_with perl_Net_RawIP_enables_network_test
%bcond_without perl_Net_RawIP_enables_optional_test
Name:           perl-Net-RawIP
Version:        0.25
Release:        55%{?dist}
Summary:        Perl extension for manipulating raw IP packets using libpcap
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-RawIP
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-RawIP-%{version}.tar.gz
Patch0:         Net-RawIP-0.23-format.patch
Patch1:         Net-RawIP-0.25-Use-_DEFAULT_SOURCE-instead-of-_BSD_SOURCE.patch
Patch2:         Net-RawIP-0.25-Decalare-used-function.patch
Patch3:         Net-RawIP-0.25-Silent-compiler-warnings.patch
%if %{without perl_Net_RawIP_enables_network_test}
%endif
%if %{with perl_Net_RawIP_enables_optional_test}
%endif
Requires:       perl(XSLoader)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Proc::ProcessTable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

unset AUTHOR_MODE
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
