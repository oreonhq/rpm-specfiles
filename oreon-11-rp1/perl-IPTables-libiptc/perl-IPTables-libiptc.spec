%global source0_hash aa06ca77118fd0f8e3c2c7975eaf643b68be677b8085d96b814c31eebb925aca

Name:           perl-IPTables-libiptc
Version:        0.52
Release:        54%{?dist}
Summary:        Perl extension for iptables libiptc
# iptables/iptables.c*:             GPL-2.0-or-later
# iptables/iptables-blocking.c:     GPL-2.0-or-later
# iptables/iptables-standalone.c*   GPL-2.0-or-later
# lib/IPTables/libiptc.pm:          GPL-2.0-or-later
# ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
# README:       GPL-2.0-or-later
License:        GPL-2.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/IPTables-libiptc
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAWK/IPTables-libiptc-%{version}.tar.gz
# RT#70639
Patch0:         %{name}-0.51-Support-iptables-1.4.12.patch
# RT#70639
Patch1:         IPTables-libiptc-0.52-Support-for-1.4.16.2.patch
# RT#70639, bug #992659
Patch2:         IPTables-libiptc-0.52-Support-for-1.4.18.patch
# RT#70639, bug #1327038
Patch3:         IPTables-libiptc-0.52-Support-for-1.6.0.patch
# RT#70639, bug #1420338
Patch4:         IPTables-libiptc-0.52-Support-for-1.6.1.patch
# croak() expects formatting string, bug #1106081
Patch5:         IPTables-libiptc-0.52-Fix-GCC-format-security-warning.patch
# Do not link to nsl library, CPAN RT#124095
Patch6:         IPTables-libiptc-0.52-Stop-linking-against-nsl-library.patch
# Disable locking in iptables library, bug #1670047
Patch7:         IPTables-libiptc-0.52-Disable-locking.patch
# Fix make install invocation
Patch8:         IPTables-libiptc-0.52-Fix-make-install.patch
# Adapt to iptables-1.8.9, CPAN RT#70639
Patch9:         IPTables-libiptc-0.52-Adapt-to-iptables-1.8.9.patch
# Adapt to GCC 13, CPAN RT#146048
Patch10:        IPTables-libiptc-0.52-Adapt-to-GCC-13.patch
# kernel-headers >= 4.5.0-0.rc0.git6.1.fc24 and < 4.6.0-0.rc7.git3.1.fc25
# were broken, bug #1300223
BuildConflicts: kernel-headers < 4.6.0-0.rc7.git3.1.fc25
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
# Makefile.PL executes iptables program
BuildRequires:  iptables-legacy
BuildRequires:  iptables-devel >= 1.6.0
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
# ExtUtils::Constant not needed
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Part of iptables is bundled because iptables do not provide a stable
# library API.
Provides:       bundled(iptables) = 1.6.1

%{?perl_default_filter}

# Filter bogus libiptc.so() Provides, this is intentional rpm-build feature,
# bug #1309664
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^libiptc\\.so()

%description
This package provides a perl interface to the netfilter/iptables C-code and
library libiptc.

%package tests
Summary:        Tests for %{name}
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n IPTables-libiptc-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor NO_PACKLIST=1 \
    NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%dir %{perl_vendorarch}/auto/IPTables
%{perl_vendorarch}/auto/IPTables/libiptc
%dir %{perl_vendorarch}/IPTables
%{perl_vendorarch}/IPTables/libiptc.pm
%{_mandir}/man3/IPTables::libiptc.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
