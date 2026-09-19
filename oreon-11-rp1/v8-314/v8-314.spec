%global source0_hash e34cdeba269a3fb7bb164b8904b250c34d5be6a1c79bb3d476f10819ea550766

# Hi Googlers! If you're looking in here for patches, nifty.
# You (and everyone else) are welcome to use any of my Chromium spec files and
# patches under the terms of the GPLv2 or later.
# You (and everyone else) are welcome to use any of my V8-specific spec files
# and patches under the terms of the BSD license.
# You (and everyone else) may NOT use my spec files or patches under any other
# terms.
# I hate to be a party-pooper here, but I really don't want to help Google
# make a proprietary browser. There are enough of those already.
# All copyrightable work in these spec files and patches is Copyright 2011
# Tom Callaway <spot@fedoraproject.org>

# This package is like a horrible time capsule. If you're reading this, it
# is never too late to turn back.

# For the 1.2 branch, we use 0s here
# For 1.3+, we use the three digit versions
# Hey, now there are four digits. What do they mean? Popsicle.
%global somajor 3
%global sominor 14
%global sobuild 5
%global sotiny 10
%global sover %{somajor}.%{sominor}.%{sobuild}
%global truename v8
# You don't really want to turn this on, because the "v8" package has this, and we'd
# conflict for no good reason.
%global with_python 0

Name:		%{truename}-314
Version:	%{somajor}.%{sominor}.%{sobuild}.%{sotiny}
Release:	42%{?dist}
Summary:	JavaScript Engine
License:	BSD-3-Clause
URL:		https://developers.google.com/v8/
# Once found at http://commondatastorage.googleapis.com/chromium-browser-official/
# Now, we're the canonical source for the tarball. :/
Source0:	v8-%{version}.tar.bz2
ExclusiveArch:	%{ix86} x86_64 %{arm} mips mipsel ppc ppc64
BuildRequires:	scons, readline-devel, libicu-devel
BuildRequires:	valgrind-devel
BuildRequires:	gcc, gcc-c++

Patch1:		v8-3.14.5.8-CVE-2013-2634.patch

Patch2:		v8-3.14.5.10-CVE-2013-2882.patch

Patch3:		v8-3.14.5.10-CVE-2013-6640.patch

#backport fix for enumeration for objects with lots of properties
#   https://codereview.chromium.org/11362182
Patch4:		v8-3.14.5.10-enumeration.patch

Patch5:		v8-3.14.5.10-CVE-2013-6650.patch

#the other two patches don't affect this version of v8
Patch6:		v8-3.14.5.10-CVE-2014-1704-1.patch

# use clock_gettime() instead of gettimeofday(), which increases performance
# dramatically on virtual machines
# https://github.com/joyent/node/commit/f9ced08de30c37838756e8227bd091f80ad9cafa
# see above link or head of patch for complete rationale
Patch7:		v8-3.14.5.10-use-clock_gettime.patch

# fix corner case in x64 compare stubs
# fixes bug resulting in an incorrect result when comparing certain integers
# (e.g. 2147483647 > -2147483648 is false instead of true)
# https://code.google.com/p/v8/issues/detail?id=2416
# https://github.com/joyent/node/issues/7528
Patch8:		v8-3.14.5.10-x64-compare-stubs.patch

# https://groups.google.com/d/msg/nodejs/-siJEObdp10/2xcqqmTHiEMJ
# https://github.com/joyent/node/commit/530af9cb8e700e7596b3ec812bad123c9fa06356
Patch9:		v8-3.14.5.10-mem-corruption-stack-overflow.patch

# backport bugfix for x64 MathMinMax:
#   Fix x64 MathMinMax for negative untagged int32 arguments.
#   An untagged int32 has zeros in the upper half even if it is negative.
#   Using cmpq to compare such numbers will incorrectly ignore the sign.
# https://github.com/joyent/node/commit/3530fa9cd09f8db8101c4649cab03bcdf760c434
Patch10:	v8-3.14.5.10-x64-MathMinMax.patch

# backport bugfix that eliminates unused-local-typedefs warning
# https://github.com/joyent/node/commit/53b4accb6e5747b156be91a2b90f42607e33a7cc
Patch11:	v8-3.14.5.10-unused-local-typedefs.patch

# backport security fix: Fix Hydrogen bounds check elimination
# https://github.com/joyent/node/commit/fd80a31e0697d6317ce8c2d289575399f4e06d21
Patch12:	v8-3.14.5.10-CVE-2013-6668.patch

# backport fix to segfault caused by the above patch
# https://github.com/joyent/node/commit/3122e0eae64c5ab494b29d0a9cadef902d93f1f9
Patch13:	v8-3.14.5.10-CVE-2013-6668-segfault.patch

# Use system valgrind header
# https://bugzilla.redhat.com/show_bug.cgi?id=1141483
Patch14:	v8-3.14.5.10-system-valgrind.patch

# Fix issues with abort on uncaught exception
# https://github.com/joyent/node/pull/8666
# https://github.com/joyent/node/issues/8631
# https://github.com/joyent/node/issues/8630
Patch15:	v8-3.14.5.10-abort-uncaught-exception.patch

# Fix unhandled ReferenceError in debug-debugger.js
# https://github.com/joyent/node/commit/0ff51c6e063e3eea9e4d9ea68edc82d935626fc7
# https://codereview.chromium.org/741683002
Patch16:	v8-3.14.5.10-unhandled-ReferenceError.patch

# Don't busy loop in CPU profiler thread
# https://github.com/joyent/node/pull/8789
Patch17:	v8-3.14.5.10-busy-loop.patch

# Log V8 version in profiler log file
# (needed for compatibility with profiler tools)
# https://github.com/joyent/node/pull/9043
# https://codereview.chromium.org/806143002
Patch18:	v8-3.14.5.10-profiler-log.patch

# Fix CVE in ARM code
# https://bugzilla.redhat.com/show_bug.cgi?id=1101057
# https://codereview.chromium.org/219473002
Patch19:	v8-3.4.14-CVE-2014-3152.patch

# Add REPLACE_INVALID_UTF8 handling that nodejs needs
Patch20:	v8-3.14.5.10-REPLACE_INVALID_UTF8.patch

# mips support (from debian)
Patch21:	0002_mips.patch
Patch22:	0002_mips_r15102_backport.patch
Patch23:	0002_mips_r19121_backport.patch

# Forced whole instruction cache flushing on Loongson (from debian)
Patch24:	0012_loongson_force_cache_flush.patch

# ppc/ppc64 support (from Ubuntu, who got it from IBM)
# Rediffed from 0099_powerpc_support.patch
Patch25:	v8-powerpc-support.patch

# Fix for CVE-2016-1669 (thanks to bhoordhuis)
Patch26:	v8-3.14.5.10-CVE-2016-1669.patch

# Report builtins by name
# https://github.com/nodejs/node/commit/5a60e0d904c38c2bdb04785203b1b784967c870d
Patch27:	v8-3.14.5.10-report-builtins-by-name.patch

# Fix compile with gcc7
# (thanks to Ben Noordhuis)
Patch28:	v8-3.14.5.10-gcc7.patch

# MOAR PPC
Patch29:	v8-powerpc-support-SConstruct.patch

# GCC8 HAPPY FUN TIME
Patch30:	v8-3.14.5.10-gcc8.patch

# Python3
Patch31:	v8-314-python3.patch

# gcc-11 diagnostics
Patch32:	v8-314-gcc11.patch

# Disable -Werror
Patch33:	v8-3.14.5.10-no-Werror.patch

%description
V8 is Google's open source JavaScript engine. V8 is written in C++ and is used 
in Google Chrome, the open source browser from Google. V8 implements ECMAScript 
as specified in ECMA-262, 3rd edition. This is version 3.14, which is no longer
maintained by Google, but was adopted by a lot of other software.

%package devel
Summary:	Development headers and libraries for v8
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for v8 3.14.

%if 0%{?with_python}
%package python
Summary:	Python libraries from v8
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description python
Python libraries from v8.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{truename}-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1 -b .system-valgrind
%patch -P15 -p1 -b .abort-uncaught-exception
%patch -P16 -p1 -b .unhandled-ReferenceError
%patch -P17 -p1 -b .busy-loop
%patch -P18 -p1 -b .profiler-log
%patch -P19 -p1 -b .cve20143152
%patch -P20 -p1 -b .riu
%patch -P21 -p1 -b .mips
%patch -P22 -p1 -b .r15102
%patch -P23 -p1 -b .r19121
%patch -P24 -p1 -b .loongson
%patch -P25 -p1 -b .ppc
%patch -P26 -p1 -b .CVE-2016-1669
%patch -P27 -p1 -b .builtinname
%patch -P28 -p1 -b .gcc7
%patch -P29 -p1 -b .ppc-harder
%patch -P30 -p1 -b .gcc8
%patch -P31 -p1 -b .python3
%patch -P32 -p1 -b .gcc11
%patch -P33 -p1 -b .no-error

# Do not need this lying about.
rm -rf src/third_party/valgrind

#Patch7 needs -lrt on glibc < 2.17 (RHEL <= 6)
%if (0%{?rhel} > 6 || 0%{?fedora} > 18)
%global lrt %{nil}
%else
%global lrt -lrt
%endif

# -fno-strict-aliasing is needed with gcc 4.4 to get past some ugly code
PARSED_OPT_FLAGS=`echo \'$RPM_OPT_FLAGS %{lrt} -fPIC -fno-strict-aliasing -Wno-unused-parameter -Wno-error=strict-overflow -Wno-unused-but-set-variable -Wno-error=cast-function-type -Wno-error=class-memaccess -Wno-error=stringop-overflow= -Wno-error=array-bounds -Wno-error=dangling-pointer= -Wno-error=use-after-free -fno-delete-null-pointer-checks\'| sed "s/ /',/g" | sed "s/',/', '/g"`
sed -i "s|'-O3',|$PARSED_OPT_FLAGS,|g" SConstruct

# clear spurious executable bits
find . \( -name \*.cc -o -name \*.h -o -name \*.py \) -a -executable \
  |while read FILE ; do
    echo $FILE
    chmod -x $FILE
  done

%build
mkdir -p obj/release/
export GCC_VERSION="44"

# SCons is going away, but for now build with
# I_know_I_should_build_with_GYP=yes
scons library=shared snapshots=on \
%ifarch x86_64
arch=x64 \
%endif
%ifarch ppc64
arch=ppc64 \
%endif
%ifarch ppc
arch=ppc \
%endif
%ifarch armv7hl armv7hnl
armeabi=hard \
%endif
%ifarch armv5tel armv6l armv7l
armeabi=soft \
%endif
visibility=default \
env=CCFLAGS:"-fPIC" \
I_know_I_should_build_with_GYP=yes

%if 0%{?fedora} >= 16
export ICU_LINK_FLAGS=`pkg-config --libs-only-l icu-i18n`
%else
export ICU_LINK_FLAGS=`pkg-config --libs-only-l icu`
%endif

# When will people learn to create versioned shared libraries by default?
# first, lets get rid of the old .so file
rm -rf libv8.so libv8preparser.so
# Now, lets make it right.
g++ $RPM_OPT_FLAGS -fPIC -o libv8preparser.so.%{sover} -shared -Wl,-soname,libv8preparser.so.%{somajor} \
	src/allocation.os \
	src/bignum.os \
	src/bignum-dtoa.os \
	src/cached-powers.os \
	src/diy-fp.os \
	src/dtoa.os \
	src/fast-dtoa.os \
	src/fixed-dtoa.os \
	src/preparse-data.os \
	src/preparser-api.os \
	src/preparser.os \
	src/scanner.os \
	src/strtod.os \
	src/token.os \
	src/unicode.os \
	src/utils.os

# "obj/release/preparser-api.os" should not be included in the libv8.so file.
export RELEASE_BUILD_OBJS=`echo src/*.os | sed 's|src/preparser-api.os||g'`

%ifarch %{arm}
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/arm/*.os $ICU_LINK_FLAGS
%endif
%ifarch %{ix86}
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/ia32/*.os $ICU_LINK_FLAGS
%endif
%ifarch x86_64
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/x64/*.os $ICU_LINK_FLAGS
%endif
%ifarch mips
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/mips/*.os $ICU_LINK_FLAGS
%endif
%ifarch mipsel
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/mipsel/*.os $ICU_LINK_FLAGS
%endif
%ifarch ppc ppc64
g++ $RPM_OPT_FLAGS -fPIC -o libv8.so.%{sover} -shared -Wl,-soname,libv8.so.%{somajor} $RELEASE_BUILD_OBJS src/extensions/*.os src/ppc/*.os $ICU_LINK_FLAGS
%endif

# We need to do this so d8 can link against it.
ln -sf libv8.so.%{sover} libv8.so
ln -sf libv8preparser.so.%{sover} libv8preparser.so

# This will fail to link d8 because it doesn't use the icu libs.
# Don't build d8 shared. Stupid Google. Hate.
# SCons is going away, but for now build with
# I_know_I_should_build_with_GYP=yes
scons d8 \
I_know_I_should_build_with_GYP=yes \
%ifarch x86_64
arch=x64 \
%endif
%ifarch armv7hl armv7hnl
armeabi=hard \
%endif
%ifarch armv5tel armv6l armv7l
armeabi=soft \
%endif
%ifarch ppc64
arch=ppc64 \
%endif
%ifarch ppc
arch=ppc \
%endif
snapshots=on console=readline visibility=default || :
# library=shared snapshots=on console=readline visibility=default || :

# Sigh. I f*****g hate scons.
# But gyp is worse.
# rm -rf d8

# g++ $RPM_OPT_FLAGS -o d8 obj/release/d8.os -lreadline -lpthread -L. -lv8 $ICU_LINK_FLAGS

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_includedir}/v8-3.14/
mkdir -p %{buildroot}%{_libdir}
install -p include/*.h %{buildroot}%{_includedir}/v8-3.14/
install -p libv8.so.%{sover} %{buildroot}%{_libdir}
install -p libv8preparser.so.%{sover} %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 d8 %{buildroot}%{_bindir}/d8-314

pushd %{buildroot}%{_libdir}
ln -sf libv8.so.%{sover} libv8.so
ln -sf libv8.so.%{sover} libv8.so.%{somajor}
ln -sf libv8.so.%{sover} libv8.so.%{somajor}.%{sominor}
ln -sf libv8preparser.so.%{sover} libv8preparser.so
ln -sf libv8preparser.so.%{sover} libv8preparser.so.%{somajor}
ln -sf libv8preparser.so.%{sover} libv8preparser.so.%{somajor}.%{sominor}
popd

chmod -x %{buildroot}%{_includedir}/v8-3.14/v8*.h

mkdir -p %{buildroot}%{_includedir}/v8-3.14/v8/extensions/
install -p src/extensions/*.h %{buildroot}%{_includedir}/v8-3.14/v8/extensions/

chmod -x %{buildroot}%{_includedir}/v8-3.14/v8/extensions/*.h

%if 0%{?with_python}
# install Python JS minifier scripts for nodejs
install -d %{buildroot}%{python_sitelib}
sed -i 's|/usr/bin/python2.4|/usr/bin/env python|g' tools/jsmin.py
sed -i 's|/usr/bin/python2.4|/usr/bin/env python|g' tools/js2c.py
install -p -m0744 tools/jsmin.py %{buildroot}%{python_sitelib}/
install -p -m0744 tools/js2c.py %{buildroot}%{python_sitelib}/
chmod -R -x %{buildroot}%{python_sitelib}/*.py*
%endif

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog
%license LICENSE
%{_bindir}/d8-314
%{_libdir}/*.so.*

%files devel
%{_includedir}/v8-3.14/
%{_libdir}/*.so

%if 0%{?with_python}
%files python
%{python2_sitelib}/j*.py*
%endif

%changelog
%autochangelog
