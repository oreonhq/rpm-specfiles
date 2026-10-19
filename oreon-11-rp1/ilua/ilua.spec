%global source0_hash 7f57c957e49da88972d90dff6050e628c645f27b1d5c19071fc985905f54e4f3
Name:           ilua
Version:        0.2.1
Release:        1%{?dist}
Summary:        Portable Lua kernel for Jupyter
License:        GPL-2.0-only AND MIT
URL:            https://github.com/guysv/ilua
Source0:        https://github.com/guysv/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          ilua-never-use-spawn.patch
BuildArch:      noarch
ExcludeArch:    %{ix86}
Requires:       python-jupyter-filesystem
Recommends:     lua
Provides:       bundled(lua-inspect) = 3.1.1
Provides:       bundled(lua-json) = 0.1.1
Provides:       bundled(lua-netstring) = 0.2.0
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ilua = %{version}-%{release}
# /oreon:deps
%description
ILua is a feature-packed, portable console and Jupyter kernel for the Lua
language. It is Lua-implementation agnostic, should work with any Lua
interpreter out of the box.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

export PYTHONPATH=%{buildroot}%{python3_sitelib}
export JUPYTER_PATH=%{buildroot}%{_datadir}/jupyter
(sleep 5 && echo 'print("assert" .. "me")') | jupyter-console --simple-prompt --kernel=lua 2>&1 | tee check.log
grep assertme check.log
grep Traceback check.log && exit 1 || true
%files

%changelog

%autochangelog
