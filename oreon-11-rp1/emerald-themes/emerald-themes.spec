%global source0_hash 54e563a4ed785b7d579a6579ff5d42c0e28fd3e0027398398b260a869ea114e1
%global  basever 0.8.18
Name:           emerald-themes
License:        GPL-2.0-only
Version:        0.8.18
Release:        1%{?dist}
Epoch:          1
Summary:        Themes for Emerald, a window decorator for Compiz Fusion
URL:            https://gitlab.com/compiz/%{name}
Source0:        https://gitlab.com/compiz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch
Requires:       compiz >= %{basever}
Requires:       emerald >= %{basever}
Obsoletes:      emerald-themes-extra
# oreon:deps
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Emerald is themeable window decorator and compositing
manager for Compiz Fusion.

This package contains themes for emerald.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}

%build

./autogen.sh
%configure
make %{?_smp_mflags} V=1
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
