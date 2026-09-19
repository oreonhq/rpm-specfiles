%global source0_hash bf607fae7a6901b9dfa666e6b120c60203016b029900068c32f8525323f9a1b2

%global min_libsolv_version 0.7.2

#global commit 1955d7faf7a7eacb96895a2c0e201135738f3750
#global shortcommit %%(c=%%{commit}; echo ${c:0:7})
#global commitdate 20191121

# for rpmdev-bumpspec to handle properly...
%global baserelease 21

Name:           perl-BSSolv
Version:        0.17
Release:        %{baserelease}%{?commit:.git%{commitdate}.%{shortcommit}}%{?dist}
Summary:        OBS solver and repository management using libsolv
# BSSolv.xs:    GPL-1.0-or-later OR Artistic-1.0-Perl
# Meta.yml:     GPL-1.0-or-later OR Artistic-1.0-Perl
# README:       GPL-1.0-or-later OR Artistic-1.0-Perl
## Not in any binary package
# dist/perl-BSSolv.spec:    "the same license as for the pristine package
#                           itself or MIT"; a referred "BSD-3-Clause" is
#                           a data, not a license declaration.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/openSUSE/perl-BSSolv
%if %{defined commit}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libsolv-devel >= %{min_libsolv_version}
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       libsolv%{?_isa} >= %{min_libsolv_version}

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}perl\\(t::testlib\\)

%description
This is a support perl module for the OBS backend. It contains functions
for repository management, dependency solving, package ordering, and meta
file creation.

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

%if %{defined commit}
%autosetup -n %{name}-%{commit} -p1
%else
%autosetup -p1
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
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
%{perl_vendorarch}/BSSolv.pm
%{perl_vendorarch}/auto/BSSolv
%doc dist/perl-BSSolv.changes README

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
