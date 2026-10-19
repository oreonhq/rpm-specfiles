%global source0_hash c835b640a40ce357e1b83666aabd95edffa24ddddd49b8daff63adb851cdab74
Name:             poppler-data
Summary:        Encoding files for use with poppler
Version:          0.4.12
Release:        1%{?dist}
License:          (GPL-2.0-only OR GPL-3.0-only) AND BSD-3-Clause
URL:              https://poppler.freedesktop.org/
Source0:        https://poppler.freedesktop.org/poppler-data-%{version}.tar.gz
BuildArch:        noarch
# oreon:deps
BuildRequires:  git
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
This package consists of encoding files for use with poppler. The encoding
files are optional and poppler will automatically read them if they are present.

When installed, the encoding files enables poppler to correctly render both CJK
and Cyrrilic characters properly.

# === SUBPACKAGES =============================================================

%package          devel
Summary:          Devel files for %{name}
Requires:         %{name} = %{version}-%{release}
BuildRequires:    pkgconfig
%description devel
This sub-package currently contains only pkgconfig file, which can be used with
pkgconfig utility allowing your software to be build with poppler-data.

# === BUILD INSTRUCTIONS ======================================================

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%make_install prefix=%{_prefix}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n poppler-data-devel -f %{oreon_filedir}/poppler-data-devel.list

%changelog

%autochangelog
