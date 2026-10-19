%global source0_hash 9283f6e13f04314b4cf622bfbe481011acad59443a4218e9bcc95bc0eb9ea6bc
%global debug_package %{nil}
%ifarch %{ix86}
%global build_type_safety_c 2
%endif
Name:           qm-dsp1.7
Version:        1.7.1
Release:        1%{?dist}
Summary:        Library for DSP and Music Informatics purposes
%global forgeurl https://github.com/c4dm/qm-dsp
%global tag qm-vamp-plugins-v%{version}
%forgemeta
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{tag}/qm-dsp-%{tag}.tar.gz
Patch0:         qm-dsp1.7-flags.patch
Patch1:         qm-dsp1.7-install.patch
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  imake
BuildRequires:  kiss-fft-static
BuildRequires:  make
# /oreon:deps
%description
%{name} is a C++ library of functions for DSP and Music Informatics purposes
developed at Queen Mary, University of London. It is used by the QM Vamp
Plugins (q.v.) among other things.

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
Provides:       qm-dsp-devel = %{version}-%{release}
Provides:       qm-dsp-static = %{version}-%{release}
Provides:       bundled(clapack)
%description devel
%{name} is a C++ library of functions for DSP and Music Informatics purposes
developed at Queen Mary, University of London. It is used by the QM Vamp
Plugins (q.v.) among other things.

This package contains header files and static library for development with
qm-dsp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{topdir} -N -Sgendiff
cp -p build/linux/Makefile.linux32 Makefile
%autopatch -p1
# use specified CFLAGS for tests
cat >> tests/Makefile <<EOF

%.o: %.cpp
	\$(CXX) \$(CPPFLAGS) \$(CFLAGS) -c \$<
EOF
# unbundle kiss-fft
rm -rf ext/
# helper Makefile without valgrind
sed -e 's/$(VG) //' tests/Makefile > tests/Makefile.novg

%build

make depend
%ifarch %{ix86}
EXTRA_CFLAGS="-msse -mfpmath=sse"
%endif
%ifarch x86_64
EXTRA_CFLAGS="-msse -msse2 -mfpmath=sse"
%endif
CFLAGS="$EXTRA_CFLAGS %{?optflags} -I%{_includedir}/kissfft" \
LDFLAGS="%{?__global_ldflags}" \
%make_build
%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qm-dsp1.7-devel -f %{oreon_filedir}/qm-dsp1.7-devel.list

%changelog

%autochangelog
