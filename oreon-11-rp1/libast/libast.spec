%global source0_hash b361b30ed58e92e4954d2d3995295c164cf1fc31271b5651f5799ba457dba4d9
%global        cvs 20080502
Summary:        Library of Assorted Spiffy Things
Name:          libast
Version:       0.7.1
Release:        1%{?dist}
License:       LicenseRef-Callaway-BSD
URL:           http://www.eterm.org/
Source0:        %{name}-%{cvs}.tar.gz
Source1:       libast-wrapper.h
Patch0:        libast-m4-include.patch
Patch1:        libast-configure-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  imlib2-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
LibAST is the Library of Assorted Spiffy Things.  It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions.  It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

It's not documented yet, mostly because it's not finished.  Hence the
version number that begins with 0.

%package       devel
Summary:       Header files, libraries and development documentation for libast
Requires:      libast = %{version}-%{release}
%description devel
This package contains the header files, static libraries and
development documentation for libast. If you like to develop programs
using libast, you will need to install libast-devel.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libast-%{cvs}

%build

./autogen.sh
autoupdate
%configure --with-regexp=posix
%make_build
%install
%make_install
for header in sysdefs types ; do
    mv %{buildroot}%{_includedir}/libast/$header.h \
       %{buildroot}%{_includedir}/libast/$header-%{_arch}.h
    install -m 0644 -c %{SOURCE1} %{buildroot}%{_includedir}/libast/$header.h
    sed -i -e 's/<HEADER>/'$header'/g' %{buildroot}%{_includedir}/libast/$header.h
    touch -r ChangeLog %{buildroot}%{_includedir}/libast/$header.h
done
sed -i -e '/^LDFLAGS=/d' %{buildroot}%{_bindir}/libast-config
touch -r ChangeLog %{buildroot}%{_bindir}/libast-config
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libast-devel -f %{oreon_filedir}/libast-devel.list

%changelog

%autochangelog
