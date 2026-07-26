%global source0_hash 9b8a6abebfda17586ef7e5fea9ba8e87a3cc688676681ef306b445c3f4034175

# NVIDIA Cg toolkit is not free
%define with_Cg         0
%if %with_Cg
%define real_name       OpenEXR_Viewers-nonfree
%define V_suffix        -nonfree
%define priority        10
%else
%define real_name       OpenEXR_Viewers
%define V_suffix        -fedora
%define priority        5
%endif

%global project openexr

Name:           %{real_name}
Version:        2.3.0
Release:        23%{?dist}
Summary:        Viewers programs for OpenEXR

# Automatically converted from old format: AMPAS BSD - review is highly recommended.
License:        AMPAS
URL:            http://www.openexr.com
Source0: https://github.com/%{project}/%{project}/releases/download/v%{version}/OpenEXR_Viewers-%{version}.tar.gz

Patch1: openexr_viewers-2.0.1-dso.patch
Patch2: openexr_viewers-gcc-11-fixes.patch
Patch3: openexr_viewers-imfheader.patch

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc-c++

BuildRequires:  fltk-devel >= 1.1
BuildRequires:  pkgconfig(OpenEXR) >= 2.1
%if %with_Cg
BuildRequires:  Cg
BuildRequires:  freeglut-devel
Provides: OpenEXR_Viewers = %{version}
%else
BuildConflicts:  Cg
%endif

%if 0%{?openexr_ctl}
BuildRequires:  pkgconfig(OpenEXR_CTL)
BuildRequires:  OpenEXR_CTL
Requires:  OpenEXR_CTL%{?_isa}
%endif
Requires(post): /usr/sbin/alternatives
Requires(preun): /usr/sbin/alternatives

%description
exrdisplay is a simple still image viewer that optionally applies color
transforms to OpenEXR images, using ctl as explained in this document:
doc/OpenEXRViewers.pdf

%if %with_Cg
playexr is a program that plays back OpenEXR image sequences, optionally
with CTL support, applying rendering and display transforms in line with
the current discussions at the AMPAS Image Interchange Framework committee
(September 2006).

This is the nonfree version compiled with NVIDIA Cg support
See: https://developer.nvidia.com/cg-toolkit
%else

%package docs
Summary:        Documentation for %{name}

%description docs
This package contains documentation files for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n openexr_viewers-%{version}

%patch -P1 -p1 -b .dso
%patch -P2 -p1 -b .gcc11
%patch -P3 -p1 -b .imfh

%if "%{_lib}" == "lib64"
sed -i -e 's|ACTUAL_PREFIX/lib/CTL|ACTUAL_PREFIX/lib64/CTL|' configure.ac
%endif
#Needed for patch1 and to update CTL compiler test
#autoconf
./bootstrap
sed -i -e 's|#include <vector>\n    using namespace Ctl|#include <vector>\n    #include <cstdlib>\nusing namespace Ctl|' configure

%build
export CXXFLAGS="$RPM_OPT_FLAGS -L%{_libdir}"
%configure  --disable-static \
  --disable-openexrtest \
  --disable-openexrctltest \
%if %with_Cg
  --with-cg-prefix=%{_prefix}
%endif

# Missing libs for playexr
sed -i -e 's|LIBS =|LIBS = -lglut|' playexr/Makefile

%make_build

%install
%make_install

# Remove the config.h - uneeded afaik
rm -rf $RPM_BUILD_ROOT%{_includedir}

# move the binary
mv $RPM_BUILD_ROOT%{_bindir}/exrdisplay $RPM_BUILD_ROOT%{_bindir}/exrdisplay%{V_suffix}

# Removing installed docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

# Owernship of the alternative provides
touch $RPM_BUILD_ROOT%{_bindir}/exrdisplay

%post
alternatives --install %{_bindir}/exrdisplay exrdisplay %{_bindir}/exrdisplay%{V_suffix} %{priority} ||:

%preun
if [ $1 -eq 0 ]; then
  alternatives --remove exrdisplay %{_bindir}/exrdisplay%{V_suffix} || :
fi

%files
%doc ChangeLog README.md
%license LICENSE
%ghost %{_bindir}/exrdisplay
%{_bindir}/exrdisplay%{V_suffix}
%if %with_Cg
%{_bindir}/playexr
%else

%files docs
%doc doc/OpenEXRViewers.odt doc/OpenEXRViewers.pdf
%endif

%changelog
%autochangelog
