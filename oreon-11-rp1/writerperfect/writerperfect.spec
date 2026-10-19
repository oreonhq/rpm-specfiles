%global source0_hash 1fe162145013a9786b201cb69724b2d55ff2bf2354c3cd188fd4466e7fc324e6
Name: writerperfect
Version: 0.9.6
Release:        1%{?dist}
Summary:        A collection of tools to transform various file formats into ODF
License: LGPL-2.1-or-later OR MPL-2.0
URL: http://sourceforge.net/p/libwpd/wiki/writerperfect/
Source0:        http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
Patch0: 0001-fix-build-with-libgsf.patch
Patch1: 0001-Fix-linking-with-newer-tools-by-getting-the-library-.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(libabw-0.1)
BuildRequires:  pkgconfig(libcdr-0.1)
BuildRequires:  pkgconfig(libe-book-0.1)
BuildRequires:  pkgconfig(libeot)
BuildRequires:  pkgconfig(libepubgen-0.1)
BuildRequires:  pkgconfig(libetonyek-0.1)
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libmspub-0.1)
BuildRequires:  pkgconfig(libmwaw-0.3)
BuildRequires:  pkgconfig(libodfgen-0.1)
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librvngabw-0.0)
BuildRequires:  pkgconfig(libstaroffice-0.0)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  pkgconfig(libzmf-0.0)
# /oreon:deps
%description
%{name} is a collection of command-line tools to transform various document
formats into ODF. Among supported input formats are:
* AbiWord
* Adobe PageMaker
* Apple Keynote
* Corel WordPerfect
* CorelDRAW
* Microsoft Publisher
* Microsoft Visio
* Microsoft Works
* QuarkXPress

%package epub
Summary: A collection of tools to transform various file formats into EPUB
%description epub
%{name} is a collection of command-line tools to transform various document
formats into EPUB. Among supported input formats are:
* AbiWord
* Adobe PageMaker
* Apple Keynote
* Corel WordPerfect
* CorelDRAW
* Microsoft Publisher
* Microsoft Visio
* Microsoft Works

%package abw
Summary: A collection of tools to transform various file formats into AbiWord
%description abw
%{name} is a collection of command-line tools to transform various document
formats into AbiWord format. Among supported input formats are:
* Apple Pages
* Corel WordPerfect
* Microsoft Works

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

aclocal
automake
%configure \
    --disable-silent-rules \
    --disable-werror \
    --with-import-libs \
    --with-export-libs \
    --with-libeot \
    --with-libgsf
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in `ls %{buildroot}%{_bindir}`; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 *2abw.1 *2epub.1 *2od?.1 %{buildroot}/%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n writerperfect-epub -f %{oreon_filedir}/writerperfect-epub.list
%files -n writerperfect-abw -f %{oreon_filedir}/writerperfect-abw.list

%changelog

%autochangelog
