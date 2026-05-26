Name:           libmspack
Version:        0.10.1
Release:        0.16.alpha%{?dist}
Summary:        Library for CAB and related files compression and decompression

# CRC32 is LicenseRef-Fedora-UltraPermissive
License:        LGPL-2.1-only AND LicenseRef-Fedora-UltraPermissive AND MIT
URL:            http://www.cabextract.org.uk/libmspack/
Source0:        http://www.cabextract.org.uk/libmspack/%{name}-%{version}alpha.tar.gz
# oreon url source checksums begin
%global source0_sha256 bac862dee6e0fc10d92c70212441d9f8ad9b0222edc9a708c3ead4adb1b24a8e
%global source0_file libmspack-0.10.1alpha.tar.gz
# oreon url source checksums end
#Source0:        https://github.com/kyz/libmspack/archive/v%%{version}alpha/%%{name}-v%%{version}alpha.tar.gz

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires: make

# Temporarily while building from github tarball:
#BuildRequires:  autoconf, automake, libtool


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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libmspack-0.10.1alpha.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bac862dee6e0fc10d92c70212441d9f8ad9b0222edc9a708c3ead4adb1b24a8e" || { echo "oreon: Source0 SHA256 mismatch for libmspack-0.10.1alpha.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}-%{version}alpha

chmod a-x mspack/mspack.h

# Temporarily while building from github tarball:
#autoreconf -fi


%build
%configure --disable-static --disable-silent-rules

# disable rpath the hard way
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

%files
%doc README TODO ChangeLog AUTHORS
%license COPYING.LIB
%{_libdir}/%{name}.so.0*

%files devel
%doc doc/html
%{_includedir}/mspack.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.1-0.16.alpha
- Prepare for Oreon 11 (RP1)
