%global source0_hash 9b5ff5c7e4468f1401efb294369a78a8ce89b41c704abecc9d9954ccae674b2c

%global libname toml

%global commit 03e8a3ab1d4d014e63a2befe8a48e74783a81521
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lib%{libname}
Version:        0
Release:        38.20161213git%{shortcommit}%{?dist}
Summary:        Fast C parser using Ragel to generate the state machine.

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ajwans/libtoml
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# https://github.com/ajwans/libtoml/pull/15
Patch0001:      0001-add-meson-buildsystem-as-experiment.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  %{_bindir}/ragel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(cunit)

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

%build
%set_build_flags
# Provide a declaration of asprintf in <stdio.h>.
CFLAGS="$CFLAGS -D__STDC_WANT_LIB_EXT2__"
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/%{libname}
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{libname}.h
%{_libdir}/%{name}.so

%changelog
%autochangelog
