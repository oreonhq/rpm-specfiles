%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%global source1_hash f14e2fcc662bf4c7ee732929756f4366dabc8a2f56aa571f65778dc064e3a621
%global source0_hash b0e93b49e52f01a049475b7886ef140407115a32d3b1e5dc5f95141c88275d1c
%global maj 0
Name:           serd
Version:        0.32.10
Release:        1%{?dist}
Summary:        A lightweight C library for RDF syntax
License:        ISC
URL:            https://drobilla.net/software/%{name}.html
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:        https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:        https://drobilla.net/drobilla.gpg
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  python-sphinxygen
BuildRequires:  python3
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_lv2_theme
# /oreon:deps
%description
%{name} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle, TRiG, NTriples, and NQuads.

Serd is suitable for performance-critical or resource-limited applications,
such as serialising very large data sets, network protocols, or embedded
systems that require minimal dependencies and lightweight deployment.

%package devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
%description devel
%{name} is a lightweight C library for RDF syntax which supports reading and 
writing Turtle, TRiG, NTriples, and NQuads.

This package contains the headers and development libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%meson -Dman_html=disabled
%meson_build
%install
%meson_install
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/%{name}-%{maj} %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n serd-devel -f %{oreon_filedir}/serd-devel.list

%changelog

%autochangelog
