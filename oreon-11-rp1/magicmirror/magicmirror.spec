%global source0_hash 352354565e7c74e5e8a701d380ceacf6d873110c6242d01dde3907666a9b1f70
%bcond_without tests
%global srcname MagicMirror
%global forgeurl https://github.com/MagicMirrorOrg/MagicMirror
Name:           magicmirror
Version:        2.37.0
Release:        1%{?dist}
Summary:        Modular smart mirror platform
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND (CC-BY-4.0 AND OFL-1.1 AND MIT) AND ISC AND MIT AND OFL-1.1 AND Python-2.0
URL:            http://magicmirror.builders
Source0:        %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        %{srcname}-%{version}-nm-prod.tgz
Source2:        %{srcname}-%{version}-nm-dev.tgz
Source3:        %{srcname}-%{version}-bundled-licenses.txt
Source4:        %{name}.service
Source5:        %{name}.sysusers
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
Requires:       nodejs
%if %{with tests}
%endif
Provides:       magicmirror-rpm-macros = %{version}-%{release}
Obsoletes:      magicmirror-rpm-macros < 2.22.0-2
# oreon:deps
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
BuildRequires:  npm
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
MagicMirror² is an open source modular smart mirror platform. With a growing
list of installable modules, the MagicMirror² allows you to convert your
hallway or bathroom mirror into your personal assistant.

This package contains the server version of MagicMirror², which is meant to be
accessed via a browser.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}
cp %{SOURCE3} .

%build

tar xfz %{SOURCE1}
for dir in node_modules fonts/node_modules vendor/node_modules; do
  mkdir -p "$dir"
  pushd "$dir"
  ln -s ../node_modules_prod/* .
  [ -e ../node_modules_prod/.bin ] && ln -s ../node_modules_prod/.bin .
  popd
done
%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json fonts/ index.html js/ modules/ serveronly/ translations/ vendor/ \
  %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{name}
install -Dpm0644 config/config.js.sample %{buildroot}%{_sysconfdir}/%{name}/config.js
install -Dpm0644 css/custom.css.sample %{buildroot}%{_sysconfdir}/%{name}/custom.css
install -Ddpm0755 %{buildroot}%{nodejs_sitelib}/%{name}/config
ln -s %{_sysconfdir}/%{name}/config.js %{buildroot}%{nodejs_sitelib}/%{name}/config
install -Dpm0644 -t %{buildroot}%{nodejs_sitelib}/%{name}/css css/main.css
ln -s %{_sysconfdir}/%{name}/custom.css %{buildroot}%{nodejs_sitelib}/%{name}/css
install -Dpm0644 -t %{buildroot}%{_unitdir} %{SOURCE4}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main
%if %{with tests}
%check

%nodejs_symlink_deps --check
tar xfz %{SOURCE2}
for dir in node_modules fonts/node_modules vendor/node_modules; do
  pushd "$dir"
  ln -sf ../node_modules_dev/* .
  popd
  if [ -e "${dir}/.bin" ]; then
    pushd "${dir}/.bin"
    [ -e ../../node_modules_dev/.bin ] && ln -sf ../../node_modules_dev/.bin/* .
    popd
  fi
done
ln -s custom.css.sample css/custom.css
./node_modules/.bin/jest \
  --modulePathIgnorePatterns node_modules_prod node_modules_dev \
  --selectProjects e2e unit \
  -i \
  --forceExit
%endif
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
