%global source0_hash 90df1eeb8354941ca65663dcf28658b67d3aa41daa71133bdd20c35abb1bcaba

%define         solib tolua++-5.3

Name:           tolua++
Version:        1.0.93
Release:        44%{?dist}
Summary:        A tool to integrate C/C++ code with Lua
License:        MIT
# Upstream is defunct, so no URL
Source0:        %{name}-%{version}.tar.bz2
Patch0:         tolua++-1.0.93-no-buildin-bytecode.patch
Patch1:         tolua++-1.0.93-lua52.patch
Patch2:         tolua++-1.0.93-scons304.patch
Patch3:         tolua++-1.0.93-scons-env.patch
BuildRequires:  gcc-c++
BuildRequires:  python3-scons
BuildRequires:  lua-devel >= 5.3

%description
tolua++ is an extended version of tolua, a tool to integrate C/C++ code with
Lua. tolua++ includes new features oriented to C++.

%package devel
Summary:        Development files for tolua++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       lua-devel >= 5.3

%description devel
Development files for tolua++

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/\r//' doc/%{name}.html

%build
# el8 provides the scons binary as scons-3 from the powertools repo
%if 0%{?el8}
SCONS_BIN=scons-3
%else
SCONS_BIN=scons
%endif

$SCONS_BIN %{?_smp_mflags} -Q CCFLAGS="%{optflags} $(pkg-config --cflags lua)" \
  LINKFLAGS="%{optflags} %{?build_ldflags} -Wl,-soname,lib%{solib}.so" \
  tolua_lib=%{solib} shared=1
# Relink the tolua++ binary, to link it without the soname which we add to
# LINKFLAGS to build a shared lib
gcc -o bin/%{name} src/bin/tolua.o $RPM_OPT_FLAGS $RPM_LD_FLAGS \
  -Llib -l%{solib} -llua -ldl -lm

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 bin/%{name}  $RPM_BUILD_ROOT%{_bindir}
install -m 755 lib/lib%{solib}.so $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{solib}.so $RPM_BUILD_ROOT%{_libdir}/libtolua++.so
install -p -m 644 include/%{name}.h $RPM_BUILD_ROOT%{_includedir}
# For use with Patch2 (not working yet)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 src/bin/lua/*.lua $RPM_BUILD_ROOT%{_datadir}/%{name}

%ldconfig_scriptlets

%files
%doc README
%license COPYRIGHT
%{_libdir}/lib%{solib}.so
%{_datadir}/%{name}

%files devel
%doc doc/*
%{_bindir}/%{name}
%{_libdir}/libtolua++.so
%{_includedir}/%{name}.h

%changelog
%autochangelog
