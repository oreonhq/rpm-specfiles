%global source0_hash 4fb351c1ae25c213cc6f17022eb62e2f0ce9678c0439916cb536d5cb3503da31
%global use_system_admesh 0
%global use_system_expat 1
%global use_system_polyclipping 1
%global use_system_poly2tri 1
Name:           slic3r
Version:        1.3.0
Release:        1%{?dist}
Summary:        G-code generator for 3D printers (RepRap, Makerbot, Ultimaker etc.)
License:        AGPL-3.0-only AND LicenseRef-Callaway-CC-BY
URL:            http://slic3r.org/
Source0:        https://github.com/alexrj/Slic3r/archive/%{version}.tar.gz
Patch0:         %{name}-buildpl.patch
Patch1:         %{name}-datadir.patch
Patch2:         %{name}-english-locale.patch
Patch3:         %{name}-linker.patch
Patch4:         %{name}-clipper.patch
Patch5:         %{name}-1.3.0-fixtest.patch
Patch6:         %{name}-wayland.patch
Patch7:         %{name}-boost169.patch
Patch8:         %{name}-endian.patch
Patch9:         %{name}-bind-placeholders.patch
Patch10:        %{name}-boost-nowide.patch
Patch11:        %{name}-CVE-2020-28591.patch
Patch12:        https://salsa.debian.org/3dprinting-team/slic3r/-/raw/boost1.88/debian/patches/Fix-FTBFS-with-boost-1.88.patch
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Provides:       bundled(admesh) = 0.98
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
ExcludeArch:    ppc ppc64 s390 s390x %{ix86}
%else
ExcludeArch:    ppc ppc64 s390 s390x
%endif
Requires:       perl(Growl::GNTP) >= 0.15
Requires:       perl(XML::SAX)
Recommends:     perl(Thread::Queue)
Recommends:     perl(threads::shared)
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Typemaps)
BuildRequires:  perl(ExtUtils::Typemaps::Default)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::WithXSpp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(SVG)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Wx)
BuildRequires:  perl(local::lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  poly2tri-devel
BuildRequires:  polyclipping-devel
# /oreon:deps
%description
Slic3r is a G-code generator for 3D printers. It's compatible with RepRaps,
Makerbots, Ultimakers and many more machines.
See the project homepage at slic3r.org and the documentation on the Slic3r wiki
for more information.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Slic3r-%{version}

%patch -p1 -P0
%patch -p1 -P1
%patch -p1 -P2
%patch -p1 -P3 -b .linker
%patch -p1 -P4
%patch -p1 -P5 -b .fixtest
%patch -p1 -P6
%patch -p1 -P7
%patch -p1 -P8
%patch -p1 -P9
%patch -p1 -P10
%patch -p1 -P11
%patch -p1 -P12

# To avoid "error: exponent has no digits" on GCC 14+
# https://bugzilla.redhat.com/2259542
# https://bugzilla.redhat.com/1321986
# Simplified from https://github.com/slic3r/Slic3r/commit/c8ccc1a38eded78256dd89faee1f82bc9c0888a8
sed -i 's/-std=c++11/-std=gnu++11/' xs/Build.PL

# Optional removals

rm -rf xs/src/expat
sed -i '/src\/expat/d' xs/MANIFEST
# These are the files with hardcoded expat/expat.h includes
sed -i 's|expat/expat.h|expat.h|g' xs/src/libslic3r/IO/AMF.cpp
sed -i 's|expat/expat.h|expat.h|g' xs/src/libslic3r/IO/TMF.hpp

#rm xs/src/clipper.*pp
export SYSTEM_LIBS="${SYSTEM_LIBS} -lpolyclipping"

rm -rf xs/src/poly2tri
sed -i '/src\/poly2tri/d' xs/MANIFEST

# We always do boost.
rm -rf xs/src/boost
sed -i '/src\/boost\/nowide/d' xs/MANIFEST

%build

export SYSTEM_LIBS="${SYSTEM_LIBS} -lexpat"
export SYSTEM_LIBS="${SYSTEM_LIBS} -lpoly2tri"
cd xs
[[ ! -z "${SYSTEM_LIBS}" ]] && echo "SYSTEM_LIBS is ${SYSTEM_LIBS}"
perl ./Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
cd -
for res in 16 32 48 128 256; do
  mkdir -p hicolor/${res}x${res}/apps
done
cd hicolor
convert ../var/Slic3r.ico %{name}.png
cp %{name}-0.png 256x256/apps/%{name}.png
cp %{name}-1.png 128x128/apps/%{name}.png
cp %{name}-2.png 48x48/apps/%{name}.png
cp %{name}-3.png 32x32/apps/%{name}.png
cp %{name}-4.png 16x16/apps/%{name}.png
rm %{name}-*.png
cd -
cd var
find . -type f -name "*.png" -exec convert {} -strip {} \;
cd -
%install
cd xs
./Build install destdir=%{buildroot} create_packlist=0
cd -
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons
mkdir -p %{buildroot}%{_datadir}/appdata
cp -a %{name}.pl %{buildroot}%{_bindir}/%{name}
cp -ar lib/* %{buildroot}%{perl_vendorlib}
cp -a var/* %{buildroot}%{_datadir}/%{name}
cp -r hicolor %{buildroot}%{_datadir}/icons
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
cp %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%{_fixperms} %{buildroot}*
%oreon_autofiles main

%check

cd xs
./Build test verbose=1
cd -
SLIC3R_NO_AUTO=1 perl Build.PL installdirs=vendor
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
