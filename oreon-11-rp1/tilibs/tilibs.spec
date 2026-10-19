%global source0_hash 589d17de97afabef251381e2719f667a028ffb3db62d116f016b2a43c7080b5a
%global forgeurl https://github.com/debrouxl/tilibs
%global commit 8ffa244e522a484146fe0d7c1130a554f8dba48e
%if 0%{?el7}
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global forgesource %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
%global date 20220228
%else
%forgemeta
%endif
%global build_destdir %{_builddir}/build_destdir
%global optflags %{optflags} -I%{build_destdir}%{_includedir}/tilp2 -L%{build_destdir}%{_libdir}
Name:           tilibs
Version:        1.19
%if 0%{?el7}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        Texas Instruments calculators interface libraries
License:        GPL-2.0-or-later
URL:            http://lpg.ticalc.org/prj_tilp
Source0:        %{forgesource}
Source1:        69-libticables.rules
%if 0%{?el7}
%else
%endif
%if 0%{?el7}
%else
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  libarchive-devel
BuildRequires:  libusb-devel
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  tfdocgen
BuildRequires:  zlib-devel
# /oreon:deps
%description
Set of libraries to interface with Texas Instruments calculators.

%package        devel
Summary:        Development files for tilibs
Requires:       libticables%{?_isa} = %{version}-%{release}
Requires:       libticalcs%{?_isa} = %{version}-%{release}
Requires:       libticonv%{?_isa} = %{version}-%{release}
Requires:       libtifiles%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       libarchive-devel
Requires:       libusb-devel
Requires:       zlib-devel
Provides:       libticables-devel = %{version}-%{release}
Provides:       libticalcs-devel = %{version}-%{release}
Provides:       libticonv-devel = %{version}-%{release}
Provides:       libtifiles-devel = %{version}-%{release}
Obsoletes:      libticables2-devel < 1.3.5-13
Provides:       libticables2-devel = %{version}-%{release}
Obsoletes:      libticalcs2-devel < 1.1.9-13
Provides:       libticalcs2-devel = %{version}-%{release}
Obsoletes:      libtifiles2-devel < 1.1.7-14
Provides:       libtifiles2-devel = %{version}-%{release}
%description    devel
Include files and libraries for linking and developing applications using
libticables, libticalcs, libticonv and libtifiles.

%package -n     libticables
Summary:        Texas Instruments link cables library
%if 0%{?el7}
Requires:       udev
%else
Requires:       systemd-udev
%endif
Obsoletes:      libticables2 < 1.3.5-13
Provides:       libticables2 = %{version}-%{release}
%description -n libticables
The ticables library is able to handle the different link cables designed for
Texas Instruments's graphing calculators (also called handhelds) in a fairly
transparent fashion. With this library, the developer does not have to worry
about the different link cables' characteristics as well as the different
platforms. The library provides a complete API which is very easy to use and
makes things easier.

%package -n     libticables-doc
Summary:        HTML documentation for libticables
BuildArch:      noarch
Obsoletes:      libticables2-doc < 1.3.5-13
Provides:       libticables2-doc = %{version}-%{release}
%description -n  libticables-doc
HTML documentation for linking and developing applications using libticables.

%package -n     libticalcs
Summary:        Texas Instruments calculator communication library
Obsoletes:      libticalcs2 < 1.1.9-13
Provides:       libticalcs2 = %{version}-%{release}
%description -n libticalcs
The ticalcs library is a library which brings about all the functions needed to
communicate with a Texas Instruments graphing calculator (or hand-held).
Currently, it does not support some education devices (such as CBL/CBR and
others). This library is able to communicate with handhelds in a fairly
transparent fashion. With this library, the developer does not have to worry
about the packet oriented protocol, the file management and some other stuff.

%package -n     libticalcs-doc
Summary:        HTML documentation for libticalcs
BuildArch:      noarch
Obsoletes:      libticalcs2-doc < 1.1.9-13
Provides:       libticalcs2-doc = %{version}-%{release}
%description -n  libticalcs-doc
HTML documentation for linking and developing applications using libticalcs.

%package -n     libticonv
Summary:        Texas Instruments calculators charsets library
%description -n libticonv
The ticonv library is a library capable of conversions between Texas
Instruments character sets and UTF-8/UTF-16 character sets.

%package -n     libticonv-doc
Summary:        HTML documentation for libticables
BuildArch:      noarch
%description -n  libticonv-doc
HTML documentation for linking and developing applications using libticonv.

%package -n     libtifiles
Summary:        Texas Instruments calculator communication library
Obsoletes:      libtifiles2 < 1.1.7-14
Provides:       libtifiles2 = %{version}-%{release}
%description -n libtifiles
The tifiles library is a library capable of reading, modifying, and writing TI
formatted files. It can also group/ungroup files. This library is able to
manipulate files in a fairly transparent fashion. With this library, the
developer does not have to worry about the different file formats.

%package -n     libtifiles-doc
Summary:        HTML documentation for libtifiles
BuildArch:      noarch
Obsoletes:      libtifiles2-doc < 1.1.7-14
Provides:       libtifiles2-doc = %{version}-%{release}
%description -n  libtifiles-doc
HTML documentation for linking and developing applications using libtifiles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?el7}
%autosetup -n %{name}-%{commit} -p1

# Drop unsupported flag
sed -i 's/-Werror=date-time//' CMakeLists.txt
%else
%forgeautosetup -p1
%endif

# Fix line endings
sed -i 's/\r$//' lib*/trunk/LOGO lib*/trunk/docs/html/style.css
rm lib*/trunk/docs/html/clean.bat

# Convert to UTF-8
for dir in lib*; do
  iconv -f iso8859-1 -t utf-8 ${dir}/trunk/LOGO > LOGO.conv && mv -f LOGO.conv ${dir}/trunk/LOGO
done

%build

export DESTDIR="%{build_destdir}"
%if 0%{?el7}
%cmake3
%cmake3_build
%else
%cmake
%cmake_build
%endif
for dir in lib*; do
  pushd ${dir}/trunk/docs && tfdocgen ../ && popd
done
%check

export DESTDIR="%{build_destdir}"
%if 0%{?el7}
%cmake3_build --target check
%else
%cmake_build --target check
%endif
%install
%if 0%{?el7}
%cmake3_install
%else
%cmake_install
%endif
%find_lang libticables2
%find_lang libticalcs2
%find_lang libtifiles2
%if 0%{?el7}
mkdir -p %{buildroot}%{_udevrulesdir}
%endif
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} %SOURCE1
rm %{buildroot}%{_libdir}/*.a
%oreon_autofiles libticables usr/*/lib*.so.*
%oreon_autofiles libticables-doc usr/*/lib*.so.*
%oreon_autofiles libticalcs usr/*/lib*.so.*
%oreon_autofiles libticalcs-doc usr/*/lib*.so.*
%oreon_autofiles libticonv usr/*/lib*.so.*
%oreon_autofiles libticonv-doc usr/*/lib*.so.*
%oreon_autofiles libtifiles usr/*/lib*.so.*
%oreon_autofiles libtifiles-doc usr/*/lib*.so.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n tilibs-devel -f %{oreon_filedir}/tilibs-devel.list
%files -n libticables -f %{oreon_filedir}/libticables.list
%files -n libticables-doc -f %{oreon_filedir}/libticables-doc.list
%files -n libticalcs -f %{oreon_filedir}/libticalcs.list
%files -n libticalcs-doc -f %{oreon_filedir}/libticalcs-doc.list
%files -n libticonv -f %{oreon_filedir}/libticonv.list
%files -n libticonv-doc -f %{oreon_filedir}/libticonv-doc.list
%files -n libtifiles -f %{oreon_filedir}/libtifiles.list
%files -n libtifiles-doc -f %{oreon_filedir}/libtifiles-doc.list

%changelog

%autochangelog
