%global source0_hash 4d341f90b6220d3e8cb251dacf726c41165285612248f2c52d15df4590a1ce3c
Name:           libsigrok
Version:        0.5.2
Release:        17%{?dist}
Summary:        Basic hardware access drivers for logic analyzers
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org/
Source0:        http://sigrok.org/download/source/libsigrok/%{name}-%{version}.tar.gz
Patch0:         libsigrok-0.5.2-lto.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  glibmm24-devel
BuildRequires:  graphviz
BuildRequires:  libftdi-devel
BuildRequires:  libieee1284-devel
BuildRequires:  libserialport-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  libzip-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{name} is a shared library written in C which provides the basic API
for talking to hardware and reading/writing the acquired data into various
input/output file formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        cxx
Summary:        C++ bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    cxx
The %{name}-cxx package contains C++ libraries for %{name}.

%package        cxx-devel
Summary:        Development files for  %{name} C++ bindings
Requires:       %{name}-cxx%{?_isa} = %{version}-%{release}
%description    cxx-devel
The %{name}-cxx-devel package contains libraries and header files for
developing applications that use %{name} C++ bindings.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for developing software
with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Upstream thinks it's a good idea to have two udev files. We disagree.
sed -e 's/ENV{ID_SIGROK}="1"/TAG+="uaccess"/g' contrib/60-libsigrok.rules -i

%build

%configure --disable-static --disable-python --disable-gpib --disable-java --disable-ruby CPPFLAGS=-I/usr/include/tirpc LDFLAGS=-ltirpc
make %{?_smp_mflags} V=1
echo "Documentation not packaged in this version" > README.fedora
%install
%make_install
install -D -p -m 0644 contrib/60-libsigrok.rules %{buildroot}%{_udevrulesdir}/60-libsigrok.rules
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libsigrok-devel -f %{oreon_filedir}/libsigrok-devel.list
%files -n libsigrok-cxx -f %{oreon_filedir}/libsigrok-cxx.list
%files -n libsigrok-cxx-devel -f %{oreon_filedir}/libsigrok-cxx-devel.list
%files -n libsigrok-doc -f %{oreon_filedir}/libsigrok-doc.list

%changelog

%autochangelog
