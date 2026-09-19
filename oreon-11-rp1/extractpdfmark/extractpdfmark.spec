%global source0_hash c62f3774c5a97df0517042dd5bbc1c3cdb65687617d1f0a3e8a6910f3191a21b

Name:           extractpdfmark
Version:        1.1.1
Release:        13%{?dist}
Summary:        Extract page mode and named destinations as PDFmark from PDF

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/trueroad/extractpdfmark/
Source0:        https://github.com/trueroad/extractpdfmark/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  make

%description
When you create a PDF document using something like a TeX system you may include
many small PDF files in the main PDF file. It is common for each of the small
PDF files to use the same fonts.

If the small PDF files contain embedded font subsets, the TeX system includes
them as-is in the main PDF. As a result, several subsets of the same font are
embedded in the main PDF. It is not possible to remove the duplicates since they
are different subsets. This vastly increases the size of the main PDF file.

On the other hand, if the small PDF files contain embedded full font sets, the
TeX system also includes all of them in the main PDF. This time, the main PDF
contains duplicates of the same full sets of fonts. Therefore, Ghostscript can
remove the duplicates. This may considerably reduce the main PDF-file's size.

Finally, if the small PDF files contain some fonts that are not embedded, the
TeX system outputs the main PDF file with some fonts missing. In this case,
Ghostscript can embed the necessary fonts. It can significantly reduce the
required disk size.

Either way, when Ghostscript reads the main PDF produced by the TeX system and
outputs the final PDF it does not preserve PDF page-mode and named-destinations
etc. As a result, when you open the final PDF, it is not displayed correctly.
Also, remote PDF links will not work correctly.

This program is able to extract page mode and named destinations as PDFmark from
PDF. By using this you can get the small PDF files that have preserved them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --with-poppler=cpp
%make_build

%install
%make_install
rm %{buildroot}%{_pkgdocdir}/COPYING

%check
make check

%files
%{_mandir}/man1/extractpdfmark.1.*
%{_bindir}/extractpdfmark

%license COPYING

%doc NEWS README.*

%changelog
%autochangelog
