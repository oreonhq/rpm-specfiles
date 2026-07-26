%global source0_hash 0860bc67bbefa4afbd8bdfa983f6db957b3fb9b03f5a9cba83b09202978a77dc

%global srcname sphinx-bootstrap-theme

%global common_sum A sphinx theme that integrates the Bootstrap framework
%global common_desc \
This sphinx theme integrates the Booststrap CSS / Javascript framework \
with various layout options, hierarchical menu navigation, and mobile-friendly \
responsive design.  It is configurable, extensible and can use any number \
of different Bootswatch CSS themes.

%global jquery_version 1.12.4
%global bootstrap_version 3.4.1

Name:           python-%{srcname}
Version:        0.8.1
Release:        17%{?dist}
Summary:        %{common_sum}

# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND Apache-2.0
URL:            http://ryan-roemer.github.com/%{srcname}
Source0:        https://github.com/ryan-roemer/sphinx-bootstrap-theme/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  web-assets-devel

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        %{common_sum}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?rhel}
Provides:       bundled(glyphicons-halflings-fonts)
%else
Requires:       glyphicons-halflings-fonts
%endif
Requires:       web-assets-filesystem
Provides:       bundled(jquery) = %{jquery_version}
Requires:       python3-sphinx

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

# Remove the bundled fonts on RHEL
%if 0%{?rhel}
for d in %{python3_sitelib}; do
  %{__rm} %{buildroot}${d}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-%{bootstrap_version}/fonts/glyphicons-halflings-regular.ttf
  %{__ln_s} -f %{_datadir}/fonts/glyphicons-halflings/glyphicons-halflings-regular.ttf \
    %{buildroot}${d}/sphinx_bootstrap_theme/bootstrap/static/bootstrap-%{bootstrap_version}/fonts/glyphicons-halflings-regular.ttf
done
%endif

%files -n python3-%{srcname}
%license LICENSE.txt
%doc *.rst
%{python3_sitelib}/sphinx_bootstrap_theme
%{python3_sitelib}/sphinx_bootstrap_theme-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
