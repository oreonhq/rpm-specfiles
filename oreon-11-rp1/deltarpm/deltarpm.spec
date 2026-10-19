%global source0_hash f3fba9b96c55be21696466bbfc3b2a623a4fb35646ff9a135f5c29406b412f22
Name:           deltarpm
Summary:        Create deltas between rpms
Version:        3.6.5
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/rpm-software-management/deltarpm
Source0:        https://github.com/rpm-software-management/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
A deltarpm contains the difference between an old
and a new version of a rpm, which makes it possible
to recreate the new rpm from the deltarpm and the old
one. You don't have to have a copy of the old rpm,
deltarpms can also work with installed rpms.

%package -n drpmsync
Summary:        Sync a file tree with deltarpms
Requires:       %{name}%{_isa} = %{version}-%{release}
%description -n drpmsync
This package contains a tool to sync a file tree with
deltarpms.

%package -n deltaiso
Summary:        Create deltas between isos containing rpms
Requires:       %{name}%{_isa} = %{version}-%{release}
%description -n deltaiso
This package contains tools for creating and using deltasisos,
a difference between an old and a new iso containing rpms.

%package -n python3-%{name}
Summary:        Python bindings for deltarpm
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires: make
Requires:       %{name}%{_isa} = %{version}-%{release}
%description -n python3-%{name}
This package contains python bindings for deltarpm.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build CFLAGS="${CFLAGS} -DWITH_ZSTD=1" \
    bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir} prefix=%{_prefix} \
    zlibbundled='' zlibldflags='-lz' zlibcppflags=''
%make_build CFLAGS="${CFLAGS} -DWITH_ZSTD=1" \
    bindir=%{_bindir} libdir=%{_libdir} mandir=%{_mandir} prefix=%{_prefix} \
    zlibbundled='' zlibldflags='-lz' zlibcppflags='' \
    python
%install
%make_build pylibprefix=%{buildroot} mandir=%{buildroot}%{_mandir} prefix=%{buildroot}%{_prefix} install
%oreon_autofiles drpmsync usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles deltaiso usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n drpmsync -f %{oreon_filedir}/drpmsync.list
%files -n deltaiso -f %{oreon_filedir}/deltaiso.list
%files -n python3-deltarpm -f %{oreon_filedir}/python3-deltarpm.list

%changelog

%autochangelog
