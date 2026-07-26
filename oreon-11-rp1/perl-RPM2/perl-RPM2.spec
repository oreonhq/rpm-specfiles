%global source0_hash 5ecb42aa69324e6f4088abfae07313906e5aabf2f46f1204f3f1de59155bb636

Name:           perl-RPM2
Version:        1.4
Release:        36%{?dist}
Summary:        Perl bindings for the RPM Package Manager API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/RPM2
Source0:        https://cpan.metacpan.org/authors/id/L/LK/LKUNDRAK/RPM2-%{version}.tar.gz
# Adapt to RPM 6, bug #2361571, proposed to upstream,
# <https://github.com/lkundrak/perl-RPM2/pull/2>
Patch0:         RPM2-1.4-Adapt-tests-to-RPM-6.patch
# Disable signature verification in root tests, proposed to upstream,
# <https://github.com/lkundrak/perl-RPM2/pull/2>
Patch1:         RPM2-1.4-Tests-Disable-package-verification.patch
# Fix a crash in RPM plugins, proposed to upstream,
# <https://github.com/lkundrak/perl-RPM2/pull/3>
Patch2:         RPM2-1.4-Fix-a-crash-in-RPM-plugins-on-add_package.patch
# Do not write into a working directory, proposed to upstream,
# <https://github.com/lkundrak/perl-RPM2/pull/4>
Patch3:         RPM2-1.4-tests-Use-File-Temp-for-creating-temporary-directori.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig
BuildRequires:  rpm-devel
# Run-time
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(overload)
# Tests
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
# rpm for rpmdb tool
BuildRequires:  rpm

%{?perl_default_filter}

%description
The RPM2 module provides an object-oriented interface to querying both the
installed RPM database as well as files on the filesystem, providing Perl
bindings for the RPM Package Manager API.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# rpm for rpmdb tool
Requires:       rpm

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n RPM2-%{version} -p1
# Correct permissions
chmod a+x test.pl

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a hdlist-test.hdr test.pl test-*.rpm %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . test.pl
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test verbose=1

%files
%doc Changes README
%{perl_vendorarch}/auto/RPM2
%{perl_vendorarch}/RPM2.pm
%{_mandir}/man3/RPM2.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
