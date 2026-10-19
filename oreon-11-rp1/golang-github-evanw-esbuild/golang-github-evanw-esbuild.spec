%global source0_hash 300162f899361d9f0263065f8728ef9086dcfc1a3d36bcbc4e0abe5de9c58bf8
%bcond check 0
%global goipath         github.com/evanw/esbuild
Version:                0.28.2
%gometa -L -f
%global common_description %{expand:
This is a JavaScript bundler and minifier. It packages up JavaScript and
TypeScript code for distribution on the web.}
%global golicenses      LICENSE.md
%global godocs          docs CHANGELOG.md README.md version.txt
Name:           golang-github-evanw-esbuild
Release:        1%{?dist}
Summary:        Fast JavaScript bundler and minifier
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/esbuild-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
# /oreon:deps
%package -n       nodejs-esbuild
Summary:        ESBuild ESM module
BuildArch:      noarch

%description -n nodejs-esbuild
ESBuild ESM module

%description %{common_description}

%package -n nodejs-esbuild
Summary: ESBuild ESM module
Requires: %{name} = %{version}-%{release}
%description -n nodejs-esbuild %{common_description} (JavaScript library)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A

%build

%gobuild -o %{gobuilddir}/bin/esbuild %{goipath}/cmd/esbuild
node scripts/esbuild.js %{gobuilddir}/bin/esbuild --neutral
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
node_platform=$(node -p 'process.platform + "-" + process.arch')
install -m 0755 -vd                     %{buildroot}%{nodejs_sitelib}/esbuild
cp -pr npm/esbuild/lib                  %{buildroot}%{nodejs_sitelib}/esbuild/
install -m 0644 -vp npm/esbuild/package.json %{buildroot}%{nodejs_sitelib}/esbuild/
install -m 0755 -vd %{buildroot}%{nodejs_sitelib}/@esbuild/${node_platform}/bin
install -m 0644 -vp npm/@esbuild/${node_platform}/package.json %{buildroot}%{nodejs_sitelib}/@esbuild/${node_platform}/
ln -s %{_bindir}/esbuild                %{buildroot}%{nodejs_sitelib}/@esbuild/${node_platform}/bin/esbuild
%oreon_autofiles nodejs-esbuild usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%ifarch ppc64le s390x
%gocheck -d internal/css_parser
%else
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n nodejs-esbuild -f %{oreon_filedir}/nodejs-esbuild.list

%changelog

%autochangelog
