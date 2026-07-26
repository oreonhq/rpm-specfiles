%global source0_hash c659b14c0c4055c44432cb83060b95d30ae0c1ecc6f50d73968e239c100f7a31

%global libmajor 2

Summary:       POSIX threads C++ access library
Name:          clthreads
Version:       2.4.2
Release:       17%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://kokkinizita.linuxaudio.org/linuxaudio/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
BuildRequires: gcc-c++
BuildRequires: make

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

%files
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
