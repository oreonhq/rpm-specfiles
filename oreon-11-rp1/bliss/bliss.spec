%global source0_hash 0acb23352184cbd0c06c361032743de0bff813b6e2460f102dc03c1e9d1a0907

%global giturl  https://github.com/scipopt/Bliss

Name:           bliss
Version:        0.77
Release:        13%{?dist}
Summary:        Compute automorphism groups and canonical labelings of graphs

License:        LGPL-3.0-only
URL:            https://users.aalto.fi/~tjunttil/bliss/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/Bliss-%{version}.tar.gz
# Man page written by Jerry James using text borrowed from the sources.
# The man page therefore has the same copyright and license as the sources.
Source1:        bliss.1
# Patch from Thomas Rehn, sent upstream 28 Oct 2011.  Fix one bug and add one
# performance enhancement.
Patch:          bliss-rehn.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Bliss is an open source tool for computing automorphism groups and canonical
forms of graphs.  It has both a command line user interface as well as C++ and
C programming language APIs.

%package devel
# The content is LGPL-3.0-only.  Other licenses are due to files installed by
# doxygen.
# html/bc_s.png: GPL-1.0-or-later
# html/bdwn.png: GPL-1.0-or-later
# html/closed.png: GPL-1.0-or-later
# html/doc.png: GPL-1.0-or-later
# html/doxygen.css: GPL-1.0-or-later
# html/doxygen.svg: GPL-1.0-or-later
# html/dynsections.js: MIT
# html/folderclosed.png: GPL-1.0-or-later
# html/folderopen.png: GPL-1.0-or-later
# html/jquery.js: MIT
# html/menu.js: MIT
# html/menudata.js: MIT
# html/nav_f.png: GPL-1.0-or-later
# html/nav_g.png: GPL-1.0-or-later
# html/nav_h.png: GPL-1.0-or-later
# html/open.png: GPL-1.0-or-later
# html/splitbar.png: GPL-1.0-or-later
# html/sync_off.png: GPL-1.0-or-later
# html/sync_on.png: GPL-1.0-or-later
# html/tab_a.png: GPL-1.0-or-later
# html/tab_b.png: GPL-1.0-or-later
# html/tab_h.png: GPL-1.0-or-later
# html/tab_s.png: GPL-1.0-or-later
# html/tabs.css: GPL-1.0-or-later
License:        LGPL-3.0-only AND MIT AND GPL-1.0-or-later
Summary:        Headers and library files for developing with bliss
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
Headers and library files needed to develop applications that use the bliss
library.

%package libs
Summary:        Compute automorphism groups and canonical labelings of graphs

%description libs
A command-line bliss tool to access the functionality of the bliss library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Bliss-%{version} -p0

%conf
# Do not override Fedora build flags.  The last sagemath version added an
# soname.  Duplicate it for compatibility.  Link the library with libgmp.
# Hidden symbols hide ALL symbols, meaning we can't use the library.
sed -e 's/ -O3//' \
    -e '/POSITION_INDEPENDENT/a\ \ VERSION 2.0.0 SOVERSION 2' \
    -e '/^install($/itarget_link_libraries(libbliss ${GMP_LIBRARIES})' \
    -e '/VISIBILITY/d' \
    -i CMakeLists.txt

# Fix installation directories
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,\(DESTINATION \)lib,\1%{_lib},' CMakeLists.txt
fi

%build
%cmake -DUSE_GMP:BOOL=ON
%cmake_build

# Build the documentation
doxygen

%install
%cmake_install

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
sed 's/@VERSION@/%{version}/' %{SOURCE1} > %{buildroot}%{_mandir}/man1/bliss.1
touch -r %{SOURCE1} %{buildroot}%{_mandir}/man1/bliss.1

%files
%{_bindir}/bliss
%{_mandir}/man1/bliss.1*

%files devel
%doc html
%{_includedir}/bliss
%{_libdir}/libbliss.so
%{_libdir}/cmake/Bliss/

%files libs
%doc CHANGES.txt
%license COPYING COPYING.LESSER
%{_libdir}/libbliss.so.2{,.*}

%changelog
%autochangelog
