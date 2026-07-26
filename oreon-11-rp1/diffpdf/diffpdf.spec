%global source0_hash c6142ee038a78108397f45b0c456dca7a4fe1d75250f21a514a134101d322433

%global _hardened_build 1
Name:           diffpdf
Version:        2.1.3
Release:        36%{?dist}
Summary:        PDF files comparator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.qtrac.eu/diffpdf.html
Source0:        http://www.qtrac.eu/%{name}-%{version}.tar.gz
Source1:        %{name}.1
Source3:        %{name}.desktop

Patch0:         qt5.patch

BuildRequires:  poppler-qt5-devel, desktop-file-utils, ImageMagick
BuildRequires:  qt5-linguist
# /usr/include/poppler/cpp/poppler-version.h
BuildRequires:  poppler-cpp-devel
BuildRequires:  make
Requires:       hicolor-icon-theme

%description
DiffPDF is used to compare two PDF files. By default the comparison is
of the text on each pair of pages, but comparing the appearance of pages
is also supported (for example, if a diagram is changed or a paragraph
reformatted). It is also possible to compare particular pages or page
ranges.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .qt5

%build
lrelease-qt5 diffpdf.pro
%{qmake_qt5}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 diffpdf $RPM_BUILD_ROOT%{_bindir}

for f in 32 16; do
   mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/"$f"x$f/apps
   convert images/icon.png -size "$f"x$f diffpdf-$f.png
   install -p diffpdf-$f.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/"$f"x$f/apps/diffpdf.png
done

desktop-file-install                                    \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications         \
  %{SOURCE3}

%{__install} -m 644 %{SOURCE1} -D $RPM_BUILD_ROOT%{_mandir}/man1/diffpdf.1

%files
%doc CHANGES gpl-2.0.txt help_cz.html help_de.html help_fr.html help.html README
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/??x??/apps/*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/diffpdf.1*

%changelog
%autochangelog
