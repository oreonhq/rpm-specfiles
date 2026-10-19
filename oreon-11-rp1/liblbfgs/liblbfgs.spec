%global source0_hash 4158ab7402b573e5c69d5f6b03c973047a91e16ca5737d3347e3af9c906868cf
Name:           liblbfgs
Version:        1.10
Release:        27%{?dist}
Summary:        Limited-memory Broyden-Fletcher-Goldfarb-Shanno library
License:        MIT
URL:            http://www.chokkan.org/software/liblbfgs/
Source0:        https://github.com/downloads/chokkan/liblbfgs/%{name}-%{version}.tar.gz
Patch0:         liblbfgs_build.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
A C port of the implementation of Limited-memory
Broyden-Fletcher-Goldfarb-Shanno (L-BFGS) method written by Jorge Nocedal.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

# Needed for patch0
autoreconf -ifv

%build

export LDFLAGS="-Wl,--as-needed"
%configure --disable-static
make %{?_smp_mflags}
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/doc
rmdir %{buildroot}%{_datadir}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liblbfgs-devel -f %{oreon_filedir}/liblbfgs-devel.list

%changelog

%autochangelog
