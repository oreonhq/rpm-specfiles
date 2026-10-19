%global source0_hash cf5091fa8e7dcdbe667335eb90a2cfdd0a3fe8f8c7c8d1ece44d9d055736a06a
Name: libeot
Version: 0.01
Release:        1%{?dist}
Summary:        A library for parsing Embedded OpenType font files
License: MPL-2.0
URL: https://github.com/umanwizard/libeot
Source0:        http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tools to transform EOT font files into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Tools to transform EOT font files into other formats. Only TTF is
supported currently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build
%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libeot-devel -f %{oreon_filedir}/libeot-devel.list
%files -n libeot-tools -f %{oreon_filedir}/libeot-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.01-1
- Prepare for Oreon 11 (RP1)
