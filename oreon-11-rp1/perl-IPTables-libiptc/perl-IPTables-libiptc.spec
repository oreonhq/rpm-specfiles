%global source0_hash aa06ca77118fd0f8e3c2c7975eaf643b68be677b8085d96b814c31eebb925aca
Name:           perl-IPTables-libiptc
Version:        0.52
Release:        54%{?dist}
Summary:        Perl extension for iptables libiptc
License:        GPL-2.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/IPTables-libiptc
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAWK/IPTables-libiptc-%{version}.tar.gz
Patch0:         %{name}-0.51-Support-iptables-1.4.12.patch
Patch1:         IPTables-libiptc-0.52-Support-for-1.4.16.2.patch
Patch2:         IPTables-libiptc-0.52-Support-for-1.4.18.patch
Patch3:         IPTables-libiptc-0.52-Support-for-1.6.0.patch
Patch4:         IPTables-libiptc-0.52-Support-for-1.6.1.patch
Patch5:         IPTables-libiptc-0.52-Fix-GCC-format-security-warning.patch
Patch6:         IPTables-libiptc-0.52-Stop-linking-against-nsl-library.patch
Patch7:         IPTables-libiptc-0.52-Disable-locking.patch
Patch8:         IPTables-libiptc-0.52-Fix-make-install.patch
Patch9:         IPTables-libiptc-0.52-Adapt-to-iptables-1.8.9.patch
Patch10:        IPTables-libiptc-0.52-Adapt-to-GCC-13.patch
BuildConflicts: kernel-headers < 4.6.0-0.rc7.git3.1.fc25
Provides:       bundled(iptables) = 1.6.1
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^libiptc\\.so()
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  iptables-devel
BuildRequires:  iptables-legacy
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-IPTables-libiptc-tests -f %{oreon_filedir}/perl-IPTables-libiptc-tests.list

%changelog

%autochangelog
