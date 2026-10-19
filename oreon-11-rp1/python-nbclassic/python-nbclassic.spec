%global source0_hash 434228763f8cee754318cd6dfa42370db191af630dabab8e30bafc8c1aa3eee6
Name:           python-nbclassic
Version:        1.3.3
Release:        1%{?dist}
Summary:        Jupyter Notebook as a Jupyter Server Extension
License:        BSD-3-Clause AND Apache-2.0 AND MIT AND (MIT AND OFL-1.1) AND ISC
URL:            https://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/n/nbclassic/nbclassic-%{version}.tar.gz
Patch:          Use-MathJax-TeX-fonts-rather-than-STIXWeb.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(jupyter-server) >= 1.17
Requires:       python3-nbclassic = %{version}-%{release}
# /oreon:deps
%package -n       python3-nbclassic+dev
Summary:        Metapackage for python3-nbclassic dev extras
Requires:       python3-nbclassic = %{version}-%{release}
Provides:       python3dist(nbclassic[dev]) = %{version}-%{release}

%description -n python3-nbclassic+dev
Metapackage for python3-nbclassic dev extras.

%package -n       python3-nbclassic+docs
Summary:        Metapackage for python3-nbclassic docs extras
Requires:       python3-nbclassic = %{version}-%{release}
Provides:       python3dist(nbclassic[docs]) = %{version}-%{release}

%description -n python3-nbclassic+docs
Metapackage for python3-nbclassic docs extras.

%package -n       python3-nbclassic+json-logging
Summary:        Metapackage for python3-nbclassic json-logging extras
Requires:       python3-nbclassic = %{version}-%{release}
Provides:       python3dist(nbclassic[json-logging]) = %{version}-%{release}

%description -n python3-nbclassic+json-logging
Metapackage for python3-nbclassic json-logging extras.

%package -n       python3-nbclassic+test
Summary:        Metapackage for python3-nbclassic test extras
Requires:       python3-nbclassic = %{version}-%{release}
Provides:       python3dist(nbclassic[test]) = %{version}-%{release}

%description -n python3-nbclassic+test
Metapackage for python3-nbclassic test extras.

%description

%package -n     python3-nbclassic
Summary:        Jupyter Notebook as a Jupyter Server Extension
Requires:       hicolor-icon-theme
Requires:       python-jupyter-filesystem
Requires:       font(fontawesome)
Requires:       fontawesome-fonts-web
Provides:        bundled(npm(MathJax)) = 2.7.9
Provides:        bundled(npm(backbone)) = 1.6.1
Provides:        bundled(npm(bootstrap)) = 3.4.1
Provides:        bundled(npm(bootstrap-tour)) = 0.12.0
Provides:        bundled(npm(codemirror)) = 5.58.3
Provides:        bundled(npm(es6-promise)) = 1.0.0
Provides:        bundled(npm(font-awesome)) = 4.7.0
Provides:        bundled(npm(google-caja-sanitizer)) = 1.0.4
Provides:        bundled(npm(jed)) = 1.1.1
Provides:        bundled(npm(jquery)) = 3.7.1
Provides:        bundled(npm(jquery-typeahead)) = 2.10.7
Provides:        bundled(npm(jquery-ui)) = 1.13.3
Provides:        bundled(npm(marked)) = 4.0.19
Provides:        bundled(npm(moment)) = 2.29.4
Provides:        bundled(npm(react)) = 16.0.0
Provides:        bundled(npm(react-dom)) = 16.0.1
Provides:        bundled(npm(requirejs)) = 2.3.7
Provides:        bundled(npm(requirejs-plugins)) = 1.0.2
Provides:        bundled(npm(requirejs-text)) = 2.0.16
Provides:        bundled(npm(text-encoding)) = 0.1.0
Provides:        bundled(npm(underscore)) = 1.13.7
# oreon:reqs
Requires:       python3dist(nest-asyncio) >= 1.5
Requires:       python3dist(notebook-shim) >= 0.2.3
# /oreon:reqs
%description -n python3-nbclassic

%prep

%autosetup -p1 -n nbclassic-%{version}
sed -ri "/(pytest-cov|coverage|nbval|pytest-playwright|pytest-tornasync)/d" pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
pushd %{buildroot}%{python3_sitelib}/nbclassic/static/components
  rm -r font-awesome/{fonts,css}
  ln -vfs %{_datadir}/fonts/fontawesome font-awesome/fonts
  ln -vfs %{_datadir}/font-awesome-web/css font-awesome/css
popd
install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/nbclassic.json
rm -v $(find %{buildroot}%{python3_sitelib}/nbclassic/i18n -type f -name '*.po')
rm -rv $(find %{buildroot}%{python3_sitelib}/nbclassic -type d -name tests)
%oreon_autofiles python3-nbclassic usr/lib/python3*/site-packages/nbclassic* usr/lib64/python3*/site-packages/nbclassic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nbclassic* usr/lib64/python3*/site-packages/nbclassic* usr/bin/*

%check

%pytest
desktop-file-validate %{buildroot}%{_datadir}/applications/jupyter-nbclassic.desktop
%if "%{python3_version}" == "3.11"
%pretrans -n python3-nbclassic -p <lua>

path = "%{python3_sitelib}/nbclassic/static/components/font-awesome/css"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
%endif
%files
%files -n python3-nbclassic -f %{oreon_filedir}/python3-nbclassic.list

%changelog

%autochangelog
