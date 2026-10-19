%global source0_hash 8e1ba552fd8b0783076d42ac1c2eeda57781c89f9bcc119f9d00ff1326e95e13
%define with_static %{?_with_static: 1} %{?!_with_static: 0}
Name:           dar
Version:        2.8.6
Release:        1%{?dist}
Summary:        Software for making/restoring incremental CD/DVD backups
License:        GPL-2.0-or-later
URL:            http://dar.linux.free.fr
Source0:        ftp://ftp.dm3c.org/dar.linux.free.fr/Releases/Source_code/%{name}-%{version}.tar.gz
Source1:        README.Fedora
Requires:       par2cmdline
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  gpgme-devel
BuildRequires:  libargon2-devel
BuildRequires:  libattr-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  librsync-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  rhash-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
DAR is a command line tool to backup a directory tree and files. DAR is
able to make differential backups, split them over a set of disks or files
of a given size, use compression, filter files or sub-trees to be saved or
not saved, directly access and restore given files. DAR is also able
to handle extended attributes, and can make remote backups through an
ssh session for example. Finally, DAR handles save and restore of hard
and symbolic links.

%package -n libdar
Summary:    Library providing support for the DAR API
%description -n libdar
This package contains the common library code for DAR, which provides the
core functionality for creating and restoring backups.

%package -n libdar-devel
Summary:    Development files for libdar
Requires:   libdar%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libdar-devel
This package contains the header files and libraries for developing
programs that use the DAR API (libdar).

# The following two subpackages are only built when enabled via "--with static"
%if %{with_static}

%package -n dar-static
Summary:    Statically linked version of dar
%description -n dar-static
Statically linked version of dar that can be installed onto backup disks for
easier file retrieval.

%package -n libdar-static-devel
Summary:    Statically linked dar library files
%description -n libdar-static-devel
Statically linked version of dar libraries that can be installed onto backup
disks for easier file retrieval.

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure \
    --disable-build-html \
    --enable-mode=64 \
%if !%{with_static}
    --disable-dar-static \
    --disable-static
%endif
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
%find_lang %{name}
rm -f  %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_datadir}/dar/
rm -f doc/Makefile*
rm -f doc/*/Makefile*
mv doc html
chmod 0644 html/samples/*
cp -a %{SOURCE1} .
%oreon_autofiles libdar usr/*/lib*.so.*
%oreon_autofiles libdar-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/dar --version
%files -f %{oreon_filedir}/main.list
%files -n libdar -f %{oreon_filedir}/libdar.list
%files -n libdar-devel -f %{oreon_filedir}/libdar-devel.list

%changelog

%autochangelog
