%global source0_hash 5e2effaf0bfe39829cf2d64e7ecc47c7d86d676a6599f7afba378c31f5e3a308
Name:           python-asgi-lifespan
Version:        2.1.0
Release:        1%{?dist}
Summary:        Programmatic startup/shutdown of ASGI apps.
License:        MIT
URL:            https://github.com/florimondmanca/asgi-lifespan
Source0:        https://files.pythonhosted.org/packages/source/a/asgi-lifespan/asgi-lifespan-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-asgi-lifespan = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-asgi-lifespan
Summary:        Programmatic startup/shutdown of ASGI apps.
%description -n python3-asgi-lifespan

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir asgi-lifespan-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-asgi-lifespan usr/lib/python3*/site-packages/asgi_lifespan* usr/lib64/python3*/site-packages/asgi_lifespan* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/asgi_lifespan* usr/lib64/python3*/site-packages/asgi_lifespan* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-asgi-lifespan -f %{oreon_filedir}/python3-asgi-lifespan.list

%changelog

%autochangelog
