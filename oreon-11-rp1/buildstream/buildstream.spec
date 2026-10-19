%global source0_hash 43c458f14a4c9993876f4e1898b41f9deb90a63994ae5800e11186908b1e1deb
Name:          buildstream
Summary:        Build/integrate software stacks
License:       Apache-2.0
URL:           https://buildstream.build/
ExcludeArch:   %{ix86}
Version:       2.8.1
Release:        1%{?dist}
Source0:        https://github.com/apache/buildstream/archive/%{version}/buildstream-%{version}.tar.gz
Patch:         0001-requirements-requirements.in-Do-not-limit-protobuf-v.patch
Requires:      buildbox
Requires:      fuse3
Requires:      fuse3-libs
Requires:      lzip
Requires:      patch
Requires:      tar
Recommends:    buildstream-plugins
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(Cython) >= 0.29.25
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-buildstream = %{version}-%{release}
# /oreon:deps
%description
BuildStream is a Free Software tool for building/integrating software stacks.
It takes inspiration, lessons and use-cases from various projects including
OBS, Reproducible Builds, Yocto, Baserock, Buildroot, Aboriginal, GNOME
Continuous, JHBuild, Flatpak Builder and Android repo.

BuildStream supports multiple build-systems (e.g. autotools, cmake, cpan,
distutils, make, meson, qmake), and can create outputs in a range of formats
(e.g. debian packages, flatpak runtimes, sysroots, system images) for multiple
platforms and chipsets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

./setup.py build_grpc
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
