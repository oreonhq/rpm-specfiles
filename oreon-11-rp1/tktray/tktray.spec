%global source0_hash ef48b75ea7979186a05b605f8c153f92bbcc46cb76dee8be1d30bcda179bfcfc

%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Summary: System Tray Icon Support for Tk on X11
Name: tktray
Version: 1.3.9
Release: 29%{?dist}
URL: http://code.google.com/p/tktray/
Source0: http://tktray.googlecode.com/files/%{name}%{version}.tar.gz
License: BSD
BuildRequires: make
BuildRequires:  gcc
BuildRequires: tk-devel,tcl-devel
BuildRequires: libXext-devel, libX11-devel

Requires: tk,tcl
Requires: tcl(abi) = 8.6

%description
Tktray is an extension that is able to create system tray icons.
It follows http://www.freedesktop.org specifications when looking 
up the system tray manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}%{version}

chmod 0644 ChangeLog license.terms docs/*

%build

%configure  --libdir=%{tcl_sitearch} \
	--with-tcl=%{_libdir} \
	--with-tk=%{_libdir}

make %{?_smp_mflags} CFLAGS_DEFAULT="" CFLAGS_WARNING="-Wall" 

%install
rm -rf $RPM_BUILD_ROOT 
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

%files
%doc ChangeLog license.terms docs/tktray.html
%{tcl_sitearch}/%{name}%{version}
%{_mandir}/*/*

%changelog
%autochangelog
