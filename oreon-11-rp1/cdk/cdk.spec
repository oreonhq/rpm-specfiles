%global source0_hash 0ed46949c680a5f42e342cc48a2ce60bcfc2cc8b9eebb176877b5a91f829435c
%global mainver 5.0
%global datever 20251014
Name:           cdk
Version:        %{mainver}.%{datever}
Release:        1%{?dist}
Summary:        Curses Development Kit
License:        X11-distribute-modifications-variant
URL:            https://invisible-island.net/cdk/
Source0:        https://invisible-island.net/archives/%{name}/%{name}-%{mainver}-%{datever}.tgz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
CDK stands for "Curses Development Kit". It contains a large number of ready
to use widgets which facilitate the speedy development of full screen curses
programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{mainver}-%{datever}

%build

%configure --with-ncurses --enable-const
make cdkshlib %{?_smp_mflags}
%check

echo "sample programs are interactive"
%install
make install installCDKSHLibrary DESTDIR=%{buildroot} INSTALL="install -pD"
chmod +x %{buildroot}%{_libdir}/*.so
find %{buildroot} -name '*.a' -delete -print
rm -vrf %{buildroot}%{_docdir}
%ldconfig_scriptlets
%oreon_autofiles cdk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cdk-devel -f %{oreon_filedir}/cdk-devel.list

%changelog

%autochangelog
