%global source0_hash 650f77feebfd08842b521273f59e0c88f7ba9d7cb5f151d89b79b8dfdd4ce633

Name:       vapoursynth
Version:    72
Release:    %autorelease
Summary:    Video processing framework with simplicity in mind
License:    LGPL-2.1-only
URL:        http://www.vapoursynth.com

Source0:    https://github.com/%{name}/%{name}/archive/R%{version}/%{name}-R%{version}.tar.gz
Patch0:     %{name}-version-info.patch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
VapourSynth is an application for video manipulation. Or a plugin. Or a library.
It’s hard to tell because it has a core library written in C++ and a Python
module to allow video scripts to be created.

%package        libs
Summary:        VapourSynth's core library with a C++ API
Obsoletes:      lib%{name} < %{version}-%{release}
Provides:       lib%{name} == %{version}-%{release}
Obsoletes:      %{name}-plugins < %{version}-%{release}
Provides:       %{name}-plugins == %{version}-%{release}

%description    libs
VapourSynth's core library with a C++ API.

%package -n     python3-%{name}
Summary:        Python interface for VapourSynth

%description -n python3-%{name}
Python interface for VapourSynth/VSSCript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%package        tools
Summary:        Extra tools for VapourSynth
Requires:       python3-vapoursynth%{?_isa} = %{version}-%{release}

%description    tools
This package contains the vspipe tool for interfacing with VapourSynth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-R%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-x86-asm \
    --enable-core \
    --enable-vsscript \
    --enable-vspipe \
    --enable-python-module

%make_build

# Make libraries available for Python linking
ln -sf .libs build
%pyproject_wheel

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%pyproject_install
%pyproject_save_files %{name}

# Create plugin directory
mkdir -p %{buildroot}%{_libdir}/%{name}

# Let RPM pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%check
export LD_LIBRARY_PATH=build
%pytest

%files libs
%doc ChangeLog
%license COPYING.LESSER
%dir %{_libdir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}-script.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-script.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-script.pc

%files tools
%{_bindir}/vspipe

%files -n python3-%{name} -f %{pyproject_files}
%{python3_sitearch}/%{name}.so

%changelog
%autochangelog
