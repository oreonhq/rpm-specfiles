%global source0_hash d870fad1e31cb787c85161a8894abb9d7283c2a654a9d3d4c6d45a1eba59952c

Name:           libtomcrypt
Version:        1.18.2
Release:        23%{?dist}
Summary:        A comprehensive, portable cryptographic toolkit
License:        Unlicense OR WTFPL
URL:            https://www.libtom.net/

Source0:        https://github.com/libtom/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtommath-devel >= 1.0
BuildRequires:  libtool

%description
A comprehensive, modular and portable cryptographic toolkit that provides
developers with a vast array of well known published block ciphers, one-way hash
functions, chaining modes, pseudo-random number generators, public key
cryptography and a plethora of other routines.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
%set_build_flags
export PREFIX="%{_prefix}"
export INCPATH="%{_includedir}"
export LIBPATH="%{_libdir}"
export EXTRALIBS="-ltommath"
export CFLAGS="%{build_cflags} -DLTM_DESC -DUSE_LTM"
%make_build V=1 -f makefile.shared library
%make_build V=1 -f makefile.shared test

%check
./test

%install
%make_install INSTALL_OPTS="-m 755" INCPATH="%{_includedir}" LIBPATH="%{_libdir}" -f makefile.shared

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

sed -i \
    -e 's|^prefix=.*|prefix=%{_prefix}|g' \
    -e 's|^libdir=.*|libdir=${prefix}/%{_lib}|g' \
    %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.18.2-23
- Import for Oreon 11
