%global source0_hash none
%global srcname KataGo
%global forgeurl https://github.com/lightvector/%{srcname}
%global katago_backends eigen opencl
%global common_description %{expand:
KataGo is a strong open-source self-play-trained Go engine, with many
improvements to accelerate learning. It can predict score and territory, play
handicap games reasonably, and handle many board sizes and rules all with the
same neural net.}
Name:           katago
Version:        1.18.2
Release:        1%{?dist}
Summary:        GTP engine and self-play learning in Go
License:        MIT AND Apache-2.0 AND BSD-3-Clause
URL:            https://katagotraining.org
Source0:        %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        README.fedora
Requires:       %{name}-backend = %{version}-%{release}
Suggests:       %{name}-doc = %{version}-%{release}
Provides:       bundled(clblast)
Provides:       bundled(sha2)
Provides:       bundled(tclap) = 1.2.2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  gulrak-filesystem-devel
BuildRequires:  half-devel
BuildRequires:  json-devel
BuildRequires:  libzip-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  sed
BuildRequires:  zlib-devel
# /oreon:deps
%description    %{common_description}

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc  %{common_description}

This package provides additional documentation for %{name}.

%package        eigen
Summary:        %{summary} - eigen backend
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Provides:       %{name}-backend = %{version}-%{release}
%description    eigen %{common_description}

This package contains the CPU-only eigen-based backend for KataGo.

%package        opencl
Summary:        %{summary} - OpenCL backend
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Provides:       %{name}-backend = %{version}-%{release}
%description    opencl %{common_description}

This package contains the OpenCL-based backend for KataGo.

%prep

%autosetup -n %{srcname}-%{version} -p1

# Copy README.fedora
cp -p %SOURCE1 .

# Fix permissions
chmod -x images/docs/*.png

# Trim bundled libraries and replace with the system ones
rm -r cpp/external/{filesystem-1.5.8,half-2.2.0,httplib,mozilla-cacerts,nlohmann_json}
mkdir -p cpp/external/filesystem-1.5.8/include
ln -s %{_includedir}/ghc cpp/external/filesystem-1.5.8/include/
mkdir -p cpp/external/half-2.2.0/include
ln -s %{_includedir}/half.hpp cpp/external/half-2.2.0/include/
ln -s %{_includedir}/nlohmann cpp/external/nlohmann_json

# Do not hardcode SSE
sed -i '/-mfpmath=sse/d' cpp/CMakeLists.txt

%build

pushd cpp
for backend in %{katago_backends}; do
  %cmake \
    -DNO_GIT_REVISION=1 \
    -DUSE_BACKEND="$(echo "$backend" | tr '[a-z]' '[A-Z]')"
  %cmake_build
  cp -p %{_vpath_builddir}/%{name} "../%{name}-${backend}"
  rm -r %{_vpath_builddir}/%{name}
done
%install
for backend in %{katago_backends}; do
  install -Dpm0755 -t %{buildroot}%{_bindir} "%{name}-${backend}"
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post eigen

%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}-eigen 10
%postun eigen

if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.eigen
fi
%post opencl

%{_sbindir}/update-alternatives --install %{_bindir}/%{name} \
  %{name} %{_bindir}/%{name}-opencl 10
%postun opencl

if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}.opencl
fi
%files -f %{oreon_filedir}/main.list
%files -n katago-doc -f %{oreon_filedir}/katago-doc.list
%files -n katago-eigen -f %{oreon_filedir}/katago-eigen.list
%files -n katago-opencl -f %{oreon_filedir}/katago-opencl.list

%changelog

%autochangelog
