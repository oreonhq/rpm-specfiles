%global source0_hash 60d286dfc4cbef47807958343fd89378e1f57ae1ffd98610ed122a1fd749bdd5
%global pkgname swh-lv2
%global gitver 5098e09
Name:		lv2-swh-plugins
Version:	1.0.15
Release:        1%{?dist}
Summary:        LV2 ports of LADSPA swh plugins
License:	GPL-3.0-only
URL:		http://lv2plug.in/
Source0:        %{pkgname}-%{gitver}.tar.gz
Patch0: lv2-swh-plugins-c99.patch
Requires:	lv2
# oreon:deps
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  libxslt
BuildRequires:  lv2-devel
BuildRequires:  make
# /oreon:deps
%description
This is an early experimental port of my LADSPA plugins to the LV2
specification, c.f. http://lv2plug.in/ . It's still quite early days, but most
things should work as well or not as they did in LADSPA.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{gitver}

# We are using the system header:
rm -f include/lv2.h

%build

make real-clean
make %{?_smp_mflags} \
	CFLAGS="-I%{_includedir} $RPM_OPT_FLAGS" \
	LDFLAGS="$RPM_OPT_FLAGS"
%install
rm -rf $RPM_BUILD_ROOT
make install-system INSTALL_DIR="$RPM_BUILD_ROOT%{_libdir}/lv2"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
