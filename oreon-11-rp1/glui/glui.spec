%global source0_hash c1ef5e83cf338e225ce849f948170cd681c99661a5c2158b4074515926702787

Name: glui
Version:  2.36
Release:  33%{?dist}
Summary: A GLUT-Based User Interface Library

License: Zlib
URL: http://glui.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
#Upstream only builds a static library, this makes a solib.
Patch0: glui-2.36-solib.patch
BuildRequires:  gcc-c++
BuildRequires: freeglut-devel libXi-devel libXmu-devel
BuildRequires: make

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description
GLUI is a GLUT-based C++ user interface library which provides controls
such as buttons, checkboxes, radio buttons, and spinners to OpenGL applications. 
It is window-system independent, relying on GLUT to handle all system-dependent 
issues, such as window and mouse management. 

%description devel
GLUI is a GLUT-based C++ user interface library which provides controls
such as buttons, checkboxes, radio buttons, and spinners to OpenGL applications. 
It is window-system independent, relying on GLUT to handle all system-dependent 
issues, such as window and mouse management. 

These are the development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .solib
find -type f -name '*.cpp' | xargs chmod -x
find -type f -name '*.h' | xargs chmod -x

%build
pushd src
%{__make} CPPFLAGS="%{optflags} -I./ -I./include -fPIC" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_includedir}/GL
install -p -m 644 src/include/GL/glui.h %{buildroot}%{_includedir}/GL/
mkdir -p %{buildroot}%{_libdir}
install -p -m 755 src/libglui.so.0.0 %{buildroot}%{_libdir}/
ln -s %{_libdir}/libglui.so.0.0 %{buildroot}%{_libdir}/libglui.so.0
ln -s %{_libdir}/libglui.so.0 %{buildroot}%{_libdir}/libglui.so

%ldconfig_scriptlets

%files
%doc src/LICENSE.txt
%{_libdir}/*.so.*

%files devel
%doc src/doc/ src/example/ www/ 
%{_libdir}/*.so
%{_includedir}/GL/
%{_includedir}/GL/glui.h

%changelog
%autochangelog
