%global source0_hash eb8fb2c3e4b6e2d336608377050892b54c3c983b646c561836550863003c05d7

%{?mingw_package_header}

Name: mingw-libunistring
Version: 0.9.10
Release: 18%{?dist}
Summary: MinGW port of GNU Unicode string library
License: GPL-2.0-or-later OR LGPL-3.0-or-later
Url: http://www.gnu.org/software/libunistring/
Source0: http://ftp.gnu.org/gnu/libunistring/libunistring-%{version}.tar.xz

BuildArch: noarch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc

%description
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package -n mingw32-libunistring
Summary: %{summary}

%description -n mingw32-libunistring
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%package -n mingw64-libunistring
Summary: %{summary}

%description -n mingw64-libunistring
This portable C library implements Unicode string types in three flavours:
(UTF-8, UTF-16, UTF-32), together with functions for character processing
(names, classifications, properties) and functions for string processing
(iteration, formatted output, width, word breaks, line breaks, normalization,
case folding and regular expressions).

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libunistring-%{version}

%build
%mingw_configure \
    --disable-static \
    --disable-rpath

%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{mingw32_infodir}/dir
rm -f $RPM_BUILD_ROOT%{mingw64_infodir}/dir

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# Move staged docs so not picked up by %%doc in main package
mv $RPM_BUILD_ROOT%{mingw32_datadir}/doc/libunistring __doc
mv $RPM_BUILD_ROOT%{mingw64_datadir}/doc/libunistring __doc

%files -n mingw32-libunistring
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README HACKING DEPENDENCIES THANKS ChangeLog
%doc __doc/*
%{mingw32_bindir}/libunistring-2.dll
%{mingw32_includedir}/*.h
%{mingw32_includedir}/unistring
%{mingw32_infodir}/libunistring.info*
%{mingw32_libdir}/libunistring.dll.a

%files -n mingw64-libunistring
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README HACKING DEPENDENCIES THANKS ChangeLog
%doc __doc/*
%{mingw64_bindir}/libunistring-2.dll
%{mingw64_includedir}/*.h
%{mingw64_includedir}/unistring
%{mingw64_infodir}/libunistring.info*
%{mingw64_libdir}/libunistring.dll.a

%changelog
%autochangelog
