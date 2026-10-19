%global source0_hash 642e8405c85dc2ebcd307e0b46ed3d366fd28de098c6d8b717720689270b2954
Name:           pslib
Version:        0.4.6
Release:        1%{?dist}
Summary:        C-library to create PostScript files
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MPLv1.0 AND LicenseRef-Callaway-MIT
URL:            http://pslib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         pslib-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  giflib-devel
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
# /oreon:deps
%description
pslib is a C-library to create PostScript files on the fly. It offers many
drawing primitives, inclusion of png and eps images and a very sophisticated
text rendering including hyphenation, kerning and ligatures. It can read
external Type1 fonts and embed them into the output file. It supports pdfmarks
which makes it in combination with ghostscript's pdfwriter an alternative for
libraries creating PDF. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod a-x ChangeLog
for file in AUTHORS; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build

%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pslib-devel -f %{oreon_filedir}/pslib-devel.list

%changelog

%autochangelog
