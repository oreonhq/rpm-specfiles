%global source0_hash d39aa08076550465fcd9871825be2899a98496605346fcd906e140e51ee19d6f
Name:           libgdither
Version:        0.6
Release:        1%{?dist}
Summary:        Library for applying dithering to PCM audio sources
License:        GPL-2.0-or-later
URL:            http://plugin.org.uk/libgdither/README
Source0:        https://github.com/aybe/libgdither-0.6/archive/refs/heads/master.tar.gz#/libgdither-0.6.tar.gz
Patch0:         libgdither-0.6-default.patch
Patch1:         libgdither-0.6-gavl.patch
Patch2:         libgdither-0.6-ldflags.patch
# oreon:deps
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
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
%setup -q -n libgdither-0.6-master
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test CFLAGS="%{optflags} -Werror --std=c99 -I%{_builddir}/%{?buildsubdir}"
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libgdither-devel -f %{oreon_filedir}/libgdither-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6-1
- Import
