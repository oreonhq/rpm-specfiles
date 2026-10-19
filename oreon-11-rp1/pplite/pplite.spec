%global source0_hash 830e841edbebcbbca3fbf1b35c29a6d783141ad301ccf388ee83f0125743dee8
%global giturl  https://github.com/ezaffanella/PPLite
Name:           pplite
Version:        0.14
Release:        1%{?dist}
Summary:        Convex polyhedra library for abstract interpretation
License:        GPL-3.0-or-later
URL:            https://www.cs.unipr.it/~zaffanella/PPLite/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{name}-%{version}-tag.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flint)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
# /oreon:deps
%description
PPLite is an open-source C++ library implementing the abstract domain of
convex polyhedra, to be used in tools for static analysis and verification.

%package        devel
Summary:        Development files for PPLite
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Header files and library links for developing applications that use PPLite.

%package        tools
Summary:        Command line tools to use PPLite functionality
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
Command line tools to use PPLite functionality.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n PPLite-%{name}-%{version}-tag

%conf
autoreconf -fi .

%build

%configure --disable-arch --disable-static --enable-integers=gmp
%make_build
%install
%make_install
%ifnarch %{power64}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%endif
%files -f %{oreon_filedir}/main.list
%files -n pplite-devel -f %{oreon_filedir}/pplite-devel.list
%files -n pplite-tools -f %{oreon_filedir}/pplite-tools.list

%changelog

%autochangelog
