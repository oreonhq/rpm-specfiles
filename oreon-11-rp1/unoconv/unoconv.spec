%global source0_hash 6ca6cf4db7f113a435558261b8335e256fec3346a6323a9c2823b69697700e8e

Summary:   A tool to convert documents from/to any format supported by LibreOffice
Name:      unoconv
Version:   0.9.0
Release:   %autorelease
License:   GPL-2.0-only
URL:       https://github.com/unoconv/unoconv/
Source:    https://github.com/unoconv/unoconv/archive/%{version}.tar.gz

Patch0:    0001-python3-added-compatibility.patch
Patch1:    0001-update-FSF-address.patch
Patch2:    0001-make-LaTeX-export-usable-with-writer2latex-ext.patch
Patch3:    0001-libreoffice-or-OO.o-has-never-had-wps-export.patch
Patch4:    0002-remove-export-formats-dropped-by-LibreOffice.patch

BuildArch: noarch

BuildRequires: make
BuildRequires: asciidoc
BuildRequires: xmlto

Requires:  libreoffice-filters
Requires:  libreoffice-pyuno
Suggests:  libreoffice-writer2latex
Suggests:  openoffice.org-diafilter

%description
Universal Office Converter (unoconv) is a command line tool to convert any
document format that LibreOffice can import to any document format that
LibreOffice can export. It makes use of the LibreOffice's UNO bindings for
non-interactive conversion of documents.

Supported document formats include Open Document Format (.odg, .odp, .ods,
.odt), MS Word (.doc), MS Office Open/MS OOXML (.docx, .pptx, .xlsx), PDF,
HTML, RTF, and many more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm doc/%{name}.1

%build
make %{?_smp_mflags}
asciidoc README.adoc

%install
make install DESTDIR="%{buildroot}" prefix=%{_prefix}

%files
%doc AUTHORS ChangeLog README.html
%doc doc/errcode.html doc/filters.html doc/formats.html doc/selinux.html
%license COPYING
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
%autochangelog
