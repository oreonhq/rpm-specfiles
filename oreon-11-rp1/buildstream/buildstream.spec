%global source0_hash 1527a3ace1233caa42a42c2d40f03de401e6815978428ed560156acdbca072d8

Name:          buildstream
Summary:       Build/integrate software stacks
License:       Apache-2.0
URL:           https://buildstream.build/

ExcludeArch:   %{ix86}

Version:       2.7.0
Release:       %autorelease
Source0:       https://github.com/apache/buildstream/archive/%{version}/buildstream-%{version}.tar.gz
Patch:         0001-requirements-requirements.in-Do-not-limit-protobuf-v.patch

BuildRequires: gcc
BuildRequires: python3-devel >= 3.9
BuildRequires: python3-grpcio-tools

Requires:      buildbox
Requires:      fuse3
Requires:      fuse3-libs
Requires:      lzip
Requires:      patch
Requires:      tar

Recommends:    buildstream-plugins

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

%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
./setup.py build_grpc
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{name}

%files -n %{name} -f %{pyproject_files}
%doc NEWS README.rst
%{_bindir}/bst*
%{_datadir}/bash-completion/completions/bst
%{_mandir}/man1/*.1*

%changelog
%autochangelog
