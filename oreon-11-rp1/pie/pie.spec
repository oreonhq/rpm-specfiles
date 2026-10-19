%global source0_hash b9d5d8b4444bbf9e8c4e754162077857f5fa22564f1dd08d7468843215871b1b
%global gh_commit        bb8b16f1f0fa5870f9de2ee6276ff5b55a8a22f6
%global gh_short         %(c=%{gh_commit}; echo ${c:0:7})
%global gh_branch        main
%global gh_owner         php
%global gh_project       pie
%global upstream_version 1.3.10
%global bashcompdir      %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot     %(dirname %{bashcompdir} 2>/dev/null)
Name:           pie
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        PHP Installer for Extensions
License:        BSD-3-Clause AND MIT
URL:            https://github.com/php/pie
Source0:        %{name}-%{upstream_version}-%{gh_short}.tgz
Source1:        %{name}-bash-completion
Source9:        makesrc.sh
Patch0:         %{name}-rpm.patch
Patch1:         %{name}-noxdg.patch
Patch2:         %{name}-nocacert.patch
BuildArch:      noarch
Requires:       php(language) >= 8.1
Requires:       php-cli
Requires:       php-zip
Requires:       /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
Requires:       php-ctype
Requires:       php-curl
Requires:       php-dom
Requires:       php-intl
Requires:       php-json
Requires:       php-mbstring
Requires:       php-posix
Requires:       php-phar
Supplements:    php-pear
# oreon:deps
BuildRequires:  composer-generators
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-json
BuildRequires:  php-zip
BuildRequires:  pkgconfig(bash-completion)
# /oreon:deps
%description
PIE (PHP Installer for Extensions).

PIE can install an extension to any installed PHP version.

A list of extensions that support PIE can be found on
https://packagist.org/extensions.

Documentation: /usr/share/doc/pie/docs/usage.md

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm
%patch -P1 -p1 -b .noxdg
%patch -P2 -p1 -b .nocacert
find . \( -name \*.rpm -o -name \*noxdg -o -name \*nocacert \) -delete -print

rm vendor/composer/ca-bundle/res/cacert.pem

%build

%install
: Bash auto-completion
install -Dpm 644 %{SOURCE1} %{buildroot}%{bashcompdir}/%{name}
: Sources and dependencies
mkdir -p      %{buildroot}%{_datadir}/%{name}
cp -pr src    %{buildroot}%{_datadir}/%{name}/src
cp -pr vendor %{buildroot}%{_datadir}/%{name}/vendor
: Command
install -Dpm 755 bin/%{name} %{buildroot}%{_bindir}/%{name}
: Licenses
cd vendor
for lic in */*/LICENSE
do dir=$(dirname $lic)
   own=$(dirname $dir)
   prj=$(basename $dir)
   ln -sf ../../pie/vendor/$own/$prj/LICENSE ../$own-$prj-LICENSE
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
