%global source0_hash eb45a480131594079f7fe84df30e4a5d0686f7a8049dc7084eebe22acc37aa9a

Name:           pdf2djvu
Version:        0.9.19
Release:        18%{?dist}
Summary:        PDF to DjVu converter
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://jwilk.net/software/pdf2djvu
Source0:        https://github.com/jwilk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# both patches are included in 0.9.19 release, remove these lines next commit
# Patch0:         pdf2djvu-PDFDoc-constructor.patch
# Patch1:         pdf2djvu-Destination-copy-constructor.patch
Patch2:         pdf2djvu-poppler-version.patch
Patch3:         pdf2djvu-poppler-26.01.0.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  djvulibre-devel djvulibre
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  poppler-devel
BuildRequires:  fontconfig-devel
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  exiv2-devel libuuid-devel
Requires:       djvulibre

%description
pdf2djvu creates DjVu files from PDF files. It's able to extract:
graphics, text layer, hyperlinks, document outline (bookmarks) and
metadata.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
export CXXFLAGS="-std=c++20 $RPM_OPT_FLAGS"
%configure
%make_build

%install
%make_install
install -p -m 644 -D {doc,%{buildroot}%{_mandir}/man1}/%{name}.1

%find_lang %{name}

%files -f %{name}.lang
%doc doc/changelog
%license doc/COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/de/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_mandir}/pl/man1/%{name}.1*
%{_mandir}/pt/man1/%{name}.1*
%{_mandir}/ru/man1/%{name}.1*

%changelog
%autochangelog
