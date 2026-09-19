%global source0_hash a9fbf23c69fbaec7b0395e9adf78e98af3f9e8263a01c0312faa27c287757608

%global gkplugindir %{_libdir}/gkrellm2/plugins

Name:           gkrellm-sun
Version:        1.0.0
Release:        44%{?dist}
Summary:        Sun clock plugin for GKrellM
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://gkrellsun.sourceforge.net/
Source0:        http://downloads.sf.net/gkrellsun/gkrellsun-%{version}.tar.gz
Source1:        gnome-%{name}.metainfo.xml
# Fix a bunch of compiler warnings
Patch0:         gkrellsun-1.0.0-fixes.patch
# Fix rhbz 1231394
Patch1:         gkrellsun-1.0.0-rhbz1231394.patch
Patch2:         gkrellsun-1.0.0-ftbfs.patch
Requires:       gkrellm >= 2.2.0
BuildRequires:  make gcc
BuildRequires:  gkrellm-devel >= 2.2.0
BuildRequires:  libappstream-glib

%description
A sun clock plugin for GKrellM which can display the sun's setting time,
rising time, path and current location and so on.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gkrellsun-%{version}

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

%files
%doc AUTHORS README
%license COPYING
%{gkplugindir}/gkrellsun.so
%{_datadir}/appdata/gnome-%{name}.metainfo.xml

%changelog
%autochangelog
