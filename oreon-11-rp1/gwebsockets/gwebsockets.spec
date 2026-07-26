%global source0_hash 2eaf57c07d821709cf4e40bdf50c8869fda3a3c1e8c2660ccb2c0a0d4ab19910

Name:          gwebsockets
Version:       0.7
Release:       24%{?dist}
Summary:       GLib based websockets server

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           https://github.com/sugarlabs/gwebsockets
Source0:       %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:     noarch 

BuildRequires: glib2-devel
BuildRequires: python3-devel

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
