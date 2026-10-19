%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%global source1_hash bea1633b4536765683a82dbe280368388c49da91fffd032d465b0d4ca931887b
%global source0_hash 0209b7d0f22c96abb416722ed735b0933be47931ecff4aa4b26ded7760b4f252
%global maj 0
Name:       sratom
Version:    0.6.22
Release:        1%{?dist}
Summary:        A C library for serializing LV2 plugins
License:    MIT
URL:        https://drobilla.net/software/%{name}
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:    https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:    https://drobilla.net/drobilla.gpg
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(sord-0)
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_lv2_theme
BuildRequires:  python3-sphinxygen
# /oreon:deps
%description
%{name} is a C library for serializing LV2 atoms to/from Turtle. It is
intended to be a full serialization solution for LV2 atoms, allowing
implementations to serialize binary atoms to strings and read them back again.
This is particularly useful for saving plugin state, or implementing plugin
control with network transparency.

%package devel
Summary:    Development libraries and headers for %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}
%description devel
%{name} is a C library for serializing LV2 atoms to/from Turtle. It is
intended to be a full serialization solution for LV2 atoms, allowing
implementations to serialize binary atoms to strings and read them back again.
This is particularly useful for saving plugin state, or implementing plugin
control with network transparency.

This package contains the headers and development libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson
%meson_build
%install
%meson_install
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/%{name}-%{maj} %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n sratom-devel -f %{oreon_filedir}/sratom-devel.list

%changelog

%autochangelog
