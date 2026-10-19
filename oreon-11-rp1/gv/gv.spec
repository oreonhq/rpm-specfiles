%global source0_hash 2162b3b3a95481d3855b3c4e28f974617eef67824523e56e20b56f12fe201a61
Summary:        A X front-end for the Ghostscript PostScript(TM) interpreter
Name: gv
Version: 3.7.4
Release:        1%{?dist}
License: GPL-3.0-or-later
Requires: ghostscript-x11
URL: http://www.gnu.org/software/gv/
Source0:        https://ftp.gnu.org/gnu/gv/gv-%{version}.tar.gz
Source1: gv.png
Patch0:  gv-resource.patch
Patch1:  gv-dat.patch
Patch2:  gv-aarch64.patch
Patch3:  gv-bounding-box.patch
Patch4:  gv-bug1071238.patch
Patch5:  gv-bz1536211.patch
Patch6:  gv-overflow.patch
# oreon:deps
BuildRequires:  /usr/bin/makeinfo
BuildRequires:  Xaw3d-devel
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libXinerama-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
GNU gv is a user interface for the Ghostscript PostScript(TM) interpreter.
Gv can display PostScript and PDF documents on an X Window System.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .resource
%patch -P1 -p1 -b .resdat
%patch -P2 -p1 -b .aarch64
%patch -P3 -p2 -b .bounding-box
%patch -P4 -p1 -b .bug1071238
%patch -P5 -p1 -b .bz1536211
%patch -P6 -p2 -b .overflow

%build

%configure
%make_build
%install
%make_install
ln $RPM_BUILD_ROOT%{_bindir}/gv $RPM_BUILD_ROOT%{_bindir}/ghostview
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > gv.desktop <<EOF
[Desktop Entry]
Name=GNU GV PostScript/PDF Viewer
GenericName=PostScript/PDF Viewer
Comment="View PostScript and PDF files"
Type=Application
Icon=gv
MimeType=application/postscript;application/pdf;
StartupWMClass=GV
Exec=gv %f
EOF
desktop-file-install \
       --add-category=Applications\
       --add-category=Graphics \
       --dir %{buildroot}%{_datadir}/applications/ \
       gv.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/pixmaps
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
