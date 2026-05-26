# python3 is not available on RHEL <= 7
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%else
%bcond_with python3
%endif

# python2 is not available on RHEL > 7
%if 0%{?fedora} > 31 || 0%{?rhel} > 7
%bcond_with python2
%else
%bcond_without python2
%endif

Summary: Utility for determining file types
Name: file
Version: 5.47
Release: 1%{?dist}

# Main license is BSD-2-Clause-Darwin
# Shipped exceptions:
# * some src/*.{c.h} - BSD-2-Clause
# Not shipped in Fedora:
# * src/mygetopt.h - BSD-4-Clause
# * src/strcasestr.h - BSD-3-Clause
# * src/strlc{at,py}.c - ISC
# * src/vasprintf.c - BSD-2-Clause-Darwin AND BSD-3-Clause
License: BSD-2-Clause-Darwin AND BSD-2-Clause

Source0: http://ftp.astron.com/pub/file/file-%{version}.tar.gz
Source1: http://ftp.astron.com/pub/file/file-%{version}.tar.gz.asc

# gpg --keyserver hkp://keys.gnupg.net --recv-keys BE04995BA8F90ED0C0C176C471112AB16CB33B3A
# gpg --output christoskey.asc --armor --export christos@zoulas.com
Source2: christoskey.asc

# Upstream says it's up to distributions to add a way to support local-magic.
Patch0: file-localmagic.patch

# not yet upstream
Patch1: file-4.17-rpm-name.patch
Patch2: file-5.04-volume_key.patch

# revert upstream commits (rhbz#2167964)
# 1. https://github.com/file/file/commit/e1233247bbe4d2d66b891224336a23384a93cce1
# 2. https://github.com/file/file/commit/f7a65dbf1739a8f8671621e41c5648d1f7e9f6ae
Patch3: file-5.45-readelf-limit-revert.patch

Patch4: file-5.46-fix-tests-rpm-magic.patch

# Fix tabs->spaces in python/magic.py (upstream 5.47 used tabs; rhbz#2419719)
Patch5: file-5.47-python-magic-close-fix-whitespace.patch
# oreon url source checksums begin
%global source0_sha256 45672fec165cb4cc1358a2d76b5d57d22876dcb97ab169427ac385cbe1d5597a
%global source0_file file-5.47.tar.gz
# oreon url source checksums end

URL: https://www.darwinsys.com/file/
Requires: file-libs%{?_isa} = %{version}-%{release}
BuildRequires: zlib-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: gnupg2

%description
The file command is used to identify a particular file according to the
type of data contained by the file.  File can identify many different
file types, including ELF binaries, system libraries, RPM packages, and
different graphics formats.

%package libs
Summary: Libraries for applications using libmagic

%description libs

Libraries for applications using libmagic.

%package devel
Summary:  Libraries and header files for file development
Requires: file-libs%{?_isa} = %{version}-%{release}

%description devel
The file-devel package contains the header files and libmagic library
necessary for developing programs using libmagic.

%package static
Summary: Static library for file development
Requires: file-devel = %{version}-%{release}

%description static
The file-static package contains the static version of the libmagic library.

%if %{with python2}
%package -n python2-magic
Summary: Python 2 bindings for the libmagic API
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildArch: noarch
Requires: file-libs = %{version}-%{release}
%{?python_provide:%python_provide python2-magic}

%description -n python2-magic
This package contains the Python 2 bindings to allow access to the
libmagic API. The libmagic library is also used by the familiar
file(1) command.
%endif

%if %{with python3}
%package -n python3-file-magic
Summary: Python 3 bindings for the libmagic API
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildArch: noarch
Requires: file-libs = %{version}-%{release}
Conflicts: python3-magic

%description -n python3-file-magic
This package contains the Python 3 bindings to allow access to the
libmagic API. The libmagic library is also used by the familiar
file(1) command.
%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/file-5.47.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "45672fec165cb4cc1358a2d76b5d57d22876dcb97ab169427ac385cbe1d5597a" || { echo "oreon: Source0 SHA256 mismatch for file-5.47.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

iconv -f iso-8859-1 -t utf-8 < doc/libmagic.man > doc/libmagic.man_
touch -r doc/libmagic.man doc/libmagic.man_
mv doc/libmagic.man_ doc/libmagic.man

%if %{with python3}
rm -rf %{py3dir}
cp -a python %{py3dir}
%endif

%build
# Fix config.guess to find aarch64 - #925339
autoreconf -fi

CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE" \
%configure --enable-fsect-man5 --disable-rpath --enable-static
# remove hardcoded library paths from local libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH=$PWD/src/.libs
%make_build
%if %{with python2}
cd python
CFLAGS="%{optflags}" %{__python2} setup.py build
%endif
%if %{with python3}
cd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py build
%endif

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man5
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/misc
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/file

%make_install
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la

# local magic in /etc/magic
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
cp -a ./magic/magic.local ${RPM_BUILD_ROOT}%{_sysconfdir}/magic

cat magic/Magdir/* > ${RPM_BUILD_ROOT}%{_datadir}/misc/magic
ln -s misc/magic ${RPM_BUILD_ROOT}%{_datadir}/magic
ln -s ../magic ${RPM_BUILD_ROOT}%{_datadir}/file/magic

%if %{with python2}
cd python
%{__python2} setup.py install -O1 --skip-build --root ${RPM_BUILD_ROOT}
%endif
%if %{with python3}
cd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root ${RPM_BUILD_ROOT}
%endif
%{__install} -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}

%ldconfig_scriptlets libs

%check
export LD_LIBRARY_PATH=$PWD/src/.libs
%ifarch s390x
# efi-signature-list-sha256: New in 5.47 (commit 2a457644). EFI Signature List magic
# in magic/Magdir/efi uses little-endian types; on big-endian s390x file reports
# "data" instead of the expected string and the test fails. Remove on s390x until
# upstream makes the EFI magic endian-safe.
rm -f tests/efi-signature-list-sha256.testfile tests/efi-signature-list-sha256.result
%endif
make -C tests check

%files
%license COPYING
%doc ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/magic

%files libs
%license COPYING
%doc ChangeLog
%{_libdir}/*so.*
%{_datadir}/magic*
%{_mandir}/man5/*
%{_datadir}/file
%{_datadir}/misc/*

%files devel
%{_libdir}/*.so
%{_includedir}/magic.h
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libmagic.pc

%files static
%{_libdir}/libmagic.a

%if %{with python2}
%files -n python2-magic
%license COPYING
%doc python/README.md python/example.py
%{python2_sitelib}/magic.py
%{python2_sitelib}/magic.pyc
%{python2_sitelib}/magic.pyo
%if 0%{?fedora} || 0%{?rhel} >= 6
%{python2_sitelib}/*egg-info
%endif
%endif

%if %{with python3}
%files -n python3-file-magic
%license COPYING
%doc python/README.md python/example.py
%{python3_sitelib}/magic.py
%{python3_sitelib}/*egg-info
%{python3_sitelib}/__pycache__/*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.47-1
- Prepare for Oreon 11 (RP1)
