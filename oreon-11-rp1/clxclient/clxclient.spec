%global source0_hash 8501e964f0e0746abc5083a0b75fe3b937281cc4a9f7d1450ff98e86bc337881

%global libmajor 3

Summary:       C++ X Windows Library
Name:          clxclient
Version:       3.9.2
Release:       17%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# patch emailed upstream
Patch0:        clxclient-3.6.1-fsf-address.patch

BuildRequires: gcc-c++
BuildRequires: clthreads-devel >= 2.4.0
BuildRequires: libXft-devel 
BuildRequires: libX11-devel
BuildRequires: make

%description 
C++ X Windows library

%package -n clxclient-devel
Summary:       C++ X Windows Library Development Files
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n clxclient-devel
Header files required for the development of applications using the clxclient 
C++ X Windows library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

# Force Fedora's flags and correct linkage
sed -e '/ldconfig/d' \
    -e '/^CXXFLAGS += -march=native/d' \
    -e 's|-lpthread -lXft -lX11|-lclthreads -lXft -lX11|' \
    -i source/Makefile

%build
%set_build_flags
CXXFLAGS="${CXXFLAGS} -I."
%make_build -C source PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
%make_install -C source PREFIX=%{_prefix} LIBDIR=%{_libdir}

%files
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}*.so.*

%files devel
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}.h

%changelog
%autochangelog
