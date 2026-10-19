%global source0_hash d177732879114c07a5ab7e6533e61d2c9dff204044335537c89ed16e7d3e4e2f
%global libname      libargon2
%global gh_commit    62358ba2123abd17fccf2a108a301d4b52c01a7c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     P-H-C
%global gh_project   phc-winner-argon2
%global soname       1
%global upstream_version 20190702
Name:    argon2
Version: %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        The password-hashing tools
License: CC0-1.0 OR Apache-2.0
URL:     https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz
Requires: %{libname}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Argon2 is a password-hashing function that summarizes the state of the art
in the design of memory-hard functions and can be used to hash passwords
for credential storage, key derivation, or other applications.

It has a simple design aimed at the highest memory filling rate and
effective use of multiple computing units, while still providing defense
against tradeoff attacks (by exploiting the cache and memory organization
of the recent processors).

Argon2 has three variants: Argon2i, Argon2d, and Argon2id.

* Argon2d is faster and uses data-depending memory access, which makes it
  highly resistant against GPU cracking attacks and suitable for applications
  with no threats from side-channel timing attacks (eg. cryptocurrencies). 
* Argon2i instead uses data-independent memory access, which is preferred for
  password hashing and password-based key derivation, but it is slower as it
  makes more passes over the memory to protect from tradeoff attacks.
* Argon2id is a hybrid of Argon2i and Argon2d, using a combination of
  data-depending and data-independent memory accesses, which gives some of
  Argon2i's resistance to side-channel cache timing attacks and much of
  Argon2d's resistance to GPU cracking attacks.

%package -n %{libname}
Summary:  The password-hashing library
%description -n %{libname}
Argon2 is a password-hashing function that summarizes the state of the art
in the design of memory-hard functions and can be used to hash passwords
for credential storage, key derivation, or other applications.

%package -n %{libname}-devel
Summary:  Development files for %{libname}
Requires: %{libname}%{?_isa} = %{version}-%{release}
%description -n %{libname}-devel
The %{libname}-devel package contains libraries and header files for
developing applications that use %{libname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{gh_project}-%{gh_commit}

if ! grep -q 'ABI_VERSION = %{soname}' Makefile; then
  : soname have changed
  grep soname Makefile
  exit 1
fi

# Fix pkgconfig file
sed -e 's:lib/@HOST_MULTIARCH@:%{_lib}:;s/@UPSTREAM_VER@/%{version}/' -i %{libname}.pc.in

%build

sed -e '/^CFLAGS/s:^CFLAGS:LDFLAGS=%{build_ldflags}\nCFLAGS:' \
    -e 's:-O3 -Wall:%{optflags}:' \
    -e '/^LIBRARY_REL/s:lib:%{_lib}:' \
    -e 's:-march=\$(OPTTARGET) :${CFLAGS} :' \
    -e 's:CFLAGS += -march=\$(OPTTARGET)::' \
    -i Makefile
make -j1 PREFIX=%{_prefix}
%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBRARY_REL=%{_lib}
rm %{buildroot}%{_libdir}/%{libname}.a
install -Dpm 644 %{libname}.pc %{buildroot}%{_libdir}/pkgconfig/%{libname}.pc
chmod -x %{buildroot}%{_includedir}/%{name}.h
chmod +x %{buildroot}%{_libdir}/%{libname}.so.%{soname}
%oreon_autofiles libargon2 usr/*/lib*.so.*
%oreon_autofiles libargon2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n libargon2 -f %{oreon_filedir}/libargon2.list
%files -n libargon2-devel -f %{oreon_filedir}/libargon2-devel.list

%changelog

%autochangelog
