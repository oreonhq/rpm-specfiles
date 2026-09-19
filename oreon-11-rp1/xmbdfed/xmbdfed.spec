%global source0_hash d1807ae89238261738d6bf69e900eabdfe1f54cf110329ebde4b6a26cc134e65

Name:		xmbdfed
Summary: 	Bitmap Font Editor
Version:	4.7
Release:	41%{?dist}
License:	MIT
Source0:	http://crl.nmsu.edu/~mleisher/%{name}-%{version}.tar.bz2
Source1:	http://crl.nmsu.edu/~mleisher/%{name}.png
Source2:	xmbdfed.desktop
Patch0:		http://crl.nmsu.edu/~mleisher/%{name}-4.7-patch1
Patch1:		xmbdfed-4.7-linux.patch
Patch2:		xmbdfed-4.7-staticfix.patch
Patch3:		xmbdfed-4.7-getline.patch
Patch4:		xmbdfed-4.7-format-security.patch
Patch5:		xmbdfed-4.7-gcc10.patch
Patch6:		xmbdfed-4.7-gcc15.patch
URL:		http://crl.nmsu.edu/~mleisher/xmbdfed.html
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	freetype-devel, libXpm-devel, libXmu-devel
%if 0%{?fedora} >= 24
BuildRequires:  motif-devel
%else
BuildRequires:  lesstif-devel
%endif
BuildRequires:	libXext-devel, libX11-devel, libSM-devel, libICE-devel
BuildRequires:	desktop-file-utils
Requires:	xorg-x11-fonts-misc

%description
The XmBDFEditor lets you interactively create new bitmap font files or 
modify existing ones. It allows editing multiple fonts and multiple 
glyphs, it allows cut and paste operations between fonts and glyphs and 
editing font properties. The editor works natively with BDF fonts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%patch -P0 -p0 -b .patch1
%patch -P1 -p1 -b .linux
%patch -P2 -p1 -b .staticfix
%patch -P3 -p1 -b .getline
%patch -P4 -p1 -b .format-security
%patch -P5 -p1 -b .gcc10
%patch -P6 -p1 -b .gcc15

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 xmbdfed %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m0644 xmbdfed.man %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps
desktop-file-install					\
	--dir %{buildroot}%{_datadir}/applications	\
	%{SOURCE2}

%files
%doc README COPYRIGHTS xmbdfedrc CHANGES
%{_bindir}/xmbdfed
%{_datadir}/pixmaps/xmbdfed.png
%{_datadir}/applications/*.desktop
%{_mandir}/man1/xmbdfed*

%changelog
%autochangelog
