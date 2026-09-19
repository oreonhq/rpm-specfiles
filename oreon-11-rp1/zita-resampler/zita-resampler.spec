%global source0_hash aa5c54e696069af26f3f1fed4a963113cc1237cddfd57ae5842abcb1acd5492c

Summary:       Fast, high-quality sample rate conversion library
Name:          zita-resampler
Version:       1.11.2
Release:       4%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://kokkinizita.linuxaudio.org/linuxaudio/zita-resampler/resampler.html
Source0:       http://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-resampler-%{version}.tar.xz
BuildRequires: gcc-c++
BuildRequires: libsndfile-devel
BuildRequires: make

%description
zita-resampler is a C++ library for resampling audio signals. It is
designed to be used within a real-time processing context, to be fast,
and to provide high-quality sample rate conversion.

The library operates on signals represented in single-precision
floating point format. For multichannel operation both the input and
output signals are assumed to be stored as interleaved samples.

The API allows a trade-off between quality and CPU load. For the
latter a range of approximately 1:6 is available. Even at the highest
quality setting zita-resampler will be faster than most similar
libraries, e.g. libsamplerate.

%package  devel
Summary:       Development libraries and headers for %{name}
Requires:      %{name} = %{version}-%{release}

%description devel
This package contains the headers and development libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# To make sure to have the correct Fedora specific flags:
sed -i -e 's|-O[23]||' -e 's|ldconfig||' -e 's|-march=native||' -e '/^CPPFLAGS += -DENABLE_SSE2/d' source/Makefile
sed -i -e 's|-O[23]||' -e 's|-march=native||' apps/Makefile

%build
%set_build_flags

# Enable SSE2 on x86_64
%ifarch x86_64
CPPFLAGS+=" -DENABLE_SSE2"
export CPPFLAGS
%endif

%make_build -C source
# In order to build apps, we need to create the symlink
# Note that this is originally done at "make install" stage
ln -sf libzita-resampler.so.%{version} source/libzita-resampler.so

CXXFLAGS+=" -I../source"
LDFLAGS+=" -L../source"
%make_build -C apps

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} -C source install
%make_install MANDIR=%{_mandir}/man1 PREFIX=%{_prefix} LIBDIR=%{_libdir} -C apps install
chmod 755 %{buildroot}/%{_libdir}/lib%{name}.so.%{version}

%files
%doc AUTHORS
%license COPYING
%{_libdir}/lib%{name}.so.1*
%{_bindir}/zresample
%{_bindir}/zretune
%{_mandir}/man1/zresample.1.*
%{_mandir}/man1/zretune.1.*

%files devel
%doc docs/*
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
