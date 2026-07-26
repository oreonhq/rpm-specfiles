%global source0_hash 72cb2be14048c0cbc89ccf1b57863013a9977fd51248c300ccc72001e7c43dbb

Name:           python-pywlroots
Version:        0.17.0
Release:        9%{?dist}
Summary:        Python binding to the wlroots library using cffi
License:        NCSA

URL:            https://github.com/flacjacket/pywlroots
Source:         %{pypi_source pywlroots}

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: gcc
BuildRequires: (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)

%global _description %{expand:
A Python binding to the wlroots library using cffi. The library uses pywayland
to provide the Wayland bindings and python-xkbcommon to provide wlroots
keyboard functionality.}

%description %_description

%package -n     python3-pywlroots
Summary:        %{summary}

%description -n python3-pywlroots %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pywlroots-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
python3 wlroots/ffi_build.py

%install
%pyproject_install
%pyproject_save_files wlroots

%check
%pyproject_check_import -t
%pytest

%files -n python3-pywlroots -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
