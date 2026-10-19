%global source0_hash 5856f6ff3ad465f8ea5dc7b7dc4f8b3d436d826f2751f91896d204b638fdc0d9
%global srcname level-zero
%global lib_version 1.34
%global patch_version 0
%global _lto_cflags %nil
Name:           oneapi-%{srcname}
Version:        %{lib_version}.%{patch_version}
Release:        1%{?dist}
Summary:        OneAPI Level Zero Specification Headers and Loader
License:        MIT
URL:            https://github.com/oneapi-src/%{srcname}
Source0:        https://github.com/oneapi-src/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
ExclusiveArch:  x86_64
Recommends:     %{name}-zello_world
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  spdlog-devel
# /oreon:deps
%description
The objective of the oneAPI Level-Zero Application Programming Interface
(API) is to provide direct-to-metal interfaces to offload accelerator
devices. Its programming interface can be tailored to any device needs
and can be adapted to support broader set of languages features such as
function pointers, virtual functions, unified memory,
and I/O capabilities.

%package        devel
Summary:        The oneAPI Level Zero Specification Headers and Loader development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%package        zello_world
Summary:        The oneAPI Level Zero quick test package with zello_world binary
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    zello_world
The %{name}-zello_world package contains a zello_world binary which is capable of a quick test
of the oneAPI Level-Zero driver and dumping out the basic device and driver characteristics.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}

%build

export CXXFLAGS="%{build_cxxflags} -DFMT_HEADER_ONLY=1"
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DSYSTEM_SDPLOG=ON
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_bindir}/
install -p -m 755 ./%{_vpath_builddir}/bin/zello_world %{buildroot}%{_bindir}/zello_world
chrpath --delete %{buildroot}%{_bindir}/zello_world
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n oneapi-level-zero-devel -f %{oreon_filedir}/oneapi-level-zero-devel.list
%files -n oneapi-level-zero-zello_world -f %{oreon_filedir}/oneapi-level-zero-zello_world.list

%changelog

%autochangelog
