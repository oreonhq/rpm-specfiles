%global source0_hash 8bd3b9477042ecc00dd71c04762fa58468e14cccc32fd8c6826c2da1e8bc3107

Name:           matio
Version:        1.5.30
Release:        2%{?dist}
Summary:        Library for reading/writing Matlab MAT files

License:        BSD-2-Clause
URL:            http://sourceforge.net/projects/matio
Source0:        http://downloads.sourceforge.net/matio/matio-%{version}.tar.gz

BuildRequires: make
BuildRequires:  doxygen
#According to the README - zlib 1.2.2 is possible but require a patch
BuildRequires:  zlib-devel >= 1.2.3
BuildRequires:  hdf5-devel >= 1.8
# 1.5.3 was released without configure
BuildRequires:  libtool
Requires:       hdf5 = %{_hdf5_version}
     

%description
matio is an open-source library for reading/writing Matlab MAT files.  This
library is designed for use by programs/libraries that do not have access or
do not want to rely on Matlab's libmat shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       hdf5-devel
Requires:       zlib-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sed -i -e '/Requires\.private/d' matio.pc.in

%build
sh ./autogen.sh
%configure \
  --enable-shared \
  --disable-static \
  --enable-mat73=yes \
  --enable-extended-sparse=yes

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

#Fix timestamp
touch -r $RPM_BUILD_ROOT%{_includedir}/matio_pubconf.h NEWS

rm -rf $RPM_BUILD_ROOT%{_datadir}/info/dir

%check
%ifnarch s390x
fail=1
#Needed to avoid rpath
export LD_LIBRARY_PATH=%{_builddir}/%{?buildsubdir}/src/.libs/
make check || ( cat test/testsuite.log && exit $fail )
%endif

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README
%{_bindir}/matdump
%{_libdir}/*.so.14*

%files devel
%{_includedir}/matio*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/Mat_*.3.*

%changelog
%autochangelog
