%global source0_hash 558544ad358283a7ab2930d69a9ceddf913f4a51ee9bf1bfb9e377322af81a69

# To get the gmp-api commit to use, run:
# rm -rf gmp-api;make gmp-bootstrap;cd gmp-api;git rev-parse HEAD
%global commit1 1f5a2f07a565a9465c14d3a8b12f3202f83c775e
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# Filter out soname provides for the mozilla plugin
%global __provides_exclude_from ^%{_libdir}/mozilla/plugins/

## WARNING ##
#
# These builds can not end up in the main buildroot automatically for
# legal reasons.
#
# It needs to be built into dedicated openh264 tags with:
#
#    fedpkg build --target=f*-openh264
#
Name:           openh264
Version:        2.6.0
Release:        2%{?dist}
Summary:        H.264 codec library

License:        BSD-2-Clause
URL:            https://www.openh264.org/
Source0:        https://github.com/cisco/openh264/archive/refs/tags/v%{version}/openh264-%{version}.tar.gz
Source1:        https://github.com/mozilla/gmp-api/archive/refs/tags/%{commit1}/gmp-api-%{shortcommit1}.tar.gz

Patch0:         0001-Update-shared-lib-version-for-meson-3860.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nasm

# Replace the stub package
Obsoletes:      noopenh264 < 1:0

%description
OpenH264 is a codec library which supports H.264 encoding and decoding. It is
suitable for use in real time applications such as WebRTC.



%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Replace the stub package
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P 0 -p1

# Extract gmp-api archive
tar -xf %{S:1}
mv gmp-api-%{commit1} gmp-api


%build
# Update the makefile with our build options
# Must be done in %%build in order to pick up correct LDFLAGS.
sed -i -e 's|^CFLAGS_OPT=.*$|CFLAGS_OPT=%{optflags}|' Makefile
sed -i -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|' Makefile
sed -i -e 's|^LIBDIR_NAME=.*$|LIBDIR_NAME=%{_lib}|' Makefile
sed -i -e 's|^SHAREDLIB_DIR=.*$|SHAREDLIB_DIR=%{_libdir}|' Makefile
sed -i -e '/^CFLAGS_OPT=/i LDFLAGS=%{__global_ldflags}' Makefile

# First build the openh264 libraries
make %{?_smp_mflags}

# ... then build the mozilla plugin
make plugin %{?_smp_mflags}


%install
%make_install

# Install mozilla plugin
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

# Remove static libraries
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
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.0-2
- Import from Fedora dist-git f43 for Oreon 11
