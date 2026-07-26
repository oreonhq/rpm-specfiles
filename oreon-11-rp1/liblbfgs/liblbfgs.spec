%global source0_hash 4158ab7402b573e5c69d5f6b03c973047a91e16ca5737d3347e3af9c906868cf

Name:           liblbfgs
Version:        1.10
Release:        27%{?dist}
Summary:        Limited-memory Broyden-Fletcher-Goldfarb-Shanno library

License:        MIT
URL:            http://www.chokkan.org/software/liblbfgs/
Source0:        https://github.com/downloads/chokkan/liblbfgs/%{name}-%{version}.tar.gz
# Fix CFLAGS override, build solib with correct versioning
Patch0:         liblbfgs_build.patch

BuildRequires:  autoconf automake libtool
BuildRequires: make

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

# Install these through %%doc
rm -rf %{buildroot}%{_datadir}/doc
rmdir %{buildroot}%{_datadir}

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/liblbfgs.so.*

%files devel
%{_includedir}/*
%{_libdir}/liblbfgs.so

%changelog
%autochangelog
