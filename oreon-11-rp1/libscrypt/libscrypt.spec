%global source0_hash a2d30ea16e6d288772791de68be56153965fe4fd4bcd787777618b8048708936

%global _hardened_build 1

Name:           libscrypt
Version:        1.22
Release:        12%{?dist}
Summary:        Library that implements the secure password hashing function "scrypt"
License:        BSD-2-Clause
URL:            http://www.lolware.net/libscrypt.html
Source0:        https://github.com/technion/libscrypt/archive/v%{version}.tar.gz

Patch0:         0001-sysendian.h-fix-aliasing-violations.patch
Patch1:         0002-b64-fix-Wold-style-definition.patch
Patch2:         0003-crypto_scrypt-nosse-fix-aliasing-violations.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make

%description
This is a library that implements the secure password hashing function "scrypt".

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="$LDFLAGS -Wl,-z,relro -Wl,-soname,libscrypt.so.0 -Wl,--version-script=libscrypt.version"
%make_build

%install
%make_install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

find $RPM_BUILD_ROOT -name '*.*a' -exec rm -f {} ';'

%check
make check

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/*.so.*
%doc README.md

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
