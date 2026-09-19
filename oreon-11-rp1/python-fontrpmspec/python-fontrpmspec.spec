%global source0_hash f1196d0f02cb9b0dd1605e3ee2f01038247c7d9c93645e531c5a77e6dd660585

%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname fontrpmspec
%global _description %{expand:
This contains tools to generate/convert a RPM spec file for fonts.
}

Name:           python-%{srcname}
Version:        0.19
Release:        2%{?dist}
Summary:        Font Packaging tool for Fedora
License:        GPL-3.0-or-later
URL:            https://github.com/fedora-i18n/font-rpm-spec-generator
Source0:        %{pypi_source %{srcname} %{version}}

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3dist(fonttools)
BuildRequires:  python3dist(termcolor)
BuildRequires:  python3dist(python-rpm-spec)

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary: Python library for rpmspec tools for fonts

%description -n python%{python3_pkgversion}-%{srcname} %_description

This package contains a Python library for %{srcname}.

%package -n %{srcname}
Requires: python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
Requires: fontconfig
Requires: fedpkg
Requires: tmt
Summary: %{summary}

%description -n %{srcname} %_description

This package contains the end-user executables for %{srcname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n  python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n %{srcname}
%license LICENSE
%doc README.md
%{_bindir}/fontrpmspec-conv
%{_bindir}/fontrpmspec-gen
%{_bindir}/fontrpmspec-gentmt

%changelog
%autochangelog
