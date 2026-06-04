%global source0_hash fedb1560b39b81148b05cb2c3b46e23a2128029eea44610e7e683c4e99d50e6d

Name:           libgdither
Version:        0.6
Release:        %autorelease
Summary:        Library for applying dithering to PCM audio sources

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://plugin.org.uk/libgdither/README
Source0:        libgdither-0.6.tar.gz
Patch0:         libgdither-0.6-default.patch
Patch1:         libgdither-0.6-gavl.patch
Patch2:         libgdither-0.6-ldflags.patch

BuildRequires:  gcc-c++
BuildRequires:  fftw-devel >= 3.0.0
BuildRequires: make
    

%description
Libgdither is a GPL'd library library for performing audio dithering on 
PCM samples. The dithering process should be carried out before reducing 
the bit width of PCM audio data (eg. float to 16 bit int conversions) to 
preserve audio quality.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .default
%patch -P1 -p1 -b .gavl_fix
%patch -P2 -p1 -b .ldflags


%build
export INIT_CFLAGS="${RPM_OPT_FLAGS}"
export LDFLAGS="%{build_ldflags}"
export PREFIX="%{_prefix}"
%make_build


%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

sed -i -e 's|/usr/local|%{_prefix}|g' \
   $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libgdither.pc
sed -i -e 's|%{_prefix}/lib|%{_libdir}|' \
  $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libgdither.pc

%check
make test CFLAGS="%{optflags} -Werror --std=c99 -I%{_builddir}/%{?buildsubdir}"


%ldconfig_scriptlets


%files
%doc README
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/libgdither/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgdither.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-1
- Import
