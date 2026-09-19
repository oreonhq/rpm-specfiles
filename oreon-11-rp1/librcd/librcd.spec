%global source0_hash 261db28bc864fd4b2d3ba88403b2e421944281e323c1e39c0e61f5160c16b664

Name:           librcd
Version:        0.1.14
Release:        29%{?dist}
Summary:        Library for autodetection charset of Russian and Ukrainian text

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://rusxmms.sourceforge.net
Source0:        http://dside.dyndns.org/files/rusxmms/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires: make

%description
LibRCD is used by RusXMMS project for encoding auto-detection. It is optimized
to handle very short titles, like ID3 tags, file names and etc, and provides
very high accuracy even for short 3-4 letter words. Current version supports
Russian and Ukrainian languages and able to distinguish UTF-8, KOI8-R, CP1251,
CP866, ISO8859-1. If compared with Enca, LibRCC provides better detection
accuracy on short titles and is able to detect ISO8859-1 (non-Cyrillic)
encoding what allows to properly display correct ID3 v.1 titles.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
LibRCD is used by RusXMMS project for encoding auto-detection. It is optimized
to handle very short titles, like ID3 tags, file names and etc, and provides
very high accuracy even for short 3-4 letter words. Current version supports
Russian and Ukrainian languages and able to distinguish UTF-8, KOI8-R, CP1251,
CP866, ISO8859-1. If compared with Enca, LibRCC provides better detection
accuracy on short titles and is able to detect ISO8859-1 (non-Cyrillic)
encoding what allows to properly display correct ID3 v.1 titles.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -delete

%ldconfig_scriptlets

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/librcd.so.*

%files devel
%doc ChangeLog
%{_includedir}/librcd.h
%{_libdir}/librcd.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
