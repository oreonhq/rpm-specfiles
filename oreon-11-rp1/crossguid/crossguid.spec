%global source0_hash 271f0cc8ca79f4e56398439c5d6e59dcc47b34f27b54ecda2491ef901e5bd65d
%global commit fef89a4174a7bf8cd99fa9154864ce9e8e3bf989
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20160908
Name:           crossguid
Version:        0.2.2
Release:        1%{?dist}
Summary:        Lightweight cross platform C++ GUID/UUID library
License:        MIT
URL:            https://github.com/graeme-hill/%{name}/
Source0:        https://github.com/graeme-hill/%{name}//archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
Source1:        Makefile.%{name}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  make
# /oreon:deps
%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and has a generic class for
parsing, stringifying, and comparing IDs.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

cp -p %{SOURCE1} Makefile

%build

%make_build CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%install
%make_install LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}
%oreon_autofiles crossguid-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
./test
%files -f %{oreon_filedir}/main.list
%files -n crossguid-devel -f %{oreon_filedir}/crossguid-devel.list

%changelog

%autochangelog
