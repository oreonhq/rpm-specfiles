%global source0_hash b524208f2b09fa5edb6720db007f2f8013089d64bebd87aabd147f79bf5f40b9
Name:           cutter-re
Version:        2.5.0
Release:        1%{?dist}
Summary:        GUI for Rizin reverse engineering framework
License:        GPL-3.0-only AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://cutter.re/
VCS:            https://github.com/rizinorg/cutter
Source0:        https://github.com/rizinorg/cutter/releases/download/v%{version}/Cutter-v%{version}-src.tar.gz
Source1:        cutter-re.desktop
Source2:        cutter-re.appdata.xml
%ifarch %{qt5_qtwebengine_arches}
%endif
Requires:       python3-jupyter-client
Requires:       python3-notebook
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz-devel
BuildRequires:  kf5-syntax-highlighting-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  rizin-devel
# /oreon:deps
%description
Cutter is a Qt and C++ GUI for Rizin. Its goal is making an advanced,
customizable and FOSS reverse-engineering platform while keeping the user
experience at mind. Cutter is created by reverse engineers for reverse
engineers.

%package devel
Summary:        Development files for the cutter-re package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the cutter-re package. See cutter-re package for more
information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Cutter-v%{version}
%oreon_prep
%build

%cmake -DCUTTER_USE_BUNDLED_RIZIN=OFF
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_bindir}/cutter %{buildroot}%{_bindir}/cutter-re
mkdir -p %{buildroot}%{_datadir}/applications
rm %{buildroot}%{_datadir}/applications/re.rizin.cutter.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
        %{SOURCE1}
mkdir -p %{buildroot}%{_metainfodir}
install -pm644 %{SOURCE2} \
        %{buildroot}%{_metainfodir}
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/{cutter,cutter-re}.svg
sed -i 's/bin\/cutter/bin\/cutter-re/g' %{buildroot}%{_libdir}/cmake/Cutter/CutterTargets-*.cmake
%oreon_autofiles cutter-re-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n cutter-re-devel -f %{oreon_filedir}/cutter-re-devel.list

%changelog

%autochangelog
