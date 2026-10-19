%global source0_hash d48282ae4dab83b3dc94c16cf011bcb63835c1c02b515490e1883049c3d1f3da
%bcond_without verbose_build
%if %{with verbose_build}
%global _verbose -v
%else
%global _verbose %{nil}
%endif
Name:           aubio
Version:        0.4.9
Release:        1%{?dist}
Summary:        An audio labeling tool
License:        GPL-3.0-or-later
URL:            https://aubio.org/
Source0:        https://aubio.org/pub/aubio-%{version}.tar.bz2
Patch0:         %{name}-unversioned-python.patch
Patch1:         %{name}-python39.patch
Patch2:         %{name}-invalid-escape-sequence.patch
Patch3:         %{name}-imp-removed.patch
Patch4:         0001-py-add-const-qualifiers-to-ufuncs-prototypes-for-lat.patch
Requires:       %{name}-python3 = %{version}-%{release}
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
BuildRequires:  txt2man
# /oreon:deps
%description
aubio is a tool and library for audio labeling. Its features include
segmenting a sound file before each of its attacks, performing pitch
detection, tapping the beat and producing midi streams from live
audio. The name aubio comes from 'audio' with a typo: several
transcription errors are likely to be found in the results too.

The aim of this project is to provide these automatic labeling
features to other audio software. Functions can be used offline in
sound editors and software samplers, or online in audio effects and
virtual instruments.

%package        lib
Summary:        An audio labeling library
%description    lib
aubio is a tool and library for audio labeling. Its features include
segmenting a sound file before each of its attacks, performing pitch
detection, tapping the beat and producing midi streams from live
audio. The name aubio comes from 'audio' with a typo: several
transcription errors are likely to be found in the results too.

The aim of this project is to provide these automatic labeling
features to other audio software. Functions can be used offline in
sound editors and software samplers, or online in audio effects and
virtual instruments.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python3
Summary:        Python 3 language bindings for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python3
%description    python3
The %{name}-python3 package contains the Python 3 language bindings for
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%{python3} ./waf configure \
    --prefix="%_prefix" \
    --bindir="%_bindir" \
    --sysconfdir="%_sysconfdir" \
    --datadir="%_datadir" \
    --includedir="%_includedir" \
    --libdir="%_libdir" \
    --mandir="%_mandir" \
    --docdir="%_docdir" \
    --enable-fftw3f \
    --enable-complex \
    --enable-jack \
    --enable-samplerate
%{python3} ./waf build %{_verbose} %{?_smp_mflags}
%py3_build
%install
%{python3} ./waf --destdir=%{buildroot} %{_verbose} install
rm -f %{buildroot}%{_libdir}/*.a
rm -rf libaubio-doc
cp -r %{buildroot}%{_docdir}/libaubio-doc libaubio-doc
rm -rf %{buildroot}%{_docdir}/libaubio-doc
%py3_install
sed -i -e '/^#![[:blank:]]*\//, 1d' %{buildroot}%{python3_sitearch}/%{name}/*.py
%oreon_autofiles aubio-lib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles aubio-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles aubio-python3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n aubio-lib -f %{oreon_filedir}/aubio-lib.list
%files -n aubio-devel -f %{oreon_filedir}/aubio-devel.list
%files -n aubio-python3 -f %{oreon_filedir}/aubio-python3.list

%changelog

%autochangelog
