%global source0_hash 0054dd3f573bd3f6f47b73ee81d1e845842fba04aadb52880aa52701c687d1ca
Name:           perl-Boost-Geometry-Utils
Version:        0.15
Release:        1%{?dist}
Summary:        Bindings for the Boost Geometry library
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSL-1.0
URL:            https://metacpan.org/release/Boost-Geometry-Utils
Source0:        https://cpan.metacpan.org/authors/id/A/AA/AAR/Boost-Geometry-Utils-%{version}.tar.gz
Patch0:         Boost-Geometry-Utils-0.15-multi_linestring2perl-only-extend-the-array-if-needed.patch
Patch1:         Boost-Geometry-Utils-0.15-Port-Boost-1.73.0.patch
Patch2:         Boost-Geometry-Utils-0.15-Normalize-shellbangs.patch
Patch3:         Boost-Geometry-Utils-0.15-Adapt-to-Boost-1.89.0.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Typemaps::Default)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build::WithXSpp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-compile.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Boost-Geometry-Utils-tests -f %{oreon_filedir}/perl-Boost-Geometry-Utils-tests.list

%changelog

%autochangelog
