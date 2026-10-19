%global source0_hash ec5e45c28e4126809872d37ea41937908e3d1f237f6faac0086332454666b067
%global appstream_minver 1.1.0
%global glib2_minver 2.80
%global asgen_jsdir %{_datadir}/appstream/templates/default/static/js
%bcond_without vendored_js
Name:           appstream-generator
Version:        1.0.0
Release:        1%{?dist}
Summary:        Fast AppStream metadata generator
License:        LGPL-3.0-or-later AND MIT
URL:            https://github.com/ximion/%{name}
Source0:        https://github.com/ximion/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-nodemodules.tar.gz
Patch0001:      0001-tests-Combine-results-and-registry-tests-to-make-the.patch
%if %{with vendored_js}
Provides:       bundled(npm(Flot)) = 0.8.3
Provides:       bundled(js-highlight) = 9.16.2
Provides:       bundled(js-jquery) = 3.4.1
%else
Requires:       npm(Flot)
Requires:       js-highlight
Requires:       js-jquery
%endif
Recommends:     ffmpeg-free
Recommends:     optipng
ExcludeArch:    %{ix86} %{arm32}
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(appstream-compose)
BuildRequires:  pkgconfig(catch2-with-main)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(inja)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libfyaml)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  pkgconfig(tbb)
# /oreon:deps
%description
appstream-generator is a tool to generate distribution metadata
from package repositories. It will extract icons, download
screenshots, validate and transform the metadata, and return
XML or YAML files that can be read by AppStream clients,
such as software centers. It will also generate issue reports
as JSON documents and HTML pages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%if %{with vendored_js}
%setup -q -T -D -a 1
%endif
%autopatch -p1

%conf
%meson -Ddownload-js=false

%build

%meson_build
%install
%meson_install
%if ! %{with vendored_js}
mkdir -p %{buildroot}%{asgen_jsdir}/jquery
ln -srf %{buildroot}%{_jsdir}/jquery/latest/jquery.min.js %{buildroot}%{asgen_jsdir}/jquery/jquery.min.js
mkdir -p %{buildroot}%{asgen_jsdir}/highlight
ln -srf %{buildroot}%{_jsdir}/highlight.js/highlight.pack.js %{buildroot}%{asgen_jsdir}/highlight/highlight.pack.js
ln -srf %{buildroot}%{nodejs_sitelib}/flot/ %{buildroot}%{asgen_jsdir}/flot
%else
mkdir -p %{buildroot}%{asgen_jsdir}/jquery
install contrib/setup/node_modules/jquery/dist/*.min.js -t %{buildroot}%{asgen_jsdir}/jquery
mkdir -p %{buildroot}%{asgen_jsdir}/highlight
install contrib/setup/node_modules/highlightjs/*.js -t %{buildroot}%{asgen_jsdir}/highlight
mkdir -p %{buildroot}%{asgen_jsdir}/flot
install contrib/setup/node_modules/jquery-flot/jquery.flot*.js -t %{buildroot}%{asgen_jsdir}/flot
%oreon_autofiles main
%endif
%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
