%global source0_hash fe60fc4943a73d93cb29b8b20b026b7da634614ef4b4f92d9c2f98d166594bf4
%global gh_owner     mongodb
%global gh_project   libmongocrypt
%global libname      %{gh_project}
%global libver       1.0
%global soname       0
Name:      %{libname}
Summary:        The companion C library for client side encryption in drivers
Version:   1.15.2
Release:        1%{?dist}
License:   Apache-2.0 AND ISC AND BSD-3-Clause
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{name}/archive/%{version}.tar.gz
Patch0:    %{libname}-static.patch
Patch1:    %{libname}-build.patch
Provides:      bundled(IntelRDFPMathLib) = 2.2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(bson-1.0)
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:    Header files and development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
Requires:   cmake-filesystem
%description devel
This package contains the header files and development libraries
for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gh_project}-%{version}%{?prever:-dev} -p1

# Gather license files
tar xf third-party/IntelRDFPMathLib*.tar.xz --strip-components=1 */eula.txt
mv eula.txt                        LICENSE.intelrdfpmathlib
cp kms-message/THIRD_PARTY_NOTICES LICENSE.kms_b64
cp kms-message/COPYING             LICENSE.kms-message

%build

%cmake \
    -DBUILD_VERSION=%{version} \
    -DENABLE_PIC:BOOL=ON \
    -DUSE_SHARED_LIBBSON:BOOL=ON \
    -DMONGOCRYPT_MONGOC_DIR:STRING=USE-SYSTEM \
    -DENABLE_ONLINE_TESTS:BOOL=OFF \
    -DENABLE_STATIC:BOOL=OFF
%cmake_build
doxygen ./doc/Doxygen
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
if grep -r static %{buildroot}%{_libdir}/cmake; then
  : cmake configuration file contain reference to static library
  exit 1
fi
%files -f %{oreon_filedir}/main.list
%files -n libmongocrypt-devel -f %{oreon_filedir}/libmongocrypt-devel.list

%changelog

%autochangelog
