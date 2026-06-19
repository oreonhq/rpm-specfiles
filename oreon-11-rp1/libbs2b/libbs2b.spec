%global source0_hash b97164dd98fda4b05722fd68ffed2427b980dfb8316bbbbcfc0cde3ae5238cd5

Name:		libbs2b
Version:	3.1.0
Release:        %autorelease
Summary:	Bauer stereophonic-to-binaural DSP library

License:	MIT
URL:		http://bs2b.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/bs2b/libbs2b/%{version}/%{name}-%{version}.tar.lzma
Patch0:		libbs2b-security.patch

BuildRequires:  gcc-c++
BuildRequires:	autoconf automake libtool
BuildRequires:	libsndfile-devel
BuildRequires: make
# the dependency (required for bs2bconvert) gets added automatically
#Requires:	libsndfile


%package devel
Summary:	Development files for libbs2b
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is designed
to improve headphone listening of stereo audio records. Recommended for
headphone prolonged listening to disable superstereo fatigue without essential
distortions.


%description devel
This package contains the development files for the Bauer
stereophonic-to-binaural (bs2b) DSP effect library.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1

# automake 1.12 removes support for lzma, it has been replaced by xz
# it is safe to substitute xz for lzma to get rid of autoreconf errors,
# we don't build the dist archive anyways
sed -i -e 's/lzma/xz/g' configure.ac
# reconf to support aarch64 (bug #925677)
autoreconf -vif

%build
%configure --disable-static
# disable rpath as suggested in
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
rm %{buildroot}/%{_libdir}/%{name}.la


%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*
%{_libdir}/%{name}.so.*


%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%ldconfig_scriptlets

%changelog
%autochangelog
