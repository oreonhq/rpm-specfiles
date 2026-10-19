%global source0_hash a9fbf23c69fbaec7b0395e9adf78e98af3f9e8263a01c0312faa27c287757608
%global gkplugindir %{_libdir}/gkrellm2/plugins
Name:           gkrellm-sun
Version:        1.0.0
Release:        44%{?dist}
Summary:        Sun clock plugin for GKrellM
License:        GPL-2.0-only
URL:            http://gkrellsun.sourceforge.net/
Source0:        http://downloads.sf.net/gkrellsun/gkrellsun-%{version}.tar.gz
Source1:        gnome-%{name}.metainfo.xml
Patch0:         gkrellsun-1.0.0-fixes.patch
Patch1:         gkrellsun-1.0.0-rhbz1231394.patch
Patch2:         gkrellsun-1.0.0-ftbfs.patch
Requires:       gkrellm >= 2.2.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gkrellm-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
A sun clock plugin for GKrellM which can display the sun's setting time,
rising time, path and current location and so on.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gkrellsun-%{version}
%oreon_prep
%build

make %{?_smp_mflags} FLAGS='%{optflags} -fPIC $(GTK_INCLUDE)' \
    LFLAGS='%{__global_ldflags} -shared'
%install
install -D -m 0755 src20/gkrellsun.so \
    %{buildroot}%{gkplugindir}/gkrellsun.so
install -p -D -m 644 %{SOURCE1} \
    %{buildroot}%{_datadir}/appdata/gnome-%{name}.metainfo.xml
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/gnome-%{name}.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
