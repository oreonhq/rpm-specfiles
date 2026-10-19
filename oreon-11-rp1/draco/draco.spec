%global source0_hash bf6b105b79223eab2b86795363dfe5e5356050006a96521477973aba8f036fe1
%global		gtestflag 0
Name:		draco
Version:	1.5.7
Release:        1%{?dist}
Summary:        A library for compressing and decompressing 3D geometric meshes and point clouds
License:	Apache-2.0
URL:            https://github.com/google/%{name}
Source0:        https://github.com/google/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:		0001-Use-system-gtest.patch
%if %{?gtestflag}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(python3)
# /oreon:deps
%description
A library for compressing and decompressing 3D geometric meshes and point clouds

%package	devel
Summary: Development files for draco
Requires: %{name}%{?_isa} = %{version}-%{release}
%description	devel
%{summary}.

%package	static
Summary: Static files for draco
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description	static
%{summary}.

%prep

%autosetup -p1 -n %{name}-%{version}

# Remove precompiled CSS and Javascript along binaries
rm -fr {javascript,maya,docs/assets}

%build

%cmake -GNinja \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DDRACO_TESTS=%{gtestflag}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N --version-string=%{version} \
	-o %{buildroot}%{_mandir}/man1/%{name}_decoder-%{version}.1 \
	%{buildroot}%{_bindir}/%{name}_decoder
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N --version-string=%{version} \
	-o %{buildroot}%{_mandir}/man1/%{name}_encoder-%{version}.1 \
	%{buildroot}%{_bindir}/%{name}_encoder
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{?gtestflag}
%check

%ifnarch s390x
%{_vpath_builddir}/draco_tests
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n draco-devel -f %{oreon_filedir}/draco-devel.list
%files -n draco-static -f %{oreon_filedir}/draco-static.list

%changelog

%autochangelog
