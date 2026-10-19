%global source0_hash 49d0fc50ab931816f6bfc1ac68f8d74b760450eebdb5374e803ee36550f26774
%bcond_without libssh2
Name:           libgit2_1.8
Version:        1.8.4
Release:        1%{?dist}
Summary:        C implementation of the Git core methods as a library with a solid API
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            https://libgit2.org/
Source0:        https://github.com/libgit2/libgit2/archive/refs/tags/v%{version}.tar.gz#/libgit2-%{version}.tar.gz
%if %{with libssh2}
%endif
Provides:       bundled(libxdiff)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libssh2-devel
BuildRequires:  llhttp-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  python3
BuildRequires:  zlib-devel
# /oreon:deps
%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       libgit2-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      pkgconfig(libgit2)
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libgit2-%{version}

# Remove VCS files from examples
find examples -name ".gitignore" -delete -print

# Don't run "online" tests
sed -i '/-sonline/s/^/#/' tests/libgit2/CMakeLists.txt

# Remove bundled libraries (except libxdiff)
pushd deps
find . -maxdepth 1 -not -name xdiff -exec rm -rf {} ';'
popd

%build

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DREGEX_BACKEND=pcre2 \
  -DBUILD_CLI=OFF \
  -DUSE_HTTP_PARSER=llhttp \
  -DUSE_SHA1=HTTPS \
  -DUSE_HTTPS=OpenSSL \
  -DUSE_NTLMCLIENT=OFF \
%if %{with libssh2}
  -DUSE_SSH=ON \
%else
  -DUSE_SSH=OFF \
%endif
  %{nil}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libgit2_1.8-devel -f %{oreon_filedir}/libgit2_1.8-devel.list

%changelog

%autochangelog
