%global source0_hash 3bd560309fd6d70b14bbb8230e1baf8706b804eb6201220bb6c3d6db72003d1b
Name:           staden-io_lib
Version:        1.14.8
Release:        1%{?dist}
Summary:        General purpose library to handle gene sequencing machine trace files
License:        MIT
URL:            http://staden.sourceforge.net
Source0:        http://downloads.sourceforge.net/staden/io_lib-%{version}.tar.gz
Patch0:         staden-libs-config.patch
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Staden I/O library provides a general purpose interface for reading and
writing trace files and other bioinformatics experiment files.  The programmer
simply calls, for example, the read_reading function to create a "Read" C
structure with the data loaded into memory.  It has been compiled and tested
on a variety of Unix systems, MacOS X and MS Windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n io_lib-%{version} -p1

# libread is too generic. Make up something more specific.
# Also fix config script name to include the "staden-" part.
mv io_lib-config.in staden-io_lib-config.in
sed -i 's/libread/libstaden-read/g' io_lib/Makefile.in progs/Makefile.in
sed -i 's/lread/lstaden-read/' staden-io_lib-config.in
sed -i 's/io_lib-config/staden-io_lib-config/g' configure Makefile.in

%build

%configure --disable-static
sed -i 's+\(search_path_spec=\"\)+\1/lib64 /usr/lib64 +' libtool
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
%ldconfig_scriptlets
%global so_version 11
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n staden-io_lib-devel -f %{oreon_filedir}/staden-io_lib-devel.list

%changelog

%autochangelog
