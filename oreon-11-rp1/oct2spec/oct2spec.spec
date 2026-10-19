%global source0_hash c7024d8c5f36b6a18c8bbbd531722c06620c95a0dbd41e91eb3229a8efaceefe
Name:           oct2spec
Version:        1.1
Release:        26%{?dist}
Summary:        Python script to generate Octave package spec file
License:        GPL-3.0-or-later
URL:            https://pagure.io/oct2spec
Source0:        https://pagure.io/oct2spec/archive/%{version}/oct2spec-%{version}.tar.gz
BuildArch:      noarch
Requires:       wget
Requires:       fedora-packager
Requires:       python%{python3_pkgversion}-jinja2
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
oct2spec is a small python tool that generates spec file for Octave packages.
It can work from a package name, URL, or a tarball.
oct2spec provides oct2rpm which generates rpm for Octave packages using the
oct2spec API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%py3_build
%install
%py3_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
