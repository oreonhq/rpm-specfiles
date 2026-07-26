%global source0_hash 28c74842ac776e7acb820561166ab8e4fe3fdeed8ec2ec6d8de1c1b04c703b84

Name:           perl-RPM-VersionCompare
Version:        0.1.1
Release:        55%{?dist}
Summary:        Compare RPM version strings
License:        GPL-3.0-or-later
URL:            https://ppisar.fedorapeople.org/RPM-VersionCompare/
Source0:        %{url}/RPM-VersionCompare-v%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(rpm)
# Tests only:
BuildRequires:  perl(Test::Simple)

%{?perl_default_filter}

%description
This module provides functions to compare RPM version strings. No function
is exported by default. If possible, calls are passed to native librpm
library. Otherwise Python extension provided with RPM sources is re-
-implemented.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n RPM-VersionCompare-v%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
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
%license COPYING
%doc Changes
%dir %{perl_vendorarch}/auto/RPM
%{perl_vendorarch}/auto/RPM/VersionCompare
%dir %{perl_vendorarch}/RPM
%{perl_vendorarch}/RPM/VersionCompare.pm
%{_mandir}/man3/RPM::VersionCompare.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
