%global source0_hash ce0f0fade0536acbb6703d0213e82fbc190d057376ff1ea9f7cae6fcab655f75
%global sum A scientific image viewer and toolkit
Name:           ginga
Version:        7.5.0
Release:        1%{?dist}
Summary:        A scientific image viewer and toolkit
License:        BSD-3-Clause AND Apache-2.0
URL:            https://ejeschke.github.io/ginga/
Source0:        https://files.pythonhosted.org/packages/source/g/ginga/ginga-%{version}.tar.gz
Requires:       python3-%{name} = %{version}-%{release}
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(babel) >= 2.18.0
BuildRequires:  python3dist(setuptools) >= 84.0.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 10.2.1
Requires:       python3-ginga = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{name}
Summary:        %{sum}
Requires:       google-roboto-fonts
Requires:       google-roboto-condensed-fonts
%description -n python3-%{name}

%package -n python3-%{name}-examples
Summary:        Examples for %{name}
Requires:       python3-%{name} = %{version}-%{release}
%description -n python3-%{name}-examples
Examples for %{name}

%prep

%autosetup
sed -i -e s/opencv-python-headless/opencv/ -e s/python-magic.*/file-magic/ setup.cfg
# we don't have pillow-heif packaged
sed -i -e /pillow-heif/d setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
sed -i '/Roboto.*LICENSE/d' %{pyproject_files}
desktop-file-install                                    \
     --dir=%{buildroot}%{_datadir}/applications         \
     %{name}.desktop
rm %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto*/*
ln -sf %{_fontbasedir}/google-roboto/Roboto-Black.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Black.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Bold.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Bold.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Light.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Light.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Medium.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Medium.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Regular.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Regular.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Thin.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Thin.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-Bold.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-Bold.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-BoldItalic.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-BoldItalic.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-Light.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-Light.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-LightItalic.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-LightItalic.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-Italic.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-Italic.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-Regular.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-Regular.ttf
chmod 755 %{buildroot}/%{python3_sitelib}/%{name}/web/pgw/ipg.py
chmod 755 %{buildroot}/%{python3_sitelib}/%{name}/util/mosaic.py
%py3_shebang_fix %{buildroot}/%{python3_sitelib}/ginga/web/pgw/ipg.py %{buildroot}/%{python3_sitelib}/ginga/examples
%oreon_autofiles main usr/lib/python3*/site-packages/ginga* usr/lib64/python3*/site-packages/ginga* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%tox
%files
%files -n python3-ginga -f %{oreon_filedir}/python3-ginga.list
%files -n python3-ginga-examples -f %{oreon_filedir}/python3-ginga-examples.list

%changelog

%autochangelog
