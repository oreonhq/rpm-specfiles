# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1dd5567b315e19cf4cfb2c32931e535fd65b326960a8770f351d7655439b1eb8
%global source1_hash 59cdcaf255add4721de38eb411d4ecfe779356b61fb671aee63c7dec78054c2b
%global source2_hash f4a8d27429458a529148f90ebafcd1ae9b1968fa323f9e5e40d579a5c8c0288f
%global source3_hash 8ad598c73ad796e0d8280b082cebd82a630d73e73cd3c70057938a6501bba5d7
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global javaver 25
%global filever 25.0.4.1
%global buildver 1
%global vcstag jdk-%{filever}+%{buildver}
%global jvmdir %{_prefix}/lib/jvm
%global jvmhome %{jvmdir}/java-%{javaver}-openjdk
%global altprio 25000

Name:           java-25-openjdk
Epoch:          1
Version:        %{filever}.%{buildver}
Release:        4%{?dist}
Summary:        OpenJDK %{javaver} runtime
License:        GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.org/
ExclusiveArch:  x86_64 aarch64

%global evr %{epoch}:%{version}-%{release}

Source0:        https://github.com/openjdk/jdk%{javaver}u/archive/refs/tags/%{vcstag}.tar.gz#/openjdk-%{vcstag}.tar.gz
Source1:        https://download.java.net/java/GA/jdk25/bd75d5f9689641da8e1daabeccb5528b/36/GPL/openjdk-25_linux-x64_bin.tar.gz
Source2:        https://download.java.net/java/GA/jdk25/bd75d5f9689641da8e1daabeccb5528b/36/GPL/openjdk-25_linux-aarch64_bin.tar.gz
Source3:        https://github.com/google/googletest/archive/v1.14.0/googletest-1.14.0.tar.gz
Patch0:         jdk8347901-c2_unused_leaf_removal.patch
Patch1:         jdk8378713-c2_missing_pow_constant_folding.patch
Patch2:         jdk8367051-clang_noexcept_includes.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  bash
BuildRequires:  clang
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  gawk
BuildRequires:  file
BuildRequires:  findutils
BuildRequires:  tar
BuildRequires:  zip
BuildRequires:  unzip
BuildRequires:  libstdc++-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  cups-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  giflib-devel
BuildRequires:  lcms2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXrandr-devel
%if %{without bootstrap}
BuildRequires:  java-25-openjdk-devel
%endif

Requires:       %{name}-headless%{?_isa} = %{evr}
Requires(post): alternatives
Requires(preun): alternatives

Provides:       java = %{evr}
Provides:       java-%{javaver} = %{evr}
Provides:       java-openjdk = %{evr}
Provides:       java-%{javaver}-openjdk = %{evr}
Provides:       jre = %{evr}
Provides:       jre-%{javaver} = %{evr}
Provides:       jre-openjdk = %{evr}
Provides:       jre-%{javaver}-openjdk = %{evr}

%description
OpenJDK %{javaver} runtime with graphics and sound support.

%package headless
Summary:        OpenJDK %{javaver} headless runtime
Requires:       javapackages-filesystem
Requires:       ca-certificates
Requires(post): alternatives
Requires(preun): alternatives
Provides:       java-headless = %{evr}
Provides:       java-%{javaver}-headless = %{evr}
Provides:       java-openjdk-headless = %{evr}
Provides:       java-%{javaver}-openjdk-headless = %{evr}
Provides:       jre-headless = %{evr}
Provides:       jre-%{javaver}-headless = %{evr}
Provides:       jre-openjdk-headless = %{evr}
Provides:       jre-%{javaver}-openjdk-headless = %{evr}

Provides:       java-25-openjdk-portable = %{evr}
Provides:       java-25-openjdk-portable-fastdebug = %{evr}
Provides:       java-25-openjdk-portable-slowdebug = %{evr}
Provides:       java-25-openjdk-portable-docs = %{evr}
Provides:       java-25-openjdk-portable-misc = %{evr}
Provides:       java-25-openjdk-portable-sources = %{evr}
Obsoletes:      java-25-openjdk-portable < %{evr}
Obsoletes:      java-25-openjdk-portable-fastdebug < %{evr}
Obsoletes:      java-25-openjdk-portable-slowdebug < %{evr}
Obsoletes:      java-25-openjdk-portable-docs < %{evr}
Obsoletes:      java-25-openjdk-portable-misc < %{evr}
Obsoletes:      java-25-openjdk-portable-sources < %{evr}


%description headless
OpenJDK %{javaver} runtime without graphics or sound support.

%package devel
Summary:        OpenJDK %{javaver} development files
Requires:       %{name}%{?_isa} = %{evr}
Requires:       %{name}-jmods%{?_isa} = %{evr}
Requires(post): alternatives
Requires(preun): alternatives
Provides:       java-devel = %{evr}
Provides:       java-%{javaver}-devel = %{evr}
Provides:       java-devel-openjdk = %{evr}
Provides:       java-%{javaver}-openjdk-devel = %{evr}
Provides:       java-sdk = %{evr}
Provides:       java-sdk-%{javaver} = %{evr}
Provides:       java-sdk-openjdk = %{evr}
Provides:       java-sdk-%{javaver}-openjdk = %{evr}
Provides:       java-25-openjdk-portable-devel = %{evr}
Provides:       java-25-openjdk-portable-devel-fastdebug = %{evr}
Provides:       java-25-openjdk-portable-devel-slowdebug = %{evr}
Provides:       java-25-openjdk-portable-static-libs = %{evr}
Provides:       java-25-openjdk-portable-static-libs-fastdebug = %{evr}
Provides:       java-25-openjdk-portable-static-libs-slowdebug = %{evr}
Obsoletes:      java-25-openjdk-portable-devel < %{evr}
Obsoletes:      java-25-openjdk-portable-devel-fastdebug < %{evr}
Obsoletes:      java-25-openjdk-portable-devel-slowdebug < %{evr}
Obsoletes:      java-25-openjdk-portable-static-libs < %{evr}
Obsoletes:      java-25-openjdk-portable-static-libs-fastdebug < %{evr}
Obsoletes:      java-25-openjdk-portable-static-libs-slowdebug < %{evr}

%description devel
OpenJDK %{javaver} development tools and headers.

%package jmods
Summary:        OpenJDK %{javaver} jmods
Requires:       %{name}-headless%{?_isa} = %{evr}
Provides:       java-jmods = %{evr}
Provides:       java-%{javaver}-jmods = %{evr}
Provides:       java-openjdk-jmods = %{evr}

%description jmods
OpenJDK %{javaver} jmod files for jlink.

%package src
Summary:        OpenJDK %{javaver} source archive
Requires:       %{name}-headless%{?_isa} = %{evr}
Provides:       java-src = %{evr}
Provides:       java-%{javaver}-src = %{evr}
Provides:       java-openjdk-src = %{evr}

%description src
OpenJDK %{javaver} source zip for debugging.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%autosetup -n jdk%{javaver}u-jdk-%{filever}-%{buildver} -p1
tar -C .. -xf %{SOURCE3}

%build
export CC=clang
export CXX=clang++
export AR=llvm-ar
export NM=llvm-nm
extra_cflags="$(printf '%s\n' "${CFLAGS:-}" | sed -e 's/-fexceptions//g') -gdwarf-4 -gdwarf-aranges"
extra_cxxflags="$(printf '%s\n' "${CXXFLAGS:-}" | sed -e 's/-fexceptions//g') -gdwarf-4 -gdwarf-aranges"
extra_ldflags="${LDFLAGS:-}"
export CFLAGS= CXXFLAGS= LDFLAGS=
%if %{with bootstrap}
rm -rf bootjdk
mkdir bootjdk
%ifarch x86_64
tar -C bootjdk --strip-components=1 -xf %{SOURCE1}
%endif
%ifarch aarch64
tar -C bootjdk --strip-components=1 -xf %{SOURCE2}
%endif
bootjdk="$PWD/bootjdk"
%else
bootjdk=%{jvmhome}
%endif
bash ./configure \
    --prefix=%{jvmhome} \
    --with-boot-jdk="$bootjdk" \
    --with-gtest="$PWD/../googletest-1.14.0" \
    --with-toolchain-type=clang \
    --with-debug-level=release \
    --with-jvm-variants=server \
    --with-native-debug-symbols=none \
    --with-stdc++lib=dynamic \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=system \
    --with-freetype=system \
    --with-harfbuzz=system \
    --with-extra-cflags="$extra_cflags" \
    --with-extra-cxxflags="$extra_cxxflags" \
    --with-extra-ldflags="$extra_ldflags" \
    --with-jobs=%{?_smp_build_ncpus}%{!?_smp_build_ncpus:1} \
    --disable-warnings-as-errors \
    --disable-precompiled-headers \
    --enable-dtrace=no \
    --with-version-pre= \
    --with-version-opt=or11 \
    --with-version-build=%{buildver} \
    --with-vendor-name=Oreon \
    --with-vendor-url=https://oreonhq.com/ \
    --with-vendor-bug-url=https://github.com/oreonhq/rpm-specfiles/issues \
    --with-vendor-vm-bug-url=https://github.com/oreonhq/rpm-specfiles/issues \
    --with-vendor-version-string=Oreon-%{version}-%{release}
make LOG=info jdk-image

%check
make LOG=info test-hotspot-gtest

%install
install -d %{buildroot}%{jvmhome}
cp -a build/*/images/jdk/. %{buildroot}%{jvmhome}/
rm -rf %{buildroot}%{jvmhome}/demo
rm -rf %{buildroot}%{jvmhome}/man

%post headless
%{_sbindir}/alternatives --install %{_bindir}/java java %{jvmhome}/bin/java %{altprio} \
    --slave %{_bindir}/jfr jfr %{jvmhome}/bin/jfr \
    --slave %{_bindir}/jrunscript jrunscript %{jvmhome}/bin/jrunscript \
    --slave %{_bindir}/keytool keytool %{jvmhome}/bin/keytool \
    --slave %{_bindir}/rmiregistry rmiregistry %{jvmhome}/bin/rmiregistry \
    --slave %{jvmdir}/jre jre %{jvmhome}

%preun headless
if [ $1 -eq 0 ]; then
    %{_sbindir}/alternatives --remove java %{jvmhome}/bin/java
fi

%post devel
%{_sbindir}/alternatives --install %{_bindir}/javac javac %{jvmhome}/bin/javac %{altprio} \
    --slave %{_bindir}/jar jar %{jvmhome}/bin/jar \
    --slave %{_bindir}/jarsigner jarsigner %{jvmhome}/bin/jarsigner \
    --slave %{_bindir}/javadoc javadoc %{jvmhome}/bin/javadoc \
    --slave %{_bindir}/javap javap %{jvmhome}/bin/javap \
    --slave %{_bindir}/jlink jlink %{jvmhome}/bin/jlink \
    --slave %{_bindir}/jmod jmod %{jvmhome}/bin/jmod \
    --slave %{_bindir}/jdeps jdeps %{jvmhome}/bin/jdeps \
    --slave %{_bindir}/jshell jshell %{jvmhome}/bin/jshell \
    --slave %{_bindir}/jcmd jcmd %{jvmhome}/bin/jcmd \
    --slave %{_bindir}/jmap jmap %{jvmhome}/bin/jmap \
    --slave %{_bindir}/jps jps %{jvmhome}/bin/jps \
    --slave %{_bindir}/jstack jstack %{jvmhome}/bin/jstack \
    --slave %{_bindir}/jstat jstat %{jvmhome}/bin/jstat \
    --slave %{_bindir}/jinfo jinfo %{jvmhome}/bin/jinfo \
    --slave %{_bindir}/jhsdb jhsdb %{jvmhome}/bin/jhsdb \
    --slave %{_bindir}/jconsole jconsole %{jvmhome}/bin/jconsole \
    --slave %{_bindir}/jpackage jpackage %{jvmhome}/bin/jpackage \
    --slave %{_bindir}/jdeprscan jdeprscan %{jvmhome}/bin/jdeprscan \
    --slave %{_bindir}/jwebserver jwebserver %{jvmhome}/bin/jwebserver \
    --slave %{_bindir}/serialver serialver %{jvmhome}/bin/serialver \
    --slave %{jvmdir}/java java_sdk %{jvmhome}

%preun devel
if [ $1 -eq 0 ]; then
    %{_sbindir}/alternatives --remove javac %{jvmhome}/bin/javac
fi

%files
%{jvmhome}/lib/libawt_xawt.so
%{jvmhome}/lib/libfontmanager.so
%{jvmhome}/lib/libjavajpeg.so
%{jvmhome}/lib/libjawt.so
%{jvmhome}/lib/libjsound.so
%{jvmhome}/lib/liblcms.so
%{jvmhome}/lib/libsplashscreen.so

%files headless
%license LICENSE ASSEMBLY_EXCEPTION
%dir %{jvmhome}
%{jvmhome}/*
%exclude %{jvmhome}/bin
%exclude %{jvmhome}/include
%exclude %{jvmhome}/jmods
%{jvmhome}/bin/java
%{jvmhome}/bin/jfr
%{jvmhome}/bin/jrunscript
%{jvmhome}/bin/keytool
%{jvmhome}/bin/rmiregistry
%exclude %{jvmhome}/lib/src.zip
%exclude %{jvmhome}/lib/libawt_xawt.so
%exclude %{jvmhome}/lib/libfontmanager.so
%exclude %{jvmhome}/lib/libjavajpeg.so
%exclude %{jvmhome}/lib/libjawt.so
%exclude %{jvmhome}/lib/libjsound.so
%exclude %{jvmhome}/lib/liblcms.so
%exclude %{jvmhome}/lib/libsplashscreen.so

%files devel
%dir %{jvmhome}/bin
%{jvmhome}/bin/*
%exclude %{jvmhome}/bin/java
%exclude %{jvmhome}/bin/jfr
%exclude %{jvmhome}/bin/jrunscript
%exclude %{jvmhome}/bin/keytool
%exclude %{jvmhome}/bin/rmiregistry
%{jvmhome}/include

%files jmods
%{jvmhome}/jmods

%files src
%{jvmhome}/lib/src.zip

%changelog
%autochangelog
