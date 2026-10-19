%global source0_hash 8192f5286185a9472d46dfe2e9c3c55fc3717791d4fb9ab71b428d25792b711c
Summary:        Library for manipulating RDF files describing LADSPA plugins
Name:         liblrdf
Version:      0.5.0
Release:        34%{?dist}
License:      GPL-2.0-or-later
URL:          https://github.com/swh/LRDF
Source0:        liblrdf-%{version}.tar.gz
Source1:      liblrdf-README.fedora
Requires:     ladspa
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ladspa-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  raptor2-devel
# /oreon:deps
%description
liblrdf is a library to make it easy to manipulate RDF files describing
LADSPA plugins.

%package devel
Summary:      Library for manipulating RDF files describing LADSPA plugins
Requires:     liblrdf%{?_isa} = %{version}-%{release}
Requires:     raptor2-devel
%description devel
This is a library to make it easy to manipulate RDF files describing
LADSPA plugins. This package includes the development tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
cp -a %{SOURCE1} README.fedora

%build

%configure --disable-static
%install
%{make_install}
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liblrdf-devel -f %{oreon_filedir}/liblrdf-devel.list

%changelog

%autochangelog
