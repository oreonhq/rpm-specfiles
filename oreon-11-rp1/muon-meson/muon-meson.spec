%global source1_hash acb1ed8554baa6a9cb1d249ebd8915c3362115fdddb01b5d51eb506efe988427
%global source0_hash acb1ed8554baa6a9cb1d249ebd8915c3362115fdddb01b5d51eb506efe988427
%global         testcommit  db92588773a24f67cda2f331b945825ca3a63fa7
%global         testshortcommit  %(c=%{testcommit}; echo ${c:0:7})
%global         srcname muon
Name:           muon-meson
Version:        5.3.1
Release:        1%{?dist}
Summary:        C implementation of meson
License:        Apache-2.0 AND GPL-3.0-only AND MIT AND Unlicense
URL:            https://muon.build
Source0:        https://git.sr.ht/~lattis/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Source1:        https://github.com/muon-build/meson-tests/archive/%{testcommit}/meson-tests-%{testshortcommit}.tar.gz
Provides:       bundled(memmem)
Provides:       bundled(samurai)
Provides:       bundled(sha_256)
Provides:       bundled(tiny_json)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpkgconf-devel
BuildRequires:  pkgconf
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyyaml)
BuildRequires:  scdoc
# /oreon:deps
%description
An implementation of the meson build system in c99 with minimal dependencies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p 1
tar xf %{SOURCE1}
mv meson-tests-%{testcommit} subprojects/meson-tests
# Make sure not used
rm -r subprojects/bestline

%build

CFLAGS="-fPIE -DBOOTSTRAP_NO_TRACY %{optflags}" ./bootstrap.sh %{_vpath_builddir}
%{_vpath_builddir}/muon-bootstrap setup \
 -Dprefix=%{_prefix} \
 -Dwebsite=disabled \
 -Dstatic=false \
 -Dman-pages=enabled \
 -Dsamurai=enabled \
 -Dlibarchive=enabled \
 -Dlibcurl=enabled \
 -Dlibpkgconf=enabled \
 -Dreadline=builtin \
 -Dui=disabled \
 -Dmeson-docs=disabled \
 -Dtracy=disabled \
 %{_vpath_builddir}
%{_vpath_builddir}/muon-bootstrap -C %{_vpath_builddir} samu
%check

%{_vpath_builddir}/muon -C %{_vpath_builddir} test
%install
DESTDIR=%{buildroot} %{_vpath_builddir}/muon \
       -C %{_vpath_builddir} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
