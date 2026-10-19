%global source0_hash c659b14c0c4055c44432cb83060b95d30ae0c1ecc6f50d73968e239c100f7a31
%global libmajor 2
Summary:        POSIX threads C++ access library
Name:          clthreads
Version:       2.4.2
Release:        17%{?dist}
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://kokkinizita.linuxaudio.org/linuxaudio/
Source0:        http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Clthreads is a C++ wrapper library around the POSIX threads API.

%package  devel
Summary:       Development files for %{name}
Requires:      %{name} = %{version}-%{release}
%description devel
Clthreads is a C++ wrapper library around the POSIX threads API. This package
contains libraries and header files for developing applications that use
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# No need to call ldconfig during packaging
sed -i '\|ldconfig|d' source/Makefile

# Fix Makefile paths (patch sent upstream)
sed -i -e 's|install -d $(DESTDIR)$(PREFIX)/$(INCDIR)|install -d $(DESTDIR)$(INCDIR)|' \
 -e 's|install -d $(DESTDIR)$(PREFIX)/$(LIBDIR)|install -d $(DESTDIR)$(LIBDIR)|' source/Makefile

# Preserve timestamps
sed -i 's|/install|/install -p|' source/Makefile

# No native arch
sed -i -e '/^CXXFLAGS += -march=native/d' source/Makefile

%build

%set_build_flags
%make_build -C source PREFIX=%{_prefix} LIBDIR=%{_libdir}
%install
%make_install -C source PREFIX=%{_prefix} LIBDIR=%{_libdir}
%oreon_autofiles clthreads-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n clthreads-devel -f %{oreon_filedir}/clthreads-devel.list

%changelog

%autochangelog
