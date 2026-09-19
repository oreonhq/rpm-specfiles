%global source0_hash 0fc09a1bd3e9c7081472f3ac78c8586d6dfbf4c246a4552752cabebfceab355b

%global commit0 673e0e8a66
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global snapdate 20260115

%global srcname migen

Name:           python-%{srcname}
Version:        0.9.2
Release:        37.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        A Python toolbox for building complex digital hardware

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://m-labs.hk/%{srcname}
Source0:        https://git.m-labs.hk/M-Labs/%{srcname}/archive/%{commit0}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# for the pdf manual:
BuildRequires:  make
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  python3-sphinx-latex

%description
Migen enables hardware designers to take advantage of the richness of
Python (object oriented programming, function parameters, generators,
operator overloading, libraries, etc.), to build well organized, reusable
and elegant digital hardware designs.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Migen enables hardware designers to take advantage of the richness of
Python (object oriented programming, function parameters, generators,
operator overloading, libraries, etc.), to build well organized, reusable
and elegant digital hardware designs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}
sed -r -i 's/(migen_version = ).*/\1"%{version}-%{release}"/' doc/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=. sphinx-build-3 -M latexpdf doc _build/pdf
PYTHONPATH=. sphinx-build-3 -b man doc _build/man

%install
%pyproject_install
%pyproject_save_files %{srcname}
install -Dpm644 -t %{buildroot}%{_mandir}/man1 _build/man/%{srcname}.1

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md _build/pdf/latex/Migen.pdf
%{_mandir}/man1/%{srcname}.1*

%changelog
%autochangelog
