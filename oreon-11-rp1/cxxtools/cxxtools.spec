%global source0_hash c48758af8c8bf993a45492fdd8acaf1109357f1c574810e353d3103277b4296b
Name:           cxxtools
Version:        3.0
Release:        1%{?dist}
Summary:        A collection of general-purpose C++ classes
Epoch:          1
License:        LicenseRef-Callaway-LGPLv2+ 
URL:            http://www.tntnet.org/cxxtools.html
Source0:        https://github.com/maekitalo/cxxtools/archive/refs/tags/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-arm.patch
Patch1:         %{name}-%{version}-gcc11.patch
Patch2:         %{name}-%{version}-i686.patch
Patch3:         %{name}-%{version}-ppc64le.patch
Patch4:         %{name}-%{version}-timer.patch
Patch5:         0001-fix-for-possible-crash-in-cxxtools-Connectable.patch
Patch6:         cxxtools-cxx20.patch
Provides:       bundled(md5-polstra)
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  tzdata
# /oreon:deps
%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description    devel
Development files for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{version}

# fix spurious executable perm
find -name "*.cpp" -exec chmod -x {} \;
find -name "*.h" -exec chmod -x {} \;

%build

%define _lto_cflags -flto=auto -ffat-lto-objects
%configure --disable-static \
%ifarch s390 s390x aarch64
    --with-atomictype=pthread \
%endif
    %{nil}
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
%%check
    test/alltests
%ldconfig_scriptlets
%oreon_autofiles cxxtools-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cxxtools-devel -f %{oreon_filedir}/cxxtools-devel.list

%changelog

%autochangelog
