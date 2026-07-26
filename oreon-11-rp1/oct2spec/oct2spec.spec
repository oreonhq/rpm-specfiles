%global source0_hash c7024d8c5f36b6a18c8bbbd531722c06620c95a0dbd41e91eb3229a8efaceefe

Name:           oct2spec
Version:        1.1
Release:        26%{?dist}
Summary:        Python script to generate Octave package spec file

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://pagure.io/oct2spec
Source0:        https://pagure.io/oct2spec/archive/%{version}/oct2spec-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(setuptools)

Requires:       wget
Requires:       fedora-packager
Requires:       python%{python3_pkgversion}-jinja2

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

%files
%license LICENSE
%doc README CHANGELOG
%{python3_sitelib}/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/oct2rpm
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/oct2rpm.1.gz

%changelog
%autochangelog
