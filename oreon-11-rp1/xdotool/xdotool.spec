%global source0_hash 96f0facfde6d78eacad35b91b0f46fecd0b35e474c03e00e30da3fdd345f9ada

Name:           xdotool
Version:        3.20211022.1
Epoch:          1
Release:        10%{?dist}
Summary:        Fake keyboard/mouse input
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jordansissel/xdotool
Source0:        https://github.com/jordansissel/xdotool/releases/download/v%{version}/xdotool-%{version}.tar.gz

Patch0:         0001-Use-XTEST-instead-of-XWarpPointer-with-a-single-scre.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: libXtst-devel, libX11-devel, libXinerama-devel, libXi-devel, perl-podlators, libxkbcommon-devel

%description
This tool lets you programmatically (or manually) simulate keyboard input
and mouse activity, move and re-size windows, etc.

%package -n libxdo
Summary: Keyboard input simulation library

%description -n libxdo
This library contains functions to simulate keyboard and mouse input

%package -n libxdo-devel
Summary:        Development files for libxdo
Requires:       libxdo = %{epoch}:%{version}-%{release}

%description -n libxdo-devel
The libxdo-devel package contains libraries and header files for
developing applications that use libxdo

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1

%build
%set_build_flags
%make_build WITHOUT_RPATH_FIX=1

%install
%make_install PREFIX=%{_prefix} INSTALLMAN=%{_mandir} INSTALLLIB=%{_libdir}

#fix permissions
chmod 0644 examples/ffsp.sh

%ldconfig_scriptlets -n libxdo

%files -n libxdo
%doc CHANGELIST COPYRIGHT README.md
%{_libdir}/*.so.3*

%files -n libxdo-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libxdo.pc

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc examples

%changelog
%autochangelog
