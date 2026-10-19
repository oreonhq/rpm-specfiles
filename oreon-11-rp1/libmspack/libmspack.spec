%global source0_hash 70dd1fb2f0aecc36791b71a1e1840e62173079eadaa081192d1c323a0eeea21b
Name:           libmspack
Version:        0.11
Release:        1%{?dist}
Summary:        Library for CAB and related files compression and decompression
License:        LGPL-2.1-only AND LicenseRef-Fedora-UltraPermissive AND MIT
URL:            http://www.cabextract.org.uk/libmspack/
Source0:        http://www.cabextract.org.uk/libmspack/%{name}-%{version}alpha.tar.gz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The purpose of libmspack is to provide both compression and decompression of 
some loosely related file formats used by Microsoft.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-doc < 0.2
%description    devel
The %{name}-devel package contains libraries, header files and documentation
for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}alpha

chmod a-x mspack/mspack.h

# Temporarily while building from github tarball:
#autoreconf -fi

%build

%configure --disable-static --disable-silent-rules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/libmspack.la
iconv -f ISO_8859-1 -t utf8 ChangeLog --output Changelog.utf8
touch -r ChangeLog Changelog.utf8
mv Changelog.utf8 ChangeLog
pushd doc
doxygen
find html -type f | xargs touch -r %{SOURCE0}
rm -f html/installdox
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmspack-devel -f %{oreon_filedir}/libmspack-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.1-0.16.alpha
- Prepare for Oreon 11 (RP1)
