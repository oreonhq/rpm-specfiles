%global source0_hash 554b2d9fb3ce668312341f43bafc95cf985059d83bf5e82f92547610c7f2bf18

%define _iconsdir %{_datadir}/icons/hicolor/24x24/apps

Summary: Edonkey 2000 file hash calculator
Name: ed2k_hash
Version: 0.4.0
URL: https://ed2k-tools.sourceforge.net/index.shtml
Release: 48%{?dist}
Source0: https://downloads.sourceforge.net/sourceforge/ed2k-tools/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
# Taken from http://dl.sourceforge.net/sourceforge/ed2k-gtk-gui/ed2k-gtk-gui-0.6.4.tar.bz2
Source2: ed2k-logo-mini.png
Patch0: %{name}-64bit.patch
Patch1: %{name}-warnings.patch
Patch2: %{name}-gcc43.patch
Patch3: %{name}-ld.patch
License: GPL-2.0-or-later
BuildRequires: desktop-file-utils
BuildRequires: fltk1.3-devel
BuildRequires: gcc-c++
BuildRequires: make

%description
A tool that outputs ed2k-links for given files.

%package gui
Summary: Edonkey 2000 file hash calculator with FLTK GUI

%description gui
A GUI tool that outputs ed2k-links for given files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CFLAGS="$CXXFLAGS -DPROTOTYPES"
%configure
%make_build

%install
%make_install
rm -rv %{buildroot}%{_docdir}/%{name}

iconv -f iso8859-1 -t utf8 AUTHORS > AUTHORS.utf8 &&\
touch -r AUTHORS AUTHORS.utf8 &&\
mv AUTHORS.utf8 AUTHORS
mkdir -p %{buildroot}%{_iconsdir}
install -pm 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO ed2k_hash/docs/en/*.html
%{_bindir}/%{name}

%files gui
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO ed2k_hash/docs/en/*.html
%{_bindir}/%{name}_gui
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png

%changelog
%autochangelog
