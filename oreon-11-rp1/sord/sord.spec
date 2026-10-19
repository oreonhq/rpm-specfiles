%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%global source1_hash b320eb1f93d12691a1483def026c3261525e58690d589cb2c84eaf0748e41a79
%global source0_hash bb23b34b216579136795d518cffa73d91cf205594ce9accebfd408afb839173f
%global maj 0
Name:       sord
Version:    0.16.22
Release:        1%{?dist}
Summary:        A lightweight Resource Description Framework (RDF) C library
License:    ISC
URL:        https://drobilla.net/software/%{name}.html
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:    https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:    https://drobilla.net/drobilla.gpg
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(zix-0)
# /oreon:deps
%description
%{name} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory. %{name} and parent library serd form 
a lightweight RDF tool-set for resource limited or performance critical 
applications.

%package devel
Summary:    Development libraries and headers for %{name}
Requires:   %{name}%{_isa} = %{version}-%{release}
%description devel
%{name} is a lightweight C library for storing Resource Description
Framework (RDF) data in memory.

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
%files -n sord-devel -f %{oreon_filedir}/sord-devel.list

%changelog

%autochangelog
