%global source0_hash 4d341f90b6220d3e8cb251dacf726c41165285612248f2c52d15df4590a1ce3c

Name:           libsigrok
Version:        0.5.2
Release:        17%{?dist}
Summary:        Basic hardware access drivers for logic analyzers
# Combined GPLv3+ and GPLv2+ and BSD
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org/
Source0:        http://sigrok.org/download/source/libsigrok/%{name}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1877485
# https://sigrok.org/gitweb/?p=libsigrok.git;a=commit;h=3decd3b1f0cbb3a035f72e9eade42279d0507b89
Patch0:         libsigrok-0.5.2-lto.patch

BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  glibmm24-devel
BuildRequires:  libzip-devel
BuildRequires:  zlib-devel
BuildRequires:  libieee1284-devel
BuildRequires:  libusb1-devel
BuildRequires:  libftdi-devel
BuildRequires:  libserialport-devel     >= 0.1.1
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libtirpc-devel
BuildRequires: make

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
# --disable-gpib: Fedora doesn't ship libgpib
# --disable-python: We don't package python bindings because they are a PITA
#                   for maintainers and are pretty horrible and useless anyway
# --disable-java: Be explicit rather than rely on missing java-devel
# --disable-ruby: Be explicit rather than rely on missing ruby-devel
%configure --disable-static --disable-python --disable-gpib --disable-java --disable-ruby CPPFLAGS=-I/usr/include/tirpc LDFLAGS=-ltirpc
make %{?_smp_mflags} V=1

# Doxygen produces different output based on the build arch. This will make
# our builds fail since -doc is a noarch package.
echo "Documentation not packaged in this version" > README.fedora

%install
%make_install
# Install udev rules
install -D -p -m 0644 contrib/60-libsigrok.rules %{buildroot}%{_udevrulesdir}/60-libsigrok.rules

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc README README.devices NEWS COPYING
%{_libdir}/libsigrok.so.4*
%{_udevrulesdir}/60-libsigrok.rules

# TODO: What are we supposed to do with these icons and MIME types?
%exclude %{_datadir}/icons/hicolor/48x48/mimetypes/libsigrok.png
%exclude %{_datadir}/icons/hicolor/scalable/mimetypes/libsigrok.svg
%exclude %{_datadir}/mime/packages/vnd.sigrok.session.xml

%files devel
%{_includedir}/libsigrok/
%{_libdir}/libsigrok.so
%{_libdir}/pkgconfig/libsigrok.pc

%files cxx
%{_libdir}/libsigrokcxx.so.4*

%files cxx-devel
%{_includedir}/libsigrokcxx/
%{_libdir}/libsigrokcxx.so
%{_libdir}/pkgconfig/libsigrokcxx.pc

%files doc
%doc README.fedora

%changelog
%autochangelog
