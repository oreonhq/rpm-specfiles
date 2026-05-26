# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 44e861476310ea1bab4dedf0a7736ba906e0037e7950909b9c48eadf72f7c170
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%{?mingw_package_header}

# Only build the 32 bit package.
%global mingw_build_win32 1
%global mingw_build_win64 0

Name:	        mingw-srvany
Version:        1.1
Release:        13%{?dist}
Summary:        Utility for creating services for Windows

License:        GPL-2.0-or-later
BuildArch:      noarch

URL:	        https://github.com/rwmjones/rhsrvany
Source0:        https://github.com/rwmjones/rhsrvany/archive/refs/tags/v%{version}.tar.gz#/rhsrvany-%{version}.tar.gz
Source1:        COPYING

# Needed because we build from the git version, using autoreconf.
BuildRequires:  make
BuildRequires:  automake autoconf libtool

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++


%description
Utility for creating a service from any MinGW Windows binary


%package -n mingw32-srvany
Summary:	Utility for creating services for Windows


%description -n mingw32-srvany
Utility for creating a service from any MinGW Windows binary


%{?mingw_debug_package}


%package redistributable
Summary:	Utility for creating services for Windows
# previously provided symlinks to the mingw32 path
Conflicts:	virt-v2v < 1:2.3.5-4


%description redistributable
srvany is a utility for creating a service from any MinGW Windows binary.
This package contains the binaries without any mingw toolchain dependencies,
for use with virt-v2v.


%prep
%oreon_verify_sources
%setup -q -n rhsrvany-%{version}
cp %{SOURCE1} .


%build
autoreconf -i
%{mingw32_configure}
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install
# redistributable
make DESTDIR=$RPM_BUILD_ROOT install bindir=%{_datadir}/virt-tools


%files -n mingw32-srvany
%license COPYING
%{mingw32_bindir}/rhsrvany.exe
%{mingw32_bindir}/pnp_wait.exe

%files redistributable
%license COPYING
%dir %{_datadir}/virt-tools/
%{_datadir}/virt-tools/rhsrvany.exe
%{_datadir}/virt-tools/pnp_wait.exe
# duplicate debuginfo
%exclude /usr/lib/debug%{_datadir}/virt-tools/*.debug


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-13
- Prepare for Oreon 11 (RP1)
