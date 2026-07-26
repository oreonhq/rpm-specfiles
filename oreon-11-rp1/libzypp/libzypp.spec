%global source0_hash 6b9a3b575d305abe80676e74edceb7ef370ba49900f258037b57782fb449eafc

# Force out of source build
%undefine __cmake_in_source_build

%global min_libsolv_ver 0.7.24

# For the generated library symbol suffix
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif

# Small macro to define (Build)Requires for solv tools
%global req_solv_tool() \
BuildRequires:  %{_bindir}/%{1} \
Requires:       %{_bindir}/%{1}
# End macro

Name:           libzypp
Version:        17.38.1
Release:        1%{?dist}
Summary:        A package management library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://en.opensuse.org/Portal:Libzypp
Source0:        https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Backports from upstream

# Patches proposed upstream

# Fedora specific patches
## Squid installs stuff in the wrong directory (rhbz#2430344)
Patch1001:      zypp-logic-squidproxy-path-check.patch

BuildRequires:  %{_bindir}/asciidoctor
BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  cmake >= 3.1
BuildRequires:  cmake(Notcurses++)
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  gpgme-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl) >= 1.1
BuildRequires:  pkgconfig(readline) >= 5.1
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(zck)
BuildRequires:  boost-devel
BuildRequires:  glib2-devel
BuildRequires:  gettext
BuildRequires:  libsolv-devel >= %{min_libsolv_ver}
BuildRequires:  libsolv-tools >= %{min_libsolv_ver}
# For tests
BuildRequires:  fcgi-devel
BuildRequires:  nginx
BuildRequires:  squid
BuildRequires:  vsftpd

# Ensure specific functionality is enabled for libsolv that libzypp needs
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
# dlopened dependency
Recommends:     libproxy.so.1()%{libsymbolsuffix}

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
# Features we provide (update doc/autoinclude/FeatureTest.doc):
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

# Create directories expected by libzypp
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

# system and vendor config supported:
mkdir -p %{buildroot}%{_sysconfdir}/zypp/zypp.conf.d
mkdir -p %{buildroot}%{_datadir}/zypp/zypp.conf.d

# Create empty file for config
touch %{buildroot}%{_sysconfdir}/zypp/zypp.conf

# Remove needreboot file, we don't have a Fedora-specific one yet...
rm %{buildroot}%{_sysconfdir}/zypp/needreboot

%check
pushd %{_vpath_builddir}
# Tests need to be compiled first and cannot be run in parallel
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:${LD_LIBRARY_PATH} ctest -VV --output-on-failure . || :
popd

%pretrans -p <lua> -n zypp-common
-- Purge repos.d symlink if it exists
path = "%{_sysconfdir}/zypp/repos.d"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files
%license COPYING
%{_libdir}/*.so.*
%{_libexecdir}/zypp/

%files devel
%{_includedir}/zypp/
%{_includedir}/zypp-common/
%{_includedir}/zypp-core/
%{_includedir}/zypp-curl/
%{_includedir}/zypp-media/
%{_includedir}/zypp-tui/
%{_libdir}/libzypp*.so
%{_libdir}/libzypp*.a
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/Zypp/

%files devel-doc
%doc %{_docdir}/libzypp/

%files -n zypp-common -f zypp.lang
%dir %{_sysconfdir}/zypp
%dir %{_sysconfdir}/zypp/services.d
%dir %{_sysconfdir}/zypp/systemCheck.d
%dir %{_sysconfdir}/zypp/vendors.d
%dir %{_sysconfdir}/zypp/multiversion.d
%dir %{_sysconfdir}/zypp/needreboot.d
%dir %{_sysconfdir}/zypp/credentials.d
%dir %{_sysconfdir}/zypp/repos.d
%dir %{_sysconfdir}/zypp/zypp.conf.d
%{_sysconfdir}/zypp/zypp.conf.README
%ghost %config(noreplace) %{_sysconfdir}/zypp/zypp.conf
%config(noreplace) %{_sysconfdir}/zypp/systemCheck
%config(noreplace) %{_sysconfdir}/logrotate.d/zypp-history.lr
%dir %{_sharedstatedir}/zypp/
%dir %attr(750,root,root) %{_localstatedir}/log/zypp
%dir %{_localstatedir}/cache/zypp
%{_mandir}/man5/*.5*
%{_datadir}/zypp/

%files -n zypp-plugins
%{_libexecdir}/zypp/plugins/

%files -n zypp-tools
%{_bindir}/zypp-*
%{_mandir}/man1/*.1*

%changelog
%autochangelog
