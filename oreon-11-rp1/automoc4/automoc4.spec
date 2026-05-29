%global source0_hash 991d0376a63983c1b62e85624b613fa2d1168f73ba166939c216cbd0a2990856

# Upstream KDE automoc 0.9.88 ships Automoc4Config.cmake without cmake_policy(SET CMP0002 OLD).
# Fedora automoc4 added that policy for ancient CMake; CMake 3.28+ rejects OLD for CMP0002 and
# find_package(KDE4) fails. Epoch so this replaces same-version distro builds in mock.
Epoch:   1
Summary: KDE4 Meta Object Compiler (automoc4)
Name:    automoc4
Version: 0.9.88
Release: 1%{?dist}

License: BSD-3-Clause
URL:     https://invent.kde.org/developer-tools/automoc

# GitHub tag tarball unpacks to directory automoc-0.9.88 (matches setup -n automoc plus hyphen plus version digits).
# Fragment after hash sets the saved tarball basename for spectool (automoc plus version tarball name).
Source0:        https://github.com/KDE/automoc/archive/refs/tags/v0.9.88.tar.gz#/automoc-0.9.88.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: kde4-filesystem
BuildRequires: qt4-devel

%ifarch x86_64 aarch64 ppc64 ppc64le s390x
%global automoc_lib_suffix 64
%else
%global automoc_lib_suffix %{nil}
%endif

%description
automoc4 scans C++ sources for Q_OBJECT macros and runs moc where needed. This package ships the
automoc4 binary and the CMake module files used by KDE4 and kdelibs4.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n automoc-%{version}


%build
# Upstream asks for CMake 2.4; CMake 4 removed compatibility with that floor. Same pattern as kde-workspace.
export CMAKE_POLICY_VERSION_MINIMUM=3.5
mkdir build
pushd build
%if 0%{?automoc_lib_suffix:1}
%__cmake .. \
  -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5 \
  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DLIB_SUFFIX:STRING=%{automoc_lib_suffix} \
  -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_qt4_bindir}/qmake
%else
%__cmake .. \
  -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5 \
  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DQT_QMAKE_EXECUTABLE:FILEPATH=%{_qt4_bindir}/qmake
%endif
%__cmake --build . -- %{?_smp_mflags}
popd


%install
DESTDIR=%{buildroot} %__cmake --install build


%files
%{_bindir}/automoc4
%{_libdir}/automoc4/


%changelog
* Sun May 03 2026 Oreon packaging <noreply@oreon.local> - 1:0.9.88-1
- Initial Oreon automoc4 from upstream tag v0.9.88; CMake 4 policy floor for configure
