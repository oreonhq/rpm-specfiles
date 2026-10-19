%global source0_hash eb45a480131594079f7fe84df30e4a5d0686f7a8049dc7084eebe22acc37aa9a
Name:           pdf2djvu
Version:        0.9.19
Release:        1%{?dist}
Summary:        PDF to DjVu converter
License:        GPL-2.0-or-later
URL:            http://jwilk.net/software/pdf2djvu
Source0:        https://github.com/jwilk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch2:         pdf2djvu-poppler-version.patch
Patch3:         pdf2djvu-poppler-26.01.0.patch
Requires:       djvulibre
# oreon:deps
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  djvulibre
BuildRequires:  djvulibre-devel
BuildRequires:  exiv2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  poppler-devel
# /oreon:deps
%description
pdf2djvu creates DjVu files from PDF files. It's able to extract:
graphics, text layer, hyperlinks, document outline (bookmarks) and
metadata.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="-std=c++20 $RPM_OPT_FLAGS"
%configure
%make_build
%install
%make_install
install -p -m 644 -D {doc,%{buildroot}%{_mandir}/man1}/%{name}.1
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
