%global source0_hash b25120a0de94884310a047eb9c8932f71a5918ed3439867e6bf9a4b4109c4a34
Name:           slowloris
Version:        0.2.6
Release:        1%{?dist}
Summary:        Low bandwidth DoS tool
License:        MIT
URL:            https://github.com/gkbrk/slowloris
Source0:        https://files.pythonhosted.org/packages/source/S/Slowloris/Slowloris-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Slowloris is basically an HTTP Denial of Service attack that affects threaded
servers.

%package -n     python3-%{name}
Summary:        Low bandwidth DoS tool
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
Slowloris is basically an HTTP Denial of Service attack that affects threaded
servers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Slowloris-%{version}
# Use setuptools
sed -i -e "s/distutils.core/setuptools/g" setup.py
# Remove shebang
sed -i -e '/^#!\//, 1d' %{name}.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-slowloris -f %{oreon_filedir}/python3-slowloris.list

%changelog

%autochangelog
