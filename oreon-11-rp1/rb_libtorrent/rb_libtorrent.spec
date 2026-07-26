%global source0_hash f0db58580f4f29ade6cc40fa4ba80e2c9a70c90265cd77332d3cdec37ecf1e6d

%global git_url https://github.com/arvidn/libtorrent
 
Name:		rb_libtorrent
Version:	2.0.11
Release:	5%{?dist}
Summary:	A C++ BitTorrent library aiming to be the best alternative

License:	BSD
URL:		https://www.libtorrent.org
Source0:	%{git_url}/releases/download/v%{version}/libtorrent-rasterbar-%{version}.tar.gz
Source1:	%{name}-README-renames.Fedora
Source2:	%{name}-COPYING.Boost
Source3:	%{name}-COPYING.zlib

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	ninja-build
BuildRequires:	openssl-devel
%if 0%{?fedora} && 0%{?fedora} >= 40
BuildRequires:	openssl-devel-engine
%endif
BuildRequires:	pkgconfig(zlib)
BuildRequires:	util-linux

%description
%{name} is a C++ library that aims to be a good alternative to all
the other BitTorrent implementations around. It is a library and not a full
featured client, although it comes with a few working example clients.

Its main goals are to be very efficient (in terms of CPU and memory usage) as
well as being very easy to use both as a user and developer.

%package 	devel
Summary:	Development files for %{name}
License:	BSD and zlib and Boost
Requires:	%{name}%{?_isa} = %{version}-%{release}
## FIXME: Same include directory. :(
Conflicts:	libtorrent-devel
## Needed for various headers used via #include directives...
Requires:	boost-devel
Requires:	pkgconfig(openssl)

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

The various source and header files included in this package are licensed
under the revised BSD, zlib/libpng, and Boost Public licenses. See the various
COPYING files in the included documentation for the full text of these
licenses, as well as the comments blocks in the source code for which license
a given source or header file is released under.

%package	examples
Summary:	Example clients using %{name}
License:	BSD
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	examples
The %{name}-examples package contains example clients which intend to
show how to make use of its various features. (Due to potential
namespace conflicts, a couple of the examples had to be renamed. See the
included documentation for more details.)

%package	python3
Summary:	Python bindings for %{name}
# Automatically converted from old format: Boost - review is highly recommended.
License:	BSL-1.0
BuildRequires:	python3-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	boost-python3-devel
BuildRequires:	python3-setuptools
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	python3
The %{name}-python3 package contains Python language bindings
(the 'libtorrent' module) that allow it to be used from within
Python applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n "libtorrent-rasterbar-%{version}"

## The RST files are the sources used to create the final HTML files; and are
## not needed.
rm -f docs/*.rst
## Ensure that we get the licenses installed appropriately.
install -p -m 0644 COPYING COPYING.BSD
install -p -m 0644 %{SOURCE2} COPYING.Boost
install -p -m 0644 %{SOURCE3} COPYING.zlib
## Finally, ensure that everything is UTF-8, as it should be.
iconv -t UTF-8 -f ISO_8859-15 AUTHORS -o AUTHORS.iconv
mv AUTHORS.iconv AUTHORS

%build
# This is ugly but can't think of an easier way to build the binding
export CPPFLAGS="$CPPFLAGS $(python%{python3_version}-config --includes)"
export LDFLAGS="$LDFLAGS -L%{_builddir}/libtorrent-rasterbar-%{version}/build/src/.libs"
export PYTHON=/usr/bin/python%{python3_version}
export PYTHON_LDFLAGS="$PYTHON_LDFLAGS $(python%{python3_version}-config --libs)"

%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_SKIP_RPATH=TRUE \
	-GNinja \
	-Dbuild_examples=ON \
	-Dbuild_tests=ON \
	-Dbuild_tools=ON \
	-Dpython-bindings=ON \
	-Dpython-egg-info=ON \
	-Dpython-install-system-dir=OFF
%cmake_build

%check
export LD_LIBRARY_PATH=%{_builddir}/libtorrent-rasterbar-%{version}/%{_vpath_builddir}
pushd %{_vpath_builddir}/test
# Skip UPnP test as it requires a UPnP server on the same network, others due to aarch64 failures
# Make test failures non-fatal as they seem to randomly fail.
echo "set (CTEST_CUSTOM_TESTS_IGNORE
 "test_upnp"
)" > CTestCustom.cmake
ctest -j %{_smp_build_ncpus} || :
popd

%install
mkdir -p %{buildroot}%{_bindir}/

%cmake_install
install -p -m 0755 \
 %{_vpath_builddir}/examples/{client_test,connection_tester,custom_storage,dump_torrent,make_torrent,simple_client,stats_counters,upnp_test} \
 %{_vpath_builddir}/tools/{dht,session_log_alerts} \
 %{buildroot}%{_bindir}/

# Written version is malformed
sed -i 's/^Version:.*/Version: %{version}/' %{buildroot}%{python3_sitearch}/libtorrent.egg-info/PKG-INFO

## Do the renaming due to the somewhat limited %%_bindir namespace.
rename client torrent_client %{buildroot}%{_bindir}/*

install -p -m 0644 %{SOURCE1} ./README-renames.Fedora

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %doc}
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/libtorrent-rasterbar.so.2.*
%{_libdir}/libtorrent-rasterbar.so.2.0

%files	devel
%doc docs/
%license COPYING.Boost COPYING.BSD COPYING.zlib
%{_libdir}/pkgconfig/libtorrent-rasterbar.pc
%{_includedir}/libtorrent/
%{_libdir}/libtorrent-rasterbar.so
%{_libdir}/cmake/LibtorrentRasterbar/
%{_datadir}/cmake/Modules/FindLibtorrentRasterbar.cmake

%files examples
%doc README-renames.Fedora
%license COPYING
%{_bindir}/*torrent*
%{_bindir}/connection_tester
%{_bindir}/custom_storage
%{_bindir}/dht
%{_bindir}/session_log_alerts
%{_bindir}/stats_counters
%{_bindir}/upnp_test

%files	python3
%doc AUTHORS ChangeLog
%license COPYING.Boost
%{python3_sitearch}/libtorrent.egg-info/
%{python3_sitearch}/libtorrent.cpython-*.so

%changelog
%autochangelog
