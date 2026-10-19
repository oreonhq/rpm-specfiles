%global source0_hash 631836aba00cdd445867c89ba8682d58cbab6e30f9f73700721631652c6a7767
%undefine __cmake_in_source_build
%global min_libsolv_ver 0.7.24
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif
%global req_solv_tool() \
Requires:       %{_bindir}/%{1}
Name:           libzypp
Version:        17.38.15
Release:        1%{?dist}
Summary:        A package management library
License:        GPL-2.0-or-later
URL:            https://en.opensuse.org/Portal:Libzypp
Source0:        https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1001:      zypp-logic-squidproxy-path-check.patch
%req_solv_tool  repo2solv
%req_solv_tool  rpmmd2solv
%req_solv_tool  helix2solv
%req_solv_tool  susetags2solv
%req_solv_tool  comps2solv
%req_solv_tool  appdata2solv
Requires:       libsolv-tools >= %{min_libsolv_ver}
Requires:       zypp-common = %{version}-%{release}
Requires:       zypp-plugins = %{version}-%{release}
Requires:       zypp-tools = %{version}-%{release}
Requires:       gnupg2
Recommends:     libproxy.so.1()%{libsymbolsuffix}
# oreon:deps
BuildRequires:  //bin/appdata2solv
BuildRequires:  //bin/asciidoctor
BuildRequires:  //bin/comps2solv
BuildRequires:  //bin/helix2solv
BuildRequires:  //bin/repo2solv
BuildRequires:  //bin/rpmmd2solv
BuildRequires:  //bin/susetags2solv
BuildRequires:  //bin/xsltproc
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(Notcurses++)
BuildRequires:  doxygen
BuildRequires:  fcgi-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gpgme-devel
BuildRequires:  graphviz
BuildRequires:  libsolv-devel
BuildRequires:  libsolv-tools
BuildRequires:  nginx
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(zck)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  squid
BuildRequires:  vsftpd
# /oreon:deps
%description
libzypp is a library for package management built on top of the
libsolv library. It is the foundation for the Zypper package manager.

%package -n zypp-common
Summary:        Common files for ZYpp
BuildArch:      noarch
%description -n zypp-common
This package provides the common files expected by %{name}
and its consumers.

%package -n zypp-plugins
Summary:        Plugins for %{name} users
Provides:       libzypp(plugin) = 0.1
Provides:       libzypp(plugin:appdata) = 0
Provides:       libzypp(plugin:commit) = 1
Provides:       libzypp(plugin:services) = 1
Provides:       libzypp(plugin:system) = 1
Provides:       libzypp(plugin:urlresolver) = 0
Provides:       libzypp(plugin:repoverification) = 0
Provides:       libzypp(repovarexpand) = 1.1
Provides:       libzypp(econf) = 0
Requires:       zypp-common = %{version}-%{release}
BuildArch:      noarch
%description -n zypp-plugins
The zypp-plugins package contains various plugin binaries used
by consumers of %{name}.

%package -n zypp-tools
Summary:        Tools for %{name} users
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n zypp-tools
The zypp-tools package contains tools shipped for consumers
of %{name} to use.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libsolv-devel%{?_isa} >= %{min_libsolv_ver}
Requires:       boost-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Documentation for development using %{name}
BuildArch:      noarch
%description    devel-doc
The %{name}-devel-doc package contains documentation for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Use correct libexecdir
find -type f -exec sed -i -e "s|/usr/lib/zypp|%{_libexecdir}/zypp|g" {} ';'
find -type f -exec sed -i -e "s|\${CMAKE_INSTALL_PREFIX}/lib/zypp|\${CMAKE_INSTALL_PREFIX}/libexec/zypp|g" {} ';'

# Update tests to use correct vendorconfdir
# Cf. https://github.com/openSUSE/libzypp/issues/693
find -type f -exec sed -i -e "s|/usr/etc|%{_datadir}|g" {} ';'
find -type f -exec sed -i -e "s|\${CMAKE_INSTALL_PREFIX}/etc|\${CMAKE_INSTALL_PREFIX}/share|g" {} ';'

%conf
%cmake \
         -DCMAKE_BUILD_TYPE=RelWithDebInfo \
         -DZYPPCONFDIR=%{_datadir} \
         -DDOC_INSTALL_DIR=%{_docdir} \
         -DENABLE_BUILD_DOCS=ON \
         -DENABLE_BUILD_TESTS=ON \
         -DENABLE_BUILD_TRANS=ON \
         -DENABLE_VISIBILITY_HIDDEN=ON \
         -DENABLE_ZCHUNK_COMPRESSION=ON \
         -DENABLE_ZSTD_COMPRESSION=ON \
         %{nil}

%build

%cmake_build
%install
%cmake_install
%find_lang zypp
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p %{buildroot}%{_sysconfdir}/zypp/repos.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/services.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/systemCheck.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/vendors.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/multiversion.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/needreboot.d
mkdir -p %{buildroot}%{_sysconfdir}/zypp/credentials.d
mkdir -p %{buildroot}%{_libexecdir}/zypp
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/appdata
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/commit
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/services
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/system
mkdir -p %{buildroot}%{_libexecdir}/zypp/plugins/urlresolver
mkdir -p %{buildroot}%{_sharedstatedir}/zypp
mkdir -p %{buildroot}%{_localstatedir}/log/zypp
mkdir -p %{buildroot}%{_localstatedir}/cache/zypp
mkdir -p %{buildroot}%{_sysconfdir}/zypp/zypp.conf.d
mkdir -p %{buildroot}%{_datadir}/zypp/zypp.conf.d
touch %{buildroot}%{_sysconfdir}/zypp/zypp.conf
rm %{buildroot}%{_sysconfdir}/zypp/needreboot
%oreon_autofiles zypp-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles zypp-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles zypp-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

pushd %{_vpath_builddir}
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:${LD_LIBRARY_PATH} ctest -VV --output-on-failure . || :
popd
%pretrans -p <lua> -n zypp-common

-- Purge repos.d symlink if it exists
path = "%{_sysconfdir}/zypp/repos.d"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end
%files -f %{oreon_filedir}/main.list
%files -n zypp-common -f %{oreon_filedir}/zypp-common.list
%files -n zypp-plugins -f %{oreon_filedir}/zypp-plugins.list
%files -n zypp-tools -f %{oreon_filedir}/zypp-tools.list
%files -n libzypp-devel -f %{oreon_filedir}/libzypp-devel.list
%files -n libzypp-devel-doc -f %{oreon_filedir}/libzypp-devel-doc.list

%changelog

%autochangelog
