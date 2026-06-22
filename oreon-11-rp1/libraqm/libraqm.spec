%global source0_hash 4d76a358358d67c5945684f2f10b3b08fb80e924371bf3ebf8b15cd2e321d05d

Name:           libraqm
Version:        0.10.1
Release:        1%{?dist}
License:        MIT
Summary:        Complex text layout library
URL:            https://github.com/HOST-Oman/libraqm
Source0:        https://github.com/HOST-Oman/libraqm/releases/download/v%{version}/raqm-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  fribidi-devel
BuildRequires:  gtk-doc

%description
Library that encapsulates the logic for complex text layout and provides a
convenient API.

%package devel
Summary:        Development files for libraqm
Requires:       libraqm%{?_isa} = %{version}-%{release}

%description devel
Development files for libraqm.

%package docs
Summary:        Documentation for libraqm
BuildArch:      noarch

%description docs
Documentation for libraqm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n raqm-%{version}

%build
%meson -Ddocs=true
%meson_build

%check
export LC_ALL=C.UTF-8
%meson_test

%install
%meson_install
rm -f %{buildroot}%{_libdir}/*.{la,a}

%files
%license COPYING
%{_libdir}/libraqm.so.*

%files devel
%license COPYING
%{_includedir}/raqm.h
%{_includedir}/raqm-version.h
%{_libdir}/libraqm.so
%{_libdir}/pkgconfig/raqm.pc

%files docs
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/gtk-doc/html/raqm

%changelog
%autochangelog
