Name:           libsass
Version:        3.6.6
%global soname_version 1
Release:        6%{?dist}
Summary:        C/C++ port of the Sass CSS precompiler

# src/ast.hpp, src/utf8* is BSL-1.0
License:        MIT AND BSL-1.0
URL:            https://sass-lang.com/libsass
Source0:        https://github.com/sass/libsass/archive/%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 11f0bb3709a4f20285507419d7618f3877a425c0131ea8df40fe6196129df15d
%global source0_file libsass-3.6.6.tar.gz
# oreon url source checksums end

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  make

%description
Libsass is a C/C++ port of the Sass CSS precompiler. The original version was
written in Ruby, but this version is meant for efficiency and portability.

This library strives to be light, simple, and easy to build and integrate with
a variety of platforms and languages.

Libsass is just a library, but if you want to RUN libsass, install the sassc
package.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libsass-3.6.6.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "11f0bb3709a4f20285507419d7618f3877a425c0131ea8df40fe6196129df15d" || { echo "oreon: Source0 SHA256 mismatch for libsass-3.6.6.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
export LIBSASS_VERSION=%{version}
autoreconf --force --install


%build
%configure --disable-static
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -print -delete


%files
%license LICENSE
%doc Readme.md SECURITY.md
%{_libdir}/libsass.so.%{soname_version}{,.*}


%files devel
%{_includedir}/sass.h
%{_includedir}/sass2scss.h
%{_includedir}/sass/
%{_libdir}/libsass.so
%{_libdir}/pkgconfig/libsass.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.6-6
- Prepare for Oreon 11 (RP1)
