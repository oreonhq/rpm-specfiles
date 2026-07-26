%global source0_hash edc266a5f7a1f1c7f71cf5c6c9727e05008b728eae3bb42beb7d0b24ce07c5c3

Name:           cutter-re
Version:        2.3.4
Release:        10%{?dist}
Summary:        GUI for Rizin reverse engineering framework

# CC-BY-SA: src/img/icons/
# CC0: src/fonts/Anonymous Pro.ttf
License:        GPL-3.0-only AND CC-BY-SA-3.0 AND CC0-1.0

URL:            https://cutter.re/
VCS:            https://github.com/rizinorg/cutter
Source0:        %{vcs}/releases/download/v%{version}/Cutter-v%{version}-src.tar.gz
Source1:        cutter-re.desktop
Source2:        cutter-re.appdata.xml

BuildRequires:  rizin-devel >= 0.6.1
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  kf5-syntax-highlighting-devel
BuildRequires:  python3-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  file-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  graphviz-devel
BuildRequires:  qt5-linguist
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  qt5-qtwebengine-devel
%endif
Requires:       python3-jupyter-client
Requires:       python3-notebook
Requires:       hicolor-icon-theme

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

%autosetup -p1 -n Cutter-v%{version}

%build
%cmake -DCUTTER_USE_BUNDLED_RIZIN=OFF
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_bindir}/cutter %{buildroot}%{_bindir}/cutter-re

# replace default .desktop file with our own, to use cutter-re name
mkdir -p %{buildroot}%{_datadir}/applications
rm %{buildroot}%{_datadir}/applications/re.rizin.cutter.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
        %{SOURCE1}

mkdir -p %{buildroot}%{_metainfodir}
install -pm644 %{SOURCE2} \
        %{buildroot}%{_metainfodir}

# rename cutter svg icon to cutter-re
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/{cutter,cutter-re}.svg
sed -i 's/bin\/cutter/bin\/cutter-re/g' %{buildroot}%{_libdir}/cmake/Cutter/CutterTargets-*.cmake

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%{_bindir}/cutter-re
%{_datadir}/applications/*.desktop
%{_datadir}/rizin/cutter/translations/*.qm
%{_metainfodir}/*.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%license COPYING src/img/icons/Iconic-LICENSE
%doc README.md

%files devel
%{_includedir}/cutter
%{_libdir}/cmake/Cutter/*.cmake
%dir %{_libdir}/cmake/Cutter

%changelog
%autochangelog
