%global source0_hash b461a31065d6912d190f78ad0041218009f44a5acdb5757545bd4a8bd6b509aa

Name:           liboglappth
Summary:        An OpenGL wrapper library
Version:        1.0.0
Release:        24%{?dist}

# SPDX confirmed
License:        GPL-2.0-or-later
URL:            http://www.bioinformatics.org/ghemical/ghemical/index.html
Source0:        http://www.bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  make

%description
Library for creating portable OpenGL applications with easy-to-code
scene setup and selection operations.

%package devel
Summary:    Libraries and header files from %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header include files for developing programs
based on %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# FIXME: set -e behavior change between f26 and f27??
[ -s NEWS ] && exit 1 || :
[ -s README ] && exit 1 || :
autoreconf -v -f -i

%build
%configure --disable-static
make %{?_smp_mflags} CCOPTIONS="%{optflags}" LIBS="-lGL -lGLU"

%install
%make_install
find %{buildroot}%{_libdir} -name *.la -exec rm -rf {} \;

%ldconfig_scriptlets

%files
%doc AUTHORS
%doc ChangeLog
%license COPYING

%{_libdir}/liboglappth.so.2{,.*}

%files devel
%{_includedir}/oglappth/
%{_libdir}/liboglappth.so
%{_libdir}/pkgconfig/liboglappth.pc

%changelog
%autochangelog
