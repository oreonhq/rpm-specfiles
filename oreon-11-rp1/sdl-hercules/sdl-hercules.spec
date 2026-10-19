%global source0_hash none
%global forgeurl https://github.com/SDL-Hercules-390/hyperion
%global libregina_major_version 3
%global libarch lib
%ifarch aarch64
%global libarch %{libarch}/aarch64
%endif
%ifarch ppc64le
%global libarch %{libarch}/ppc
%endif
%ifarch s390x
%global libarch %{libarch}/s390x
%endif
Name:           sdl-hercules
Version:        4.9.1
Release:        1%{?dist}
Summary:        SoftDevLabs version of the Hercules S/370, ESA/390, and z/Arch Emulator
License:        QPL-1.0 AND (QPL-1.0 AND BSD-3-Clause) AND (QPL-1.0 AND MIT) AND (QPL-1.0 AND BSD-4-Clause)
URL:            https://www.sdl-hercules-390.org
Source0:        %{forgeurl}/archive/Release_%{version}/hyperion-Release_%{version}.tar.gz
Patch:          sdl-hercules-set-soversion.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-data = %{version}-%{release}
Recommends:     regina-rexx
Provides:       bundled(dyn76) = 0
Provides:       bundled(musl-headers) = 0
Provides:       bundled(netbsd-getopt) = 0
Conflicts:      hercules
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  regina-rexx
BuildRequires:  regina-rexx-devel
BuildRequires:  sdl-crypto-devel
BuildRequires:  sdl-crypto-static(x86-64)
BuildRequires:  sdl-decnumber-devel
BuildRequires:  sdl-decnumber-static(x86-64)
BuildRequires:  sdl-softfloat-devel
BuildRequires:  sdl-softfloat-static(x86-64)
BuildRequires:  sdl-telnet-devel
BuildRequires:  sdl-telnet-static(x86-64)
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Hercules is an open source software implementation of the mainframe System/370
and ESA/390 architectures, in addition to the latest 64-bit z/Architecture.
Hercules runs under Linux, Windows, Solaris, FreeBSD, and Mac OS X.

This version of Hercules 4.x Hyperion is a SoftDevLabs maintained version of
the Hercules emulator containing fixes for bugs that may still exist in the
original hercules-390 version of Hercules 4.0 Hyperion, as well as enhancements
and improvements to the overall functionality above and beyond what is provided
by the hercules-390 version of Hercules.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
Conflicts:      hercules
%description    data
This package contains data files for %{name}.

%prep

%autosetup -n hyperion-Release_%{version} -p1

# Replace bundled libraries with the system ones
for lib in crypto decNumber SoftFloat telnet; do
  rm -r ${lib}/include
  rm ${lib}/lib/*
  mkdir -p ${lib}/%{libarch}
  ln -s %{_libdir}/lib${lib}%{__isa_bits}.a ${lib}/%{libarch}/lib${lib}%{__isa_bits}.a
done

# Use correct soname for libregina as we don't want to runtime depend on the
# devel package
sed -i 's/libregina.so/libregina.so.%{libregina_major_version}/' hRexx_r.c

# Fix paths and permissions in the example configs
sed -i hercules.cnf \
  -e 's:/usr/local/lib/hercules:%{_libdir}/hercules:g' \
  -e 's:./util/:%{_datadir}/:g' \
  -e 's:/usr/local/share/hercules/:%{_datadir}/hercules/:g'
sed -i 's:_PWD"/util/:"%{_datadir}/hercules/:g' hercules.cnf.rexx
chmod -x hercules.cnf.rexx

%build

./autogen.sh
%configure \
  --enable-ipv6 \
  --enable-cckd-bzip2 \
  --enable-het-bzip2 \
  --enable-optimization="%{optflags}" \
  --enable-capabilities \
  --enable-regina-rexx
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
mkdir stubs
ln -s /bin/true stubs/setcap
export PATH="${PWD}/stubs:${PATH}"
%make_install
rm %{buildroot}%{_libdir}/*.{la,so} %{buildroot}%{_libdir}/hercules/*.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH="%{buildroot}%{_libdir}" make check
%files -f %{oreon_filedir}/main.list
%files -n sdl-hercules-data -f %{oreon_filedir}/sdl-hercules-data.list

%changelog

%autochangelog
