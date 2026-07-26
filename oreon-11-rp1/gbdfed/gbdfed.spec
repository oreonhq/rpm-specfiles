%global source0_hash 5db25d4ce688dcb188dee056e58614a94a5e4fce4b6066fbb310951ab999093c

Name:		gbdfed
Summary: 	Bitmap Font Editor
Version:	1.6
Release:	28%{?dist}
License:	MIT
Source0:	http://www.math.nmsu.edu/~mleisher/Software/gbdfed/%{name}-%{version}.tar.bz2
Source1:	http://www.math.nmsu.edu/~mleisher/Software/gbdfed/%{name}16x16.png
Source2:	gbdfed.desktop
Patch0:		gbdfed-1.6-format-security-fix.patch
# Fix some of the gtk issues
Patch2:		gbdfed-1.6-gtkfix.patch
# c23
Patch3:		gbdfed-1.6-c23.patch
URL:		http://www.math.nmsu.edu/~mleisher/Software/gbdfed/
BuildRequires:  gcc
BuildRequires:	freetype-devel, pango-devel, libX11-devel, libICE-devel, gtk2-devel
BuildRequires:	desktop-file-utils, autoconf
BuildRequires:  make

%description
gbdfed lets you interactively create new bitmap font files or
modify existing ones. It allows editing multiple fonts and multiple
glyphs, it allows cut and paste operations between fonts and glyphs and
editing font properties. The editor works natively with BDF fonts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .format-security-fix
%patch -P2 -p1 -b .gtkfix
%patch -P3 -p1 -b .c23

# This is incredibly hackish, and will likely not work when these deprecated bits are removed outright.
sed "s:-D.*_DISABLE_DEPRECATED::" -i Makefile.in

%build
autoreconf -ifv
%configure
make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}" install
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/gbdfed.png
desktop-file-install					\
	--dir %{buildroot}%{_datadir}/applications	\
	%{SOURCE2}

%files
%doc README
%{_bindir}/gbdfed
%{_datadir}/pixmaps/gbdfed.png
%{_datadir}/applications/*.desktop
%{_mandir}/man1/gbdfed*

%changelog
%autochangelog
