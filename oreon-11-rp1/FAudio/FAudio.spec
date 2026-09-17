%global source0_hash dbcf99a869da402d5f538e435ab7fd4992b2b255c9939e546f1905c3e6e80ff9

Name:     FAudio
Version:  25.05
Release:  4%{?dist}
Summary:  FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries

License:  zlib
URL:      https://fna-xna.github.io/
Source0:  https://github.com/FNA-XNA/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++

BuildRequires: SDL3-devel

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL3

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL3

%description
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%package -n libFAudio
Summary:  %{summary}

%description -n libFAudio
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.

%package -n libFAudio-devel
Summary:  Development files for the FAudio library
Requires: libFAudio%{?_isa} = %{version}-%{release}

%description -n libFAudio-devel
Development files for the FAudio library.

%package -n mingw32-%{name}
Summary:        %{summary}
BuildArch:      noarch

%description -n mingw32-%{name}
%{summary}.

%package -n mingw64-%{name}
Summary:        %{summary}
BuildArch:      noarch

%description -n mingw64-%{name}
%{summary}.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mkdir ../mingw-build
cp -rp . ../mingw-build

%build
%cmake
%cmake_build

pushd ../mingw-build
%mingw_cmake
%mingw_make %{?_smp_mflags}
popd

%install
%cmake_install

pushd ../mingw-build
%mingw_make_install
%mingw_debug_install_post
popd

%files -n libFAudio
%license LICENSE
%doc README
%{_libdir}/libFAudio.so.0*

%files -n libFAudio-devel
%{_libdir}/libFAudio.so
%{_libdir}/cmake/FAudio/
%{_libdir}/pkgconfig/FAudio.pc
%{_includedir}/F3DAudio.h
%{_includedir}/FACT.h
%{_includedir}/FACT3D.h
%{_includedir}/FAPO.h
%{_includedir}/FAPOBase.h
%{_includedir}/FAPOFX.h
%{_includedir}/FAudio.h
%{_includedir}/FAudioFX.h

%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/FAudio.dll
%{mingw32_includedir}/F3DAudio.h
%{mingw32_includedir}/FACT.h
%{mingw32_includedir}/FACT3D.h
%{mingw32_includedir}/FAPO.h
%{mingw32_includedir}/FAPOBase.h
%{mingw32_includedir}/FAPOFX.h
%{mingw32_includedir}/FAudio.h
%{mingw32_includedir}/FAudioFX.h
%{mingw32_libdir}/cmake/%{name}/
%{mingw32_libdir}/libFAudio.dll.a
%{mingw32_libdir}/pkgconfig/%{name}.pc

%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/FAudio.dll
%{mingw64_includedir}/F3DAudio.h
%{mingw64_includedir}/FACT.h
%{mingw64_includedir}/FACT3D.h
%{mingw64_includedir}/FAPO.h
%{mingw64_includedir}/FAPOBase.h
%{mingw64_includedir}/FAPOFX.h
%{mingw64_includedir}/FAudio.h
%{mingw64_includedir}/FAudioFX.h
%{mingw64_libdir}/cmake/%{name}/
%{mingw64_libdir}/libFAudio.dll.a
%{mingw64_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
