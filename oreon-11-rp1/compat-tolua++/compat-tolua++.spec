%global source0_hash 90df1eeb8354941ca65663dcf28658b67d3aa41daa71133bdd20c35abb1bcaba

%global         solib tolua++-5.1

Name:           compat-tolua++
Version:        1.0.93
Release:        28%{?dist}
Summary:        Lua-5.1 compatible version of tolua++ (C++ Lua integration)
License:        MIT
# Upstream is defunct, so no URL
Source0:        tolua++-%{version}.tar.bz2
Patch0:         tolua++-1.0.93-lua51.patch
Patch1:         tolua++-1.0.93-lua-include-path.patch
Patch2:         tolua++-1.0.93-scons304.patch
Patch3:         tolua++-1.0.93-scons-env.patch
BuildRequires:  gcc
BuildRequires:  python3-scons
BuildRequires:  compat-lua-devel >= 5.1

%description
This is a lua-5.1 compatible version of tolua++.

tolua++ is an extended version of tolua, a tool to integrate C/C++ code with
Lua. tolua++ includes new features oriented to C++.

%package devel
Summary:        Development files for compat-tolua++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       compat-lua-devel >= 5.1
# tolua++-devel and compat-tolua++ cannot be installed at the same time
Conflicts:      tolua++-devel

%description devel
Development files for compat-tolua++.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tolua++-%{version}
sed -i 's/\r//' doc/tolua++.html

%build
# el8 provides the scons binary as scons-3 from the powertools repo
%if 0%{?el8}
SCONS_BIN=scons-3
%else
SCONS_BIN=scons
%endif

$SCONS_BIN %{?_smp_mflags} -Q CCFLAGS="%{optflags} $(pkg-config --cflags lua-5.1)" \
  LINKFLAGS="%{optflags} %{?build_ldflags} -Wl,-soname,lib%{solib}.so" \
  tolua_lib=%{solib} shared=1
# Relink the tolua++ binary, there are 2 reasons for this:
# -Link it without the soname which we add to LINKFLAGS to build a shared lib
# -On non x86_64 link it against the pre-generated toluabind rather then the
#  bootstapped one as something goes wrong with the bootstrap on ARM, x86_32
#  (rhbz#1094103) and ppc (rhbz#704372) causing a segfault for unknown reasons.
%ifarch x86_64
gcc -o bin/tolua++ src/bin/tolua.o src/bin/toluabind.o $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  -Llib -l%{solib} -llua-5.1 -ldl -lm
%else
gcc -o bin/tolua++ src/bin/tolua.o src/bin/toluabind_default.o $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  -Llib -l%{solib} -llua-5.1 -ldl -lm
%endif

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 bin/tolua++  $RPM_BUILD_ROOT%{_bindir}
install -m 755 lib/lib%{solib}.so $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{solib}.so $RPM_BUILD_ROOT%{_libdir}/libtolua++.so
install -p -m 644 include/tolua++.h $RPM_BUILD_ROOT%{_includedir}

%ldconfig_scriptlets

%files
%doc README
%license COPYRIGHT
%{_libdir}/lib%{solib}.so

%files devel
%doc doc/*
%{_bindir}/tolua++
%{_libdir}/libtolua++.so
%{_includedir}/tolua++.h

%changelog
%autochangelog
