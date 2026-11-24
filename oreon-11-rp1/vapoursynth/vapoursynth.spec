# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cb7ea3c75431176f8ce1f466e1c1fff7ffdacdd2d397be8fabc2d467194ab5a6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:       vapoursynth
Version:    79
Release:        %{autorelease}
Summary:    Video processing framework with simplicity in mind
License:    LGPL-2.1-only
URL:        http://www.vapoursynth.com

Source0:    https://github.com/%{name}/%{name}/archive/R%{version}/%{name}-R%{version}.tar.gz
Patch0:     %{name}-vsscript-soversion.patch
Patch1:     %{name}-float16-native-check.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(zimg)
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global vsdir %{python3_sitearch}/%{name}

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
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

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
%oreon_sha256
%autosetup -p1 -n %{name}-R%{version}

%generate_buildrequires
%pyproject_buildrequires -R

%build
%pyproject_wheel -C setup-args=-Dpython.allow_limited_api=false

%install
%pyproject_install
%pyproject_save_files -l %{name}

rm -fr %{buildroot}%{_docdir}/%{name}

mkdir -p %{buildroot}%{vsdir}/plugins

mkdir -p %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{vsdir}/include/*.h %{buildroot}%{_includedir}/%{name}/
rmdir %{buildroot}%{vsdir}/include

rm -fr %{buildroot}%{vsdir}/pkgconfig
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc <<EOF
prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/%{name}

Name: vapoursynth
Description: A frameserver for the 21st century
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lvapoursynth
EOF

mkdir -p %{buildroot}%{_libdir}
for lib in $(cd %{buildroot}%{vsdir} && ls libvapoursynth.so.* libvsscript.so.*); do
    ln -s %{vsdir}/${lib} %{buildroot}%{_libdir}/${lib}
    ln -s ${lib} %{buildroot}%{_libdir}/${lib%%.so.*}.so
done

sed -i -e '\#/%{name}/lib.*\.so#d' \
       -e '\#/%{name}/vspipe$#d' \
       -e '\#/%{name}/include#d' \
       -e '\#/%{name}/pkgconfig#d' \
       -e '\#^%%dir %{vsdir}$#d' \
       %{pyproject_files}

%check
%pytest

%files libs
%doc ChangeLog
%license COPYING.LESSER
%dir %{vsdir}
%dir %{vsdir}/plugins
%{vsdir}/lib%{name}.so.*
%{vsdir}/lib%{name}filters*.so
%{vsdir}/libvsscript.so.*
%{_libdir}/lib%{name}.so.*
%{_libdir}/libvsscript.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/libvsscript.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/%{name}
%{_bindir}/vspipe
%{vsdir}/vspipe

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
