%global source0_hash 8acd7af4d8af21d28b9c15ae137fe76cd064dad7d26eba8a30b97ebc6e1f6b49

Name:           perl-PerlIO-via-dynamic
Version:        0.14
Release:        38%{?dist}
Summary:        Dynamic PerlIO layers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlIO-via-dynamic
Source0:        https://cpan.metacpan.org/modules/by-module/PerlIO/PerlIO-via-dynamic-%{version}.tar.gz
# Do not download sources from the Internet
Patch0:         PerlIO-via-dynamic-0.14-Disable-installing-missing-dependencies-from-CPAN.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
# Module::Install::AutoInstall disabled
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time:
# Internals not used with recent Perl
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)

%description
PerlIO::via::dynamic is used for creating dynamic PerlIO layers. It is
useful when the behavior or the layer depends on variables. You should not
use this module as via layer directly (ie :via(dynamic)).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PerlIO-via-dynamic-%{version}
%patch -P0 -p1
# Remove bundled modules
rm -rf inc
sed -i -e '/^inc\//d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
