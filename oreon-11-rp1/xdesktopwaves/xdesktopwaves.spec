%global source0_hash 17ec7c6a865e8f5f8b370161b7379caeb4f7dc1b51ade220a31364c03d720ea3

Name:          xdesktopwaves
Version:       1.4
Release:       16%{?dist}

Summary:       Simulation of water waves on the X Window System desktop
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://xdesktopwaves.sf.net/
Source:        https://downloads.sourceforge.net/project/xdesktopwaves/xdesktopwaves/xdesktopwaves-%{version}.tar.gz
BuildRequires: make
BuildRequires: libX11-devel, desktop-file-utils, libXext-devel
BuildRequires: gcc

%description
xdesktopwaves is a cellular automata setting the background of your X
Window System desktop under water. Windows and mouse are like ships on
the sea. Each movement of these ends up in moving water waves. You can
even have rain and/or storm stirring up the water.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{__sed} -i -e "s,-s,," Makefile

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" LFLAGS="-L/usr/%{_lib}" %{?_smp_mflags}

%install
%{__mkdir_p} $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__mkdir_p} $RPM_BUILD_ROOT{%{_datadir}/applications,%{_datadir}/pixmaps}
%{__make} install BINDIR=$RPM_BUILD_ROOT%{_bindir} MAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1
%{__cp} -p %{name}.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps

cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=xdesktopwaves
Type=Application
Comment=Simulation of water waves on the X Window System desktop
Exec=xdesktopwaves
Icon=xdesktopwaves.xpm
Terminal=false
EOF

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications           \
  --add-category X-Fedora                              \
  --add-category Application                           \
  --add-category Graphics                              \
  %{name}.desktop

%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
%autochangelog
