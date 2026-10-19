%global source0_hash af384350e529c152faac1edcfd7033adcc09891f0b533129ffd1f5e0445ff27f
Name:           python-willow
Version:        1.12.0
Release:        1%{?dist}
Summary:        A single API for multiple Python image libraries
License:        BSD-3-Clause
URL:            https://github.com/wagtail/Willow
Source0:        https://github.com/wagtail/Willow/archive/v%{version}/willow-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-willow = %{version}-%{release}
# /oreon:deps
%package -n       python3-willow+pillow
Summary:        Metapackage for python3-willow pillow extras
Requires:       python3-willow = %{version}-%{release}
Requires:       python3dist(pillow) >= 11.3.0
Provides:       python3dist(willow[pillow]) = %{version}-%{release}

%description -n python3-willow+pillow
Metapackage for python3-willow pillow extras.

%package -n       python3-willow+wand
Summary:        Metapackage for python3-willow wand extras
Requires:       python3-willow = %{version}-%{release}
Requires:       python3dist(wand) >= 0.6
Requires:       python3dist(wand) < 1.0
Provides:       python3dist(willow[wand]) = %{version}-%{release}

%description -n python3-willow+wand
Metapackage for python3-willow wand extras.

%package -n       python3-willow+heif
Summary:        Metapackage for python3-willow heif extras
Requires:       python3-willow = %{version}-%{release}
Requires:       python3dist(pillow-heif) >= 1.0.0
Provides:       python3dist(willow[heif]) = %{version}-%{release}

%description -n python3-willow+heif
Metapackage for python3-willow heif extras.

%package -n       python3-willow+testing
Summary:        Metapackage for python3-willow testing extras
Requires:       python3-willow = %{version}-%{release}
Requires:       python3dist(coverage[toml]) >= 7.2.7
Requires:       python3dist(coverage[toml]) < 8.0
Requires:       python3dist(pre-commit) >= 3.4.0
Provides:       python3dist(willow[testing]) = %{version}-%{release}

%description -n python3-willow+testing
Metapackage for python3-willow testing extras.

%package -n       python3-willow+docs
Summary:        Metapackage for python3-willow docs extras
Requires:       python3-willow = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.0
Requires:       python3dist(sphinx-wagtail-theme) >= 6.1.1
Requires:       python3dist(sphinx-wagtail-theme) < 7.0
Requires:       python3dist(sphinxcontrib-spelling) >= 8.0
Requires:       python3dist(sphinxcontrib-spelling) < 9.0
Requires:       python3dist(sphinx-copybutton) >= 0.5
Provides:       python3dist(willow[docs]) = %{version}-%{release}

%description -n python3-willow+docs
Metapackage for python3-willow docs extras.

%description

%package -n python3-willow
Summary:        A single API for multiple Python image libraries
# oreon:reqs
Requires:       python3dist(defusedxml) < 1.0
Requires:       python3dist(defusedxml) >= 0.7
Requires:       python3dist(filetype) >= 1.0.10
# /oreon:reqs
%description -n python3-willow

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Willow-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-willow usr/lib/python3*/site-packages/willow* usr/lib64/python3*/site-packages/willow* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/willow* usr/lib64/python3*/site-packages/willow* usr/bin/*

%check

%pytest --ignore tests/test_wand.py \
    -k "not test_avif and not test_heic and not test_save_as_avif and not test_save_as_heic and not test_detect_faces"
%files
%files -n python3-willow -f %{oreon_filedir}/python3-willow.list

%changelog

%autochangelog
