%global source0_hash c066f0ecbd4aad3a3398b55fef3e774e1dfc6dd89fef4c6901dff4cf29d84295

Name:          domtt
Version:       0.7.3
Release:       32%{?dist}
Summary:       DOM Tooltip (aka domTT) is a Javascript widget

License:       Apache-2.0
URL:           http://www.mojavelinux.com/projects/domtooltip/
Source0:       http://www.mojavelinux.com/cooker/download/index.php?file=domtooltip/%{name}-0.7.3.tar.gz
Source1:       %{name}.conf
BuildArch:     noarch

%description
DOM Tooltip (aka domTT) is a Javascript widget, released under the Apache 2.0
license, which allows developers to add customized tool-tips to their web sites. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n domTT

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/html/en
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/js
install -m 0644 *.html $RPM_BUILD_ROOT%{_datadir}/%{name}/html/en
install -m 0644 *.js $RPM_BUILD_ROOT%{_datadir}/%{name}/js
cp -p %{SOURCE1} %{name}.conf

%files
%doc AUTHORS BUGS Changelog README TODO %{name}.conf
%{_datadir}/%{name}/html/en
%{_datadir}/%{name}/js

%changelog
%autochangelog
