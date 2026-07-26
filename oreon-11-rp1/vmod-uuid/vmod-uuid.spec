%global source0_hash e40db037b1c0ecc8e753cb86afeea9edccde58b5a58d98ffc7911e7805903c2d

%global docutils python3-docutils
%global rst2man rst2man

Name: vmod-uuid
Summary: UUID module for Varnish Cache
Version: 1.10
Release: 29%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://github.com/otto-de/libvmod-uuid
Source0: https://github.com/otto-de/lib%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: varnish%{?_isa} = %(pkg-config --silence-errors --modversion varnishapi || echo 0)
Requires: uuid

BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: uuid-devel
BuildRequires: varnish-devel >= 6.3.0
BuildRequires: varnish
BuildRequires: check-devel

# To build from a git checkout, add these
BuildRequires: automake
BuildRequires: libtool
BuildRequires: %docutils
BuildRequires: autoconf-archive

%description
UUID Varnish vmod used to generate a uuid, including versions 1, 3, 4 and 5
as specified in RFC 4122. See the RFC for details about the various versions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lib%{name}-%{version}

%build
./autogen.sh
export RST2MAN=%rst2man
%configure \
  --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# We have to remove rpath - not allowed in Fedora
# (This problem only visible on 64 bit arches)
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;
        s|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%check
%make_build check

%install
%make_install

# None of these for fedora/epel
find %{buildroot}/%{_libdir}/ -name '*.la' -delete
find %{buildroot}/%{_libdir}/ -name  '*.a' -delete

%files
%{_libdir}/varnish*/vmods/
%license LICENSE
%doc README.rst COPYING
%{_mandir}/man3/*.3*

%changelog
%autochangelog
