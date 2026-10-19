%global source5_hash 0c1d62e7abae0ff77b7dd42b66ec0f0a446990f1c2fb7071dfd675bae41dc7ae
%global source4_hash 2c711deae69718776883184f9c3c1f638e431e0a14bf922f84797b3c75023552
%global source3_hash 30e086ba9b559f12fc854c7f2b60917985052799c182c260e75deee872b80d38
%global source2_hash 2b85363878a45ed20218c951ac234f6ef4f1f7646f7d31554e74ca565691fa40
%global source1_hash 9d8b3899096aeb83e4e21ef8a40fec9e03b28db18c48452efac882ce25a91e27
%global source0_hash 3a2e7a47604ba702f345878308e6fefeca612ee895cf4a5f222e7955fabfe0c0
%global use_tzdata_update 0
%define version_dash %{gsub %{version} %. -}
%define version_underscore %{gsub %{version} %. _}
Name:      icu
Version:   78.3
Release:        1%{?dist}
Summary:        International Components for Unicode
License:   Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND NAIST-2003 AND LicenseRef-Fedora-Public-Domain
URL:       http://site.icu-project.org/
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{version}/icu4c-%{version}-sources.tgz
%if 0%{?use_tzdata_update}
Source1:   https://github.com/unicode-org/icu/releases/download/release-%{version}/icu4c-%{version}-data.zip
Source2:   https://raw.githubusercontent.com/unicode-org/icu-data/main/tzdata/icunew/2022b/44/metaZones.txt
Source3:   https://raw.githubusercontent.com/unicode-org/icu-data/main/tzdata/icunew/2022b/44/timezoneTypes.txt
Source4:   https://raw.githubusercontent.com/unicode-org/icu-data/main/tzdata/icunew/2022b/44/windowsZones.txt
Source5:   https://raw.githubusercontent.com/unicode-org/icu-data/main/tzdata/icunew/2022b/44/zoneinfo64.txt
%endif
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Patch4: gennorm2-man.patch
Patch5: icuinfo-man.patch
Patch6: 3496.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
Tools and utilities for developing with icu.

%package -n lib%{name}
Summary: International Components for Unicode - libraries
%description -n lib%{name}
The International Components for Unicode (ICU) libraries provide
robust and full-featured Unicode services on a wide variety of
platforms. ICU supports the most current version of the Unicode
standard, and they provide support for supplementary Unicode
characters (needed for GB 18030 repertoire support).
As computing environments become more heterogeneous, software
portability becomes more important. ICU lets you produce the same
results across all the various platforms you support, without
sacrificing performance. It offers great flexibility to extend and
customize the supplied services.

%package  -n lib%{name}-devel
Summary:  Development files for International Components for Unicode
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description -n lib%{name}-devel
Includes and definitions for developing with icu.

%package -n lib%{name}-doc
Summary: Documentation for International Components for Unicode
BuildArch: noarch
%description -n lib%{name}-doc
%{summary}.

%{!?endian: %global endian %(%{__python3} -c "import sys;print (0 if sys.byteorder=='big' else 1)")}
# " this line just fixes syntax highlighting for vim that is confused by the above and continues literal

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n icu
%if 0%{?use_tzdata_update}
pushd source
unzip -o %{SOURCE1}
rm -f data/in/icudt*l.dat
cp -v -f %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} data/misc
popd
%endif

%build

pushd source
autoconf
CFLAGS='%optflags -fno-strict-aliasing'
CXXFLAGS='%optflags -fno-strict-aliasing'
%if ! 0%{?endian}
CPPFLAGS='-DU_IS_BIG_ENDIAN=1'
%endif
OPTIONS='--with-data-packaging=library --disable-samples'
%if 0%{?debugtrace}
OPTIONS=$OPTIONS' --enable-debug --enable-tracing'
%endif
%configure $OPTIONS
sed -i 's|-nodefaultlibs -nostdlib||' config/mh-linux
sed -i 's| \$(docfilesdir)/installdox||' Makefile
sed -i '/^\s\+\$(INSTALL_DATA) \$(docsrchfiles) \$(DESTDIR)\$(docdir)\/\$(docsubsrchdir)\s*$/d' Makefile
test -f uconfig.h.prepend && sed -e '/^#define __UCONFIG_H__/ r uconfig.h.prepend' -i common/unicode/uconfig.h
sed -i -r 's|(PKGDATA_OPTS = )|\1-v |' data/Makefile
%make_build
%make_build doc
%install
%make_install %{?_smp_mflags} -C source
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so.*
(
 cd $RPM_BUILD_ROOT%{_bindir}
 mv icu-config icu-config-%{__isa_bits}
)
cat > $RPM_BUILD_ROOT%{_bindir}/icu-config <<'EOF'
bits=$(getconf LONG_BIT 2>/dev/null || echo 64)
exec "/usr/bin/icu-config-${bits}" "$@"
EOF
chmod 755 $RPM_BUILD_ROOT%{_bindir}/icu-config
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

if grep -q @VERSION@ source/tools/*/*.8 source/tools/*/*.1 source/config/*.1; then
    exit 1
fi
%make_build -C source check
pushd source
LD_LIBRARY_PATH=lib:stubdata:tools/ctestfw:$LD_LIBRARY_PATH bin/uconv -l
%files -f %{oreon_filedir}/main.list
%files -n libicu -f %{oreon_filedir}/libicu.list
%files -n libicu-devel -f %{oreon_filedir}/libicu-devel.list
%files -n libicu-doc -f %{oreon_filedir}/libicu-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 77.1-2
- Prepare for Oreon 11 (RP1)
