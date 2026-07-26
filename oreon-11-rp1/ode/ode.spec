%global source0_hash c91a28c6ff2650284784a79c726a380d6afec87ecf7a35c32a6be0c5b74513e8

%global somajor 8

Name:           ode
Version:        0.16.6
Release:        3%{?dist}
Summary:        High performance library for simulating rigid body dynamics
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://bitbucket.org/odedevs/ode
Source0:        https://bitbucket.org/odedevs/ode/downloads/ode-%{version}.tar.gz
Patch1:         ode-0.11.1-multilib.patch
# Modify ode-double.pc and ode-double-config to set dDOUBLE, link right lib
Patch2:         ode-0.16.6-double-config.patch
# Modify ode.pc and ode-config to set dSINGLE
Patch3:         ode-0.16.3-single-config.patch
BuildRequires:  make gcc-c++
BuildRequires:  libGL-devel libGLU-devel libtool

%description
ODE is an open source, high performance library for simulating rigid body
dynamics. It is fully featured, stable, mature and platform independent with
an easy to use C/C++ API. It has advanced joint types and integrated collision
detection with friction. ODE is useful for simulating vehicles, objects in
virtual reality environments and virtual creatures. It is currently used in
many computer games, 3D authoring tools and simulation tools.

%package        double
Summary:        Ode physics library compiled with double precision

%description    double
The %{name}-double package contains a version of the ODE library for simulating
rigid body dynamics compiled with double precision.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-double = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} or %{name}-double.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
./bootstrap
%patch -P 1 -p1
# allow overriding EXTRA_LIBTOOL_LDFLAGS from the make cmdline
sed -i 's/libode_la_LDFLAGS = @EXTRA_LIBTOOL_LDFLAGS@/libode_la_LDFLAGS = $(EXTRA_LIBTOOL_LDFLAGS)/' \
  ode/src/Makefile.in
# mv some license files around to give them all a unique name
mv OPCODE/COPYING OPCODE-COPYING
for i in ou/LICENSE*.TXT; do
  sed -i.bak 's/\r//' $i
  touch -r $i.bak $i
  mv $i `echo $i|sed 's|ou/LICENSE|OU-LICENSE|'`
done
mv libccd/BSD-LICENSE LIBCCD-LICENSE.TXT

%build
# Use internal libccd as system libccd is not build with double support
ODE_CONFIGURE_FLAGS="--enable-shared --disable-static --with-libccd=internal \
  --with-cylinder-cylinder=libccd --with-capsule-cylinder=libcdd \
  --with-convex-box=libccd --with-convex-capsule=libccd \
  --with-convex-cylinder=libccd"
%configure $ODE_CONFIGURE_FLAGS --enable-double-precision
make %{?_smp_mflags} X_LIBS=-lX11 EXTRA_LIBTOOL_LDFLAGS="-release double"
mv ode-config ode-double-config
mv ode.pc ode-double.pc
# Adjust ode-double-config and ode-double.pc to set dDOUBLE, use proper lib
patch -p1 < %{PATCH2}
mv ode/src/.libs/libode-double.so.%{somajor}.?.? .
make distclean

CFLAGS="%{optflags} -ffast-math"
CXXFLAGS="%{optflags} -ffast-math"
%configure $ODE_CONFIGURE_FLAGS
make %{?_smp_mflags} X_LIBS=-lX11
# Modify ode-config and ode.pc to set dSINGLE
patch -p1 < %{PATCH3}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libode.la
# DIY libode-double install
install -m 755 ode-double-config $RPM_BUILD_ROOT%{_bindir}
install -m 755 libode-double.so.%{somajor}.?.? $RPM_BUILD_ROOT%{_libdir}
ln -s libode-double.so.%{somajor}.?.? $RPM_BUILD_ROOT%{_libdir}/libode-double.so.%{somajor}
ln -s libode-double.so.%{somajor}.?.? $RPM_BUILD_ROOT%{_libdir}/libode-double.so
install -m 644 ode-double.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig

%ldconfig_scriptlets

%ldconfig_scriptlets double

%files
%doc CHANGELOG.txt README.md
%license *COPYING *LICENSE*.TXT
%{_libdir}/libode.so.%{somajor}*

%files double
%doc CHANGELOG.txt README.md
%license *COPYING *LICENSE*.TXT
%{_libdir}/libode-double.so.%{somajor}*

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-double-config
%{_includedir}/%{name}
%{_libdir}/libode.so
%{_libdir}/libode-double.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-double.pc

%changelog
%autochangelog
