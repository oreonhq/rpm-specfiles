%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%global source1_hash 3af469fc30e076fcbf0ee5f4599fb556d7237ef5b2102b359a3e807a21d7ac79
%global source0_hash 8dcb70adb5cf072335115a6b091f4113710bdc73abaadaa3f9e9c1e55957b149
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global maj 0
Name:       lilv
Version:    0.28.0
Release:        1%{?dist}
Summary:        An LV2 Resource Description Framework Library
License:    MIT
URL:        https://drobilla.net/software/lilv
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:    https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:    https://drobilla.net/drobilla.gpg
Patch0:     %{name}-bindings-test.patch
Requires:       lv2 >= 1.18.2
Obsoletes:      lilv < 0.24.12-2
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0)
BuildRequires:  pkgconfig(sratom-0)
BuildRequires:  pkgconfig(zix-0)
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_lv2_theme
BuildRequires:  python3-sphinxygen
# /oreon:deps
%description
%{name} is a library to make the use of LV2 plugins as simple as possible
for applications. Lilv is the successor to SLV2, rewritten to be significantly
faster and have minimal dependencies.

%package libs
Summary:    Libraries for %{name}
Obsoletes:  lilv < 0.24.12-2
%description libs
%{name} is a lightweight C library for Resource Description Syntax which
supports reading and writing Turtle and NTriples.

This package contains the libraries for %{name}.

%package devel
Summary:    Development libraries and headers for %{name}
Requires:   %{name}-libs%{_isa} = %{version}-%{release}
%description devel
%{name} is a lightweight C library for Resource Description Syntax which
supports reading and writing Turtle and NTriples.

This package contains the headers and development libraries for %{name}.

%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary:    Python bindings for %{name}
Requires:   %{name}-libs%{_isa} = %{version}-%{release}
%description -n python3-%{name}
%{name} is a lightweight C library for Resource Description Syntax which
supports reading and writing Turtle and NTriples.

This package contains the python libraries for %{name}.

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n lilv-libs -f %{oreon_filedir}/lilv-libs.list
%files -n lilv-devel -f %{oreon_filedir}/lilv-devel.list
%files -n python3-lilv -f %{oreon_filedir}/python3-lilv.list

%changelog

%autochangelog
