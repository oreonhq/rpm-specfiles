%global source0_hash 9aa11484fb30b4e6ef00c8a3281eebcfad9221e3937b1beb5fe21b748d89325f

Summary:       Convolution engine library
Name:          zita-convolver
Version:       4.0.3
Release:       18%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://kokkinizita.linuxaudio.org/
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: fftw-devel
BuildRequires: gcc-c++

%description
%{name} is a fast, partitioned convolution engine library.

%package  devel
Summary:       Fast, partitioned convolution engine library
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      fftw-devel

%description devel
%{name} is a fast, partitioned convolution engine library. This package
contains libraries and header files for developing applications that use
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Preserve timestamps
sed -i 's|install |install -p |' source/Makefile

# No need to call ldconfig during packaging
sed -i '\|ldconfig|d' source/Makefile

sed -i '\|^CXXFLAGS += -march=native|d' source/Makefile

%build
%set_build_flags
%make_build -C source PREFIX=%{_prefix}

%install
%make_install -C source PREFIX=%{_prefix} LIBDIR=%{_libdir}

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/lib%{name}.so.4*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
