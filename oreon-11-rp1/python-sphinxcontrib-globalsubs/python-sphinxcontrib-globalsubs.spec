%global source0_hash 2f32b6e95b6500d24cd6332207eb67b9324298f60fe1d7d8948a2964aaebea53
%global commit 5acbe50717a4f53a411310f03eb5f6ad13b3d1ea
Name:           python-sphinxcontrib-globalsubs
Version:        1.1.0
Release:        1%{?dist}
Summary:        Global substitutions defined in conf.py
License:        BSD-2-Clause
URL:            https://github.com/missinglinkelectronics/sphinxcontrib-globalsubs
%global forgeurl %{url}
%forgemeta
Source0:        https://github.com/missinglinkelectronics/sphinxcontrib-globalsubs/archive/%{commit}/sphinxcontrib-globalsubs-%{commit}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-sphinxcontrib-globalsubs
Summary:        Global substitutions defined in conf.py
%description -n python3-sphinxcontrib-globalsubs

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sphinxcontrib-globalsubs-%{commit}

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-sphinxcontrib-globalsubs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-sphinxcontrib-globalsubs -f %{oreon_filedir}/python3-sphinxcontrib-globalsubs.list

%changelog

%autochangelog
