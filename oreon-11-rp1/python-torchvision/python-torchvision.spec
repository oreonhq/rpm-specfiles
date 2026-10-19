%global source0_hash f799cdd1d67a3edbcdc6af8fb416fe1b019b512fb426c0314302cd81518a0095
%global pypi_name torchvision
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2c4665ffbb64f03f5d18016d3398af4ac4da5f03
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20240326 
%global pypi_version 0.19.0a0
%else
%global pypi_version 0.24.0
%endif
%bcond_with test
%global toolchain gcc
Name:           python-%{pypi_name}
%if %{with gitcommit}
Version:        %{pypi_version}^git%{date0}.%{shortcommit0}
%else
Version:        %{pypi_version}
%endif
Release:        1%{?dist}
Summary:        Image and video datasets for torch deep learning
License:        BSD-3-Clause AND BSD-2-Clause AND MIT
URL:            https://github.com/pytorch/vision
%if %{with gitcommit}
Source0:        https://github.com/pytorch/vision/archive/refs/tags/v%{version}.tar.gz#/vision-v%{version}.tar.gz
%else
%endif
Patch1:         0001-A-better-cuda-version.patch
Patch2:         %{name}-ffmpeg8.patch
ExclusiveArch:  aarch64 x86_64
%if %{with test}
%endif
Requires:      python3dist(numpy)
Requires:      python3dist(pillow)
Requires:      python3dist(requests)
Requires:      python3dist(torch)
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-torchvision = %{version}-%{release}
# /oreon:deps
%description
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%package -n     python3-%{pypi_name}
Summary:        Image and video datasets for torch deep learning
%description -n python3-%{pypi_name}
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%autosetup -p1 -n vision-%{commit0}
%else
%autosetup -p1 -n vision-%{version}
%endif

# Need some debug info
sed -i -e 's@extra_compile_args["cxx"].append("-g0")@extra_compile_args["cxx"].append("-g")@' setup.py
# Find ffmpeg on fedora
sed -i -e 's@ffmpeg_include_dir = os.path.join(ffmpeg_root, "include")@ffmpeg_include_dir = os.path.join(ffmpeg_root, "include/ffmpeg")@' setup.py
sed -i -e 's@ffmpeg_library_dir = os.path.join(ffmpeg_root, "lib")@ffmpeg_library_dir = os.path.join(ffmpeg_root, "lib64")@'              setup.py

%build

export ROCM_HOME=/usr
export TORCHVISION_USE_WEBP=1
%pyproject_wheel
%install
%pyproject_install
for f in `find %{buildroot}%{python3_sitearch} -name '*.py'`; do
    if [ ! -x $f ]; then
        sed -i '1{\@^#!/usr/bin@d}' $f
    fi
done
%oreon_autofiles main usr/lib/python3*/site-packages/torchvision* usr/lib64/python3*/site-packages/torchvision* usr/bin/*

%files
%files -n python3-torchvision -f %{oreon_filedir}/python3-torchvision.list

%changelog

%autochangelog
