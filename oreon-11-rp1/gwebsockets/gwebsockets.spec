%global source0_hash 116e7e9e2e316011b88c2410e5a9b86c93db1e133ff76534d225302810873d68
Name:          gwebsockets
Version:       0.7
Release:        1%{?dist}
Summary:        GLib based websockets server
License:       Apache-2.0
URL:           https://github.com/sugarlabs/gwebsockets
Source0:        https://github.com/sugarlabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:     noarch 
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gwebsockets = %{version}-%{release}
# /oreon:deps
%description
A websocket server written in python. It uses GIO for network
communication and hence it easily integrates with the GLib mainloop.

%package -n python3-%{name}
Summary:  GLib based websockets server
%{?python_provide:%python_provide python3-gwebsockets}
Requires: glib2
%description -n python3-%{name}
A websocket server written in python3. It uses GIO for network
communication and hence it easily integrates with the GLib mainloop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/gwebsockets* usr/lib64/python3*/site-packages/gwebsockets* usr/bin/*

%files
%files -n python3-gwebsockets -f %{oreon_filedir}/python3-gwebsockets.list

%changelog

%autochangelog
