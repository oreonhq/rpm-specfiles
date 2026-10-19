%global source0_hash dd5403f12283cb7dfb6bea04a2474277d798ba6149cf38143258d1525073dd57
Name:           fmf-jinja
Version:        0.1.0
Release:        1%{?dist}
Summary:        Jinja template engine using FMF metadata
License:        GPL-3.0-or-later
URL:            https://github.com/LecrisUT/fmf-jinja
Source0:        https://files.pythonhosted.org/packages/source/f/fmf_jinja/fmf_jinja-%{version}.tar.gz
BuildArch:      noarch
%py_provides python3-fmf-jinja
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fmf-jinja = %{version}-%{release}
# /oreon:deps
%package -n       python3-fmf-jinja+test
Summary:        Metapackage for python3-fmf-jinja test extras
Requires:       python3-fmf-jinja = %{version}-%{release}
Provides:       python3dist(fmf-jinja[test]) = %{version}-%{release}

%description -n python3-fmf-jinja+test
Metapackage for python3-fmf-jinja test extras.

%package -n       python3-fmf-jinja+test-cov
Summary:        Metapackage for python3-fmf-jinja test-cov extras
Requires:       python3-fmf-jinja = %{version}-%{release}
Provides:       python3dist(fmf-jinja[test-cov]) = %{version}-%{release}

%description -n python3-fmf-jinja+test-cov
Metapackage for python3-fmf-jinja test-cov extras.

%package -n       python3-fmf-jinja+docs
Summary:        Metapackage for python3-fmf-jinja docs extras
Requires:       python3-fmf-jinja = %{version}-%{release}
Provides:       python3dist(fmf-jinja[docs]) = %{version}-%{release}

%description -n python3-fmf-jinja+docs
Metapackage for python3-fmf-jinja docs extras.

%description
Jinja template engine using FMF metadata

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fmf_jinja-%{version}
# Workaround for hatchling not preserving symlinks
# https://github.com/pypa/hatch/issues/2008
mkdir -p test/data/input
cp -r example/* test/data/input

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pytest
%files

%changelog

%autochangelog
