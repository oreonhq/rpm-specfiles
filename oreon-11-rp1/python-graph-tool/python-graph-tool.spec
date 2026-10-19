%global source0_hash a04ba99fc8745f440fc77dbaca07da4d05cd8d4a96e6aafabdf5c57e3809867d
%global _smp_tasksize_proc 15360
Name:           python-graph-tool
Version:        3.7
Release:        1%{?dist}
Summary:        Efficient network analysis tool written in Python
License:        %{shrink:
                LGPL-3.0-or-later AND
                BSL-1.0 AND
                BSD-3-Clause AND
                GPL-3.0-or-later AND
                MIT AND
                (MIT OR Apache-2.0)
                }
URL:            https://graph-tool.skewed.de/
Source0:        https://downloads.skewed.de/graph-tool/graph-tool-%{version}.tar.bz2
Patch:          https://git.skewed.de/count0/graph-tool/-/merge_requests/78.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  CGAL-devel
BuildRequires:  CGAL-static
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  expat-devel
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gmp-devel
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pcg-cpp-devel
BuildRequires:  pcg-cpp-static
BuildRequires:  pkgconfig(cairomm-1.16)
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pycairo)
BuildRequires:  python3dist(scipy)
BuildRequires:  sparsehash-devel
# /oreon:deps
%description

%package -n python3-graph-tool
Summary:        Efficient network analysis tool written in Python
BuildRequires:  python3-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  CGAL-devel
BuildRequires:  CGAL-static
BuildRequires:  pkgconfig(cairomm-1.16)
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pycairo}
BuildRequires:  python3-cairo-devel
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  sparsehash-devel
BuildRequires:  pcg-cpp-devel
BuildRequires:  pcg-cpp-static
Recommends:     %{py3_dist pycairo}
Recommends:     %{py3_dist matplotlib}
Provides:       graph-tool%{?_isa} = %{version}-%{release}
%description -n python3-graph-tool

%package -n python3-graph-tool-devel
Summary:        Efficient network analysis tool written in Python
License:        LGPL-3.0-or-later AND BSL-1.0
Requires:       python3-graph-tool%{?_isa} = %{version}-%{release}
Requires:       pcg-cpp-devel
Provides:       graph-tool-devel%{?_isa} = %{version}-%{release}
%description -n python3-graph-tool-devel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n graph-tool-%{version}
# Remove shebangs from non-script sources
#
# The pattern of selecting files before modifying them with sed keeps us from
# unnecessarily discarding the original mtimes on unmodified files.
find 'src' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'

# Unbundle pcg-cpp. To avoid having to patch the Makefiles, we use symbolic
# links from the original locations. Note that these are followed when the
# extension API headers are installed, so we need to re-create them afterwards.
rm -vf src/pcg-cpp/include/*
ln -sv \
    '%{_includedir}/pcg_extras.hpp' \
    '%{_includedir}/pcg_random.hpp' \
    '%{_includedir}/pcg_uint128.hpp' \
    'src/pcg-cpp/include/'

# Remove assets for HTML documentation to prove that they are not installed. We
# are most particularly concerned with fonts (in WOFF2 format). To avoid having
# to patch build-system files that explicitly list these assets and expect them
# to exist, we truncate the files to zero length rather than deleting them.
find doc/_static -type f -print -execdir truncate --size=0 '{}' '+'

%conf
./autogen.sh

# We get a few thousand warnings like:
#   warning: 'always_inline' attribute does not apply to types [-Wattributes]
# and since each is very verbose, with a lot of context, the build log explodes
# to many gigabytes, which ends up failing the build. Disable this class of
# warnings as a pragmatic matter.
export CXXFLAGS="${CXXFLAGS-} -Wno-attributes"

# Keeping track of full debugging symbols causes us to run out of *disk space*
# (not memory!) on some koji builders. Reduce the debuginfo level to -g1.
export CXXFLAGS="$(echo "${CXXFLAGS-}" | sed -r 's/(^| )-g($| )/\1-g1\2/')"

%configure \
    --with-python-module-path=%{python3_sitearch} \
    --with-boost-libdir=%{_libdir} \
    --enable-debug

%build

%make_build
%global graph_tool_distinfo graph_tool-%{version}.dist-info
mkdir %{graph_tool_distinfo}
cat > %{graph_tool_distinfo}/METADATA << EOF
Metadata-Version: 2.1
Name: graph-tool
Version: %{version}
Requires-dist: numpy
Requires-dist: scipy
EOF
echo rpm > %{graph_tool_distinfo}/INSTALLER
%install
%make_install
rm -r %{buildroot}/%{_datadir}/doc/graph-tool
find %{buildroot} -name '*.la' -print -delete
ln -svf \
    '%{_includedir}/pcg_extras.hpp' \
    '%{_includedir}/pcg_random.hpp' \
    '%{_includedir}/pcg_uint128.hpp' \
    '%{buildroot}%{python3_sitearch}/graph_tool/include/pcg-cpp/'
cp -a %{graph_tool_distinfo} %{buildroot}%{python3_sitearch}
%oreon_autofiles python3-graph-tool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-graph-tool-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-graph-tool -f %{oreon_filedir}/python3-graph-tool.list
%files -n python3-graph-tool-devel -f %{oreon_filedir}/python3-graph-tool-devel.list

%changelog

%autochangelog
