%global source0_hash 0f163516ecef2e3331500266751de3098835a3c3ae0c2290448046c632bc0e93
%global git_url https://github.com/arvidn/libtorrent
Name:		rb_libtorrent
Version:	2.1.1
Release:        1%{?dist}
Summary:        A C++ BitTorrent library aiming to be the best alternative
License:	BSD
URL:		https://www.libtorrent.org
Source0:        %{git_url}/releases/download/v%{version}/libtorrent-rasterbar-%{version}.tar.gz
Source1:	%{name}-README-renames.Fedora
Source2:	%{name}-COPYING.Boost
Source3:	%{name}-COPYING.zlib
# oreon:deps
BuildRequires:  boost-python3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  util-linux
# /oreon:deps
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
Conflicts:	libtorrent-devel
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
sed -i 's/^Version:.*/Version: %{version}/' %{buildroot}%{python3_sitearch}/libtorrent.egg-info/PKG-INFO
rename client torrent_client %{buildroot}%{_bindir}/*
install -p -m 0644 %{SOURCE1} ./README-renames.Fedora
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rb_libtorrent-devel -f %{oreon_filedir}/rb_libtorrent-devel.list
%files -n rb_libtorrent-examples -f %{oreon_filedir}/rb_libtorrent-examples.list
%files -n rb_libtorrent-python3 -f %{oreon_filedir}/rb_libtorrent-python3.list

%changelog

%autochangelog
