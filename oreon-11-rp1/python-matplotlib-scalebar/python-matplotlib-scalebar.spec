%global source0_hash b0dd5e618784c69c79d938708c43007c53349f87aa85265b5308b6a92eff1f38
Name:           python-matplotlib-scalebar
Version:        0.9.0
Release:        1%{?dist}
Summary:        Artist for matplotlib to display a scale bar
License:        BSD-2-Clause
URL:            https://github.com/ppinard/matplotlib-scalebar
Source0:        https://github.com/ppinard/matplotlib-scalebar/archive/%{version}/matplotlib-scalebar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-matplotlib-scalebar = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-matplotlib-scalebar
Summary:        Artist for matplotlib to display a scale bar
%description -n python3-matplotlib-scalebar

%package doc
Summary:        Documentation and examples for matplotlib-scalebar
Requires:       %{name} = %{version}-%{release}
Requires:       python3dist(numpy)
Requires:       python3dist(pillow)
Requires:       python3dist(requests)
%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir matplotlib-scalebar-%{version}
%oreon_prep
%build

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-matplotlib-scalebar usr/lib/python3*/site-packages/matplotlib_scalebar* usr/lib64/python3*/site-packages/matplotlib_scalebar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/matplotlib_scalebar* usr/lib64/python3*/site-packages/matplotlib_scalebar* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-matplotlib-scalebar -f %{oreon_filedir}/python3-matplotlib-scalebar.list
%files -n python-matplotlib-scalebar-doc -f %{oreon_filedir}/python-matplotlib-scalebar-doc.list

%changelog

%autochangelog
