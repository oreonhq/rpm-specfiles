# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 558544ad358283a7ab2930d69a9ceddf913f4a51ee9bf1bfb9e377322af81a69
%global source1_hash 6698c9f0fa21e940542a0e7e45c88df078ef19ab35d6ad59eccaeae4e696f322
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global commit1 1f5a2f07a565a9465c14d3a8b12f3202f83c775e
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

%global __provides_exclude_from ^%{_libdir}/mozilla/plugins/

Name:           openh264
Version:        2.6.0
Release:        1%{?dist}
Summary:        H.264 codec library

License:        BSD-2-Clause
URL:            https://www.openh264.org/
Source0:        https://github.com/cisco/openh264/archive/v%{version}/openh264-%{version}.tar.gz
Source1:        https://github.com/mozilla/gmp-api/archive/%{commit1}/gmp-api-%{shortcommit1}.tar.gz

Patch0:         0001-Update-shared-lib-version-for-meson-3860.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  make
BuildRequires:  nasm

Obsoletes:      noopenh264 < 1:0

%description
OpenH264 is a codec library which supports H.264 encoding and decoding. It is
suitable for use in real time applications such as WebRTC.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      noopenh264-devel < 1:0

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n mozilla-openh264
Summary:        H.264 codec support for Mozilla browsers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mozilla-filesystem%{?_isa}

%description -n mozilla-openh264
The mozilla-openh264 package contains a H.264 codec plugin for Mozilla
browsers.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%setup -q
%patch -P 0 -p1

tar -xf %{S:1}
mv gmp-api-%{commit1} gmp-api

%build
sed -i -e 's|^CFLAGS_OPT=.*$|CFLAGS_OPT=%{optflags}|' Makefile
sed -i -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|' Makefile
sed -i -e 's|^LIBDIR_NAME=.*$|LIBDIR_NAME=%{_lib}|' Makefile
sed -i -e 's|^SHAREDLIB_DIR=.*$|SHAREDLIB_DIR=%{_libdir}|' Makefile

%ifarch %{ix86}
sed -i -e '/^CFLAGS_OPT=/i LDFLAGS=-Wl,-z,notext' Makefile
%else
sed -i -e '/^CFLAGS_OPT=/i LDFLAGS=%{__global_ldflags}' Makefile
%endif

make %{?_smp_mflags}

make plugin %{?_smp_mflags}

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed
cp -a libgmpopenh264.so* gmpopenh264.info $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed/

mkdir -p $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/pref
cat > $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/pref/gmpopenh264.js << EOF
pref("media.gmp-gmpopenh264.autoupdate", false);
pref("media.gmp-gmpopenh264.version", "system-installed");
EOF

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/gmpopenh264.sh << 'EOF'
if [[ ":$MOZ_GMP_PATH:" != *":%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed:"* ]]; then
    MOZ_GMP_PATH="${MOZ_GMP_PATH}${MOZ_GMP_PATH:+:}%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed"
    export MOZ_GMP_PATH
fi
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fish/vendor_conf.d
cat > $RPM_BUILD_ROOT%{_datadir}/fish/vendor_conf.d/gmpopenh264.fish << 'EOF'
set -x --path MOZ_GMP_PATH $MOZ_GMP_PATH
set dir %{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed
if not contains $dir $MOZ_GMP_PATH
    set -p MOZ_GMP_PATH $dir
end
set -e dir
EOF

rm $RPM_BUILD_ROOT%{_libdir}/*.a

%files
%license LICENSE
%doc README.md
%{_libdir}/libopenh264.so.8
%{_libdir}/libopenh264.so.%{version}

%files devel
%{_includedir}/wels/
%{_libdir}/libopenh264.so
%{_libdir}/pkgconfig/openh264.pc

%files -n mozilla-openh264
%{_sysconfdir}/profile.d/gmpopenh264.sh
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/defaults
%dir %{_libdir}/firefox/defaults/pref
%{_libdir}/firefox/defaults/pref/gmpopenh264.js
%{_libdir}/mozilla/plugins/gmp-gmpopenh264/
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/gmpopenh264.fish

%changelog
%autochangelog
