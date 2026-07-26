%global source0_hash 33f12605e0054965996c25c1382b3e463b0af91799001f5bb8c0630f2ec8c852

# FORCE NOARCH
# This package is noarch intentionally, although it supplies binaries,
# as they're not intended for the build platform, but for ARM.
# The related discussion can be found here:
# https://www.redhat.com/archives/fedora-devel-list/2009-February/msg02261.html
%global _binaries_in_noarch_packages_terminate_build 0

%global target arm-none-eabi
%global pkg_version %{version}

Name:           %{target}-newlib
Version:        4.5.0.20241231
Release:        5%{?dist}
Summary:        C library intended for use on %{target} embedded systems
# For a breakdown of the licensing, see NEWLIB-LICENSING
License:        BSD-2-Clause AND BSD-4-Clause AND LGPL-2.1-or-later AND ISC AND GPL-3.0-or-later AND MIT
URL:            http://sourceware.org/newlib/
Source0:        ftp://sourceware.org/pub/newlib/newlib-%{pkg_version}.tar.gz
Source1:        README.fedora
Source2:        NEWLIB-LICENSING

BuildRequires:  gcc
BuildRequires:  %{target}-binutils %{target}-gcc %{target}-gcc-c++ texinfo texinfo-tex
BuildRequires: make
BuildArch:      noarch

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software licenses
that make them easily usable on embedded products.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n newlib-%{pkg_version}

%build
rm -rf build-{newlib,nano}
mkdir build-{newlib,nano}

pushd build-newlib

export CFLAGS_FOR_TARGET="-g -O2 -ffunction-sections -fdata-sections"
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --htmldir=%{_docdir}/html \
    --pdfdir=%{_docdir}/pdf \
    --target=%{target} \
    --enable-newlib-io-long-long \
    --enable-newlib-register-fini \
    --enable-newlib-retargetable-locking \
    --disable-newlib-supplied-syscalls \
    --disable-nls \
    --enable-multilib \
    --disable-libssp \
    --with-float=soft

make

popd
pushd build-nano
export CFLAGS_FOR_TARGET="-g -Os -ffunction-sections -fdata-sections"
../configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --target=%{target} \
    --disable-newlib-supplied-syscalls    \
    --enable-newlib-reent-small           \
    --enable-newlib-retargetable-locking  \
    --disable-newlib-fvwrite-in-streamio  \
    --disable-newlib-fseek-optimization   \
    --disable-newlib-wide-orient          \
    --enable-newlib-nano-malloc           \
    --disable-newlib-unbuf-stream-opt     \
    --enable-lite-exit                    \
    --enable-newlib-global-atexit         \
    --enable-newlib-nano-formatted-io     \
    --disable-nls

make -j

popd

%install
pushd build-newlib
make install DESTDIR=%{buildroot}
popd
pushd build-nano
NANO_ROOT=%{buildroot}/nano
make install DESTDIR=$NANO_ROOT

for i in $(find $NANO_ROOT -regex ".*/lib\(c\|g\|rdimon\)\.a"); do
    file=$(basename $i | sed "s|\.a|_nano\.a|")
    target_path=$(dirname $i | sed "s|$NANO_ROOT||")
    cp $i "%{buildroot}$target_path/$file"
done
mkdir -p %{buildroot}/usr/arm-none-eabi/include/newlib-nano/
cp -p $NANO_ROOT/usr/arm-none-eabi/include/newlib.h %{buildroot}/usr/arm-none-eabi/include/newlib-nano/newlib.h
popd

cp %{SOURCE1} .
cp %{SOURCE2} .

# we don't want these as we are a cross version
rm -rf %{buildroot}%{_infodir}

rm -rf $NANO_ROOT
# despite us being noarch redhat-rpm-config insists on stripping our files
%global __os_install_post /usr/lib/rpm/brp-compress

%files
%doc README.fedora
%license NEWLIB-LICENSING COPYING*
%dir %{_prefix}/%{target}
%dir %{_prefix}/%{target}/include/
%{_prefix}/%{target}/include/*
%dir %{_prefix}/%{target}/lib
%{_prefix}/%{target}/lib/*

%changelog
%autochangelog
