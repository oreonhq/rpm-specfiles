%global source0_hash aa557dd1fae02976d51dc90a36395b93e2d57d21db1cffc73e1c367ed4f8d7cf

Name:           coldet
Version:        1.2
Release:        40%{?dist}
Summary:        3D Collision Detection Library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://coldet.sourceforge.net/
Source0:        http://downloads.sourceforge.net/coldet/coldet12.zip
Patch0:         coldet-1.1-fixes.patch
Patch1:         coldet-1.2-gcc46.patch

BuildRequires:  gcc-c++
BuildRequires: make
%description
This library is an effort to provide a free collision detection library for
generic polyhedra. Its purpose is mainly for 3D games where accurate detection
is needed between two non-simple objects.

Features:
    * Works on any model, even polygon soups.
    * Uses bounding box hierarchies for fast detection.
    * Uses additional triangle intersection tests for 100% accuracy.
    * Provides (upon request) exact point of collision, plus the pair of
      triangles that collided.
    * Supports timeout setting, to limit detection time.
    * Model-Model collision test.
    * Ray-Model collision test.
    * Segment-Model collision test.
    * Sphere-Model collision test.
    * Ray-Sphere and Sphere-Sphere primitive collision tests.

%package devel
Summary: Development libraries and headers for coldet
Requires: %{name} = %{version}-%{release}

%description devel
The developmental files that must be installed in order to compile
applications which use coldet.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1 -z .fixes
%patch -P1 -p1
# for %doc
sed -i 's/\r//' readme.txt COPYING doc/quickstart.html doc/html/{*.html,*.css}
mv doc/quickstart.html doc/html

%build
pushd src
make %{?_smp_mflags} -f makefile.g++ OPT="$RPM_OPT_FLAGS"
popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m 755 src/lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
install -m 644 src/coldet.h src/math3d.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%ldconfig_scriptlets

%files
%doc COPYING readme.txt
%{_libdir}/lib%{name}.so.0

%files devel
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
