%global source1_hash edd2c5b3ebd5ac33f038e346c772d1f3e7168481ae3e3f71248152a370a04860
%global source0_hash e637c32731dc07396b812c4019f34d1417a3f7aa39d450b7f27c9bcdc23b3e12
%global mingw_build_ucrt64 1
%{?mingw_package_header}
Name:          mingw-objfw
Version:       1.5.7
Release:        1%{?dist}
Summary:        MinGW port of ObjFW
License:       LGPL-3.0-only
URL:           https://objfw.nil.im
Source0:        https://objfw.nil.im/downloads/objfw-%{version}.tar.gz
Source1:       https://objfw.nil.im/downloads/objfw-%{version}.tar.gz.sig
Source2:       gpgkey-objfw.gpg
BuildArch:     noarch
# oreon:deps
BuildRequires:  clang
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-openssl
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-openssl
# /oreon:deps
%description
ObjFW is a portable, lightweight framework for the Objective-C language. It
enables you to write an application in Objective-C that will run on any
platform supported by ObjFW without having to worry about differences between
operating systems or various frameworks you would otherwise need if you want to
be portable.

It supports all modern Objective-C features when using Clang, but is also
compatible with GCC ≥ 4.6 to allow maximum portability.

ObjFW also comes with its own lightweight and extremely fast Objective-C
runtime, which in real world use cases was found to be significantly faster
than both GNU's and Apple's runtime.

%package -n mingw32-objfw
Summary:       MinGW port of ObjFW
Requires:      mingw32-openssl
%description -n mingw32-objfw
MinGW port of ObjFW for mingw32

%package -n mingw64-objfw
Summary:       MinGW port of ObjFW
Requires:      mingw64-openssl
%description -n mingw64-objfw
MinGW port of ObjFW for mingw64

%package -n ucrt64-objfw
Summary:       MinGW port of ObjFW
Requires:      ucrt64-openssl
%description -n ucrt64-objfw
MinGW port of ObjFW for ucrt64

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p0 -n objfw-%{version}

mkdir ../mingw32
mv * ../mingw32
mv ../mingw32/COPYING ../mingw32/COPYING.LESSER .
mv ../mingw32 .
cp -Rp mingw32 mingw64
cp -Rp mingw32 ucrt64

%build

pushd mingw32
%mingw32_configure --with-tls=openssl                     \
                   --disable-silent-rules                 \
                   OBJC="clang -target %{mingw32_target}" \
                   OBJCFLAGS="$mingw32_cflags"            \
                   LDFLAGS="$mingw32_ldflags"
%make_build
popd
pushd mingw64
%mingw64_configure --with-tls=openssl                     \
                   --disable-silent-rules                 \
                   OBJC="clang -target %{mingw64_target}" \
                   OBJCFLAGS="$mingw64_cflags"            \
                   LDFLAGS="$mingw64_ldflags"
%make_build
popd
pushd ucrt64
%ucrt64_configure --with-tls=openssl                    \
                  --enable-static                       \
                  --disable-silent-rules                \
                  OBJC="clang -target %{ucrt64_target}" \
                  OBJCFLAGS="$ucrt64_cflags"            \
                  LDFLAGS="$ucrt64_ldflags"
%make_build
popd
%install
mkdir -p %{buildroot}/%{_bindir}
pushd mingw32
%make_install
for i in objfw-config objfw-compile objfw-embed; do
        mv %{buildroot}/%{mingw32_bindir}/%{mingw32_target}-$i %{buildroot}/%{_bindir}/
done
for i in objfw-new ofarc ofdns ofhash ofhttp ofgctester; do
        rm %{buildroot}/%{mingw32_bindir}/$i.exe
        rm -fr %{buildroot}/%{mingw32_datadir}/$i
done
rm %{buildroot}/%{mingw32_mandir}/man1/*.1
popd
pushd mingw64
%make_install
for i in objfw-config objfw-compile objfw-embed; do
        mv %{buildroot}/%{mingw64_bindir}/%{mingw64_target}-$i %{buildroot}/%{_bindir}/
done
for i in objfw-new ofarc ofdns ofhash ofhttp ofgctester; do
        rm %{buildroot}/%{mingw64_bindir}/$i.exe
        rm -fr %{buildroot}/%{mingw64_datadir}/$i
done
rm %{buildroot}/%{mingw64_mandir}/man1/*.1
popd
pushd ucrt64
%make_install
for i in objfw-config objfw-compile objfw-embed; do
        mv %{buildroot}/%{ucrt64_bindir}/%{ucrt64_target}-$i %{buildroot}/%{_bindir}/
done
for i in objfw-new ofarc ofdns ofhash ofhttp ofgctester; do
        rm %{buildroot}/%{ucrt64_bindir}/$i.exe
        rm -fr %{buildroot}/%{ucrt64_datadir}/$i
done
rm %{buildroot}/%{ucrt64_mandir}/man1/*.1
popd
%oreon_autofiles mingw32-objfw usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-objfw usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-objfw usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-objfw -f %{oreon_filedir}/mingw32-objfw.list
%files -n mingw64-objfw -f %{oreon_filedir}/mingw64-objfw.list
%files -n ucrt64-objfw -f %{oreon_filedir}/ucrt64-objfw.list

%changelog

%autochangelog
