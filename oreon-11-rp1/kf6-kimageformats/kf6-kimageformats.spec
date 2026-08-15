%global source0_hash 91808c6de080ab5b506721c1f78ad5772bcb1f70bba7262c275ccd98de8b6b38

%undefine __cmake_in_source_build
%global framework kimageformats

%global stable_kf6 stable
%global majmin_ver_kf6 6.28

Name:           kf6-%{framework}
Version:        6.28.0
Release:        2%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with additional image plugins for QtGui

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# upstream patches

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(KF6Archive) >= %{version}
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  pkgconfig(cups)
BuildRequires:  openexr-devel >= 3.2
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(libavif)
BuildRequires:  pkgconfig(libheif) >= 1.10.0
%if !((0%{?fedora} && 0%{?fedora} < 41) || (0%{?rhel} && 0%{?rhel} < 10))
BuildRequires:  pkgconfig(libjxl) >= 0.9.4
BuildRequires:  pkgconfig(libjxl_threads) >= 0.9.4
BuildRequires:  pkgconfig(libjxl_cms) >= 0.9.4
%endif
BuildRequires:  cmake(OpenJPEG)
BuildRequires:  pkgconfig(libraw) >= 0.20.2
BuildRequires:  pkgconfig(libraw_r) >= 0.20.2
BuildRequires:  jxrlib-devel

Requires:       kf6-filesystem
Requires:       openexr-libs%{?_isa}
Requires:       LibRaw%{?_isa}
# for eps plugin read/write support
Recommends:     poppler-utils
Recommends:     ghostscript

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
  -DKIMAGEFORMATS_HEIF:BOOL=ON \
  -DKIMAGEFORMATS_JXR:BOOL=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose

%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_qtplugindir}/imageformats/*.so

%files devel
%{_kf6_libdir}/cmake/KF6ImageFormats/

%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-10
- Rebuild

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-9
- Rebuild for OpenEXR 3.3 / LibRaw SONAMEs (ISO dep fix)

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-8
- Rebuild for OpenEXR 3.3 and LibRaw 0.22 SONAMEs

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Use kf6 cmake build/install macros (avoid qt6 prepare_docs / install_html_docs)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-2
- Prepare for Oreon 11 (RP1)
