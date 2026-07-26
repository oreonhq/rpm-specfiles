%global source0_hash 0054dd3f573bd3f6f47b73ee81d1e845842fba04aadb52880aa52701c687d1ca

Name:           perl-Boost-Geometry-Utils
Version:        0.15
Release:        47%{?dist}
Summary:        Bindings for the Boost Geometry library
# README:               GPL+ or Artistic
# src/medial_axis.hpp:  Boost
# src/ppport.h:         GPL+ or Artistic
## Unbundled
# src/boost/type.hpp:   Boost
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSL-1.0
URL:            https://metacpan.org/release/Boost-Geometry-Utils
Source0:        https://cpan.metacpan.org/authors/id/A/AA/AAR/Boost-Geometry-Utils-%{version}.tar.gz
# Fix for RT#96145
Patch0:         Boost-Geometry-Utils-0.15-multi_linestring2perl-only-extend-the-array-if-needed.patch
# Fix building with Boost 1.73.0, CPAN RT#133057
Patch1:         Boost-Geometry-Utils-0.15-Port-Boost-1.73.0.patch
# Correct shellbangs in the tests, CPAN RT#156188
Patch2:         Boost-Geometry-Utils-0.15-Normalize-shellbangs.patch
# Fix building with Boost 1.90.0, bug #2431531, posted to upstream,
# CPAN RT#172828
Patch3:         Boost-Geometry-Utils-0.15-Adapt-to-Boost-1.89.0.patch
BuildRequires:  boost-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Typemaps::Default) >= 0.05
BuildRequires:  perl(Module::Build::WithXSpp) >= 0.10
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)

%description
This Perl module provides bindings to perform some geometric operations using
the Boost Geometry library. It does not aim at providing full bindings.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Boost-Geometry-Utils-%{version}
# Unbundle Boost
rm -r src/boost
perl -i -ne 'print $_ unless m{^src/boost/}' MANIFEST
# Remove always skipped tests
for T in t/release-pod-* t/05_medial_axis_visual.t; do
    rm -- "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done
# Correct permissions
chmod a+x t/*.t

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove tests which search modules in CWD
rm %{buildroot}%{_libexecdir}/%{name}/t/00-compile.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc CHANGES README
%dir %{perl_vendorarch}/auto/Boost
%dir %{perl_vendorarch}/auto/Boost/Geometry
%{perl_vendorarch}/auto/Boost/Geometry/Utils
%dir %{perl_vendorarch}/Boost
%dir %{perl_vendorarch}/Boost/Geometry
%{perl_vendorarch}/Boost/Geometry/Utils.pm
%{_mandir}/man3/Boost::Geometry::Utils.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
