%global source0_hash none

Name:           vaultwarden-web
Version:        2025.7.0
Release:        2%{?dist}
Summary:        Web vault for vaultwarden

License:        GPL-3.0-only AND MIT AND BSD-3-Clause AND (MIT OR GPL-3.0-only)
URL:            https://github.com/dani-garcia/bw_web_builds
Source0:        %{url}/releases/download/v%{version}/bw_web_v%{version}.tar.gz
Source1:        LICENSE.txt

BuildArch:      noarch

# these are all included static js libs
Provides:       bundled(npm(buffer)) = 6.0.3
Provides:       bundled(npm(jszip)) = 3.10.1
Provides:       bundled(npm(papaparse)) = 5.4.1
Provides:       bundled(npm(lunr)) = 2.3.9
Provides:       bundled(npm(bootstrap) = 4.6.0
Provides:       bundled(npm(jquery)) = 3.7.1
Provides:       bundled(npm(ieee754))
Provides:       bundled(npm(popper.js)) = 1.16.1
Provides:       bundled(npm(qrious)) = 4.0.2

%description
%{summary}.

%prep
%autosetup -n web-vault

%build
# nothing to do

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/
cp -ra * %{buildroot}/%{_datadir}/%{name}
install -pm644 %{SOURCE1} %{_builddir}/web-vault/

%check
# nothing to do

%files
%license LICENSE.txt
%license *.js.LICENSE.txt
%license app/*.js.LICENSE.txt
%license scripts/*.js.LICENSE.txt
%{_datadir}/%{name}/

%changelog
%autochangelog
