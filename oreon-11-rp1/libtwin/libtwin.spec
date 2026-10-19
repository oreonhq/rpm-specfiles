%global source0_hash f57fec5b616bad6457636e8ea034be3fa09a10a5d977e1d89c29e5b4358b62f0
Name:		libtwin
Version:	0.0.3
Release:        35%{?dist}
Summary:        Tiny Window System
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://ozlabs.org/~jk/projects/petitboot/
Source0:        http://ozlabs.org/~jk/projects/petitboot/downloads/%{name}-%{version}.tar.gz
Patch0:		libtwin-0.0.2-no-altivec.patch
Patch1:		libtwin-0.0.2-no-float.patch
Patch2:		libtwin-0.0.2-sqrt.patch
# oreon:deps
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
With embedded systems gaining high resolution displays and powerful
cpus, the desire for sophisticated graphical user interfaces can be
realized in even the smallest of systems. While the cpupower available
for a given power budget has increased dramatically, these tiny
systems remain severely memory constrained. This unique environment
presents interesting challenges in graphical system design and
implementation. To explore this particular space, a new window system,
Twin, has been developed. Using ideas from modern window systems in
larger environments, Twin offers overlapping translucent windows,
anti-aliased graphics and scalable fonts in a total memory budget of
100KB.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	static
Summary:	Static build files for %{name}
Requires:	%{name}-devel = %{version}-%{release}
%description	static
The %{name}-static package contains static libraries from %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

CFLAGS="$RPM_OPT_FLAGS -flax-vector-conversions" %configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libtwin-devel -f %{oreon_filedir}/libtwin-devel.list
%files -n libtwin-static -f %{oreon_filedir}/libtwin-static.list

%changelog

%autochangelog
