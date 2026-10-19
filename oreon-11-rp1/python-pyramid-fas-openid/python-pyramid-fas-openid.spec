%global source0_hash a2c3ebb8e2370ea6b830abce3de8b9416248dc7d3006e9b9867fa0a5cb57889a
%global modname pyramid_fas_openid
Summary:        A view for pyramid that functions as an OpenID consumer for FAS
License:            LicenseRef-Callaway-BSD
URL:                https://github.com/fedora-infra/pyramid_fas_openid
Source0:        https://github.com/fedora-infra/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildArch:          noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-openid
BuildRequires:  python3-openid-cla
BuildRequires:  python3-openid-teams
BuildRequires:  python3-pyramid
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-pyramid-fas-openid
Summary: %summary
Requires:           python3-pyramid
Requires:           python3-openid
Requires:           python3-openid-teams
Requires:           python3-openid-cla
%{?python_provide:%python_provide python3-pyramid-fas-openid}
%description -n python3-pyramid-fas-openid

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-pyramid-fas-openid usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pyramid-fas-openid -f %{oreon_filedir}/python3-pyramid-fas-openid.list

%changelog

%autochangelog
