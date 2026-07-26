%global source0_hash b552bc91817294c7f90ea07d70938642ebf15d5e3bafc81cf7d55efab9995399

Name:           vamp-plugin-sdk
Version:        2.10
Release:        %autorelease
Summary:        An API for audio analysis and feature extraction plugins

%global hostsdk_soname_version 3
%global sdk_soname_version 2

%global gittag %{name}-v%{version}

# KissFFT code in src/vamp-sdk/ext is BSD-3-Clause
# Automatically converted from old format: MIT AND BSD-3-Clause - review is highly recommended.
License:        MIT AND BSD-3-Clause
URL:            https://vamp-plugins.org/
Source:         https://github.com/vamp-plugins/vamp-plugin-sdk/archive/%{gittag}/%{name}-%{version}.tar.gz
Patch:          %{name}-libdir.diff

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel

%description
Vamp is an API for C and C++ plugins that process sampled audio data
to produce descriptive output (measurements or semantic observations).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel = %{version}-%{release}

%description    static
The %{name}-static package contains library files for
developing static applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{gittag}
sed -i 's|/lib/vamp|/%{_lib}/vamp|g' src/vamp-hostsdk/PluginHostAdapter.cpp
sed -i 's|/lib/|/%{_lib}/|g' src/vamp-hostsdk/PluginLoader.cpp

%build
%configure
%make_build

%install
# fix libdir
find . -name '*.pc.in' -exec sed -i 's|/lib|/%{_lib}|' {} ';'
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# create Makefile for examples
cd examples
echo CXXFLAGS=$RPM_OPT_FLAGS -fpic >> Makefile-%{_arch}
echo bundle: `ls *.o` >> Makefile
echo -e "\t"g++ \$\(CXXFLAGS\) -shared -Wl,-Bsymbolic \
     -o vamp-example-plugins.so \
     *.o \$\(pkg-config --libs vamp-sdk\) >> Makefile
echo `ls *.cpp`: >> Makefile
echo -e "\t"g++ \$\(CXXFLAGS\) -c $*.cpp >> Makefile
echo clean: >> Makefile
echo -e "\t"-rm *.o *.so >> Makefile
# clean directory up so we can package the sources
make clean

%check
# Scan shared libs for unpatched '/lib' strings to prevent issues
# on 64-bit multilib platforms.
[ $(strings ${RPM_BUILD_ROOT}%{_libdir}/lib*.so.?|grep /lib/|sed -e 's!/%{_lib}!/__FEDORA-LIB__!g'|grep -c /lib/) -eq 0 ]

%files
%license COPYING
%doc README
%{_libdir}/libvamp-hostsdk.so.%{hostsdk_soname_version}
%{_libdir}/libvamp-hostsdk.so.%{hostsdk_soname_version}.*
%{_libdir}/libvamp-sdk.so.%{sdk_soname_version}
%{_libdir}/libvamp-sdk.so.%{sdk_soname_version}.*
%{_libdir}/vamp

%files devel
%doc examples
%{_bindir}/vamp-*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files static
%{_libdir}/*.a

%changelog
%autochangelog
